# Google Cloud SQL Access with Twingate

## Summary
Configure secure access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, Spanner) using Twingate Connectors. Supports both private IP/PSC and public IP (Authorized Networks) connection methods. Traffic routes through Connectors, eliminating the need to expose databases publicly.

## Key Information
- Two connection methods: Private IP/PSC (preferred) or Public IP via Authorized Networks
- Supported databases: Cloud SQL (MySQL/PostgreSQL/SQL Server), AlloyDB, Memorystore, Spanner, Bigtable, Firestore
- Private connectivity keeps traffic on Google's internal network fabric entirely
- Public IP method requires adding Connector public IPs to Authorized Networks in `/32` CIDR format

## Prerequisites
- Twingate Remote Network created and Connector(s) deployed
- For private: Connector in same VPC (or peered VPC) as database
- For public: Connector's public IP addresses captured
- Existing GCP database instance

## Port Configuration Values
| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

## Step-by-Step: Private IP/PSC Method

1. **Enable Private IP** — GCP Console → Cloud SQL → Instance → Connections → Networking → enable Private IP, select VPC, remove Public IP if unneeded
2. **Create Twingate Resource** — Use private IP or private DNS name of database; set correct port; assign user group(s)
3. **Connect** — Run Twingate Client, connect via standard database client to private IP

## Step-by-Step: Public IP Method (Authorized Networks)

1. **Create Twingate Resource** — Use database's public IP or FQDN with correct port
2. **Add Connector IPs** — GCP Console → Cloud SQL → Connections → Authorized Networks → add each Connector public IP in `/32` CIDR format
3. **Connect** — Run Twingate Client; connections only succeed from Connector IPs

## Gotchas
- Memorystore is internal-IP only; requires VPC Network Peering at instance creation
- BigQuery/Spanner require PSC endpoint inside VPC (no direct private IP config)
- Cloud SQL denies all connections by default — Connector IP must be explicitly authorized
- Port mismatch between database engine and Twingate Resource definition breaks connections
- If another VPN is running, it may intercept traffic before Twingate Client
- DNS resolution failures: ensure DNS zone is tied to VPC and DNS server is reachable from Connector

## Troubleshooting via Recent Activity
| Status | Cause |
|--------|-------|
| DNS Failed | Connector can't resolve hostname; check DNS zone/VPC binding |
| Connection Failed | Connector reached but can't connect to DB; check firewall/IP allowlist |
| No Activity | Client not sending traffic; check Client running, resource access, other VPN conflicts |

## Optional: GCP Console Access Control
Gate `console.cloud.google.com` using Twingate SSO/SaaS App Gating with Google Workspace, Okta, or Azure AD — GCP has no native IP allowlist for the console.

## Related Docs
- Twingate Troubleshooting Guide
- SaaS App Gating Guide
- Connector Best Practices
- AWS/Azure/Oracle Database Access Guides
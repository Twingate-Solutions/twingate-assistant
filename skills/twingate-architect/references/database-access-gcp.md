# Google Cloud SQL Access with Twingate

## Summary
Configure Twingate to securely access GCP managed databases (Cloud SQL, AlloyDB, Memorystore) without public exposure. Traffic routes through Connectors deployed in your VPC, enabling private IP/PSC connectivity or minimal Authorized Networks allowlisting for public endpoints.

## Key Information
- Two connection methods: Private IP/PSC (preferred) or Public IP with Authorized Networks
- Connectors must be in the same VPC (or peered VPC) as the database for private connectivity
- PSC/PSA keeps all traffic on Google's internal network—no public IP allowlisting needed
- Memorystore is internal-only; requires VPC Network Peering at creation time
- BigQuery/Spanner use PSC endpoints inside your VPC

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- For private: Connector inside same VPC as database; use private IPs in firewall rules
- For public: Connector's public IP(s) captured for Authorized Networks
- Existing Cloud SQL, AlloyDB, Memorystore, or other GCP database instance

## Configuration Values

| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

## Step-by-Step: Private IP/PSC (Recommended)

1. **Enable Private IP or PSC** — GCP Console → Cloud SQL → Instance → Connections → Networking → enable Private IP, select VPC, remove Public IP
2. **Create Twingate Resource** — Use private IP or private DNS name of database; set correct port; assign user groups
3. **Connect** — Run Twingate Client, connect via database client using private IP

```bash
psql -h <private-ip> -U <username> -d <database>
mysql -h <private-ip> -u <username> -p
sqlcmd -S <private-ip> -U <username> -P <password> -d <database>
```

## Step-by-Step: Public IP / Authorized Networks (Fallback Only)

1. **Create Twingate Resource** — Use database's public IP or FQDN with correct port
2. **Add Connector IPs to Authorized Networks** — GCP Console → Cloud SQL → Connections → Authorized Networks → add each Connector IP as `/32` CIDR
3. **Connect** — Twingate Client must be running; traffic routes through Connector IPs

## Gotchas
- **No Activity in logs**: Client not sending to Connector — check Client is running, user has resource access, no other VPN intercepting
- **DNS Failed**: Connector can't resolve hostname — ensure DNS zone is tied to VPC and accessible from Connector
- **Connection Failed**: Connector reached destination but was blocked — verify IP allowlists and firewall rules on both ends
- **Port mismatch**: Twingate Resource port must exactly match database engine port
- GCP Console has no native IP allowlist; gate it via SSO + Twingate SaaS App Gating instead

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
- AWS/Azure/Oracle Database Access Guides (parallel docs)
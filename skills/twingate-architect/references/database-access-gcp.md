# Google Cloud SQL Access with Twingate

## Summary
Twingate enables secure, private access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, Spanner, etc.) by routing traffic through Connectors deployed in your VPC. Supports both private IP/PSC (preferred) and public IP/Authorized Networks approaches. Eliminates need to expose database endpoints publicly.

## Key Information
- Two connectivity modes: Private IP/PSC (recommended) or Public IP with Authorized Networks
- Private connectivity keeps all traffic on Google's internal network fabric
- Connector must be in same VPC (or peered VPC) as database for private connectivity
- Public IP method requires adding Connector public IPs to Authorized Networks in `/32` CIDR format

## Prerequisites
- Twingate Remote Network created with Connector deployed
  - Private mode: Connector inside same VPC as database
  - Public mode: Connector's public IP captured for allowlisting
- GCP database instance (Cloud SQL, AlloyDB, Memorystore, etc.)

## Default Ports by Database Type
| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

## Step-by-Step: Private IP/PSC (Recommended)

1. **Enable Private IP** — GCP Console → Cloud SQL → Instance → Connections → Networking → Enable Private IP, select VPC, remove Public IP if unused
2. **Create Twingate Resource** — Use private IP or private DNS name, set correct port, assign user group(s)
3. **Connect** — Run Twingate Client, use standard DB client with private IP

```bash
psql -h <private-ip> -U <username> -d <database>
mysql -h <private-ip> -u <username> -p
sqlcmd -S <private-ip> -U <username> -P <password> -d <database>
```

## Step-by-Step: Public IP / Authorized Networks

1. **Create Twingate Resource** — Use database's public IP or FQDN with correct port
2. **Add Connector IPs** — GCP Console → Cloud SQL → Connections → Authorized Networks → Add each Connector IP in `/32` CIDR format
3. **Connect** — Traffic routes through Connector IPs only

## Gotchas
- Memorystore only supports internal IP; requires VPC Network Peering at instance creation
- API-only services (BigQuery, Spanner) require creating a PSC endpoint inside VPC
- GCP Console has no native IP allowlist; use Twingate SSO/SaaS App Gating for console access control
- Cloud SQL denies ALL incoming connections unless explicitly authorized

## Troubleshooting Reference
| Symptom | Cause | Fix |
|---------|-------|-----|
| DNS Failed | Connector can't resolve hostname | Check DNS zone tied to VPC |
| Connection Failed | Connector can't reach destination | Check routes, IP allowlists, firewall rules |
| No Activity | Client not sending traffic | Verify Client running, resource access granted, no conflicting VPN |
| Connection Denied | IP not in Authorized Networks | Add Connector IPs |
| Port Mismatch | Wrong port in Resource config | Match DB engine port |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- AWS/Azure/Oracle Database Access Guides
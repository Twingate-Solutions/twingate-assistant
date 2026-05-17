# Google Cloud SQL Access with Twingate

## Summary
Twingate enables secure access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, etc.) by routing traffic through Connectors, eliminating the need for public database exposure. Supports both private IP/PSC (preferred) and public IP with Authorized Networks methods.

## Key Information
- Supports MySQL, PostgreSQL, SQL Server, Redis/Memorystore, BigQuery, Spanner
- Two connection models: Private IP/PSC (recommended) or Public IP with Authorized Networks
- Private connectivity keeps all traffic on Google's internal network fabric
- PSC/PSA requires Connector deployed in same or peered VPC as database

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- For private: Connector inside same VPC as database
- For public: Connector's public IP captured for Authorized Networks allowlisting
- Existing GCP database instance (Cloud SQL, AlloyDB, etc.)

## Configuration Values

**Database Ports:**
| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

## Step-by-Step

### Private IP / PSC Method (Recommended)
1. Enable Private IP on database: Cloud SQL → Instance → Connections → Networking (or AlloyDB → Cluster → Networking)
2. Remove Public IP if not needed
3. Create Twingate Resource using **private IP or private DNS name** + appropriate port
4. Assign resource to user group(s)
5. Connect via database client using private IP

### Public IP / Authorized Networks Method
1. Create Twingate Resource using database's **public IP or FQDN** + port
2. In GCP Console: Cloud SQL → Instance → Connections → Authorized Networks
3. Add each Connector's public IP in `/32` CIDR format
4. Connect via database client (traffic must originate from Connector IPs)

## Connection Commands
```bash
mysql -h <private-ip> -u <username> -p
psql -h <private-ip> -U <username> -d <database>
sqlcmd -S <private-ip> -U <username> -P <password> -d <database>
```

## Gotchas
- Memorystore is **internal IP only** — requires VPC Network Peering at instance creation
- API-only services (BigQuery, Spanner) require a PSC endpoint created inside VPC
- GCP Cloud Console has no native IP allowlist — use Twingate SSO + SaaS App Gating instead
- Authorized Networks: Cloud SQL denies **all** connections not explicitly listed
- Cloud SQL Auth Proxy: instance connection name must exactly match target instance

## Troubleshooting
- **DNS Failed**: Connector can't resolve hostname — check DNS hosted zone VPC binding
- **Connection Failed**: Connector reached but can't connect — verify routes, IP allowlists, firewall port rules
- **No Activity**: Client not sending traffic — check Client running, resource access granted, no conflicting VPN

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs)
- [Google Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
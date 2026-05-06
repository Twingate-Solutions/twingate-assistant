# Google Cloud SQL Access with Twingate

## Summary
Twingate enables secure access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, etc.) by routing traffic through Connectors without exposing databases publicly. Supports both private IP/PSC (preferred) and public IP (Authorized Networks) connection methods.

## Key Information
- Private IP/PSC is the recommended approach—traffic stays on Google's internal network
- Public IP method requires whitelisting Connector public IPs in Authorized Networks
- Connectors must be deployed in the same VPC (or peered VPC) for private connectivity

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- GCP database instance (Cloud SQL, AlloyDB, Memorystore, etc.)
- For private: Connector inside same VPC as database
- For public: Connector's public IP addresses available

## Step-by-Step: Private IP / PSC (Recommended)

1. **Enable Private IP on database**: Cloud SQL → Instance → Connections → Networking; enable Private IP, select VPC, remove Public IP if unused
2. **Create Twingate Resource**: Use private IP or private DNS name of database
3. **Set port** per engine type (see Configuration Values)
4. **Assign group access** in Twingate Admin Console
5. **Connect** using database client pointed at private IP

## Step-by-Step: Public IP (Authorized Networks)

1. **Create Twingate Resource** using database's public IP or FQDN with correct port
2. **Add Connector IPs to Authorized Networks**: Cloud SQL → Connections → Authorized Networks; add each Connector IP as `/32` CIDR
3. **Connect** via database client—connections must originate from Connector IPs

## Configuration Values

| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

## Gotchas
- Memorystore is **only** accessible via internal IP; requires VPC Network Peering at instance creation
- API-only services (BigQuery, Spanner) require creating a PSC endpoint inside your VPC
- GCP Console has no native IP allowlist—use Twingate SSO/SaaS App Gating instead
- Cloud SQL denies **all** incoming connections unless explicitly authorized
- If using PSC/private IP, no public IP allowlisting needed

## Troubleshooting
- **DNS Failed**: Connector can't resolve hostname—check DNS hosted zone is tied to VPC
- **Connection Failed**: Connector reached but can't connect to DB—check firewall rules, IP allowlists, and port settings
- **No Activity**: Client not sending traffic—check Client is running, user has Resource access, no conflicting VPN
- **Port mismatch**: Twingate Resource port must exactly match database engine port
- Use Admin Console → Recent Activity on the Resource for diagnostics

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
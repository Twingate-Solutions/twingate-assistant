# Google Cloud SQL Access with Twingate

## Summary
Twingate enables secure private access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, Spanner, etc.) by routing traffic through Connectors deployed in your VPC. Supports both private IP/PSC (preferred) and public IP with Authorized Networks (fallback). No public database exposure required.

## Key Information
- Two connection methods: **Private IP/PSC** (recommended) or **Public IP with Authorized Networks** (fallback only)
- Connectors act as traffic proxies; only Connector IPs need database firewall access
- PSC/Private IP keeps all traffic on Google's internal network fabric
- GCP Admin Console access can be gated via SSO (SaaS App Gating)

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- For private: Connector inside the same VPC (or peered VPC) as the database
- For public: Connector's public IP address available for allowlisting
- GCP database instance (Cloud SQL, AlloyDB, Memorystore, etc.) already running

## Step-by-Step

### Method 1: Private IP / PSC (Recommended)
1. In GCP Console, enable **Private IP** on Cloud SQL/AlloyDB instance (`Instance → Connections → Networking`); remove Public IP if unneeded
2. For Memorystore: configure VPC Network Peering at instance creation
3. For API-only services (BigQuery, Spanner): create a PSC endpoint in your VPC
4. In Twingate Admin Console, create a Resource using the **private IP or private DNS name**
5. Set correct port for database type (see below)
6. Assign Resource to user group(s)
7. Connect via database client with Twingate Client running

### Method 2: Public IP / Authorized Networks (Fallback)
1. In Twingate Admin Console, create a Resource using the **public IP or FQDN**
2. In GCP Console, go to `Cloud SQL → Instance → Connections → Authorized Networks`
3. Add each Connector's public IP in `/32` CIDR format
4. Connect via database client with Twingate Client running

## Configuration Values

| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

**CLI connection examples:**
```bash
mysql -h <private-ip> -u <username> -p
psql -h <private-ip> -U <username> -d <database>
sqlcmd -S <private-ip> -U <username> -P <password> -d <database>
```

## Gotchas
- Authorized Networks deny **all** connections by default unless IP is explicitly listed
- Port in Twingate Resource must exactly match the database engine port
- If using Cloud SQL Auth Proxy: instance connection name must match the target instance
- **No Activity** in Twingate logs = Client not sending to Connector (check: Client running, Resource access granted, no conflicting VPN)
- **DNS Failed** = Connector can't resolve hostname; DNS zone must be tied to the VPC
- **Connection Failed** = Connector reached destination but was rejected; check firewall rules and IP allowlists on both ends

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [Azure Database Access Guide](https://www.twingate.com/docs/database-access-azure)
- [GCP Private Service Connect Docs](https://cloud.google.com/vpc/docs/private-service-connect)
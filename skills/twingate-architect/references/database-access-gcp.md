# Google Cloud SQL Access with Twingate

## Summary
Twingate secures access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, Spanner, etc.) by routing traffic through Connectors, eliminating public exposure. Supports both private IP/PSC (preferred) and public IP (Authorized Networks) connection methods.

## Key Information
- Two connection methods: **Private IP/PSC** (recommended) or **Public IP with Authorized Networks**
- Private method requires Connector deployed in same VPC (or peered VPC) as database
- Public method requires adding Connector public IPs to GCP Authorized Networks in `/32` CIDR format
- GCP Console access can be gated via Twingate SSO integration

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- GCP database instance (Cloud SQL, AlloyDB, Memorystore, etc.)
- For private: Connector inside same VPC; for public: Connector's public IP address

## Step-by-Step (Private IP/PSC — Recommended)

1. **Enable Private IP or PSC** on database:
   - Cloud SQL: Console → Cloud SQL → Instance → Connections → Networking → Enable Private IP
   - AlloyDB: Cluster → Networking → Enable Private IP
   - Memorystore: Configure VPC Network Peering at instance creation
   - BigQuery/Spanner: Create PSC endpoint inside VPC

2. **Create Twingate Resource** using private IP or private DNS name of database

3. **Connect** using standard database client with private IP

## Step-by-Step (Public IP/Authorized Networks)

1. **Create Twingate Resource** using database's public IP or FQDN
2. **Add Connector IPs** to Authorized Networks (Cloud SQL → Connections → Authorized Networks or AlloyDB → Networking)
3. **Connect** via database client — traffic routes through Connector

## Configuration Values

| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

**Connection commands:**
```bash
mysql -h <private-ip> -u <username> -p
psql -h <private-ip> -U <username> -d <database>
sqlcmd -S <private-ip> -U <username> -P <password> -d <database>
```

## Gotchas
- Authorized Networks deny **all** incoming connections unless explicitly listed — verify Connector IPs are added
- Port in Twingate Resource must exactly match database engine port
- **DNS Failed** in Recent Activity = Connector can't resolve hostname; ensure DNS zone is tied to VPC
- **Connection Failed** = Connector reached destination but was blocked; check firewall rules and IP allowlists
- **No Activity** = Client not sending traffic; check Client is running and no other VPN intercepting
- Cloud SQL Auth Proxy requires correct IAM credentials and matching instance connection name

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- AWS/Azure/Oracle Database Access Guides
- [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
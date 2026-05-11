# Google Cloud SQL Access with Twingate

## Summary
Twingate enables secure access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, Spanner, etc.) by routing traffic through Connectors deployed in your VPC. Supports both private IP/PSC (preferred) and public IP (Authorized Networks) connection methods. Eliminates need to expose database endpoints publicly.

## Key Information
- Two connection modes: **Private IP/PSC** (recommended) or **Public IP with Authorized Networks** (fallback)
- Private mode keeps all traffic on Google's internal network fabric—no public IP allowlisting needed
- Public mode requires adding Connector public IPs to GCP Authorized Networks in `/32` CIDR format
- GCP Admin Console access can be gated via Twingate SSO integration

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- For private: Connectors deployed **inside the same VPC** as the database
- For public: Connector **public IP addresses** captured for allowlisting
- Existing GCP database instance (Cloud SQL, AlloyDB, Memorystore, etc.)

## Configuration Values

| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

## Step-by-Step

### Private IP / PSC (Recommended)
1. **Enable Private IP on database**: Cloud SQL → Instance → Connections → Networking → Enable Private IP; disable Public IP if unused
2. **Memorystore**: Configure VPC Network Peering at instance creation (internal IP only)
3. **API services** (BigQuery, Spanner): Create PSC endpoint inside your VPC
4. **Create Twingate Resource** using private IP or private DNS name with correct port
5. **Assign access** to relevant user groups
6. Connect via database client using private IP while Twingate Client is running

### Public IP / Authorized Networks (Fallback Only)
1. Create Twingate Resource using database's **public IP or FQDN** with correct port
2. In GCP Console → Cloud SQL/AlloyDB → Authorized Networks → add each Connector's public IP in `/32` CIDR
3. Connect via database client while Twingate Client is running

## Gotchas
- **DNS Failed** in Recent Activity: Connector can't resolve hostname—check DNS zone is tied to VPC and DNS server is reachable
- **Connection Failed**: Connector reached destination but was blocked—verify IP allowlists, firewall/security group rules, and routing
- **No Activity**: Client not sending traffic—check Client is running, Resource access is granted, no conflicting VPN
- Port in Twingate Resource must exactly match database engine port
- Cloud SQL denies **all** incoming connections unless explicitly authorized
- PSA/PSC requires Connector in same or peered VPC

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Security Policies Guide](https://www.twingate.com/docs/security-policies)
- [GCP Private Service Connect docs](https://cloud.google.com/vpc/docs/private-service-connect)
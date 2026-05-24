# Google Cloud SQL Access with Twingate

## Summary
Twingate enables secure private access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, Spanner, etc.) by routing traffic through Connectors deployed in your VPC. Supports both private IP/PSC (preferred) and public IP with Authorized Networks as a fallback method.

## Key Information
- Supports MySQL, PostgreSQL, SQL Server, Redis (Memorystore), and API-only services (BigQuery, Spanner via PSC)
- Two connectivity modes: private IP/PSC (recommended) or public IP with Authorized Networks
- Private Service Connect (PSC) or Private Service Access (PSA) keeps all traffic on Google's internal network fabric

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- For private: Connectors inside same VPC as database (or peered VPC)
- For public: Connector's public IP addresses available for allowlisting
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
1. **Enable private connectivity**: Cloud SQL → Instance → Connections → Networking → enable Private IP; remove Public IP if unused
2. **Memorystore**: Configure VPC Network Peering at instance creation
3. **API-only services**: Create PSC endpoint inside your VPC
4. **Create Twingate Resource**: Use private IP or private DNS name + appropriate port
5. **Assign access** to relevant user groups
6. **Connect** using standard DB client with private IP

### Public IP / Authorized Networks (Fallback)
1. **Create Twingate Resource**: Use public IP/FQDN + appropriate port
2. **Add Connector IPs**: Cloud SQL → Connections → Authorized Networks → add each Connector public IP in `/32` CIDR format
3. **Connect** using standard DB client (traffic routes through Connector)

## Gotchas
- **Authorized Networks deny all by default** — every Connector IP must be explicitly added
- **Memorystore** is internal-only; no public IP option exists
- **Cloud SQL Auth Proxy**: instance connection name must match exactly
- **No GCP Console IP allowlist natively** — use SSO + Twingate SaaS App Gating instead

## Troubleshooting
| Symptom | Check |
|---------|-------|
| Connection denied | Connector IP in Authorized Networks? |
| DNS Failed (Recent Activity) | DNS zone tied to VPC? DNS server defined as Twingate Resource? |
| Connection Failed (Recent Activity) | Route exists? Firewall allows port on both ends? |
| No Activity | Client running? Resource access granted? Another VPN intercepting? |
| Timeouts | Connectors online and reachable? |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Private Service Connect (Google)](https://cloud.google.com/vpc/docs/private-service-connect)
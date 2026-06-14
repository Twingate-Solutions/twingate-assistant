# Google Cloud SQL Access with Twingate

## Summary
Twingate secures access to GCP managed databases (Cloud SQL, AlloyDB, Memorystore, Spanner, etc.) by routing traffic through Connectors, eliminating the need to expose databases publicly. Supports both private IP/PSC and public IP (Authorized Networks) connection methods.

## Key Information
- Preferred method: Private IP or Private Service Connect (PSC) — traffic stays on Google's internal network
- Fallback method: Public IP with Authorized Networks — whitelist only Connector public IPs
- Connectors act as the network bridge; database clients connect normally via Twingate Client

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- For private access: Connectors inside same VPC (or peered VPC) as database
- For public access: Connector public IPs available for allowlisting
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
1. Enable Private IP on database: Cloud SQL → Instance → Connections → Networking → enable Private IP, select VPC, remove Public IP
2. Create Twingate Resource using private IP or private DNS name with correct port
3. Assign Resource to user group(s)
4. Connect via client: `psql -h <private-ip> -U <user> -d <db>`

### Public IP / Authorized Networks (Fallback)
1. Create Twingate Resource using database's public IP/FQDN with correct port
2. In GCP Console: Cloud SQL → Instance → Connections → Authorized Networks → add each Connector's public IP in `/32` CIDR format
3. Connect via database client while Twingate Client is running

### GCP Console Access (Optional)
- No native IP allowlist for `console.cloud.google.com`
- Gate access via Twingate SSO + SaaS App Gating (Google Workspace, Okta, Azure AD)

## Gotchas
- Memorystore only accessible via internal IP; requires VPC Network Peering at creation time
- API-only services (BigQuery, Spanner) require creating a PSC endpoint inside your VPC
- With Authorized Networks: connections only work when originating from whitelisted Connector IPs
- **DNS Failed** in Recent Activity → Connector can't resolve hostname; check DNS zone is VPC-bound
- **Connection Failed** → Connector reached but can't connect to DB; check firewall rules and IP allowlists
- **No Activity** → Client not sending traffic; check Client is running, Resource access granted, no conflicting VPN

## Troubleshooting Checklist
- Verify Connector IPs in Authorized Networks (for public access)
- Confirm port in Twingate Resource matches database engine port
- Check Connectors are online in Admin Console
- Review Recent Activity on the Resource for specific failure type

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- AWS/Azure/Oracle Database Access Guides
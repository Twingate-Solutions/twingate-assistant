---
source: https://www.twingate.com/docs/database-access-gcp
type: docs
fetched: 2026-08-14
source_version: 55e516c797628f16a2876a03969968d6ed82f610126fd7451487777f711e5928
---

# Google Cloud SQL Access with Twingate

## Summary
Twingate routes GCP database traffic through Connectors, enabling private access to Cloud SQL, AlloyDB, Memorystore, and other GCP databases without public exposure. Supports both private IP/PSC (preferred) and public IP Authorized Networks approaches. Connectors act as the network bridge, eliminating the need to expose databases publicly.

## Key Information
- Supports: Cloud SQL (MySQL/PostgreSQL/SQL Server), AlloyDB, Memorystore (Redis/Memcached), Spanner, BigQuery, Bigtable, Firestore
- Two access models: Private IP/PSC (recommended) or Public IP Authorized Networks (fallback)
- Private Service Connect (PSC) or Private Service Access (PSA) keeps all traffic on Google's internal network fabric
- GCP Admin Console access can be gated via Twingate SSO/SaaS App Gating

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- For private: Connector in same VPC (or peered VPC) as database
- For public: Connector's public IP captured for Authorized Networks allowlisting
- Existing GCP database instance (Cloud SQL, AlloyDB, etc.)

## Step-by-Step

### Private IP / PSC (Recommended)
1. Enable Private IP in GCP Console: **Cloud SQL → Instance → Connections → Networking** or **AlloyDB → Cluster → Networking**; disable Public IP if unused
2. For Memorystore: configure VPC Network Peering at instance creation
3. For API-only services (BigQuery, Spanner): create PSC endpoint inside VPC
4. Create Twingate Resource using private IP or private DNS name with appropriate port
5. Connect via database client with Twingate Client running

### Public IP / Authorized Networks (Fallback)
1. Create Twingate Resource using database's public IP/FQDN with appropriate port
2. In GCP Console: **Cloud SQL → Instance → Connections → Authorized networks** → add each Connector's public IP in `/32` CIDR format
3. Connect via database client with Twingate Client running

## Configuration Values

| Database | Port |
|----------|------|
| MySQL | 3306 |
| PostgreSQL | 5432 |
| SQL Server | 1433 |
| Redis (Memorystore) | 6379 |

```bash
# Connection examples
mysql -h <private-ip> -u <username> -p
psql -h <private-ip> -U <username> -d <database>
sqlcmd -S <private-ip> -U <username> -P <password> -d <database>
```

## Gotchas
- Cloud SQL denies **all** incoming connections unless explicitly authorized
- Connector must be in same or peered VPC for private IP access to work
- Public IP Authorized Networks requires Connector's public IP in `/32` CIDR format — not a range
- Memorystore is internal-only; no public IP option exists
- If using Cloud SQL Auth Proxy: IAM credentials must be correct and instance connection name must match exactly
- Other active VPNs may hijack connections ("No Activity" in Recent Activity logs)

## Troubleshooting
- **DNS Failed**: Connector can't resolve hostname — check DNS zone is VPC-attached, DNS server is a Twingate Resource if self-hosted
- **Connection Failed**: Connector reached but can't connect to DB — check firewall rules, IP allowlists, port configuration on both ends
- **No Activity**: Client not sending traffic to Connector — check Client is running, user has Resource access, no conflicting VPN

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- AWS/Azure/Oracle Database Access Guides
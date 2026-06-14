# Azure SQL Database Access with Twingate

## Summary
Securely connect to Azure SQL Database and other Azure-managed or VM-hosted databases using Twingate Connectors. Traffic routes through Connectors deployed in your VNet, enabling private endpoint or firewall-restricted access without public database exposure.

## Key Information
- Supports Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on VMs
- Preferred approach: Azure Private Endpoint — traffic stays on Microsoft's internal backbone, no public IP allowlisting required
- Public endpoint fallback: allowlist Connector's public egress IP in Azure firewall rules
- Azure SQL firewall checks database-level rules before server-level rules
- Max 256 server-level firewall rules; use database-level rules or CIDR aggregation beyond that

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- For private endpoints: Connector inside the **same VNet** as the database
- For public endpoints: Connector's public IP address for allowlisting
- Azure SQL Database instance or self-hosted SQL Server on Azure VM

## Step-by-Step (Azure SQL Database)

**Step 1 – Configure Azure Private Connectivity**
- Disable "Allow Azure services" (adds `0.0.0.0/0`)
- Disable public access; create Private Endpoint with Connector's VNet as source
- Verify DNS resolves to private IP

**Step 2 – Create Twingate Resource**
- Host: `<servername>.database.windows.net`
- Port: `1433`
- Assign to relevant user group(s)

**Step 3 – Connect**
```bash
sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
```
Compatible with Azure Data Studio, SSMS, or any SQL client.

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default port | `1433` |
| Host format | `<servername>.database.windows.net` |
| Private Endpoint source | Connector's VNet |

**Database-level firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

## Self-Hosted SQL Server on Azure VMs
- Assign VM a private IP; deploy Connector in same VNet
- Allow inbound DB port from Connector's private IP in NSG/host firewall
- Create Twingate Resource using VM's private IP and port

## Gotchas
- `Allow Azure services` setting adds `0.0.0.0/0` — disable unless intentional
- Azure SQL checks **database-level** firewall rules first, then server-level
- 256 server-level rule limit — migrate to database-level or CIDR blocks if exceeded
- Port 1433 must be open on local firewall and corporate proxies
- DNS resolution failures: ensure DNS hosted zone is tied to VPC and reachable from Connector
- If no activity shows in Admin Console, check for conflicting VPN intercepting traffic

## Troubleshooting Reference
| Symptom | Cause | Fix |
|---------|-------|-----|
| Firewall denial | Connector IP not allowlisted | Add to server- or database-level rule |
| DNS Failed | Connector can't resolve hostname | Verify DNS zone/server reachability |
| Connection Failed | No route or port blocked | Check NSG, firewall, IP allowlists |
| No Activity | Client not routing traffic | Verify Client running, Resource access granted, no VPN conflict |

## Related Docs
- [AWS Database Access](https://www.twingate.com/docs/database-access-aws)
- [GCP Database Access](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting](https
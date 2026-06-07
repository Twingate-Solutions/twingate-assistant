# Azure SQL Database Access with Twingate

## Summary
Twingate secures access to Azure SQL Database and other Azure-managed/self-hosted databases by routing traffic through Connectors, eliminating the need for public database exposure. Supports both Private Endpoint (preferred) and public endpoint with IP allowlisting approaches.

## Key Information
- Supports Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on VMs
- Private Endpoint is strongly preferred: traffic stays on Microsoft's internal backbone, no public IP allowlisting needed
- Connector placement inside the same VNet as the database is required for private connectivity
- Azure SQL firewall checks database-level rules before server-level rules

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- For private endpoints: Connector deployed **inside the same VNet** as the database
- For public endpoints: Connector's public egress IP address captured for allowlisting
- Azure SQL Database instance or self-hosted SQL Server on Azure VM

## Step-by-Step (Azure SQL Database)

**Step 1 – Configure Azure Private Connectivity**
1. Disable "Allow Azure services" (adds `0.0.0.0/0` — too broad)
2. Disable public access on the DB server
3. Create a Private Endpoint with Connector's VNet as source, DB as destination
4. Verify DNS resolves to private IP address

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
| Default SQL port | `1433` |
| Azure SQL host format | `<servername>.database.windows.net` |
| Public endpoint firewall rule | Start IP = End IP = Connector public IP |

**Database-level firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

## Self-Hosted SQL Server on Azure VMs
- Assign VM a private IP; deploy Connector in same VNet
- Allow inbound DB port traffic from Connector's private IP in NSG/host firewall
- Create Twingate Resource using VM's private IP and port

## Gotchas
- "Allow Azure services" adds `0.0.0.0/0` — disable unless intentional
- Server-level firewall limit: **256 rules max**; use database-level rules or CIDR aggregation if exceeded
- Port 1433 must be open on local firewalls and corporate proxies
- **DNS Failed** in Activity log = Connector can't resolve hostname; check DNS zone is VNet-linked
- **Connection Failed** = Connector reached destination but was blocked; verify IP allowlists and security group rules
- **No Activity** = Client not capturing traffic; check Client is running and no VPN conflict

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Microsoft: Configure server-level IP firewall rule](https://learn.microsoft.com/azure/azure-sql/database/firewall-configure)
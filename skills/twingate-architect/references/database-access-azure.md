# Azure SQL Database Access with Twingate

## Summary
Configure Twingate to provide secure private access to Azure SQL Database and other Azure-managed databases. Traffic routes through Connectors deployed in your VNet, enabling firewall restrictions without public database exposure. Supports both Private Endpoint (preferred) and public endpoint configurations.

## Key Information
- Supports Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on VMs
- Private Endpoint is preferred: traffic stays on Microsoft's internal backbone, no public IP allowlisting needed
- Azure SQL Database uses IP-based firewall rules; Connectors must be allowlisted when using public endpoints
- Default port: **1433** for SQL Server/Azure SQL

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- Connector placement: **inside the same VNet** as the database (for private endpoints)
- Azure SQL Database instance or self-hosted SQL Server on Azure VM

## Step-by-Step (Azure SQL Database)

### Private Endpoint Setup (Recommended)
1. Disable **Allow Azure services** in SQL Server networking settings
2. Create a Private Endpoint with Connector's VNet as source, DB as destination
3. Verify database server is configured to use Private Endpoint
4. Create Twingate Resource: host = `<servername>.database.windows.net`, port = `1433`
5. Assign Resource to relevant user groups

### Connect
```bash
sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
```
Also works with Azure Data Studio, SSMS, or any SQL client.

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Host | `<servername>.database.windows.net` |
| Port | `1433` |
| Firewall rule scope | Server-level or database-level |

**Database-level firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

## Self-Hosted SQL Server on Azure VMs
- Assign VM a private IP; deploy Connector in the same VNet
- Allow inbound DB port from Connector's private IP in NSG/host firewall
- Create Twingate Resource using VM's private IP and port

## Gotchas
- `Allow Azure services` setting adds `0.0.0.0/0` — disable unless all Azure resources need access
- Azure SQL checks **database-level firewall rules first**, then server-level
- Server-level rule limit: **256 rules** — use database-level rules or CIDR aggregation if exceeded
- Port 1433 must be open on local firewall and corporate proxies
- **DNS Failed** in Activity logs: DNS hosted zone not tied to VPC or no route from Connector to DNS server
- **No Activity** in logs: Client not running, missing Resource access, or another VPN intercepting traffic

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Microsoft: Configure server-level IP firewall rule](https://docs.microsoft.com/azure/azure-sql/database/firewall-configure)
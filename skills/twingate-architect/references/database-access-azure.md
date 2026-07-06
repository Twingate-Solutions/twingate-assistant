# Azure SQL Database Access with Twingate

## Summary
Configure Twingate to provide secure private access to Azure SQL Database and other Azure-managed databases. Connectors route traffic through private endpoints or allowlisted public IPs, eliminating direct public database exposure.

## Key Information
- Supports Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on VMs
- Preferred approach: Azure Private Endpoint keeps all traffic on Microsoft's internal backbone
- Connector placement inside the same VNet as the database eliminates need for public IP allowlisting
- Azure SQL firewall checks database-level rules before server-level rules
- Azure SQL default port: **1433**

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- For private endpoints: Connector deployed **inside the same VNet** as the database
- For public endpoints: Connector's public egress IP address for allowlisting
- Azure SQL Database instance or self-hosted SQL Server on Azure VM

## Step-by-Step (Azure SQL Database)

### Step 1 – Configure Azure Private Connectivity (Recommended)
1. Disable **Allow Azure services** unless all Azure resources need access (adds `0.0.0.0/0`)
2. Create a Private Endpoint: Connector's VNet as source, DB as destination
3. Disable public access on the DB server
4. Verify DNS resolves to private IP

### Step 2 – Create Twingate Resource
- **Host:** `<servername>.database.windows.net` (found in Database → Overview → Server name)
- **Port:** `1433`
- Assign to relevant user groups

### Step 3 – Connect
```bash
sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
```
Compatible with Azure Data Studio, SSMS, or any SQL client.

## Configuration Values

| Parameter | Value |
|---|---|
| Default SQL port | `1433` |
| Azure SQL hostname pattern | `<servername>.database.windows.net` |
| Public access firewall | Start IP = End IP = Connector public IP |

**Database-level firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

## Self-Hosted SQL Server on Azure VMs
- Assign VM a private IP; deploy Connector in same VNet
- Allow inbound DB port in NSGs **from Connector's private IP only**
- Create Twingate Resource using VM's private IP and port

## Gotchas
- `Allow Azure services` setting adds `0.0.0.0/0` — disable unless intentional
- Server-level firewall rules have a **256-rule limit**; use database-level rules or CIDR aggregation if exceeded
- Port 1433 must be open on local firewall and corporate proxies
- **DNS Failed** in activity logs = Connector cannot resolve hostname; verify DNS zone is tied to VNet
- **Connection Failed** = Connector reached destination but was blocked; check IP allowlists and security groups
- **No Activity** = Client not sending traffic; check Client is running and no other VPN is intercepting

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Microsoft: Configure server-level IP firewall rule](https://docs.microsoft.com/azure/azure-sql/database/firewall-configure)
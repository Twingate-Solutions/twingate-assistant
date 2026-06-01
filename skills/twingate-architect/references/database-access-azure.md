# Azure SQL Database Access with Twingate

## Summary
Configure Twingate to provide secure access to Azure SQL Database and other Azure-managed databases by routing traffic through Connectors. Supports both Private Endpoint (preferred) and public endpoint configurations with IP allowlisting.

## Key Information
- Supports Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on VMs
- Private Endpoint is strongly preferred: traffic stays on Microsoft's internal backbone, no public IP allowlisting needed
- Connector must be deployed in the same VNet as the database for private connectivity
- Public endpoint requires allowlisting each Connector's egress IP in Azure firewall rules

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- For private endpoints: Connector inside same VNet as database
- For public endpoints: Connector's public IP addresses available for allowlisting
- Azure SQL Database instance or self-hosted SQL Server on Azure VM

## Step-by-Step (Azure SQL Database)

**Step 1 – Configure Azure Private Connectivity**
- Disable "Allow Azure services" (adds `0.0.0.0/0` implicitly)
- Create Private Endpoint with Connector's VNet as source, DB as destination
- Verify DNS resolves to private IP address

**Step 2 – Create Twingate Resource**
- Host: `<servername>.database.windows.net`
- Port: `1433`
- Assign to relevant user groups

**Step 3 – Connect**
```bash
sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
```
Also works with Azure Data Studio, SSMS, or any SQL client.

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default port | `1433` |
| Host format | `<servername>.database.windows.net` |

**Database-level firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

## Self-Hosted SQL Server on Azure VMs
- Assign VM a private IP; deploy Connector in same VNet
- Allow inbound DB port from Connector's private IP in NSGs/host firewall
- Create Twingate Resource using VM's private IP and port

## Gotchas
- Azure SQL checks **database-level** firewall rules before server-level rules
- Server-level rules cap at **256 rules**; use database-level rules or CIDR aggregation if exceeded
- Disabling "Allow Azure services" removes implicit `0.0.0.0/0` — do this before restricting access
- **DNS Failed** in activity logs = Connector can't resolve hostname; verify DNS zone is tied to VPC
- **Connection Failed** = Connector reached destination but was blocked; check IP allowlists and security group rules
- **No Activity** = Client not running, no resource access, or another VPN intercepting traffic

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Microsoft: Configure server-level IP firewall rule](https://docs.microsoft.com/azure/azure-sql/database/firewall-configure)
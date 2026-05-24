# Azure SQL Database Access with Twingate

## Summary
Secure Azure SQL Database and other Azure-managed databases by routing traffic through Twingate Connectors instead of exposing public endpoints. Supports both Private Endpoint (preferred) and public endpoint with IP allowlisting. Works for managed databases (Azure SQL, Cosmos DB, PostgreSQL/MySQL) and self-hosted SQL Server on Azure VMs.

## Key Information
- Twingate Connectors act as secure proxies; Azure firewalls see only Connector IP addresses
- Private Endpoint is strongly preferred: traffic stays on Microsoft's internal backbone, no public IP allowlisting needed
- Azure SQL Database uses port **1433**
- Server-level firewall rules apply to all databases; database-level rules are more granular
- 256 server-level rule limit applies; use database-level rules or CIDR aggregation if exceeded

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- For Private Endpoint: Connector deployed **inside the same VNet** as the database
- For public endpoint: Connector's public egress IP address captured for allowlisting
- Azure SQL Database instance or self-hosted SQL Server on Azure VM

## Step-by-Step (Azure SQL Database)

**Step 1 – Configure Azure Private Connectivity**
- Disable "Allow Azure services" (avoids adding `0.0.0.0/0`)
- Preferred: Create a Private Endpoint with Connector's VNet as source, DB as destination
- Disable public access on DB server
- Verify DNS resolves to private IP

**Step 2 – Create Twingate Resource**
- Host: `<servername>.database.windows.net` (from Database → Overview → Server name)
- Port: `1433`
- Assign to relevant user groups

**Step 3 – Connect**
```bash
sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
```
Compatible with Azure Data Studio, SSMS, or any SQL client.

## Configuration Values
| Setting | Value |
|---|---|
| Default DB port | `1433` |
| Azure SQL host format | `<servername>.database.windows.net` |
| Firewall rule scope (public) | Start IP = End IP = Connector public IP |

**Database-level firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

## Self-Hosted SQL Server on VMs
- Assign VM a private IP; deploy Connector in same VNet
- Allow inbound DB port from Connector's private IP in NSG/host firewall
- Create Twingate Resource using VM's private IP and port

## Gotchas
- Disabling "Allow Azure services" removes `0.0.0.0/0`—required for proper lockdown
- Azure SQL checks database-level firewall rules **before** server-level rules
- Exceeding 256 server-level rules requires migration to database-level rules or CIDR aggregation
- Port 1433 must be open on local firewall and corporate proxies
- If no activity in Twingate logs: check Client is running, access is granted, no VPN conflict
- DNS Failed in logs = Connector cannot resolve hostname; verify DNS zone is tied to VNet

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting](https://www.twingate.com/docs/troubleshooting)
- [Microsoft: Configure server-level IP firewall rule](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure)
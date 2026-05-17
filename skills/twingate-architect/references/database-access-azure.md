# Azure SQL Database Access with Twingate

## Summary
Securely connect to Azure SQL Database and other Azure-managed databases by routing traffic through Twingate Connectors. Supports both private endpoint (recommended) and public endpoint configurations with IP allowlisting.

## Key Information
- Connectors act as secure proxies; Azure SQL sees only the Connector's egress IP
- Private Endpoint is preferred: traffic stays on Microsoft's internal backbone, no public IP allowlisting needed
- Supports Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on VMs
- Azure SQL checks database-level firewall rules before server-level rules
- Server-level firewall rule limit: 256 rules max

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- For Private Endpoint: Connector deployed **inside the same VNet** as the database
- For public endpoint: Connector's public egress IP captured for allowlisting
- Azure SQL Database instance or self-hosted SQL Server on Azure VM

## Step-by-Step (Azure SQL Database)

1. **Configure Private Connectivity** — Disable *Allow Azure services* (adds `0.0.0.0/0`); create Private Endpoint with Connector's VNet as source, DB as destination; disable public access
2. **Create Twingate Resource**
   - Host: `<servername>.database.windows.net`
   - Port: `1433`
   - Assign to relevant user group(s)
3. **Connect** via Twingate Client using `sqlcmd`, Azure Data Studio, SSMS, or any SQL client

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Default port | `1433` |
| Host format | `<servername>.database.windows.net` |
| Public endpoint firewall | Start IP = End IP = Connector public IP |

**Database-level firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

**Test connection:**
```bash
sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
```

## Self-Hosted SQL Server on Azure VMs
- Assign VM a private IP; deploy Connector in same VNet
- Allow inbound DB port from Connector's private IP in NSG/host firewall
- Create Twingate Resource using VM's private IP and port

## Gotchas
- Enabling *Allow Azure services* adds `0.0.0.0/0` — avoid unless intentional
- Exceeding 256 server-level rules requires moving to database-level rules or aggregating IPs into CIDRs
- Port 1433 must be open on local firewall and corporate proxies
- **DNS Failed** in Activity logs = Connector can't resolve hostname (check DNS zone/routing)
- **Connection Failed** = Connector reached but can't connect to DB (check IP allowlists, security groups)
- **No Activity** = Client not sending traffic (check Client is running, no conflicting VPN)

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Microsoft: Configure server-level IP firewall rule](https://docs.microsoft.com/azure/azure-sql/database/firewall-configure)
- [Microsoft: Azure Private Endpoint docs](https://docs.microsoft.com/azure/private-link/private-endpoint-overview)
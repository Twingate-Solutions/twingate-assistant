# Azure SQL Database Access with Twingate

## Summary
Configure Twingate to provide secure access to Azure SQL Database and other Azure-managed/self-hosted databases. Twingate Connectors route traffic through private networks, eliminating public database exposure. Supports both Private Endpoint (preferred) and public endpoint configurations.

## Key Information
- Works with Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on VMs
- Private Endpoint is strongly preferred: traffic stays on Microsoft's internal backbone, no public IP allowlisting needed
- Connector must be deployed inside the same VNet as the database
- Azure SQL default port: **1433**
- Azure SQL firewall checks database-level rules before server-level rules

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- Connector placed **inside the same VNet** as the database (for Private Endpoint)
- Azure SQL Database instance or self-hosted DB on Azure VM

## Step-by-Step (Azure SQL with Private Endpoint)

1. **Disable public access** on the Azure SQL Server (uncheck "Allow Azure services" unless needed — adds `0.0.0.0/0`)
2. **Create Private Endpoint** — source: Connector's VNet; destination: DB server
3. **Verify DNS** resolves to private IP address
4. **Create Twingate Resource**:
   - Host: `<servername>.database.windows.net`
   - Port: `1433`
   - Assign to relevant user group(s)
5. **Connect** with Twingate Client running:
   ```bash
   sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
   ```

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
- **"Allow Azure services"** checkbox adds `0.0.0.0/0` — disable unless intentional
- **256 server-level rule limit** — exceed it by using database-level rules or CIDR aggregation
- With public endpoint, Azure SQL sees only the **Connector's public egress IP** (not the user's IP)
- If using Private Endpoint, skip public IP allowlisting entirely
- `No Activity` in logs = Client not sending traffic (check Client is running, no conflicting VPN)
- `DNS Failed` = Connector can't resolve hostname (check DNS zone binding to VNet)
- `Connection Failed` = Connector reached but DB unreachable (check NSG/firewall rules, port 1433)

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Microsoft: Configure server-level IP firewall rule](https://docs.microsoft.com/azure/azure-sql/database/firewall-configure)
- [Microsoft: Azure Private Endpoint docs](https://docs.microsoft.com/azure/private-link/private-endpoint-overview)
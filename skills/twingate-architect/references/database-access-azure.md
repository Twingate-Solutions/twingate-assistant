# Azure SQL Database Access with Twingate

## Summary
Configure Twingate to provide secure access to Azure SQL Database and other Azure-managed/self-hosted databases. Twingate Connectors route traffic through private networks, eliminating public database exposure. Supports both Private Endpoint (recommended) and public endpoint configurations.

## Key Information
- Preferred approach: Azure Private Endpoint keeps all traffic on Microsoft's internal backbone
- Connector placement determines connectivity model (private IP vs. public IP allowlisting)
- Default SQL Server port: **1433**
- Azure SQL firewall checks database-level rules before server-level rules
- Server-level firewall limit: 256 rules maximum

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- Azure SQL Database instance or self-hosted SQL Server on Azure VM
- For private endpoint: Connector deployed inside the same VNet as the database
- For public endpoint: Connector's public egress IP address identified

## Step-by-Step (Azure SQL Database with Private Endpoint)

1. **Disable public access** on the Azure SQL Server (`Networking` settings)
2. **Create Private Endpoint** — source: Connector's VNet; destination: DB server
3. **Verify DNS** resolves the server hostname to a private IP address
4. **Create Twingate Resource**:
   - Host: `<servername>.database.windows.net`
   - Port: `1433`
   - Assign to relevant user groups
5. **Connect** with Twingate Client running:
   ```bash
   sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
   ```

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Default port | `1433` |
| Resource host | `<servername>.database.windows.net` |
| Database-level firewall T-SQL | `sp_set_database_firewall_rule` |

**Public endpoint firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

## Self-Hosted VMs
- Assign VM a private IP; deploy Connector in the same VNet
- Allow inbound DB port from Connector's private IP in NSG/host firewall
- Create Twingate Resource using VM's private IP and port

## Gotchas
- `Allow Azure services` setting adds `0.0.0.0/0` — disable unless all Azure resources need access
- Azure SQL firewall sees only the **Connector's** public IP, not the client's IP
- Exceeding 256 server-level rules requires moving to database-level rules or CIDR aggregation
- **DNS Failed** in activity logs = Connector can't resolve hostname; check DNS zone association
- **Connection Failed** = Connector reached destination but was blocked; verify IP allowlists and firewall ports
- **No Activity** = Client not sending traffic; check Client is running and no other VPN intercepting

## Related Docs
- [Twingate SaaS App Gating](https://www.twingate.com/docs/)
- [Connector Best Practices](https://www.twingate.com/docs/)
- [Microsoft: Configure server-level IP firewall rules](https://docs.microsoft.com/azure/azure-sql/database/firewall-configure)
- [Azure Private Endpoint documentation](https://docs.microsoft.com/azure/private-link/private-endpoint-overview)
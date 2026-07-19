# Azure SQL Database Access with Twingate

## Summary
Twingate secures access to Azure-managed databases (Azure SQL, Cosmos DB, PostgreSQL/MySQL/MariaDB) and self-hosted databases on Azure VMs by routing traffic through Connectors. Databases remain on private networks with no public exposure. Preferred approach uses Azure Private Endpoints to keep all traffic on Microsoft's internal backbone.

## Key Information
- Connectors act as the sole network ingress point to databases
- Azure Private Endpoint is strongly preferred: no public IP allowlisting needed, traffic stays internal
- Azure SQL firewall sees only the Connector's public egress IP (not the user's IP)
- Database-level firewall rules checked before server-level rules in Azure SQL

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- For Private Endpoint: Connector in same VNet as database
- For public endpoint: Connector's public egress IP address known for allowlisting
- Azure SQL Database or self-hosted SQL Server on Azure VM

## Step-by-Step (Azure SQL Database)

1. **Configure Private Connectivity** — Disable "Allow Azure services" (avoids 0.0.0.0/0 rule). Create Private Endpoint with Connector's VNet as source, DB as destination. Disable public access.

2. **Create Twingate Resource**
   - Host: `<servername>.database.windows.net`
   - Port: `1433`
   - Assign to relevant user groups

3. **Connect** with Twingate Client running:
   ```bash
   sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
   ```
   Or use Azure Data Studio, SSMS, or any SQL client.

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Default port | `1433` |
| Host format | `<servername>.database.windows.net` |
| Public endpoint firewall rule | Start IP = End IP = Connector's public IP |

**Database-level firewall rule (T-SQL):**
```sql
EXECUTE sp_set_database_firewall_rule
  @name = N'TwingateConnector',
  @start_ip_address = '1.2.3.4',
  @end_ip_address = '1.2.3.5';
```

## Gotchas
- "Allow Azure services" setting adds `0.0.0.0/0` — disable unless all Azure resources need access
- Azure SQL server-level rules capped at **256 rules** — use database-level rules or CIDR aggregation if exceeded
- Port 1433 must be open on local firewall and corporate proxies
- If using Private Endpoint, verify DNS resolves to private IP (not public)
- No Activity in logs = Client not sending to Connector (check Client running, resource access granted, no conflicting VPN)
- DNS Failed = Connector can't resolve hostname — ensure DNS hosted zone is tied to VNet

## Self-Hosted VMs (SQL Server, PostgreSQL, MySQL, MongoDB)
- Assign VM a private IP; deploy Connector in same VNet
- Allow inbound DB port from Connector's private IP in NSGs/host firewall
- Create Twingate Resource with VM's private IP and port
- No public IP exposure needed

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting](https://www.twingate.com/docs/troubleshooting)
- [Microsoft: Configure server-level IP firewall rule](https://docs.microsoft.com/azure/azure-sql/database/firewall-configure)
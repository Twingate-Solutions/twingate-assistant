## Azure SQL Database Access with Twingate

Twingate routes traffic to Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on Azure VMs through secure Connectors. The recommended approach is Private Endpoint with the Connector inside the same VNet, eliminating any public exposure. When private connectivity is not possible, the Connector's public egress IP is allowlisted in Azure firewall rules.

**Key Information**
- Default port: 1433 (Azure SQL, SQL Server); use appropriate port for other engines
- Resource hostname: `<servername>.database.windows.net` (found under DB Overview -> Server name)
- Private Endpoint: Connector connects via private IP inside VNet; disable "Allow Azure services" (adds 0.0.0.0/0)
- Public endpoint: add Connector public IP as server-level or database-level firewall rule
- Server-level rules apply to all databases on the server; database-level rules require T-SQL
- Maximum 256 server-level firewall rules; use CIDR aggregation or database-level rules if exceeded
- Self-hosted on Azure VMs: assign private IP to VM, NSG rule from Connector private IP, no public IP needed

**Prerequisites**
- Remote Network and Connector deployed (inside same VNet for private endpoint path)
- Azure SQL Database or self-hosted SQL Server running in Azure
- Connector private IP (for Private Endpoint) or public IP (for firewall rules)

**Step-by-Step**
1. Configure Azure Private Connectivity: disable "Allow Azure services", create Private Endpoint with Connector's VNet as source
2. Create Twingate Resource: host = `<server>.database.windows.net`, port 1433, assign to user groups
3. Connect: `sqlcmd -S myserver.database.windows.net -U <user> -P <pass> -d <db>`

**Configuration Values**
- T-SQL database-level rule: `EXECUTE sp_set_database_firewall_rule @name=N'TwingateConnector', @start_ip_address='1.2.3.4', @end_ip_address='1.2.3.4'`
- Private Endpoint DNS: verify DNS resolves to private IP, not public FQDN

**Gotchas**
- Enabling "Allow Azure services" effectively opens 0.0.0.0/0 -- disable it
- Azure checks database-level firewall rules before server-level rules
- Server-level rule limit is 256; plan for CIDR aggregation early on large deployments
- Use Azure Data Studio, SSMS, or any SQL client -- no special Twingate config needed in the client

**Related Docs**
- /docs/database-access-guide
- /docs/database-access-aws
- /docs/saas-app-gating

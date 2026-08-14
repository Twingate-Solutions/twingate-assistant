---
source: https://www.twingate.com/docs/database-access-azure
type: docs
fetched: 2026-08-14
source_version: 0b29e8cd2a0bf19b25383a5a872c3d9a488414c346785e6b77ab1a0f095b4ebe
---

# Azure SQL Database Access with Twingate

## Summary
Twingate secures access to Azure SQL Database and other Azure-managed/self-hosted databases by routing traffic through Connectors deployed in your VNet. Supports both Private Endpoint (recommended) and public endpoint configurations with IP allowlisting.

## Key Information
- Supports Azure SQL Database, Cosmos DB, PostgreSQL/MySQL/MariaDB, and self-hosted SQL Server on VMs
- Private Endpoint is strongly preferred: traffic stays on Microsoft's internal backbone, no public IP allowlisting needed
- Connector must be in the same VNet as the database for private connectivity
- Azure SQL default port: **1433**

## Prerequisites
- Twingate Remote Network created with at least one Connector deployed
- For private endpoints: Connector deployed inside same VNet as the database
- For public endpoints: Connector's public egress IP captured for allowlisting
- Azure SQL Database or self-hosted DB instance

## Step-by-Step (Azure SQL Database)

1. **Configure Private Connectivity** — Disable "Allow Azure services" (avoids `0.0.0.0/0`), create Private Endpoint with Connector's VNet as source and DB as destination, verify DNS resolves to private IP

2. **Create Twingate Resource**
   - Host: `<servername>.database.windows.net`
   - Port: `1433`
   - Assign to relevant user groups

3. **Connect** with Twingate Client running:
   ```bash
   sqlcmd -S myserver.database.windows.net -U <username> -P <password> -d <database>
   ```
   Also works with Azure Data Studio, SSMS, or any SQL client.

## Configuration Values
| Setting | Value |
|---|---|
| SQL Server Port | `1433` |
| Host format | `<servername>.database.windows.net` |
| Database-level firewall rule | `sp_set_database_firewall_rule` T-SQL stored procedure |
| Server-level firewall rule | Start IP = End IP = Connector's public IP |

## Self-Hosted SQL Server on Azure VMs
- Assign VM a private IP; deploy Connector in same VNet
- Allow inbound DB port from Connector's private IP in NSG/host firewall
- Create Twingate Resource using VM's private IP and port

## Gotchas
- `Allow Azure services` toggle adds `0.0.0.0/0` — disable it unless all Azure resources need access
- Azure SQL checks **database-level** firewall rules before server-level rules
- Server-level rules capped at **256**; use database-level rules or CIDR aggregation if exceeded
- Port 1433 must be open on local firewall and corporate proxies
- **DNS Failed** in Activity = Connector can't resolve hostname; check DNS zone binding to VNet
- **Connection Failed** = Connector reached but can't connect; check IP allowlists and security group rules
- **No Activity** = Client not routing to Connector; check Client running, Resource access, no conflicting VPN

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/aws-database-access)
- [GCP Database Access Guide](https://www.twingate.com/docs/gcp-database-access)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Microsoft: Configure server-level IP firewall rule](https://docs.microsoft.com/azure/azure-sql/database/firewall-configure)
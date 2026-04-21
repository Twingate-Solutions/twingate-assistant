## Database Access with Twingate -- General Guide

This index page describes two generic database access patterns (private and public/SaaS) and links to cloud-specific and database-specific guides. It also covers GUI client setup with DBeaver and SSMS, and a shared troubleshooting section that applies across all database types.

**Key Information**
- Two patterns:
  - **Private/self-hosted**: Connector and database share a private network; use Connector private IP in firewall/security group rules; Resource uses private IP or internal DNS
  - **Public/SaaS**: database reachable only via public internet (e.g. Atlas, RDS public endpoint); use Connector public IP in IP access lists; prefer PrivateLink/PSC when available
- GUI clients work without any special Twingate configuration: DBeaver (open-source, multi-database) and SSMS (SQL Server)
- Recent Activity in Admin Console is the primary troubleshooting tool: DNS Failed, Connection Failed, No Activity

**Prerequisites**
- Remote Network and Connector deployed in the appropriate network
- Connector private IP (for private databases) or public IP (for SaaS/public endpoints)

**Step-by-Step (Private)**
1. Create Twingate Resource using private IP or internal DNS of database
2. Note Connector private IP from Connectors page
3. Configure firewall/security group to allow Connector private IP on database port

**Step-by-Step (Public/SaaS)**
1. Create Twingate Resource for public database hostname and management endpoints
2. Note Connector public IP from Connectors page
3. Add Connector public IP to database service IP access list or network policy

**Configuration Values**
- DBeaver: Database -> New Database Connection -> enter hostname, credentials -> Test Connection
- SSMS: Connect -> Database Engine -> enter Server Name -> choose auth method -> Connect

**Gotchas**
- Use Connector private IP whenever possible -- keeps traffic off the public internet and removes public IP allowlist management
- Switch to public IP only when the managed service has no private connectivity option
- DNS Failed in Recent Activity means the Connector can reach the network but cannot resolve the hostname -- check the DNS zone is associated with the VPC and accessible from the Connector

**Related Docs**
- /docs/database-access-aws
- /docs/database-access-gcp
- /docs/database-access-azure
- /docs/database-access-oracle
- /docs/database-access-mongodb
- /docs/troubleshooting-guide

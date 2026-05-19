# Database Access with Twingate

## Summary
Index page for Twingate database access guides covering private/self-hosted and SaaS databases. Explains the two core connectivity patterns (private IP vs. public egress IP) and links to service-specific guides. Also covers GUI client setup and connection troubleshooting.

## Key Information
- **Private/self-hosted DB**: Use Connector's **private IP** in firewall/security group rules; never expose public IPs
- **SaaS/public DB**: Use Connector's **public egress IP** in service IP allowlists (MongoDB Atlas, RDS public, Snowflake, Redis Cloud, etc.)
- **Prefer private connectivity** (AWS PrivateLink, VPC endpoints) over public when provider supports it
- Connector IP addresses are visible on the **Connectors page** in the Admin Console
- GUI clients (DBeaver, SSMS) work transparently once Twingate Client is active and Resource is defined

## Prerequisites
- Remote Network configured
- Connector deployed inside target network
- Twingate Resource created for the database endpoint (IP or internal DNS name)
- Twingate Client active on end-user machine

## Step-by-Step: Private Database Access
1. Create a Twingate Resource for the DB endpoint (e.g., `10.0.1.15` or `db.internal.example.com`)
2. Get Connector's private IP from Admin Console → Connectors page
3. Add Connector private IP to DB host firewall/security group on the appropriate port

## Step-by-Step: Public/SaaS Database Access
1. Create a Twingate Resource for the public endpoint (e.g., `cloud.mongodb.com`, `rds.amazonaws.com`)
2. Get Connector's public egress IP from Admin Console → Connectors page
3. Add Connector public IP to service's IP access list / network policy / firewall rules

## Configuration Values
| Item | Notes |
|------|-------|
| Connector private IP | Found on Connectors page; use for same-VPC/network DBs |
| Connector public IP | Found on Connectors page; use for SaaS/public DBs |
| Resource hostname | Private IP, internal DNS, or public FQDN depending on setup |

## Troubleshooting
| Symptom | Cause/Fix |
|---------|-----------|
| **Connection Refused** | Connector IP not in DB allowlist |
| **Slow Connections** | Check Connector health; verify no blocking firewall rules |
| **Timeouts** | Connector offline or misconfigured |
| **DNS Failed** (Recent Activity) | Connector can't resolve hostname; check DNS zone/VPC binding or DNS Resource definition |
| **Connection Failed** (Recent Activity) | Connector reached but can't connect to DB; verify routes, IP allowlists, port rules |
| **No Activity** (Recent Activity) | Client not running, no Resource access, or another VPN intercepting traffic |

## Gotchas
- If another VPN is active, it may intercept traffic before Twingate Client can route it
- For DBeaver/SSMS: Twingate Client must be running **before** launching the client tool
- Management endpoints (e.g., `rds.amazonaws.com`) may need their own Twingate Resource separate from the DB endpoint

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/aws-database-access)
- [GCP Database Access Guide](https://www.twingate.com/docs/gcp-database-access)
- [Azure Database Access Guide](https://www.twingate.com/docs/azure-database-access)
- [MongoDB Access Guide](https://www.twingate.com/docs/mongodb-access)
- [Redis Access Guide](https://www.twingate.com/docs/redis-access)
- [Snowflake Access Guide](https://www.twingate.com/docs/snowflake-access)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- Best Practices for Connector Placement
- Securing Resource Access with Policies
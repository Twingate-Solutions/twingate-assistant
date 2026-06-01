# Database Access with Twingate

## Page Title
Database Access Guide

## Summary
Covers configuring Twingate to securely access private and public/SaaS databases. Uses Connector IP addresses (private or public) added to database allowlists instead of exposing databases publicly. Includes service-specific guides and client tool setup.

## Key Information
- **Private/self-hosted DB**: Use Connector's **private IP** in firewall/security group rules
- **Public/SaaS DB** (RDS public endpoints, Snowflake, Redis Cloud): Use Connector's **public egress IP**
- Where available, prefer private connectivity (AWS PrivateLink, VPC endpoints) over public
- Connector IP addresses visible on the **Connectors page** in Admin Console
- Supported GUI clients: DBeaver (multi-DB), SSMS (SQL Server)

## Prerequisites
- Remote Network defined in Twingate
- Connector deployed within target network
- Twingate Resource created for the database endpoint (IP or DNS name)
- Twingate Client active on user's device

## Step-by-Step (General Setup)

**Private DB:**
1. Create Twingate Resource for DB endpoint (e.g., `10.0.1.15` or `db.internal.example.com`)
2. Find Connector's private IP on Connectors page
3. Add Connector private IP to DB host firewall/security group on required port

**Public/SaaS DB:**
1. Create Twingate Resource for DB endpoint (e.g., `*.rds.amazonaws.com`)
2. Find Connector's public IP on Connectors page
3. Add Connector public IP to DB service's IP access list/network policy

## Configuration Values
| Service | Guide Available |
|---|---|
| AWS RDS/Aurora | Yes |
| GCP Cloud SQL | Yes |
| Azure SQL | Yes |
| Oracle DB | Yes |
| Redis / Redis Cloud | Yes |
| Snowflake | Yes |

## Troubleshooting

| Symptom | Fix |
|---|---|
| Connection Refused | Verify Connector IP (private vs public) is in DB allowlist |
| Slow Connections | Check Connector health; verify no blocking firewall rules |
| Timeouts | Confirm Connectors are online and reachable |
| DNS Failed (Activity log) | Ensure DNS zone tied to VPC; DNS server defined as Resource if self-hosted |
| Connection Failed (Activity log) | Check routing, IP allowlists, port rules on both ends |
| No Activity (Activity log) | Confirm Client running, user has Resource access, no VPN conflict |

## Gotchas
- Do **not** expose public IPs for databases co-located with the Connector in a private network
- If another VPN is running alongside Twingate Client, it may hijack connections (causes "No Activity")
- For SaaS DBs, even if private connectivity exists (PrivateLink), use private IP path—do not default to public

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/aws-database-access)
- [GCP Database Access Guide](https://www.twingate.com/docs/gcp-database-access)
- [Azure Database Access Guide](https://www.twingate.com/docs/azure-database-access)
- [Oracle Database Access Guide](https://www.twingate.com/docs/oracle-database-access)
- [Redis Access Guide](https://www.twingate.com/docs/redis-access)
- [Snowflake Access Guide](https://www.twingate.com/docs/snowflake-access)
- Twingate Troubleshooting Guide
- Best Practices for Connector Placement
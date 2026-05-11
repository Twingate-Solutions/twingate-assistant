# Database Access with Twingate

## Summary
Index page for Twingate database access guides covering private/self-hosted and public/SaaS database configurations. Explains how to route database traffic through Twingate Connectors using either private or public egress IPs depending on database hosting model.

## Key Information
- Two access patterns: **private** (same VPC/network as Connector) and **public** (SaaS/internet-facing databases)
- Private: use Connector's **private IP** in firewall/security group rules
- Public: use Connector's **public egress IP** in database IP allowlists
- Where available, prefer private connectivity (AWS PrivateLink, VPC endpoints) over public internet routing
- Connector IP addresses visible on the **Connectors** page in Admin Console

## Prerequisites
- Remote Network defined in Twingate Admin Console
- Connector deployed inside target network
- Twingate Resource created for database endpoint (IP or DNS name)
- Twingate Client active on user's machine with Resource visible

## General Setup Steps

**Private/Self-hosted Database:**
1. Create Twingate Resource for database endpoint (private IP or internal DNS)
2. Find Connector's private IP on Connectors page
3. Add Connector's private IP to database firewall/security group rules on appropriate port

**Public/SaaS Database:**
1. Create Twingate Resource for database and management endpoints
2. Find Connector's public egress IP on Connectors page
3. Add Connector's public IP to database service's IP allowlist/network policy

## Supported Database Guides
- AWS RDS/Aurora
- GCP Cloud SQL
- Azure SQL Database
- Oracle Database
- MongoDB / MongoDB Atlas
- Redis / Redis Cloud
- Snowflake

## Client Tools
- **DBeaver**: Database → New Database Connection → enter hostname/credentials → Test Connection
- **SSMS**: Connect → Database Engine → enter Server Name → Connect

## Troubleshooting

| Symptom | Fix |
|---|---|
| Connection Refused | Verify Connector IP (private or public) is in database allowlist |
| Slow Connections | Check Connector health; verify no blocking firewall rules |
| Timeouts | Confirm Connectors are online and reachable |
| DNS Failed (Recent Activity) | DNS zone must be tied to VPC; DNS server must be a Twingate Resource if self-hosted |
| Connection Failed (Recent Activity) | Check route exists, IP allowlists correct, ports open on both ends |
| No Activity (Recent Activity) | Client not running, no Resource access, or another VPN intercepting traffic |

## Gotchas
- Use private IP whenever possible; only use public egress IP when the service cannot see your private network
- "No Activity" in Recent Activity means traffic never left the client — check for conflicting VPNs
- DNS resolution failures are distinct from connection failures; check them separately via Recent Activity

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- Best Practices for Connector Placement
- Securing Resource Access with Policies
- How to Ingest Connector Logs into a SIEM
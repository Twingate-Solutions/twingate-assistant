# Database Access Guide

## Summary
Twingate enables secure, zero-trust access to private and cloud-hosted databases by routing connections through Connectors. Setup requires creating a Twingate Resource for the database endpoint and allowing the Connector's IP address in the database's firewall/access list. Private databases use the Connector's private IP; SaaS databases use the Connector's public egress IP.

## Key Information
- **Private/self-hosted databases**: Use Connector's **private IP address** in firewall/security group rules
- **SaaS/public databases** (Atlas, RDS public endpoints, Snowflake, etc.): Use Connector's **public egress IP address**
- Prefer private IP routing whenever possible; use public IP only when required by the service
- Connector IP addresses are visible on the **Connectors page** in Admin Console

## Prerequisites
- Remote Network defined in Twingate
- Connector deployed within the target network
- Twingate Client active on the user's machine
- Database Resource created in Twingate (IP or internal DNS name)

## Step-by-Step (General Setup)

**Private Database:**
1. Create a Resource (private IP like `10.0.1.15` or internal DNS like `db.internal.example.com`)
2. Find Connector's private IP on the Connectors page
3. Add Connector's private IP to database firewall/security group on the appropriate port

**SaaS/Public Database:**
1. Create a Resource for the public endpoint (e.g., `cloud.mongodb.com`)
2. Find Connector's public egress IP on the Connectors page
3. Add Connector's public IP to the database service's IP access list/network policy

## Configuration Values
| Context | Value to Use |
|---|---|
| Private/VPC database | Connector private IP |
| SaaS database (Atlas, Snowflake, Redis Cloud, etc.) | Connector public egress IP |
| AWS PrivateLink/VPC endpoints available | Connector private IP |

## Gotchas
- Do **not** expose public IPs for databases in private networks — route through Connector's private IP only
- If using a VPN alongside Twingate Client, the VPN may hijack connections (check Recent Activity for "No Activity")
- DNS resolution failures at the Connector level require the DNS server to either be a Twingate Resource or reachable from the Connector's network

## Troubleshooting (via Admin Console → Recent Activity)
| Status | Cause | Fix |
|---|---|---|
| DNS Failed | Connector can't resolve hostname | Verify DNS zone/VPC binding or add DNS server as Resource |
| Connection Failed | Connector can't reach destination | Check IP allow lists, routes, firewall rules, port access |
| No Activity | Client not sending traffic | Verify Client is running, Resource access granted, no VPN conflict |
| Connection Refused | IP not in allow list | Add correct Connector IP (private or public) |

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/aws-database-access)
- [GCP Database Access Guide](https://www.twingate.com/docs/gcp-database-access)
- [Azure Database Access Guide](https://www.twingate.com/docs/azure-database-access)
- [Oracle Database Access Guide](https://www.twingate.com/docs/oracle-database-access)
- [MongoDB Access Guide](https://www.twingate.com/docs/mongodb-access)
- [Redis Access Guide](https://www.twingate.com/docs/redis-access)
- [Snowflake Access Guide](https://www.twingate.com/docs/snowflake-access)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- Best Practices for Connector Placement
- Securing Resource Access with Policies
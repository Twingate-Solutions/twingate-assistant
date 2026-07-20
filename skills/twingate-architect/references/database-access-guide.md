# Database Access Guide

## Page Title
Twingate Database Access Guide

## Summary
Covers configuring Twingate for secure database access across cloud and on-premises environments. Uses Connector IP addresses (private or public depending on database hosting) added to database allow lists. Minimal configuration required beyond defining a Remote Network and deploying a Connector.

## Key Information
- **Private/on-prem databases**: Use Connector's **private IP address** in firewall/security group rules
- **SaaS/public databases**: Use Connector's **public egress IP address** in IP access lists
- Find both IP addresses on the **Connectors page** in Admin Console
- Prefer private IP addresses whenever possible to keep traffic internal
- Supported tools: DBeaver (multi-DB GUI), SSMS (SQL Server)

## Prerequisites
- Remote Network defined in Twingate
- Connector deployed within the target network
- Twingate Client active on end-user device
- Resource created in Twingate for the database endpoint

## Step-by-Step

### Private Database Setup
1. Create a Twingate Resource (private IP or internal DNS, e.g., `10.0.1.15` or `db.internal.example.com`)
2. Find Connector's **private IP** on the Connectors page
3. Add private IP to database firewall/security group rules on the correct port

### SaaS/Public Database Setup
1. Create a Twingate Resource for the public endpoint (e.g., `cloud.mongodb.com`)
2. Find Connector's **public IP** on the Connectors page
3. Add public IP to database service's IP access list/network policy

### Client Tool Connection (DBeaver / SSMS)
1. Ensure Connector is active and Resource appears in Client's resource list
2. Enter database hostname, username, password in tool
3. Test connection through tool's built-in test function

## Configuration Values
| Item | Value/Location |
|------|---------------|
| Private IP | Connectors page → private IP field |
| Public egress IP | Connectors page → public IP field |
| Resource hostname | Private IP, internal DNS, or public FQDN |

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Connection Refused | Connector IP not in database allow list |
| Slow Connections | Connector health; blocking firewall rules |
| Timeouts | Connector online and reachable |
| DNS Failed (Recent Activity) | DNS zone tied to VPC; DNS server defined as Resource |
| Connection Failed (Recent Activity) | Route exists Connector→DB; IP allow lists; port open both ends |
| No Activity (Recent Activity) | Client running; Resource access granted; no conflicting VPN |

**Admin Console path for diagnostics**: Admin Console → Resource → Recent Activity

## Gotchas
- Use private IP by default; only switch to public IP when service has no private connectivity option
- If using AWS PrivateLink/VPC endpoints, use private IP even for managed services
- Another VPN running simultaneously can hijack connections (causes "No Activity" in logs)
- DNS resolution must be reachable from the Connector, not just the client

## Related Docs
- AWS Database Access Guide
- GCP Database Access Guide
- Azure Database Access Guide
- Oracle Database Access Guide
- MongoDB Access Guide
- Redis Access Guide
- Snowflake Access Guide
- Twingate Troubleshooting Guide
- Best Practices for Connector Placement
- Securing Resource Access with Policies
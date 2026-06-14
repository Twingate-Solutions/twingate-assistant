# Database Access with Twingate

## Summary
Twingate secures database connections by routing traffic through a Connector deployed in your network, eliminating the need for public database exposure. Supports both private/self-hosted databases (using Connector's private IP) and public/SaaS databases (using Connector's public egress IP). Covers AWS, GCP, Azure, Oracle, Redis, and Snowflake.

## Key Information
- Connector acts as outbound-only proxy; databases never need public exposure for private deployments
- Two access models: **private** (same VPC/network) and **public** (SaaS/managed services)
- Connector IP addresses are visible in the Admin Console → Connectors page
- Use private IP whenever possible; fall back to public IP only when required by the service
- Supported GUI clients: DBeaver (multi-DB) and SSMS (SQL Server)

## Prerequisites
- Remote Network defined in Twingate Admin Console
- Connector deployed within the target network
- Twingate Client active on end-user machine
- Resource created in Twingate for the database endpoint

## Step-by-Step

### Private Database Setup
1. Create a Twingate Resource using private IP (e.g., `10.0.1.15`) or internal DNS (`db.internal.example.com`)
2. Note the Connector's **private IP** from Admin Console → Connectors
3. Update database host/VPC firewall/security group to allow traffic from Connector's private IP on the database port

### Public/SaaS Database Setup
1. Create a Twingate Resource for the database's public endpoint (e.g., `rds.amazonaws.com`)
2. Note the Connector's **public egress IP** from Admin Console → Connectors
3. Add Connector's public IP to the database service's IP access list/network policy/firewall rules

### DBeaver Connection
1. Install DBeaver; ensure Connector is active and Resource appears in Twingate Client
2. Database → New Database Connection → select DB type
3. Enter hostname, username, password → Test Connection → Finish

### SSMS Connection
1. Install SSMS; ensure Connector is active and Resource appears in Twingate Client
2. Connect → Database Engine → enter Server Name and credentials → Connect

## Troubleshooting

| Symptom | Fix |
|---|---|
| **Connection Refused** | Verify Connector IP is in database allow list (private vs. public) |
| **Slow Connections** | Check Connector health; verify no blocking firewall rules |
| **Timeouts** | Confirm Connectors are online and reachable |
| **DNS Failed** (Recent Activity) | Check DNS zone is tied to VPC; DNS server defined as Twingate Resource |
| **Connection Failed** (Recent Activity) | Verify route exists Connector→DB; check IP allow lists and port rules both ends |
| **No Activity** (Recent Activity) | Confirm Client is running, user has Resource access, no other VPN intercepting traffic |

## Gotchas
- If another VPN is active, it may hijack traffic before Twingate captures it (check "No Activity" in Recent Activity)
- SaaS databases that support PrivateLink/VPC endpoints should use private IP even for managed services
- DNS resolution failures mean the Connector—not the client—cannot resolve the hostname

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/aws-database-access)
- [GCP Database Access Guide](https://www.twingate.com/docs/gcp-database-access)
- [Azure Database Access Guide](https://www.twingate.com/docs/azure-database-access)
- [Oracle Database Access Guide](https://www.twingate.com/docs/oracle-database-access)
- [Redis Access Guide](https://www.twingate.com/docs/redis-access)
- [Snowflake Access Guide](https://www.twingate.com/docs/snowflake-access)
- Twingate Troubleshooting Guide
- Best Practices for Connector Placement
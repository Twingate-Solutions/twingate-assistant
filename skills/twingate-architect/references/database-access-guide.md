# Database Access Guide

## Page Title
Database Access Guide - Twingate

## Summary
Twingate enables secure access to private and public/SaaS databases by routing traffic through a Connector deployed in the same network. Configuration requires adding the Connector's IP address (private or public) to the database's firewall/allow list and defining a Twingate Resource for the database endpoint.

## Key Information
- **Private databases**: Use Connector's **private IP address** in firewall/security group rules
- **SaaS/public databases**: Use Connector's **public egress IP address** in IP access lists
- Find both IP addresses on the **Connectors page** in the Admin Console
- Prefer private connectivity (AWS PrivateLink, VPC endpoints) over public when available
- Supported GUIs: DBeaver (multi-DB) and SSMS (SQL Server)

## Prerequisites
- Remote Network defined in Twingate Admin Console
- Connector deployed within target network
- Twingate Resource created for the database endpoint (IP or DNS name)
- Twingate Client active on user device with Resource visible

## Step-by-Step: General Setup

**Private/Self-hosted Database:**
1. Create a Twingate Resource for the database (e.g., `10.0.1.15` or `db.internal.example.com`)
2. Find Connector's **private IP** on the Connectors page
3. Add private IP to database host/VPC firewall rules on the appropriate port

**SaaS/Public Database:**
1. Create a Twingate Resource for the public endpoint (e.g., `cloud.mongodb.com`)
2. Find Connector's **public IP** on the Connectors page
3. Add public IP to database service's IP access list/network policy

## Configuration Values
| Context | Value to Use |
|---|---|
| Private DB / same VPC | Connector private IP |
| SaaS DB (Atlas, RDS public, Snowflake, etc.) | Connector public egress IP |
| DBeaver hostname field | Resource hostname/IP as defined in Twingate |
| SSMS Server Name field | Resource hostname (e.g., `your-db-instance.rds.amazonaws.com`) |

## Gotchas
- **No Activity in logs**: Client isn't sending traffic to Connector — check Client is running, Resource access is granted, no VPN conflict
- **DNS Failed**: Connector can't resolve hostname — verify DNS zone is tied to VPC or DNS server is itself a Twingate Resource
- **Connection Failed**: Connector reached destination but was blocked — verify IP allow lists and port-level firewall rules on both ends
- Never expose database public IPs when private connectivity is available
- SaaS databases that support PrivateLink/VPC endpoints should use private IP instead of public

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
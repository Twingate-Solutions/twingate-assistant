# Database Access with Twingate

## Page Title
Database Access Guide

## Summary
Overview guide for configuring Twingate to secure database connections, covering both private/self-hosted and public/SaaS databases. Explains the two core access patterns (private IP vs. public egress IP) and links to service-specific guides. Includes client tool setup and troubleshooting steps.

## Key Information
- Two access patterns based on database location:
  - **Private/self-hosted**: Use Connector's **private IP** in firewall/security group rules
  - **Public/SaaS**: Use Connector's **public egress IP** in IP access lists/network policies
- Connector private IP visible on the **Connectors page** in Admin Console
- Connector public IP also visible on **Connectors page**
- Supported service-specific guides: AWS RDS/Aurora, GCP Cloud SQL, Azure SQL, Oracle, Redis, Snowflake
- GUI client support: DBeaver (multi-DB) and SSMS (SQL Server)

## Prerequisites
- Remote Network defined in Twingate Admin Console
- Connector deployed within the target network
- Twingate Resource created for the database endpoint (IP or DNS name)
- Twingate Client active on end-user device with Resource visible

## Step-by-Step (General Setup)

**Private Database:**
1. Create a Twingate Resource for the database (e.g., `10.0.1.15` or `db.internal.example.com`)
2. Note the Connector's private IP from the Connectors page
3. Add Connector's private IP to database firewall/security group on the appropriate port

**Public/SaaS Database:**
1. Create a Twingate Resource for the public endpoint (e.g., `rds.amazonaws.com`)
2. Note the Connector's public egress IP from the Connectors page
3. Add public IP to the database service's IP access list/network policy

## Configuration Values
| Context | Value to Use |
|---|---|
| Private/VPC database | Connector private IP |
| SaaS/public database | Connector public egress IP |
| AWS VPC endpoints / PrivateLink available | Use private IP instead |

## Gotchas
- Never expose public IPs for private-network databases — route through Connector private IP only
- If a DNS server is self-hosted, it must also be defined as a Twingate Resource for hostname resolution to work
- Other active VPNs can intercept traffic before it reaches the Twingate Client ("No Activity" in logs)
- "DNS Failed" in Recent Activity = Connector can't resolve hostname; check DNS zone is tied to VPC
- "Connection Failed" = Connector reached destination attempt but was blocked; check both firewall ends and IP allowlists
- "No Activity" = Client never sent traffic; check Client is running and Resource is accessible

## Troubleshooting Quick Reference
- **Connection Refused**: Wrong IP in database allowlist
- **Slow Connections**: Connector health or firewall blocking
- **Timeouts**: Connector offline or misconfigured
- Use **Admin Console → Resource → Recent Activity** for diagnostic events

## Related Docs
- AWS Database Access Guide
- GCP Database Access Guide
- Azure Database Access Guide
- Oracle Database Access Guide
- Redis Access Guide
- Snowflake Access Guide
- Twingate Troubleshooting Guide
- Best Practices for Connector Placement
- Securing Resource Access with Policies
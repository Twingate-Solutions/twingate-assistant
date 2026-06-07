# Database Access with Twingate

## Summary
Overview and index page for configuring Twingate to secure database connections, covering both private/self-hosted and public/SaaS databases. Provides general setup patterns, links to service-specific guides, client tool examples, and troubleshooting steps.

## Key Information
- **Private databases**: Use Connector's **private IP address** in firewall/security group rules
- **Public/SaaS databases**: Use Connector's **public egress IP address** in IP allowlists
- Where providers support PrivateLink/VPC endpoints, prefer private connectivity over public
- Connector IP addresses are visible on the **Connectors page** in the Admin Console
- Both DBeaver and SSMS work as GUI clients once Twingate Client is active

## Prerequisites
- Remote Network configured
- Connector deployed within the target network
- Twingate Resource created for the database endpoint (IP or DNS name)
- Twingate Client active on the user's machine

## General Setup Steps

**Private/Self-hosted Database:**
1. Create a Twingate Resource for the private endpoint (e.g., `10.0.1.15` or `db.internal.example.com`)
2. Note the Connector's private IP from the Connectors page
3. Add Connector's private IP to database firewall/security group on the appropriate port

**Public/SaaS Database:**
1. Create a Twingate Resource for the public endpoint (e.g., `rds.amazonaws.com`)
2. Note the Connector's public egress IP from the Connectors page
3. Add Connector's public IP to the database service's IP allowlist/network policy

## Troubleshooting

| Symptom | Check |
|---|---|
| Connection Refused | Connector IP in database allowlist (private vs. public) |
| Slow Connections | Connector health, firewall rules |
| Timeouts | Connectors online and reachable |
| DNS Failed (Recent Activity) | DNS zone tied to VPC; DNS server defined as Resource |
| Connection Failed (Recent Activity) | Route exists Connector→DB; port open on both ends |
| No Activity (Recent Activity) | Client running; Resource access granted; no conflicting VPN |

## Service-Specific Guides
- AWS RDS/Aurora → AWS Database Access Guide
- Cloud SQL → GCP Database Access Guide
- Azure SQL → Azure Database Access Guide
- Oracle → Oracle Database Access Guide (sqlnet.ora, SQL*Plus)
- Redis → Redis Access Guide (redis-cli, Redis Cloud)
- Snowflake → Snowflake Access Guide (network rules/policies)

## Gotchas
- Never expose database public IPs when Connector is co-located in the same VPC
- A second VPN running alongside Twingate Client may intercept traffic (No Activity symptom)
- For self-hosted DNS, the DNS server itself must be defined as a Twingate Resource

## Related Docs
- Twingate Troubleshooting Guide
- Best Practices for Connector Placement
- Securing Resource Access with Policies
- How to Ingest Connector Logs into a SIEM
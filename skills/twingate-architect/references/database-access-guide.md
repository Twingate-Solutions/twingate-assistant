# Database Access with Twingate

## Summary
Guide for configuring Twingate to securely access private or public databases. Covers general setup patterns for private/VPC-hosted and SaaS databases, plus specific guides for major cloud and database providers.

## Key Information
- Two access patterns: **private** (Connector private IP) and **public/SaaS** (Connector public egress IP)
- Connector acts as outbound-only proxy—no public ports exposed on database host
- Connector IP addresses visible on the **Connectors** page in Admin Console
- Prefer private IP routing whenever possible; use public IP only when service requires internet access
- Supported GUI clients: DBeaver (multi-DB) and SSMS (SQL Server)

## Prerequisites
- Remote Network defined in Twingate Admin Console
- Connector deployed within target network/VPC
- Twingate Client active on end-user device
- Resource created for database endpoint (IP or DNS)

## Step-by-Step

### Private/Self-hosted Database
1. Create Twingate Resource using private IP (e.g., `10.0.1.15`) or internal DNS (`db.internal.example.com`)
2. Get Connector's **private IP** from Connectors page
3. Add Connector private IP to database firewall/security group rules on required port

### Public/SaaS Database
1. Create Twingate Resource for database endpoint (e.g., `rds.amazonaws.com`)
2. Get Connector's **public egress IP** from Connectors page
3. Add Connector public IP to database service's IP access list / network policy

### DBeaver Connection
1. Install DBeaver; ensure Connector active and Resource visible in Client
2. Database → New Database Connection → select DB type
3. Enter hostname, username, password → Test Connection

### SSMS Connection
1. Install SSMS; ensure Connector active and Resource visible in Client
2. Connect → Database Engine → enter Server Name
3. Select Authentication Method → Connect

## Troubleshooting

| Symptom | Check |
|---|---|
| Connection Refused | Connector IP in DB allow list (private vs. public) |
| Slow Connections | Connector health; firewall rules |
| Timeouts | Connectors online and reachable |
| DNS Failed (Recent Activity) | DNS zone tied to VPC; DNS server defined as Resource |
| Connection Failed (Recent Activity) | Route exists Connector→DB; firewall allows port both ends |
| No Activity (Recent Activity) | Client running; Resource access granted; no conflicting VPN |

## Related Docs
- AWS / GCP / Azure / Oracle / Redis / Snowflake Database Access Guides
- Twingate Troubleshooting Guide
- Best Practices for Connector Placement
- Securing Resource Access with Policies
- How to Ingest Connector Logs into a SIEM
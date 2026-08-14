---
source: https://www.twingate.com/docs/database-access-guide
type: docs
fetched: 2026-08-14
source_version: d6940a351bb3b162660813ff93b7430ce0f4620b933c36fea0bca6a93a506631
---

# Database Access Guide

## Page Title
Database Access Guide (Twingate)

## Summary
Covers configuring Twingate for secure database access across cloud and on-premises environments. Uses Connector IP addresses (private or public) added to database allow lists to restrict access. Requires a Remote Network and Connector deployed before configuring database-specific access.

## Key Information
- **Private/self-hosted DBs**: Use Connector's **private IP address** in firewall/security group rules
- **SaaS/public DBs**: Use Connector's **public egress IP address** in IP access lists
- Prefer private IPs whenever possible; use public only when private connectivity isn't available
- Connector IP addresses found on the **Connectors page** in Admin Console
- Supported GUI clients: DBeaver (multi-DB) and SSMS (SQL Server)

## Prerequisites
- Remote Network defined in Twingate Admin Console
- Connector deployed within target network
- Twingate Client active on user's machine
- Resource created in Twingate for the database endpoint

## Step-by-Step (General Setup)

**Private Database:**
1. Create a Twingate Resource (private IP or internal DNS, e.g., `10.0.1.15` or `db.internal.example.com`)
2. Find Connector's private IP on the Connectors page
3. Add Connector's private IP to database host/VPC firewall rules on the appropriate port

**SaaS/Public Database:**
1. Create a Twingate Resource for public endpoints (e.g., `cloud.mongodb.com`, `rds.amazonaws.com`)
2. Find Connector's public IP on the Connectors page
3. Add Connector's public IP to database service's IP access list/network policy

## Configuration Values
- Resource hostname examples: `your-db-instance.rds.amazonaws.com`, `db.internal.example.com`
- Port: database-specific (configure in security group/firewall rules)

## Gotchas
- **DNS Failed**: Connector can't resolve hostname — check DNS zone is tied to VPC or DNS server is a Twingate Resource
- **Connection Failed**: Connector can't reach destination — verify routes, IP allow lists, and firewall rules on both ends
- **No Activity**: Client not sending traffic — check Client is running, Resource access granted, no other VPN intercepting
- **Connection Refused**: Connector IP not in database allow list
- Never expose database public IPs when Connector and DB share a private network

## Database-Specific Guides
- AWS RDS/Aurora → AWS Database Access Guide
- GCP Cloud SQL → GCP Database Access Guide (supports Cloud SQL Auth Proxy)
- Azure SQL → Azure Database Access Guide
- Oracle DB → Oracle Database Access Guide (`sqlnet.ora`, SQL*Plus)
- MongoDB/Atlas → MongoDB Access Guide (`mongosh`)
- Redis/Redis Cloud → Redis Access Guide (`redis-cli`)
- Snowflake → Snowflake Access Guide (network rules/policies)

## Related Docs
- Twingate Troubleshooting Guide
- How to Ingest Connector Logs into a SIEM
- Best Practices for Connector Placement
- Securing Resource Access with Policies
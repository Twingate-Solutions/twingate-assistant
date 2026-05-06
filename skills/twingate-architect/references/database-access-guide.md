# Database Access with Twingate

## Page Title
Database Access Guide

## Summary
Covers configuring Twingate to securely access private and SaaS databases by routing traffic through Connectors. Uses Connector private IP for same-network databases and Connector public egress IP for internet-accessible managed services. Includes guides for AWS, GCP, Azure, Oracle, MongoDB, Redis, and Snowflake.

## Key Information
- **Private/self-hosted DB**: Use Connector's **private IP** in firewall/security group rules
- **SaaS/public DB**: Use Connector's **public egress IP** in IP access lists
- Connector IP addresses visible on the **Connectors page** in Admin Console
- Prefer private connectivity (VPC endpoints, PrivateLink) over public when available
- GUI clients (DBeaver, SSMS) work transparently once Twingate Client is active

## Prerequisites
- Remote Network defined in Twingate Admin Console
- Connector deployed within target network
- Twingate Client active on user device
- Resource created for the database endpoint

## Step-by-Step: Private Database Setup
1. Create a Twingate Resource using private IP (`10.0.1.15`) or internal DNS (`db.internal.example.com`)
2. Find Connector's private IP on the Connectors page
3. Add Connector private IP to database firewall/security group on the appropriate port

## Step-by-Step: SaaS/Public Database Setup
1. Create a Twingate Resource for public endpoints (e.g., `cloud.mongodb.com`, `rds.amazonaws.com`)
2. Find Connector's public egress IP on the Connectors page
3. Add Connector public IP to the database service's IP access list/network policy

## Troubleshooting Reference

| Symptom | Check |
|---|---|
| Connection Refused | Correct IP (private vs. public) in DB allow list |
| Slow Connections | Connector health, firewall rules |
| Timeouts | Connectors online and reachable |
| DNS Failed (Recent Activity) | DNS zone tied to VPC; DNS server defined as Resource |
| Connection Failed (Recent Activity) | Route exists Connector→DB; IP allow lists and port rules correct |
| No Activity (Recent Activity) | Client running; Resource access granted; no conflicting VPN |

## Gotchas
- Using public IP when private is available (or vice versa) is the most common misconfiguration
- If another VPN is active, it may intercept traffic before Twingate Client (causes "No Activity")
- For Oracle: firewall *and* `sqlnet.ora` may both need the Connector IP
- SaaS databases that support PrivateLink (AWS RDS, etc.) should use private IP via that mechanism

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
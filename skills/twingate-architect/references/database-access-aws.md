# AWS Database Access with Twingate

## Summary
Guide for securing access to Amazon RDS, Aurora, and DynamoDB using Twingate Connectors as network intermediaries. Traffic is routed through Connectors deployed in your VPC, eliminating the need to expose database ports to the internet. Security Group rules restrict database access to Connector IPs only.

## Key Information
- Supports RDS, Aurora (MySQL/PostgreSQL), DynamoDB, and self-hosted databases on EC2/on-premises
- Prefer **private IP addresses** of Connectors for Security Group rules when Connector is in same VPC
- Use **Security Group referencing** (Connector's SG) over IP-based rules for resilience and scalability
- DynamoDB has no native IP allowlist; access control requires VPC endpoints + IAM policies
- Aurora: use **cluster endpoint**, not instance endpoint, for failover/load balancing

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed in the target VPC
- AWS permissions to modify Security Groups, VPC endpoints, and IAM policies

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to RDS/Aurora endpoint with appropriate port (3306 MySQL, 5432 PostgreSQL)
2. Note Connector private IP from Admin Console → Connectors page
3. Add inbound Security Group rule on RDS instance allowing Connector private IP on database port
4. Connect via Twingate Client using standard database clients

### DynamoDB
1. Create Twingate Resource for regional endpoint (e.g., `dynamodb.us-east-1.amazonaws.com`) on port 443
2. Create VPC Gateway Endpoint for DynamoDB in your VPC
3. Update VPC endpoint Security Group to allow inbound from Connector private IPs
4. Optionally restrict via IAM policy using `aws:SourceVpce` condition
5. Connect using AWS CLI or SDKs through Twingate Client

## Configuration Values
| Database | Port | Endpoint Pattern |
|----------|------|-----------------|
| MySQL/Aurora MySQL | 3306 | `mydb.cluster-xxxx.us-east-1.rds.amazonaws.com` |
| PostgreSQL/Aurora PostgreSQL | 5432 | `mydb.cluster-xxxx.us-east-1.rds.amazonaws.com` |
| DynamoDB | 443 | `dynamodb.us-east-1.amazonaws.com` |

**IAM Condition Key:** `aws:SourceVpce` — restrict DynamoDB to specific VPC endpoint

## Gotchas
- DynamoDB **cannot** be restricted by IP allowlist; without VPC endpoint, only IAM policies enforce access control
- Connector IP may change during Terraform updates or lifecycle events unless explicitly pinned — prefer Security Group referencing
- DynamoDB VPC endpoint is a **Gateway Endpoint**, not Interface Endpoint — routing is automatic within same VPC/region
- If no VPC endpoint is created, DynamoDB is still accessible via public endpoint (weaker security posture)
- `No Activity` in Recent Activity means Client isn't forwarding traffic — check Client is running and no other VPN is active

## Troubleshooting
- **DNS Failed**: Connector can't resolve hostname — check DNS hosted zone is VPC-associated
- **Connection Failed**: Connector reached but can't connect to DB — verify IP allowlist and Security Group port rules
- **No Activity**: Client not sending traffic — verify Client running, Resource access granted, no conflicting VPN

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- GCP Database Guide
- Azure Database Guide
- Connector Best Practices
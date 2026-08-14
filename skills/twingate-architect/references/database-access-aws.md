---
source: https://www.twingate.com/docs/database-access-aws
type: docs
fetched: 2026-08-14
source_version: e94e2da0299c06a1719d5e62823a1414832d01746839074e883f2360971f4d70
---

# AWS Database Access with Twingate

## Page Title
AWS Database Access with Twingate (RDS, Aurora, DynamoDB)

## Summary
Twingate routes private traffic to AWS databases without exposing them to the internet. Security Groups are configured to allow only Connector IP addresses, eliminating public database exposure. DynamoDB requires a different approach using VPC endpoints since it lacks IP allowlist support.

## Key Information
- Supports: Amazon RDS, Aurora (MySQL/PostgreSQL), DynamoDB, self-hosted databases on EC2/on-prem
- Prefer **private IP** of Connector for Security Group rules; use public IP only when required
- Prefer **Security Group referencing** over IP-based rules for RDS/Aurora (more resilient, scales better)
- Aurora: use **cluster endpoint**, not instance endpoint, for failover/load balancing
- DynamoDB: no native IP allowlist; access control via **VPC Gateway Endpoint** + IAM `aws:SourceVpce` condition

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed in the VPC

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to RDS/Aurora endpoint (port 3306 MySQL, 5432 PostgreSQL)
2. Add inbound Security Group rule on RDS instance allowing Connector's private IP(s) on appropriate port
3. Connect via client (mysql/psql/DBeaver) using the RDS hostname

### DynamoDB
1. Create Twingate Resource for `dynamodb.<region>.amazonaws.com` on port 443
2. Create VPC Gateway Endpoint for DynamoDB; update its Security Group to allow Connector private IPs
3. Apply IAM policy restricting DynamoDB access via `aws:SourceVpce` condition
4. Connect using AWS CLI/SDK (optionally specifying `--endpoint-url` for the VPC endpoint)

## Configuration Values

| Parameter | Value |
|-----------|-------|
| MySQL/Aurora MySQL port | 3306 |
| PostgreSQL/Aurora PostgreSQL port | 5432 |
| DynamoDB endpoint port | 443 |
| DynamoDB regional endpoint | `dynamodb.<region>.amazonaws.com` |
| IAM condition for VPC endpoint | `aws:SourceVpce` |

## Gotchas
- Connector private IP can change during Terraform updates or lifecycle events if not explicitly pinned — prefer Security Group referencing
- DynamoDB has **no IP allowlist**; if no VPC endpoint is used, access control must be IAM-only
- Using VPC endpoint for DynamoDB requires matching IAM policies — misconfigured policies block all access
- "No Activity" in Recent Activity means Client isn't sending traffic (check Client running, resource access, conflicting VPN)
- "DNS Failed" means Connector can't resolve hostname — verify DNS zone is VPC-attached

## Troubleshooting Reference
| Symptom | Check |
|---------|-------|
| Connection Refused | Connector IP in Security Group/allowlist |
| DNS Failed | DNS zone tied to VPC, DNS server reachable from Connector |
| Connection Failed | Route exists Connector→DB, firewall rules, correct port |
| No Activity | Client running, resource permissions, no conflicting VPN |
| Timeouts | Connector online and reachable |

## Related Docs
- GCP Database Guide
- Azure Database Guide
- Connector Best Practices
- Twingate Troubleshooting Guide
- [Amazon DynamoDB endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ddb.html)
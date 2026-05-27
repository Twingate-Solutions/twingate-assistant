# AWS Database Access with Twingate

## Summary
Guide for securing access to Amazon RDS, Aurora, and DynamoDB using Twingate Connectors. Traffic is routed through Connectors deployed in your VPC, eliminating public database exposure. Security Group rules and VPC endpoints restrict access to Connector IPs only.

## Key Information
- Supports RDS, Aurora (MySQL/PostgreSQL), and DynamoDB
- Prefer **private IP** of Connector for security rules; use public IP only when database is in different VPC/region
- Recommended: use Connector's **Security Group** (not IP) for RDS/Aurora rules — more resilient to IP changes, scales better
- DynamoDB has no native IP allowlist; access control via VPC Gateway Endpoint + IAM `aws:SourceVpce` condition
- Aurora: use **cluster endpoint**, not individual instance endpoint

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed in the target VPC

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to RDS/Aurora endpoint with correct port (3306 MySQL, 5432 PostgreSQL)
2. Edit RDS instance's VPC Security Group inbound rules — allow Connector private IP(s) on database port
3. Connect via Twingate Client using standard DB clients

### DynamoDB
1. Create Twingate Resource for regional endpoint (e.g., `dynamodb.us-east-1.amazonaws.com`), port 443
2. Create VPC Gateway Endpoint for DynamoDB; update its Security Group to allow Connector private IPs
3. Write IAM policy restricting DynamoDB access using `aws:SourceVpce` condition
4. Connect via AWS CLI/SDK through Twingate Client

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MySQL/Aurora MySQL port | 3306 |
| PostgreSQL/Aurora PostgreSQL port | 5432 |
| DynamoDB HTTPS port | 443 |
| DynamoDB regional endpoint pattern | `dynamodb.<region>.amazonaws.com` |

## Gotchas
- Without a VPC endpoint, DynamoDB is reachable via public endpoint but **cannot** be IP-restricted — enforce via IAM only
- Connector IP can change during Terraform lifecycle events if not explicitly pinned — prefer Security Group referencing
- For cross-VPC/cross-region databases, Connector's public IP may be required in security rules
- `aws:SourceVpce` IAM condition only works when a VPC endpoint is configured

## Troubleshooting
| Symptom | Cause |
|---------|-------|
| DNS Failed (Recent Activity) | Connector can't resolve hostname; check DNS zone/VPC association |
| Connection Failed | Connector reached destination but blocked; check Security Group/firewall rules |
| No Activity | Client not sending traffic; check Client running, resource access, no conflicting VPN |
| Connection Refused | Connector IP not in database allowlist |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- GCP Database Guide
- Azure Database Guide
- Connector Best Practices
- [Amazon DynamoDB endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ddb.html)
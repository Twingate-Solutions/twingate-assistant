# AWS Database Access with Twingate

## Summary
Guide for securing access to Amazon RDS, Aurora, and DynamoDB using Twingate Connectors. Traffic is routed through Connectors so databases are never exposed to the public internet. Security is enforced via AWS Security Groups (RDS/Aurora) and VPC endpoints with IAM policies (DynamoDB).

## Key Information
- Supports RDS, Aurora, DynamoDB, and self-hosted databases
- Prefer Connector **private IP** for same-VPC databases; use public IP only when crossing networks
- **Recommended**: Use Security Group referencing (Connector's SG) instead of IP-based rules for resilience and scalability
- DynamoDB has no native IP allow list—access control requires VPC endpoints + IAM `aws:SourceVpce` conditions
- For Aurora clusters, use the **cluster endpoint** (not instance endpoint) for failover/load balancing

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed inside the target VPC

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to DB endpoint (e.g., `mydb.cluster-1234abcd.us-east-1.rds.amazonaws.com`), specify port (3306 MySQL, 5432 PostgreSQL)
2. In AWS Console → RDS → Databases → VPC Security Group → Edit Inbound Rules → add rule allowing Connector's private IP on the DB port
3. Connect via CLI or GUI client through Twingate Client

### DynamoDB
1. Create Twingate Resource pointing to `dynamodb.us-east-1.amazonaws.com`, port 443
2. Create **VPC Gateway Endpoint** for DynamoDB; update endpoint Security Group to allow Connector private IPs
3. Write IAM policy restricting DynamoDB actions using `aws:SourceVpce` condition
4. Connect via AWS CLI/SDK through Twingate

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MySQL/Aurora MySQL port | 3306 |
| PostgreSQL/Aurora PostgreSQL port | 5432 |
| DynamoDB endpoint port | 443 |
| DynamoDB regional endpoint format | `dynamodb.us-east-1.amazonaws.com` |

## Gotchas
- **IP vs. SG referencing**: Connector IPs can change during Terraform lifecycle events—prefer Security Group referencing
- **DynamoDB**: Cannot restrict via IP allow list; if no VPC endpoint exists, traffic goes public and only IAM controls access
- **Public IP usage**: Only use Connector public IP when DB is in a different VPC/region or exposed over internet
- **VPC endpoint CLI**: Must specify `--endpoint-url` explicitly when using VPC endpoint with AWS CLI

## Troubleshooting
| Symptom | Check |
|---------|-------|
| DNS Failed | Connector can't resolve hostname; verify DNS hosted zone is tied to VPC |
| Connection Failed | Route exists? IP allow lists correct? Security group rules allow port on both ends? |
| No Activity | Client running? Resource access granted? Another VPN hijacking traffic? |
| Slow connections | Connector health; firewall blocking |

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Security Policies Guide](https://www.twingate.com/docs/security-policies)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Amazon DynamoDB endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ddb.html)
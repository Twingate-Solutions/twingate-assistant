# AWS Database Access with Twingate

## Summary
Configures secure access to Amazon RDS, Aurora, and DynamoDB using Twingate Connectors as traffic intermediaries. Eliminates direct internet exposure by routing database connections through Connectors and restricting AWS Security Groups to Connector IP addresses only.

## Key Information
- Supports RDS, Aurora (MySQL/PostgreSQL), DynamoDB, and self-hosted databases
- Connector private IP (within VPC) is preferred over public IP for security group rules
- RDS/Aurora: restrict via Security Group rules; DynamoDB: restrict via VPC endpoint + IAM policies
- For Aurora clusters, use the **cluster endpoint** (not instance endpoint) for failover/load balancing
- DynamoDB has no native IP allow list—access control requires VPC Gateway Endpoint + `aws:SourceVpce` IAM condition

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed in the target VPC
- Connector private IP address(es) from the Connectors page

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to DB endpoint (e.g., `mydb.cluster-1234abcd.us-east-1.rds.amazonaws.com`)
2. Edit RDS instance's inbound Security Group rules → allow Connector private IP(s) on DB port
3. Connect via client through Twingate Client

### DynamoDB
1. Create Twingate Resource for regional endpoint (e.g., `dynamodb.us-east-1.amazonaws.com`) on port 443
2. Create VPC Gateway Endpoint for DynamoDB; update its Security Group to allow Connector private IPs
3. Add IAM policy restricting DynamoDB access via `aws:SourceVpce` condition
4. Connect using AWS CLI/SDK through Twingate Client

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MySQL/Aurora MySQL port | 3306 |
| PostgreSQL/Aurora PostgreSQL port | 5432 |
| DynamoDB port | 443 (HTTPS) |
| DynamoDB regional endpoint pattern | `dynamodb.us-east-1.amazonaws.com` |

## Gotchas
- **Prefer Security Group referencing over IP rules** for RDS/Aurora—IP addresses can shift during Terraform updates or lifecycle events
- DynamoDB without a VPC endpoint is reachable but **cannot be IP-restricted**; use IAM policies instead
- If Connector is in a different VPC/region than the database, use public IP address for Security Group rules
- For DynamoDB VPC endpoint, use the VPC endpoint URL explicitly with `--endpoint-url` in AWS CLI

## Troubleshooting Reference
| Symptom | Check |
|---------|-------|
| DNS Failed | Connector cannot resolve hostname; verify DNS zone is VPC-bound |
| Connection Failed | Route/firewall between Connector and DB; verify Security Group port rules |
| No Activity in Recent Activity | Client not running, no Resource access, or VPN conflict |
| DynamoDB access denied | Verify `aws:SourceVpce` IAM policy condition matches endpoint ID |

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Amazon DynamoDB Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/ddb.html)
# AWS Database Access with Twingate

## Summary
Guide for securely connecting to Amazon RDS, Aurora, and DynamoDB using Twingate Connectors as network intermediaries. Traffic is routed through Connectors deployed in your VPC, eliminating the need to expose database ports to the internet. Access control is enforced via AWS Security Groups and VPC endpoints.

## Key Information
- Works with RDS, Aurora (MySQL/PostgreSQL), and DynamoDB
- Connectors should use **private IPs** within the same VPC; only use public IPs when crossing networks
- Security Group referencing (by SG, not IP) is preferred over IP-based rules for RDS/Aurora
- DynamoDB has no native IP allowlist; use VPC Gateway Endpoint + IAM `aws:SourceVpce` condition
- Self-hosted databases (EC2, on-prem) follow the same pattern

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed in target VPC

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to RDS/Aurora endpoint with appropriate port
2. Edit RDS instance's VPC Security Group → add inbound rule for Connector's private IP on DB port
3. Connect via Twingate Client using standard DB clients

### DynamoDB
1. Create Twingate Resource: `dynamodb.us-east-1.amazonaws.com`, port 443
2. Create VPC Gateway Endpoint for DynamoDB; restrict Security Group to Connector's private IP
3. Write IAM policy with `aws:SourceVpce` condition to enforce VPC endpoint usage
4. Connect via AWS CLI/SDK through Twingate Client

## Configuration Values
| Database | Port | Endpoint Format |
|----------|------|-----------------|
| MySQL / Aurora MySQL | 3306 | `mydb.cluster-xxxx.us-east-1.rds.amazonaws.com` |
| PostgreSQL / Aurora PostgreSQL | 5432 | same pattern |
| DynamoDB | 443 | `dynamodb.us-east-1.amazonaws.com` |

**CLI example (DynamoDB with VPC endpoint):**
```bash
aws dynamodb list-tables \
  --region us-east-1 \
  --endpoint-url https://dynamodb.us-east-1.vpce-<id>.vpce-svc-<id>.amazonaws.com
```

## Gotchas
- Use Aurora **cluster endpoint**, not instance endpoint, for failover support
- Without a VPC endpoint, DynamoDB is reachable via public endpoint but cannot restrict by IP — must use IAM
- Connector IP can change during Terraform lifecycle events if not explicitly pinned — prefer Security Group referencing
- DynamoDB VPC endpoint is a **Gateway** type (not Interface), traffic routes automatically once endpoint is created

## Troubleshooting
- **DNS Failed**: Connector can't resolve hostname → check DNS zone is tied to VPC
- **Connection Failed**: Connector reached but DB unreachable → verify Security Group rules and IP allowlists
- **No Activity**: Client not sending traffic → check Client is running, user has Resource access, no conflicting VPN

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- GCP Database Guide, Azure Database Guide, Oracle Database Guide
# AWS Database Access with Twingate

## Page Title
AWS Database Access with Twingate (RDS, Aurora, DynamoDB)

## Summary
Covers routing traffic to AWS databases (RDS, Aurora, DynamoDB) through Twingate Connectors and restricting AWS network access so only Connector traffic is permitted. Includes Security Group configuration for RDS/Aurora and VPC endpoint setup for DynamoDB.

## Key Information
- **RDS/Aurora**: Runs inside VPC; restrict access via Security Group inbound rules allowing only Connector IPs
- **DynamoDB**: Publicly accessible by default; no IP allowlist support—use VPC Gateway Endpoint + IAM `aws:SourceVpce` condition
- **Preferred**: Use Connector's Security Group (not IP) in RDS Security Group rules—avoids IP drift, scales better, aligns with AWS VPC best practices
- Use **private IP** of Connector for same-VPC databases; use **public IP** only for internet-exposed services
- Aurora clusters: use the **cluster endpoint**, not individual instance endpoint

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed in the target VPC

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to DB endpoint (e.g., `mydb.cluster-1234abcd.us-east-1.rds.amazonaws.com`) with correct port
2. AWS Console → RDS → Database → VPC Security Group → Inbound Rules → add Connector private IP on DB port
3. Connect via client through Twingate Client

### DynamoDB
1. Create Twingate Resource for regional endpoint (e.g., `dynamodb.us-east-1.amazonaws.com`) on port 443
2. Create **VPC Gateway Endpoint** for DynamoDB; update its Security Group to allow Connector private IPs
3. Write IAM policy restricting DynamoDB access using `aws:SourceVpce` condition
4. Connect via AWS CLI/SDK through Twingate Client

## Configuration Values
| Service | Port |
|---|---|
| MySQL / Aurora MySQL | 3306 |
| PostgreSQL / Aurora PostgreSQL | 5432 |
| DynamoDB (HTTPS) | 443 |

**DynamoDB CLI with VPC endpoint:**
```bash
aws dynamodb list-tables \
  --region us-east-1 \
  --endpoint-url https://dynamodb.us-east-1.vpce-<endpoint-id>.vpce-svc-<service-id>.amazonaws.com
```

## Gotchas
- DynamoDB has **no IP allowlist**—without VPC endpoint, access control is IAM-only
- If no VPC endpoint is created, DynamoDB is reachable via public endpoint; IAM policies must enforce access
- Connector IPs can change during Terraform updates/lifecycle events—prefer Security Group referencing
- Self-hosted databases (EC2, on-prem): same pattern—add Connector private IP to firewall rules

## Troubleshooting
- **DNS Failed**: Connector can't resolve hostname—check DNS zone/VPC association
- **Connection Failed**: Connector can't reach destination—check Security Group rules, IP allowlists, port rules both sides
- **No Activity**: Client not sending traffic—check Client is running, Resource access granted, no conflicting VPN
- **DynamoDB access denied**: Verify `aws:SourceVpce` IAM condition matches correct endpoint ID

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs)
- [Amazon DynamoDB endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ddb.html)
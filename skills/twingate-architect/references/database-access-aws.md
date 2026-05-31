# AWS Database Access with Twingate

## Summary
Guide for securing access to Amazon RDS, Aurora, and DynamoDB using Twingate Connectors as network intermediaries. Eliminates need to expose database ports to the internet by routing traffic through Connectors and restricting AWS Security Groups to Connector IPs only.

## Key Information
- Covers RDS/Aurora (VPC-based) and DynamoDB (HTTPS/API-based) with different approaches for each
- Prefer **Security Group referencing** over IP-based rules for RDS/Aurora (more resilient to IP changes, scales better)
- DynamoDB has no IP allowlist support; access control requires VPC endpoints + IAM policies
- Use **private IP** of Connector for intra-VPC rules; public IP only when database is accessed over internet

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed in the target VPC/network
- Connector's private IP address (found on Connectors page in Admin Console)

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to RDS/Aurora endpoint (e.g., `mydb.cluster-1234abcd.us-east-1.rds.amazonaws.com`)
2. Edit RDS instance's VPC Security Group → add inbound rule allowing Connector's private IP on DB port
3. Connect via Twingate Client using standard DB clients

### DynamoDB
1. Create Twingate Resource for regional endpoint (e.g., `dynamodb.us-east-1.amazonaws.com`), port 443
2. Create VPC Gateway Endpoint for DynamoDB; restrict Security Group to Connector's private IP
3. Add IAM policy with `aws:SourceVpce` condition to enforce endpoint-only access
4. Connect using AWS CLI/SDK through Twingate Client

## Configuration Values

| Service | Port | Endpoint Pattern |
|---------|------|-----------------|
| MySQL / Aurora MySQL | 3306 | `*.rds.amazonaws.com` |
| PostgreSQL / Aurora PostgreSQL | 5432 | `*.rds.amazonaws.com` |
| DynamoDB | 443 | `dynamodb.<region>.amazonaws.com` |

**CLI Examples:**
```bash
# MySQL
mysql -h mydb.cluster-1234abcd.us-east-1.rds.amazonaws.com -u <username> -p

# PostgreSQL
psql -h mydb.cluster-1234abcd.us-east-1.rds.amazonaws.com -U <username> -d <database>

# DynamoDB via VPC endpoint
aws dynamodb list-tables --region us-east-1 \
  --endpoint-url https://dynamodb.us-east-1.vpce-<id>.vpce-svc-<id>.amazonaws.com
```

## Gotchas
- DynamoDB is **publicly accessible by default**; without VPC endpoint, you cannot restrict by IP — must use IAM
- For Aurora, use **cluster endpoint** (not instance endpoint) for failover/load balancing
- Terraform lifecycle events can cause Connector IP changes — prefer Security Group referencing
- If no VPC endpoint for DynamoDB, traffic still routes through public endpoint; IAM is sole access control
- Self-hosted databases on EC2 follow same pattern: add Connector IP to security group, create Resource with FQDN/IP

## Troubleshooting
- **DNS Failed**: Connector can't resolve hostname — check DNS hosted zone is VPC-linked
- **Connection Failed**: Connector reached but can't connect — verify Security Group rules and port access
- **No Activity**: Client not sending traffic — check Twingate Client is running, no conflicting VPN
- Check Recent Activity in Admin Console per Resource for diagnosis

## Related Docs
- Twingate Troubleshooting Guide
- Connector Best Practices
- GCP/Azure/Oracle Database Guides
- Security Policies Guide
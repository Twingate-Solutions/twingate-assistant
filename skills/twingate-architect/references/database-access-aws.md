# AWS Database Access with Twingate

## Summary
Covers configuring Twingate to securely access Amazon RDS, Aurora, and DynamoDB without exposing databases to the internet. Traffic is routed through Twingate Connectors, with AWS Security Groups restricting access to Connector IP addresses only.

## Key Information
- RDS/Aurora: restrict via VPC Security Group rules allowing only Connector IPs
- DynamoDB: no native IP allowlist; use VPC Gateway Endpoint + IAM `aws:SourceVpce` condition
- Prefer Connector **private IP** for same-VPC resources; use public IP only when crossing networks
- Prefer **Security Group referencing** over IP-based rules for RDS/Aurora (more resilient, scales better)
- Aurora clusters: use **cluster endpoint**, not instance endpoint (enables failover/load balancing)

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Connector deployed in the target VPC/network
- Connector private IP(s) noted from Connectors page

## RDS/Aurora Setup
1. Create Twingate Resource pointing to RDS/Aurora endpoint with appropriate port (3306 MySQL, 5432 PostgreSQL)
2. In AWS Console → RDS → Databases → VPC Security Group → Inbound Rules: add rule allowing Connector private IP on database port
3. Connect via Twingate Client using standard DB clients

## DynamoDB Setup
1. Create Twingate Resource: `dynamodb.us-east-1.amazonaws.com`, port 443
2. Create VPC Gateway Endpoint for DynamoDB in your VPC
3. Update Security Group on VPC endpoint to allow Connector private IPs
4. Add IAM policy restricting access via `aws:SourceVpce` condition
5. Connect using AWS CLI/SDKs through Twingate Client

## Configuration Values
| Database | Port | Endpoint Type |
|----------|------|---------------|
| MySQL/Aurora MySQL | 3306 | Cluster endpoint |
| PostgreSQL/Aurora PostgreSQL | 5432 | Cluster endpoint |
| DynamoDB | 443 | `dynamodb.<region>.amazonaws.com` |

**CLI example (DynamoDB via VPC endpoint):**
```bash
aws dynamodb list-tables \
  --region us-east-1 \
  --endpoint-url https://dynamodb.us-east-1.vpce-<endpoint-id>.vpce-svc-<service-id>.amazonaws.com
```

## Gotchas
- DynamoDB has **no IP allowlist**—access control requires VPC endpoint + IAM policies
- Without a VPC endpoint, DynamoDB remains reachable via public endpoint (IAM-only enforcement)
- Connector IPs can change during Terraform lifecycle events if not explicitly pinned—prefer Security Group referencing
- `DNS Failed` in Recent Activity = Connector can't resolve hostname; verify DNS zone is tied to VPC
- `Connection Failed` = Connector reached destination but was blocked; check Security Group/firewall rules
- `No Activity` = Client not sending traffic; check Client is running and no other VPN is intercepting

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- GCP Database Guide
- Azure Database Guide
- Connector Best Practices
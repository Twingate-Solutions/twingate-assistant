# AWS Database Access with Twingate

## Page Title
AWS Database Access with Twingate (RDS, Aurora, DynamoDB)

## Summary
Twingate routes private traffic to AWS databases (RDS, Aurora, DynamoDB) through Connectors deployed in your VPC, eliminating public internet exposure. Access control is enforced via AWS Security Groups and/or IAM policies rather than opening ports publicly. DynamoDB requires a different approach (VPC endpoint + IAM) since it lacks IP-based allow lists.

## Key Information
- RDS/Aurora: restrict via Security Group inbound rules allowing only Connector IPs
- DynamoDB: no IP allow list available; use VPC Gateway Endpoint + `aws:SourceVpce` IAM condition
- Prefer Connector **private IP** for same-VPC databases; public IP only when crossing network boundaries
- Prefer **Security Group referencing** over IP-based rules for resilience and scalability
- Aurora: use **cluster endpoint**, not instance endpoint, for failover support

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed within the VPC
- Connector private IP(s) noted from the Connectors page

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to DB endpoint (e.g., `mydb.cluster-1234abcd.us-east-1.rds.amazonaws.com`) with appropriate port
2. Edit RDS instance's VPC Security Group → add inbound rule allowing Connector private IP on DB port
3. Connect via client using the endpoint hostname through Twingate Client

### DynamoDB
1. Create Twingate Resource for `dynamodb.us-east-1.amazonaws.com` on port 443
2. Create VPC Gateway Endpoint for DynamoDB; update its Security Group to allow Connector private IPs
3. Write IAM policy restricting DynamoDB access using `aws:SourceVpce` condition
4. Access via AWS CLI/SDK through Twingate Client

## Configuration Values

| Database | Port | Endpoint Pattern |
|----------|------|-----------------|
| MySQL / Aurora MySQL | 3306 | `mydb.cluster-xxxx.region.rds.amazonaws.com` |
| PostgreSQL / Aurora PostgreSQL | 5432 | same pattern |
| DynamoDB | 443 | `dynamodb.us-east-1.amazonaws.com` |

**CLI example (DynamoDB with VPC endpoint):**
```bash
aws dynamodb list-tables \
  --region us-east-1 \
  --endpoint-url https://dynamodb.us-east-1.vpce-<id>.vpce-svc-<id>.amazonaws.com
```

## Gotchas
- DynamoDB **cannot** be restricted by IP allow list — IAM + VPC endpoint is the only enforcement mechanism
- Without a VPC endpoint, DynamoDB remains reachable via public endpoint; access control falls back to IAM only
- Connector IPs can change during Terraform updates or lifecycle events unless explicitly pinned — prefer Security Group referencing
- Self-hosted/EC2 databases: add Connector private IP to host firewall rules, not just AWS Security Groups

## Troubleshooting
- **DNS Failed** in Recent Activity → DNS zone not linked to VPC or DNS server unreachable from Connector
- **Connection Failed** → route or firewall missing between Connector and database
- **No Activity** → Twingate Client not running, no Resource access granted, or another VPN intercepting traffic

## Related Docs
- Twingate Troubleshooting Guide
- GCP / Azure / Oracle Database Guides
- Connector Best Practices
- Security Policies Guide
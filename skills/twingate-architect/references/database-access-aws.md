# AWS Database Access with Twingate

## Summary
Guide for securely connecting to Amazon RDS, Aurora, and DynamoDB using Twingate Connectors as network intermediaries. Traffic is routed through Connectors deployed in your VPC, eliminating the need to expose database ports to the internet. Access control is enforced via AWS Security Groups and IAM policies.

## Key Information
- Supports RDS, Aurora (MySQL/PostgreSQL), and DynamoDB
- Connector private IP (within VPC) is preferred over public IP for security group rules
- Security Group referencing (by SG, not IP) is recommended for RDS/Aurora — more resilient to IP changes
- DynamoDB has no native IP allowlist; use VPC Gateway Endpoint + IAM `aws:SourceVpce` condition
- Self-hosted/EC2 databases follow same pattern: create Resource, allowlist Connector IP in firewall

## Prerequisites
- Remote Network defined in Twingate Admin Console
- At least one Twingate Connector deployed in the target VPC
- Connector private IP address (from Connectors page in Admin Console)

## Step-by-Step

### RDS / Aurora
1. Create Twingate Resource pointing to RDS/Aurora endpoint with appropriate port (3306 MySQL, 5432 PostgreSQL)
2. Edit RDS instance's VPC Security Group → add inbound rule allowing Connector's private IP on that port
3. Connect via Twingate Client using standard DB clients (mysql, psql, DBeaver)

### DynamoDB
1. Create Twingate Resource for regional endpoint (e.g., `dynamodb.us-east-1.amazonaws.com`) on port 443
2. Create VPC Gateway Endpoint for DynamoDB; update its Security Group to allow Connector private IP
3. Write IAM policy restricting DynamoDB access via `aws:SourceVpce` condition
4. Connect using AWS CLI/SDK through Twingate Client

## Configuration Values
| Setting | Value |
|---|---|
| MySQL/Aurora MySQL port | 3306 |
| PostgreSQL/Aurora PostgreSQL port | 5432 |
| DynamoDB endpoint port | 443 |
| DynamoDB regional endpoint format | `dynamodb.us-east-1.amazonaws.com` |
| Aurora recommended endpoint type | Cluster endpoint (not instance endpoint) |

## Gotchas
- Use **cluster endpoint** for Aurora (not instance endpoint) to get failover/load balancing
- Without a VPC endpoint, DynamoDB is reachable via public endpoint but **cannot** be IP-restricted — must use IAM
- Connector IP can change during Terraform updates/lifecycle events if not explicitly pinned — prefer SG referencing
- If using VPC endpoint for DynamoDB, CLI requires `--endpoint-url` with the VPC endpoint URL

## Troubleshooting
| Symptom | Cause |
|---|---|
| DNS Failed | Connector can't resolve hostname; check DNS zone/VPC association |
| Connection Failed | Connector reached but can't connect; check Security Group rules and IP allowlists |
| No Activity | Client not sending traffic; check Client is running, Resource access granted, no VPN conflict |
| Connection Refused | Connector IP not in database allowlist |

## Related Docs
- [GCP Database Guide](https://www.twingate.com/docs/database-access-gcp)
- [Azure Database Guide](https://www.twingate.com/docs/database-access-azure)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
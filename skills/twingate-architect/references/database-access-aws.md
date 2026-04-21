## Page Title
AWS Database Access with Twingate

## Summary
Practical guide to securing access to Amazon RDS, Aurora, and DynamoDB using Twingate. Covers creating Resources, configuring AWS Security Groups or VPC endpoints to allow only Connector traffic, and connecting with common database clients. Includes troubleshooting steps for common connection failures.

## Key Information
- **RDS/Aurora**: run inside VPC; restrict via Security Group rules allowing only Connector IP(s) on the DB port
- **Preferred SG approach**: reference the Connector's Security Group (not its IP) -- more resilient to IP changes, scales when adding Connectors
- **DynamoDB**: publicly accessible by default; restrict via VPC Gateway Endpoint + IAM policy with `aws:SourceVpce` condition; no native IP allow list
- **Resource definition**: use RDS/Aurora cluster endpoint FQDN for failover support; use DynamoDB regional endpoint (`dynamodb.<region>.amazonaws.com`) on port 443
- **Self-hosted databases**: define Resource with FQDN or IP + port; add Connector private IP to firewall rules

## Prerequisites
- Remote Network and Connector deployed in the same VPC as the database
- Connector's private IP (preferred) or public IP noted from Connectors page

## Step-by-Step
**RDS/Aurora:**
1. Create Resource: `mydb.cluster-xxx.us-east-1.rds.amazonaws.com` on port 3306 (MySQL) or 5432 (Postgres)
2. Edit RDS Security Group inbound rules: allow Connector private IP on the DB port (or reference Connector SG)
3. Connect: `mysql -h <endpoint> -u <user> -p` or `psql -h <endpoint> -U <user>`

**DynamoDB:**
1. Create Resource: `dynamodb.<region>.amazonaws.com` on port 443
2. Create VPC Gateway Endpoint for DynamoDB in the VPC
3. Update endpoint Security Group: allow Connector private IP
4. Write IAM policy with `aws:SourceVpce` condition to restrict access to the endpoint

## Configuration Values
- MySQL/Aurora MySQL port: `3306`
- PostgreSQL/Aurora PostgreSQL port: `5432`
- DynamoDB HTTPS port: `443`
- DynamoDB endpoint format: `dynamodb.<region>.amazonaws.com`

## Gotchas
- Use Aurora cluster endpoint (not instance endpoint) for failover/load balancing
- DynamoDB has no IP allow list -- VPC endpoint + IAM is the only restriction mechanism
- "DNS Failed" in Recent Activity: Connector can't resolve the DB hostname -- check VPC DNS settings
- "Connection Failed": route or SG blocking Connector-to-DB traffic
- "No Activity": Client not sending traffic to Connector -- check Client is running and Resource is assigned

## Related Docs
- `/docs/database-access-guide` -- general database access overview
- `/docs/connector-best-practices` -- Connector IP and SG best practices
- `/docs/saas-app-gating` -- accessing public/SaaS database endpoints
- `/docs/troubleshooting` -- general troubleshooting guide

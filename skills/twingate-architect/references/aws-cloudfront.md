# AWS CloudFront SaaS App Gate via Twingate

## Summary
Restricts AWS CloudFront distribution access to Twingate exit node IPs using AWS WAF IP sets. Users must connect through Twingate (routed via AWS Exit Nodes) to reach protected CloudFront content.

## Key Information
- Uses AWS Firewall Manager WAF IP sets to whitelist exit node Elastic IPs
- WAF ACL must be scoped to **Global (CloudFront)** region
- S3-backed CloudFront distributions may require additional Origin Access Identity (OAI) configuration
- Twingate resource name must match the CloudFront FQDN exactly (e.g., `beamreach.cloudfront.net`)

## Prerequisites
- AWS Exit Nodes provisioned with Elastic IPs assigned to EC2 instances
- Access to AWS Firewall Manager and CloudFront console
- Twingate admin console access

## Step-by-Step

### 1. Create IP Set in AWS Firewall Manager
- Navigate to AWS Firewall Manager → IP Sets
- Create new IP Set, set Region to **Global (CloudFront)**
- Add exit node Elastic IPs in CIDR notation (e.g., `35.164.107.72/32`)

### 2. Assign WAF ACL to CloudFront Distribution
- In AWS CloudFront, open your Distribution settings
- Set **AWS WAF Web ACL** field to the IP Set created above

### 3. (Optional) Restrict S3 Origin Access
- Create an Origin Access Identity (OAI) to ensure S3 content is only accessible via CloudFront + WAF
- Consult AWS S3 documentation for OAI setup

### 4. Create Twingate Resource
- In Twingate admin console, create a Resource using the CloudFront FQDN (e.g., `beamreach.cloudfront.net`)

### 5. Authorize Users
- Create a Group in Twingate
- Add the CloudFront Resource to the Group
- Assign users to the Group

## Configuration Values
| Field | Value |
|-------|-------|
| WAF IP Set Region | `Global (CloudFront)` |
| IP format | CIDR (e.g., `35.164.107.72/32`) |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource name | Exact CloudFront FQDN |

## Gotchas
- IP Set region **must** be `Global (CloudFront)` — regional IP sets won't work with CloudFront
- Each exit node EC2 instance needs its own `/32` CIDR entry
- Twingate matches on exact FQDN/IP in connection requests — resource name mismatch will deny access
- S3 origins without OAI can be accessed directly, bypassing WAF — OAI is required to fully lock down S3-backed distributions

## Related Docs
- [AWS Exit Nodes setup](https://www.twingate.com/docs/aws-exit-nodes)
- [Create Twingate Resources](https://www.twingate.com/docs/resources)
- AWS S3 Origin Access Identity documentation
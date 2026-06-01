# How to SaaS App Gate AWS CloudFront

## Summary
Configures IP whitelisting for AWS CloudFront using Twingate AWS Exit Nodes as the allowed IP source. Traffic is restricted via AWS WAF IP Sets, and Twingate controls user authorization through Resources and Groups.

## Key Information
- Uses AWS WAF (via Firewall Manager) to restrict CloudFront access to Exit Node IPs
- IP Set must be created with **Global (CloudFront)** region — not a standard AWS region
- Exit Node IPs must be Elastic IPs (static) assigned to EC2 instances
- S3-backed CloudFront distributions require additional Origin Access Identity configuration

## Prerequisites
- AWS Exit Nodes already created (EC2 instances with Elastic IPs)
- Access to AWS Firewall Manager and CloudFront console
- Twingate admin console access

## Step-by-Step

### 1. Create IP Set in AWS Firewall Manager
- Navigate to AWS Firewall Manager → IP Sets
- Create new IP Set with **Region: Global (CloudFront)**
- Add Exit Node Elastic IPs in CIDR format (e.g., `35.164.107.72/32`)

### 2. Assign WAF ACL to CloudFront Distribution
- In AWS CloudFront, open your Distribution settings
- Set **AWS WAF Web ACL** to the IP Set created above
- For S3 origins: create an Origin Access Identity to restrict S3 access to CloudFront only (see AWS S3 docs)

### 3. Create Twingate Resource
- In Twingate admin console, create a Resource using the CloudFront FQDN (e.g., `beamreach.cloudfront.net`)
- Twingate matches on FQDN or IP in the connection request

### 4. Authorize Users
- Create a Group in Twingate
- Add the CloudFront Resource to the Group
- Assign users to the Group

## Configuration Values
| Field | Value |
|-------|-------|
| IP Set Region | `Global (CloudFront)` |
| IP format | CIDR notation, e.g. `<elastic-ip>/32` |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource name | CloudFront FQDN (e.g., `beamreach.cloudfront.net`) |

## Gotchas
- IP Set region **must** be `Global (CloudFront)` — a regional IP Set will not work with CloudFront
- Exit Node IPs must be static (Elastic IPs); dynamic IPs will break whitelisting
- S3 content requires Origin Access Identity separately — WAF ACL alone does not restrict direct S3 bucket access
- Resource name in Twingate must exactly match the FQDN users will request

## Related Docs
- AWS Exit Nodes setup (prerequisite)
- Twingate Resource/Group authorization instructions
- AWS S3 Origin Access Identity documentation
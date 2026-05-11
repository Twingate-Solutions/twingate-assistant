# How to SaaS App Gate AWS CloudFront

## Summary
Configures IP whitelisting for AWS CloudFront using Twingate's AWS Exit Nodes as the allowed IP sources. Traffic is restricted via AWS WAF IP Sets applied to CloudFront distributions, with Twingate controlling which users can route through the exit node IPs.

## Key Information
- Uses AWS WAF (Firewall Manager) IP Sets scoped to `Global (CloudFront)` region
- Exit Node Elastic IPs are the whitelisted IPs in CloudFront WAF rules
- Twingate Resource is defined by the CloudFront FQDN (e.g., `beamreach.cloudfront.net`)
- S3-backed CloudFront may require additional Origin Access Identity configuration

## Prerequisites
- AWS Exit Nodes already created (EC2 instances with Elastic IPs assigned)
- Access to AWS Firewall Manager and CloudFront console
- Twingate admin console access
- External IPs (Elastic IPs) of exit node EC2 instances

## Step-by-Step

### 1. Create IP Set in AWS Firewall Manager
- Navigate to AWS Firewall Manager → IP Sets
- Create new IP Set with **Region: Global (CloudFront)**
- Add exit node Elastic IPs in CIDR notation (e.g., `35.164.107.72/32`)

### 2. Assign WAF ACL to CloudFront Distribution
- In AWS CloudFront, open your Distribution settings
- Set **AWS WAF Web ACL** to the IP Set created above
- For S3 origins: create an Origin Access Identity to restrict S3 access to CloudFront only

### 3. Create Twingate Resource
- In Twingate admin console, create a Resource using the CloudFront FQDN (e.g., `beamreach.cloudfront.net`)

### 4. Authorize Users
- Create a Group in Twingate
- Add the CloudFront Resource to the Group
- Assign users to the Group

## Configuration Values
| Field | Value |
|-------|-------|
| IP Set Region | `Global (CloudFront)` |
| IP format | CIDR (`x.x.x.x/32` for single IPs) |
| WAF setting location | CloudFront Distribution → `AWS WAF Web ACL` |
| Twingate Resource name | CloudFront FQDN or IP |

## Gotchas
- IP Set **must** be scoped to `Global (CloudFront)` — regional IP sets won't work with CloudFront
- S3 origins require separate Origin Access Identity setup to prevent direct S3 bucket access bypassing WAF
- All exit node IPs must be added; missing one means some Twingate traffic will be blocked

## Related Docs
- [AWS Exit Nodes setup](https://www.twingate.com/docs/aws-exit-nodes)
- [Creating Twingate Resources](https://www.twingate.com/docs/resources-and-access)
- AWS S3 Origin Access Identity documentation (AWS docs)
# How to SaaS App Gate AWS CloudFront

## Summary
Restricts AWS CloudFront distribution access to Twingate users via IP whitelisting using AWS WAF. Traffic is routed through AWS Exit Nodes with Elastic IPs, which are whitelisted in CloudFront's WAF ACL. Users must be in an authorized Twingate Group to access protected content.

## Key Information
- Uses AWS WAF IP Sets scoped to **Global (CloudFront)** region
- Requires pre-created AWS Exit Nodes with Elastic IPs assigned to EC2 instances
- Works for both CloudFront distributions and S3 origins
- Twingate Resource name must match the CloudFront FQDN exactly

## Prerequisites
- AWS Exit Nodes created (EC2 instances with Elastic IPs)
- External IP addresses of exit node EC2 instances noted
- AWS Firewall Manager access
- AWS CloudFront distribution already configured
- Twingate admin console access

## Step-by-Step

### 1. Create IP Set in AWS Firewall Manager
- Navigate to AWS Firewall Manager → IP Sets
- Create new IP Set with **Region: Global (CloudFront)**
- Add exit node Elastic IPs in CIDR notation (e.g., `35.164.107.72/32`)

### 2. Assign WAF ACL to CloudFront Distribution
- In AWS CloudFront, open your distribution settings
- Set **AWS WAF Web ACL** field to the IP Set created above
- For S3 origins: create an Origin Access Identity to restrict S3 access to CloudFront only (see AWS S3 docs)

### 3. Create Twingate Resource
- In Twingate admin console, create a Resource using the CloudFront FQDN as the name
- Example: `beamreach.cloudfront.net`

### 4. Authorize Users
- Create a Twingate Group
- Add the CloudFront Resource to the Group
- Assign users to the Group

## Configuration Values

| Parameter | Value |
|---|---|
| IP Set Region | `Global (CloudFront)` |
| IP format | CIDR notation (e.g., `35.164.107.72/32`) |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource name | Exact CloudFront FQDN (e.g., `beamreach.cloudfront.net`) |

## Gotchas
- IP Set **must** be scoped to `Global (CloudFront)` — regional IP sets will not work with CloudFront distributions
- S3 bucket policies may also need updating via Origin Access Identity to prevent direct S3 URL access bypassing WAF
- Twingate matches on exact FQDN/IP in connection requests — Resource name must match precisely
- All exit node IPs must be added; missing one will cause access failures for users routed through that node

## Related Docs
- [AWS Exit Nodes setup](https://www.twingate.com/docs/aws-exit-nodes)
- [Create a Twingate Resource](https://www.twingate.com/docs/resources)
- [AWS S3 Origin Access Identity documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
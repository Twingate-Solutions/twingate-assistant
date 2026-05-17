# SaaS App Gate: AWS CloudFront

## Summary
Restricts AWS CloudFront access to users connecting through Twingate by combining AWS WAF IP whitelisting with Twingate exit nodes. Only traffic egressing through designated Elastic IPs (via AWS exit nodes) is permitted to reach CloudFront distributions.

## Key Information
- Uses AWS WAF IP Sets scoped to **Global (CloudFront)** region
- Requires pre-created AWS Exit Nodes with assigned Elastic IPs
- Works for both CloudFront-served content and S3 origins
- Access control enforced via Twingate Resources matched by FQDN or IP

## Prerequisites
- AWS Exit Nodes created with Elastic IPs assigned to EC2 instances
- Access to AWS Firewall Manager and CloudFront console
- Twingate admin console access

## Step-by-Step

### 1. Create IP Set in AWS Firewall Manager
- Region: **Global (CloudFront)**
- Add Elastic IPs of exit node EC2 instances in CIDR format (e.g., `35.164.107.72/32`)

### 2. Assign WAF ACL to CloudFront Distribution
- In CloudFront Distribution settings → **AWS WAF Web ACL** → assign the IP Set
- For S3 origins: create an Origin Access Identity to restrict S3 access exclusively to CloudFront + WAF ACL

### 3. Create Twingate Resource
- Resource name = FQDN of protected CloudFront domain (e.g., `beamreach.cloudfront.net`)
- Create a Group, add the Resource and authorized users to the Group

## Configuration Values
| Parameter | Value/Format |
|-----------|-------------|
| IP Set Region | `Global (CloudFront)` |
| IP CIDR format | `<ElasticIP>/32` |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource identifier | CloudFront FQDN or IP |

## Gotchas
- IP Set **must** be scoped to `Global (CloudFront)` — regional scopes won't apply to CloudFront
- S3 content requires additional Origin Access Identity configuration to prevent direct S3 bucket access bypassing WAF
- Elastic IPs must be used (not dynamic public IPs) to ensure stable CIDR entries

## Related Docs
- [AWS Exit Nodes setup](https://www.twingate.com/docs/aws-exit-nodes)
- [Create Twingate Resource](https://www.twingate.com/docs/resources)
- [AWS S3 Origin Access Identity documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
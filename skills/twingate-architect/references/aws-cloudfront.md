# AWS CloudFront SaaS App Gating with Twingate

## Page Title
How to SaaS App Gate AWS CloudFront

## Summary
Configure IP whitelisting for AWS CloudFront using Twingate AWS Exit Nodes. Traffic to CloudFront is restricted to Exit Node Elastic IPs via AWS WAF, and Twingate controls which users can route through those Exit Nodes.

## Key Information
- Uses AWS WAF IP Sets (not Security Groups) to restrict CloudFront access
- IP Set must be created with **Region: Global (CloudFront)** — standard regional IP sets will not work
- Exit Node Elastic IPs are added in CIDR `/32` format
- S3 origins behind CloudFront require additional Origin Access Identity (OAI) configuration
- Twingate Resource name must match the CloudFront FQDN exactly (e.g., `beamreach.cloudfront.net`)

## Prerequisites
- One or more [AWS Exit Nodes](https://www.twingate.com/docs/aws-exit-nodes) provisioned with Elastic IPs
- AWS Firewall Manager access
- AWS CloudFront Distribution already created
- Twingate admin console access

## Step-by-Step

1. **Create IP Set in AWS Firewall Manager**
   - Navigate to AWS WAF & Shield → IP Sets
   - Create new IP Set, set Region to **Global (CloudFront)**
   - Add each Exit Node Elastic IP in CIDR format: `x.x.x.x/32`

2. **Assign WAF ACL to CloudFront Distribution**
   - Open CloudFront Distribution settings
   - Set **AWS WAF Web ACL** field to the IP Set created above
   - For S3 origins: configure Origin Access Identity to restrict S3 access exclusively to CloudFront

3. **Create Twingate Resource**
   - In Twingate admin console, create a Resource using the CloudFront domain as the name/address (e.g., `beamreach.cloudfront.net`)

4. **Authorize Users**
   - Create a Group in Twingate
   - Add the CloudFront Resource to the Group
   - Assign users to the Group

## Configuration Values
| Field | Value |
|-------|-------|
| AWS IP Set Region | `Global (CloudFront)` |
| IP format | `<Elastic-IP>/32` |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource identifier | CloudFront FQDN (e.g., `beamreach.cloudfront.net`) |

## Gotchas
- **Region must be Global**: CloudFront is a global service; regional IP sets cannot be attached to CloudFront distributions
- **S3 direct access**: Without OAI, users could bypass CloudFront/WAF by hitting S3 directly — OAI is required to fully lock down S3 content
- **Elastic IPs required**: Dynamic IPs on Exit Nodes will break the whitelist; EC2 Exit Nodes must have Elastic IPs assigned

## Related Docs
- [AWS Exit Nodes setup](https://www.twingate.com/docs/aws-exit-nodes)
- [Creating Twingate Resources](https://www.twingate.com/docs/resources)
- AWS S3 Origin Access Identity documentation (external)
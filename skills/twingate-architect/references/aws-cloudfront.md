---
source: https://www.twingate.com/docs/aws-cloudfront
type: docs
fetched: 2026-08-14
source_version: 528356781c08132237c7b56d14ea4191a2e31ec21105d9bd833634181bce2bbd
---

# AWS CloudFront SaaS App Gating with Twingate

## Page Title
How to SaaS App Gate AWS CloudFront

## Summary
Configure IP whitelisting for AWS CloudFront using Twingate AWS Exit Nodes as the allowed IP sources. Traffic is restricted via AWS WAF/Firewall Manager IP Sets, and access is controlled through Twingate Resources and Groups.

## Key Information
- Uses AWS Exit Node Elastic IPs as the whitelist source for CloudFront
- IP Set must be created with **Global (CloudFront)** region in AWS Firewall Manager
- CloudFront protection is enforced via AWS WAF Web ACL attached to the Distribution
- S3 origins require additional Origin Access Identity configuration to restrict direct S3 access

## Prerequisites
- AWS Exit Nodes created with Elastic IPs assigned to EC2 instances
- Access to AWS Firewall Manager and CloudFront console
- Twingate admin console access
- CloudFront Distribution already configured

## Step-by-Step

1. **Create IP Set in AWS Firewall Manager**
   - Region: `Global (CloudFront)`
   - Add Elastic IPs of Exit Node EC2 instances in CIDR format (e.g., `35.164.107.72/32`)

2. **Assign WAF ACL to CloudFront Distribution**
   - In CloudFront Distribution settings, set `AWS WAF Web ACL` to the IP Set created above

3. **Restrict S3 Origin (if applicable)**
   - Create an Origin Access Identity in S3 to limit access to CloudFront CDN + WAF ACL only

4. **Create Twingate Resource**
   - Resource name = FQDN of the CloudFront domain (e.g., `beamreach.cloudfront.net`)

5. **Authorize Users**
   - Create a Group, add the Resource and users to the Group

## Configuration Values
| Parameter | Value/Format |
|-----------|-------------|
| IP Set Region | `Global (CloudFront)` |
| IP CIDR format | `<Elastic_IP>/32` |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource name | CloudFront FQDN (e.g., `beamreach.cloudfront.net`) |

## Gotchas
- IP Set region **must** be `Global (CloudFront)` — not a standard AWS region; using a regional setting will not work with CloudFront
- S3-backed distributions need a separate Origin Access Identity or S3 direct access bypasses the WAF restriction entirely
- Twingate matches on FQDN/IP in the connection request — Resource name must exactly match the CloudFront domain

## Related Docs
- [AWS Exit Nodes setup](https://www.twingate.com/docs/aws-exit-nodes)
- [Creating Twingate Resources and Groups](https://www.twingate.com/docs/resources-and-groups)
- [AWS S3 Origin Access Identity documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/)
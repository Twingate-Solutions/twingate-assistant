# AWS CloudFront SaaS App Gating with Twingate

## Page Title
How to SaaS App Gate AWS CloudFront

## Summary
Configure IP whitelisting for AWS CloudFront using Twingate AWS Exit Nodes as the allowed IP sources. Traffic is restricted via AWS WAF IP Sets applied to CloudFront distributions, with Twingate controlling which users can route through the exit node IPs.

## Key Information
- Uses AWS Firewall Manager WAF IP Sets to whitelist Twingate exit node IPs
- CloudFront WAF rules must be created in **Global (CloudFront)** region, not a standard AWS region
- Exit node IPs are Elastic IPs assigned to EC2 instances
- Twingate Resource name must match the exact FQDN or IP address of the CloudFront domain (e.g., `beamreach.cloudfront.net`)

## Prerequisites
- AWS Exit Nodes created and running (EC2 instances with Elastic IPs assigned)
- External/Elastic IP addresses of exit node EC2 instances noted
- AWS Firewall Manager access
- Twingate admin console access
- CloudFront Distribution already configured

## Step-by-Step

1. **Create WAF IP Set** — In AWS Firewall Manager, create a new IP Set with Region set to `Global (CloudFront)`
2. **Add exit node IPs** — Enter each EC2 Elastic IP in CIDR format (e.g., `35.164.107.72/32`)
3. **Attach WAF ACL to CloudFront** — In CloudFront Distribution settings, set `AWS WAF Web ACL` to the IP Set created above
4. **(Optional) S3 Origin Access Identity** — If serving S3 content, create an Origin Access Identity to restrict S3 access exclusively to CloudFront + WAF ACL
5. **Create Twingate Resource** — Add a Resource in Twingate using the CloudFront FQDN (e.g., `beamreach.cloudfront.net`)
6. **Authorize users** — Create/assign a Group containing the Resource and the authorized users

## Configuration Values
| Parameter | Value |
|---|---|
| WAF IP Set Region | `Global (CloudFront)` |
| IP format | CIDR notation, e.g., `35.164.107.72/32` |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource identifier | CloudFront FQDN or IP address |

## Gotchas
- IP Set **must** use `Global (CloudFront)` region — standard regional IP Sets won't work with CloudFront
- Twingate matches on exact FQDN/IP in connection requests — Resource name must precisely match the protected CloudFront domain
- S3-backed distributions require an additional Origin Access Identity step to fully restrict direct S3 access

## Related Docs
- [AWS Exit Nodes setup](https://www.twingate.com/docs/aws-exit-nodes)
- [Create a Twingate Resource](https://www.twingate.com/docs/resources)
- [AWS S3 Origin Access Identity documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privateaccess-overview.html)
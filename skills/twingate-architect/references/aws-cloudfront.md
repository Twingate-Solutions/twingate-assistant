# AWS CloudFront SaaS App Gate

## Summary
Configure IP whitelisting for AWS CloudFront using Twingate AWS Exit Nodes. Traffic is restricted via AWS WAF IP Sets scoped to CloudFront (Global), ensuring only requests from designated Elastic IPs (exit nodes) reach your CloudFront distribution.

## Key Information
- Uses AWS Firewall Manager WAF + CloudFront WAF Web ACL for IP restriction
- Exit Node Elastic IPs are the allowlisted IPs in the WAF IP Set
- CloudFront WAF IP Sets must use **Global (CloudFront)** region, not a regional setting
- Twingate Resource name must match the CloudFront FQDN (e.g., `beamreach.cloudfront.net`)
- S3-backed CloudFront may require additional Origin Access Identity (OAI) configuration

## Prerequisites
- AWS Exit Nodes created with Elastic IPs assigned ([AWS Exit Nodes docs](https://www.twingate.com/docs/aws-exit-nodes))
- Access to AWS Firewall Manager and AWS CloudFront console
- Twingate admin console access

## Step-by-Step

1. **Create WAF IP Set** in AWS Firewall Manager
   - Region: `Global (CloudFront)`
   - Add Elastic IPs of all exit node EC2 instances in CIDR format (e.g., `35.164.107.72/32`)

2. **Assign WAF ACL to CloudFront Distribution**
   - In CloudFront Distribution settings, set `AWS WAF Web ACL` to the IP Set created above

3. **(S3 only) Restrict S3 origin access**
   - Create an Origin Access Identity to limit S3 content access exclusively to CloudFront + WAF ACL
   - Consult AWS S3 documentation for OAI setup

4. **Create Twingate Resource**
   - Resource name/address = CloudFront FQDN (e.g., `beamreach.cloudfront.net`)

5. **Authorize Users**
   - Create a Twingate Group
   - Add the CloudFront Resource to the Group
   - Assign users to the Group

## Configuration Values

| Parameter | Value |
|-----------|-------|
| WAF IP Set Region | `Global (CloudFront)` |
| IP format | CIDR (e.g., `35.164.107.72/32`) |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource identifier | CloudFront FQDN or IP |

## Gotchas
- WAF IP Set **must** be set to `Global (CloudFront)` — regional IP sets will not work with CloudFront
- Each exit node Elastic IP must be added individually as `/32` CIDR entries
- Without OAI on S3 origins, users may bypass CloudFront WAF by accessing S3 directly
- Twingate authorizes based on exact FQDN/IP match in the connection request — Resource name must match the actual CloudFront domain

## Related Docs
- [AWS Exit Nodes setup](https://www.twingate.com/docs/aws-exit-nodes)
- [Creating Twingate Resources](https://www.twingate.com/docs/resources)
- AWS S3 Origin Access Identity documentation
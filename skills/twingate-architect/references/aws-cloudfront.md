# How to SaaS App Gate AWS CloudFront

## Summary
Configures IP whitelisting for AWS CloudFront using Twingate AWS Exit Nodes as the allowed IP sources. Traffic is restricted via AWS WAF/Firewall Manager to only allow connections from Twingate Exit Node Elastic IPs. Users must be authorized in Twingate to route through those exit nodes.

## Key Information
- Uses AWS WAF IP Sets scoped to **Global (CloudFront)** region
- Exit Node Elastic IPs are added in CIDR notation (e.g., `35.164.107.72/32`)
- WAF ACL is attached directly to the CloudFront Distribution
- S3-backed distributions may require additional Origin Access Identity (OAI) configuration
- Twingate Resource name must match the CloudFront FQDN exactly

## Prerequisites
- AWS Exit Nodes created and running (EC2 instances with Elastic IPs assigned)
- External/Elastic IP addresses of those EC2 instances
- AWS Firewall Manager access
- AWS CloudFront Distribution already exists
- Twingate admin console access

## Step-by-Step

1. **Create IP Set in AWS Firewall Manager**
   - Region: `Global (CloudFront)`
   - Add each Exit Node Elastic IP in CIDR format: `<IP>/32`

2. **Assign WAF ACL to CloudFront Distribution**
   - In CloudFront Distribution settings → `AWS WAF Web ACL`
   - Select the IP Set created above

3. **(Optional) Restrict S3 Origin Access**
   - Create Origin Access Identity (OAI) to limit S3 content access to CloudFront + WAF only
   - Follow AWS S3 documentation for OAI setup

4. **Create Twingate Resource**
   - Resource name = CloudFront FQDN (e.g., `beamreach.cloudfront.net`)
   - Twingate matches on FQDN/IP from the connection request

5. **Authorize Users**
   - Create a Group in Twingate
   - Add the CloudFront Resource to the Group
   - Assign users to the Group

## Configuration Values
| Parameter | Value |
|-----------|-------|
| IP Set Region | `Global (CloudFront)` |
| IP format | `<Elastic-IP>/32` |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource identifier | CloudFront FQDN or IP |

## Gotchas
- IP Set **must** be created with `Global (CloudFront)` region — standard regional IP sets won't work with CloudFront
- Each Elastic IP needs its own `/32` CIDR entry
- Twingate Resource name must be the **exact FQDN** used in requests — mismatch will block access
- S3 origins need OAI separately; WAF ACL alone doesn't restrict direct S3 bucket access

## Related Docs
- AWS Exit Nodes setup (prerequisite)
- Twingate Resource creation instructions
- AWS S3 Origin Access Identity documentation
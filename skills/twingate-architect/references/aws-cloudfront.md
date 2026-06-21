# AWS CloudFront SaaS App Gating

## Page Title
How to SaaS App Gate AWS CloudFront

## Summary
Configure IP whitelisting for AWS CloudFront using Twingate AWS Exit Nodes. Traffic is restricted via AWS WAF/Firewall Manager to only allow connections from Exit Node Elastic IPs. Users are then authorized through Twingate Resources and Groups.

## Key Information
- Uses AWS WAF IP Sets scoped to **Global (CloudFront)** region
- Exit Node IPs must be Elastic IPs assigned to EC2 instances
- CloudFront protection is FQDN-based in Twingate (e.g., `beamreach.cloudfront.net`)
- S3-backed CloudFront distributions may require additional Origin Access Identity configuration

## Prerequisites
- AWS Exit Nodes created and running (EC2 instances with assigned Elastic IPs)
- External IP addresses of Exit Node EC2 instances noted in CIDR format
- Access to AWS Firewall Manager and CloudFront console
- Twingate admin console access

## Step-by-Step

1. **Create IP Set in AWS Firewall Manager**
   - Navigate to AWS Firewall Manager → IP Sets
   - Set Region to `Global (CloudFront)`
   - Add Exit Node Elastic IPs in CIDR format (e.g., `35.164.107.72/32`)

2. **Assign WAF ACL to CloudFront Distribution**
   - In AWS CloudFront, open your Distribution settings
   - Set `AWS WAF Web ACL` field to the IP Set created above

3. **(Optional) Restrict S3 Origin Access**
   - Create an Origin Access Identity to limit S3 content access exclusively to CloudFront + WAF ACL
   - Refer to AWS S3 documentation

4. **Create Twingate Resource**
   - In Twingate admin console, create a Resource using the CloudFront FQDN (e.g., `beamreach.cloudfront.net`)

5. **Authorize Users**
   - Create a Group in Twingate
   - Add the CloudFront Resource to the Group
   - Assign users to the Group

## Configuration Values
| Field | Value |
|-------|-------|
| AWS IP Set Region | `Global (CloudFront)` |
| IP format | CIDR notation (e.g., `x.x.x.x/32`) |
| CloudFront setting | `AWS WAF Web ACL` |
| Twingate Resource name | CloudFront FQDN or IP address |

## Gotchas
- IP Set **must** use `Global (CloudFront)` region — regional settings will not work with CloudFront
- Each Exit Node IP needs its own `/32` CIDR entry
- S3 origins require separate Origin Access Identity configuration or S3 content remains publicly accessible bypassing WAF
- Twingate authorizes based on exact FQDN/IP in the connection request — Resource name must match the CloudFront domain precisely

## Related Docs
- AWS Exit Nodes setup (prerequisite)
- Twingate Resource creation instructions
- AWS S3 Origin Access Identity documentation
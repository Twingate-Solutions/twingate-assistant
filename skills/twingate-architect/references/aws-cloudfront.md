# AWS CloudFront SaaS App Gating with Twingate

## Page Title
How to SaaS App Gate AWS CloudFront

## Summary
Restricts AWS CloudFront access to users connecting through Twingate by whitelisting Elastic IPs of AWS Exit Nodes via AWS WAF/Firewall Manager. Combines CloudFront WAF ACL IP filtering with Twingate resource authorization to enforce identity-based access control.

## Key Information
- Uses AWS WAF IP Sets scoped to **Global (CloudFront)** region
- Exit Node Elastic IPs are the whitelisted IPs — not user IPs
- CloudFront distribution is represented as a Twingate Resource by its FQDN
- S3-backed CloudFront may require additional Origin Access Identity configuration

## Prerequisites
- AWS Exit Nodes created with Elastic IPs assigned (see AWS Exit Nodes docs)
- Access to AWS Firewall Manager and CloudFront console
- Twingate admin console access

## Step-by-Step

### 1. Create IP Set in AWS Firewall Manager
- Navigate to AWS Firewall Manager → IP Sets
- Create new IP Set with **Region: Global (CloudFront)**
- Add Exit Node Elastic IPs in CIDR notation (e.g., `35.164.107.72/32`)

### 2. Assign WAF ACL to CloudFront Distribution
- In AWS CloudFront, open the target Distribution settings
- Set **AWS WAF Web ACL** to the IP Set created above
- *For S3 origins*: Create an Origin Access Identity to restrict S3 access to CloudFront only

### 3. Create Twingate Resource
- In Twingate admin console, create a Resource using the CloudFront FQDN
- Example: `beamreach.cloudfront.net`

### 4. Authorize Users
- Create a Group in Twingate
- Assign the CloudFront Resource to the Group
- Add users to the Group

## Configuration Values

| Parameter | Value/Format |
|-----------|-------------|
| IP Set Region | `Global (CloudFront)` |
| IP CIDR format | `<Elastic-IP>/32` |
| Twingate Resource name | CloudFront FQDN (e.g., `example.cloudfront.net`) |

## Gotchas
- IP Set **must** be created with `Global (CloudFront)` region — regional IP sets won't apply to CloudFront
- Twingate matches on the **exact FQDN or IP** in the connection request — Resource name must match the CloudFront domain precisely
- S3 origins require separate Origin Access Identity setup; WAF ACL alone doesn't restrict direct S3 bucket access
- All Exit Node IPs must be added to the IP Set — missing one will block users routed through that node

## Related Docs
- AWS Exit Nodes setup (prerequisite)
- Twingate Resource creation instructions
- AWS S3 Origin Access Identity documentation (for S3-backed distributions)
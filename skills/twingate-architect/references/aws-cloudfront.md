## SaaS App Gate: AWS CloudFront

Configures IP whitelisting for AWS CloudFront using Twingate Connector Elastic IPs and AWS WAF. Requires AWS Exit Nodes with static Elastic IP addresses deployed before starting.

**Key Information:**
- Uses AWS WAF IP Sets and Web ACLs to restrict CloudFront access to Connector IPs
- CloudFront WAF must use region `Global (CloudFront)` -- not a regional WAF
- The Twingate Resource address is the CloudFront FQDN (e.g., `beamreach.cloudfront.net`), not an IP
- For S3-backed CloudFront, an Origin Access Identity (OAI) may be needed to block direct S3 access

**Prerequisites:**
- AWS Exit Nodes (EC2 instances with Elastic IPs) already deployed -- see `/docs/aws-exit-node`
- External (Elastic) IP addresses of the Connector EC2 instances

**Step-by-Step:**
1. In AWS Firewall Manager, create an IP Set with Region = `Global (CloudFront)`
2. Add Connector Elastic IPs in CIDR format (e.g., `35.164.107.72/32`)
3. In AWS CloudFront, assign the IP Set as the `AWS WAF Web ACL` on the CloudFront Distribution
4. (Optional) For S3 origins: create an Origin Access Identity to restrict S3 content to CloudFront only
5. In Twingate admin console, create a Resource for the CloudFront FQDN
6. Associate the Resource with the Remote Network containing the Exit Node Connectors
7. Add the Resource to a Group and assign authorized users

**Gotchas:**
- The WAF IP Set region must be `Global (CloudFront)` -- regional WAF ACLs cannot be applied to CloudFront distributions
- Both the Resource FQDN and the actual CloudFront domain must match; Twingate uses the FQDN from the connection request for authorization

**Related Docs:**
- /docs/aws-exit-node -- Deploying AWS Exit Nodes with static IPs
- /docs/whitelisting-traffic-to-public-services -- General SaaS IP whitelisting pattern
- /docs/resources -- Creating Resources

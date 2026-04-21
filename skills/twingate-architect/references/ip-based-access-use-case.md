## Page Title
Application Gating (IP-Based Access)

## Summary
Use case overview for using Twingate as an egress IP gateway to secure SaaS apps and private services that restrict access by IP address. Covers staging server protection, lightweight CASB deployment, and layering device controls on top of IP-restricted services.

## Key Information
- Connector acts as a static egress IP — allowlist the Connector's IP in the target SaaS app or service
- Split-tunnel routes only IP-restricted traffic through the Connector; rest of traffic is unaffected
- Adds MFA and device posture checks to SaaS apps that don't natively support them
- Two Connector deployment options: Twingate-managed static IPs, or self-hosted Connectors with company-specific IPs (e.g. AWS Elastic IP)
- Audit log export for access monitoring and compliance evidence
- Compatible with IdP-native conditional access policies (Okta, Entra ID, Google Workspace, JumpCloud, OneLogin)

## Prerequisites
- Connector deployed with a stable/static IP address (or Twingate-managed static IP)
- Target service must support IP allowlisting

## Step-by-Step
Not applicable on this page — see linked guides for each IdP/service combination.

## Configuration Values
None on this page.

## Gotchas
- Twingate does not provide a dedicated "static IP" product — you must deploy a Connector in infrastructure with a static/elastic IP, or use exit nodes
- This is split-tunnel: only traffic explicitly routed to the Connector's network gets the egress IP; misconfigured resource definitions mean traffic bypasses the Connector
- "Application Gating" and "SaaS App Gating" are used interchangeably in Twingate docs

## Related Docs
- `/docs/saas-app-gating` — SaaS app gating getting started
- `/docs/whitelisting-traffic-to-public-services` — best practices for IP whitelisting
- `/docs/exit-networks` — full-tunnel exit node alternative
- `/docs/configuring-aws-exit-nodes` — AWS Elastic IP exit node setup
- `/docs/saas-app-gating-best-practices` — SaaS gating best practices

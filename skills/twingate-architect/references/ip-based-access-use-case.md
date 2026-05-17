# Application Gating (IP-Based Access) - Twingate

## Summary
Twingate enables IP address-based access control for SaaS applications and private services by routing traffic through Connectors with known IP addresses. This allows organizations to whitelist specific IPs at the service level while applying additional security controls like MFA and device checks. Traffic uses split tunneling, so only relevant traffic routes through the Connector.

## Key Information
- Route traffic to IP-restricted resources through Twingate Connectors with static/known IPs
- Apply security controls (MFA, device policy) to SaaS apps that don't natively support them
- Split tunnel architecture: only restricted-resource traffic routes through Connector
- Audit logs available for compliance/export
- Connector options: Twingate-managed (static IPs) or self-hosted in private infrastructure

## Use Cases
- Third-party SaaS apps that restrict access by IP allowlist
- Securing staging servers via IP whitelisting
- Lightweight CASB deployment

## Prerequisites
- Twingate Connector deployed (cloud-managed or self-hosted)
- Admin access to Twingate web console
- Target service must support IP-based access restrictions

## Integration Guides Available
- Google Workspace
- JumpCloud
- Microsoft Entra ID (two guides: general + Office 365)
- Okta
- OneLogin
- AWS Exit Nodes with app-native IP filtering
- AWS CloudFront

## Gotchas
- Self-hosted Connectors use your infrastructure's IP addresses; Twingate-managed Connectors use Twingate-assigned static IPs — choose based on which IPs you whitelist at the target service
- Split tunneling means general internet traffic is unaffected, but confirm the target service sees Connector egress IP, not the user's local IP

## Related Docs
- Getting Started with SaaS App Gating
- Best Practices for Whitelisting Traffic to Public Resources
- Best Practices for SaaS App Gating
- Connector deployment documentation
- Audit logs documentation
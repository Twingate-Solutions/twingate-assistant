# Application Gating (IP-Based Access) - Twingate

## Summary
Twingate enables IP address-based access control for SaaS apps and private services by routing traffic through Connectors with static or company-specific IP addresses. This allows organizations to whitelist specific IPs for third-party services, staging servers, and act as a lightweight CASB. Only traffic bound for restricted resources is routed through the Connector (split tunnel), preserving general network performance.

## Key Information
- **Use cases**: SaaS app IP whitelisting, staging server access, lightweight CASB deployment
- **Split tunnel architecture**: Only IP-restricted traffic routes through Connector; other traffic unaffected
- **Connector IP options**: Use Twingate-managed static IPs or deploy Connectors in private infrastructure with company-owned IPs
- **Security controls**: Layered MFA and device controls can be applied to SaaS apps that don't natively support them
- **Audit logs**: Access activity logs available for download/export for compliance

## Prerequisites
- Twingate Connector deployed (cloud-managed or self-hosted in private infrastructure)
- Twingate client installed on end-user devices
- Admin access to Twingate web console
- Admin access to target SaaS app for IP whitelist configuration

## Configuration Guides (by IdP/Service)
- Google Workspace
- JumpCloud
- Microsoft Entra ID
- Okta
- OneLogin
- AWS Exit Nodes (app-native IP filtering)
- AWS CloudFront
- Office 365 with Microsoft Entra ID

## Gotchas
- Connectors must have static/predictable egress IPs for whitelisting to work reliably; verify IP stability before configuring third-party restrictions
- Self-hosted Connectors use your infrastructure's egress IPs; Twingate-managed Connectors use Twingate's IPs — confirm which type is deployed before whitelisting
- Split tunnel behavior is by design; ensure the resource's IP range is correctly defined in Twingate so traffic routes through the Connector

## Related Docs
- Getting Started with SaaS App Gating
- Best Practices for Whitelisting Traffic to Public Resources
- Best Practices for SaaS App Gating
- Connector deployment documentation
- Audit logs documentation
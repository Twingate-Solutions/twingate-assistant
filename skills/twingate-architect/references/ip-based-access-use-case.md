# Application Gating (IP-Based Access)

## Summary
Twingate enables IP address-based access control for SaaS apps and private services by routing traffic through Connectors with static IPs. This allows organizations to whitelist specific IP addresses while applying additional security controls like MFA and device policies. Traffic uses split tunneling, so only restricted-resource traffic routes through Twingate.

## Key Information
- Routes only IP-restricted traffic through Connectors (split tunnel architecture)
- Connectors can use Twingate-managed static IPs or company-owned IPs in private infrastructure
- Applies security controls (MFA, device policies) to SaaS apps lacking native support
- Audit logs available for compliance and access monitoring
- End-user client supports multiple platforms, no technical knowledge required

## Prerequisites
- Twingate account with admin access
- Twingate Connector deployed (cloud-managed or self-hosted)
- Target SaaS app or service that supports IP allowlisting
- Twingate client installed on end-user devices

## Primary Use Cases
- Third-party services restricting access by IP address
- Securing staging/dev servers
- Lightweight CASB deployment
- SaaS apps requiring IP whitelisting (Google Workspace, Okta, Office 365, etc.)

## Configuration Approach
1. Deploy a Connector in target infrastructure or use Twingate-managed Connector
2. Note the static egress IP address of the Connector
3. Whitelist that IP in the target SaaS app or service
4. Create a Twingate Resource pointing to the SaaS app domain/IP
5. Assign Resource to appropriate Group with desired access policies
6. Users access the resource via Twingate client

## Supported Integrations (Documented Guides)
- Google Workspace
- JumpCloud
- Microsoft Entra ID (including Office 365 / CloudFront)
- Okta
- OneLogin
- AWS Exit Nodes / AWS CloudFront

## Gotchas
- Traffic must be routed through the Connector for IP whitelisting to work — users accessing the SaaS app directly (bypassing Twingate) will be blocked
- Self-hosted Connectors use your infrastructure's IP; verify static IP assignment at the infrastructure level
- Twingate-managed Connectors provide static IPs automatically, but self-hosted requires manual static IP configuration

## Related Docs
- [Getting Started with SaaS App Gating](https://www.twingate.com/docs/getting-started-saas-app-gating)
- [Best Practices for Whitelisting Traffic to Public Resources](https://www.twingate.com/docs/best-practices-whitelisting)
- [Best Practices for SaaS App Gating](https://www.twingate.com/docs/best-practices-saas-app-gating)
- [Deploy Connectors](https://www.twingate.com/docs/connectors)
- [Audit Logs](https://www.twingate.com/docs/audit-logs)
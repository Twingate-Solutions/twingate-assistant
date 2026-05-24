# Application Gating (IP-Based Access)

## Summary
Twingate enables IP address-based access control for SaaS apps and private services by routing traffic through Connectors with static or company-specific IP addresses. Only traffic bound for restricted resources is tunneled, preserving general network performance via split-tunnel architecture.

## Key Information
- Routes only relevant traffic through Connectors (split-tunnel), avoiding VPN gateway bottlenecks
- Connectors can use Twingate-managed static IPs or customer-deployed IPs in private infrastructure
- Supports layered security controls (MFA, device posture) on top of SaaS apps that lack native support
- Audit logs available for export/download for compliance purposes
- Client supports multiple platforms with no end-user technical knowledge required

## Prerequisites
- Twingate account with admin access
- Connector deployed (cloud-managed or self-hosted in private infrastructure)
- Target SaaS app or service must support IP allowlisting

## Common Use Cases
- Third-party services restricting access by IP address
- Securing staging servers
- Lightweight CASB deployment

## Configuration Approach
1. Deploy a Connector (Twingate-managed or self-hosted)
2. Obtain the static egress IP of the Connector
3. Whitelist that IP in the target SaaS app or service
4. Create a Twingate Resource pointing to the SaaS app domain/IP
5. Assign the Resource to appropriate Groups/Users

## Supported Integrations (Documented Guides)
- Google Workspace
- JumpCloud
- Microsoft Entra ID (including Office 365)
- Okta
- OneLogin
- AWS Exit Nodes / CloudFront

## Gotchas
- Twingate-managed Connector IPs are static but Twingate-controlled; use self-hosted Connectors if company-owned IPs are required for whitelisting
- Traffic to non-Twingate resources is NOT tunneled — ensure the SaaS resource is explicitly defined in Twingate
- Review "Best Practices for Whitelisting Traffic to Public Resources" before configuring to avoid split-tunnel misconfigurations

## Related Docs
- [Getting Started with SaaS App Gating](https://www.twingate.com/docs)
- Best Practices for Whitelisting Traffic to Public Resources
- Best Practices for SaaS App Gating
- Deploy Connectors
- Audit Logs
# Application Gating (IP-Based Access)

## Summary
Twingate enables IP address-based access control for SaaS apps and private services by routing traffic through Connectors with static or company-specific IPs. Only traffic bound for IP-restricted resources routes through the Connector (split tunnel), avoiding VPN gateway bottlenecks. Supports adding security controls (MFA, device checks) to SaaS apps that lack native support.

## Key Information
- Routes only relevant traffic through Connectors (split tunnel architecture)
- Connectors can use Twingate-managed static IPs or self-hosted IPs in private infrastructure
- Audit logs available for compliance/export
- Admin console is web-based; client supports multiple platforms

## Use Cases
- SaaS apps restricting access by IP whitelist
- Securing staging servers
- Lightweight CASB deployment
- Adding MFA/device controls to SaaS apps without native support

## Prerequisites
- Twingate Connector deployed (cloud-managed or self-hosted)
- Access to target SaaS app's IP allowlist configuration
- Twingate admin console access

## Configuration Options
- **Twingate-managed Connectors**: Static IPs managed by Twingate
- **Self-hosted Connectors**: Deploy in private infrastructure using company-specific IP addresses

## Related Docs
- Getting Started with SaaS App Gating
- Best Practices for Whitelisting Traffic to Public Resources
- Best Practices for SaaS App Gating
- SaaS App Gating with Google Workspace
- SaaS App Gating with JumpCloud
- SaaS App Gating with Microsoft Entra ID
- SaaS App Gating with Okta
- SaaS App Gating with OneLogin
- SaaS App Gate with App Native IP Filtering and AWS Exit Nodes
- SaaS App Gate AWS CloudFront
- SaaS App Gate Office 365 with Microsoft Entra ID

## Gotchas
- IP whitelisting alone does not enforce user-level authentication — combine with Twingate access policies for full security
- Self-hosted Connectors require managing your own static IP assignment to ensure the whitelist remains valid after restarts/redeployments
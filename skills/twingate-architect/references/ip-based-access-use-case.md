# Application Gating (IP-Based Access)

## Summary
Twingate enables IP address-based access control for SaaS apps and private services by routing traffic through Connectors with known static IPs. This allows organizations to whitelist Twingate Connector IPs at the application level, enforcing access controls without a full VPN architecture.

## Key Information
- Routes only restricted-resource traffic through Connectors (split tunnel), not all traffic
- Supports both Twingate-managed Connectors (with Twingate-provided static IPs) and self-hosted Connectors (company-owned IPs)
- Enables applying device controls and MFA to SaaS apps that don't natively support them
- Audit logs available for compliance/export
- Admin console is web-based; client installs without IT assistance

## Prerequisites
- Twingate account with admin access
- Connector deployed (cloud-managed or self-hosted in private infrastructure)
- Target SaaS app or service must support IP allowlisting

## Common Use Cases
- Restricting SaaS app access to known Connector IPs
- Securing staging servers via IP whitelist
- Lightweight CASB deployment

## Configuration Approach
1. Deploy a Twingate Connector (Twingate-managed for static IPs, or self-hosted for company IPs)
2. Note the static egress IP(s) of the Connector
3. Whitelist those IPs in the target SaaS app or service
4. Define the SaaS app as a Resource in Twingate
5. Assign Resource access to appropriate users/groups
6. Users access the resource through the Twingate client

## Supported Identity Provider Integrations
- Google Workspace
- JumpCloud
- Microsoft Entra ID
- Okta
- OneLogin

## Supported Service-Specific Guides
- AWS CloudFront
- AWS Exit Nodes
- Office 365 with Microsoft Entra ID

## Gotchas
- Twingate-managed Connectors provide Twingate-owned IPs; use self-hosted Connectors if company-specific egress IPs are required
- Split tunnel only routes target resource traffic through Connector — other traffic is unaffected
- IP allowlisting at the SaaS app must match the Connector's egress IP exactly

## Related Docs
- Getting Started with SaaS App Gating
- Best Practices for Whitelisting Traffic to Public Resources
- Best Practices for SaaS App Gating
- Connector deployment documentation
- Audit logs documentation
# Application Gating (IP-Based Access)

## Summary
Twingate enables IP address-based access control for SaaS apps and private services by routing traffic through Connectors with static/known IP addresses. Only traffic bound for restricted resources is routed through Twingate (split tunnel), avoiding VPN gateway bottlenecks. Supports adding security controls (MFA, device checks) to SaaS apps lacking native support.

## Key Information
- Routes only targeted traffic through Connectors, not all network traffic
- Connectors can use Twingate-managed static IPs or customer-deployed infrastructure IPs
- Audit logs available for compliance/export
- Admin console is web-based; end-user clients require no technical knowledge
- Supports major IdPs: Okta, Entra ID, JumpCloud, Google Workspace, OneLogin

## Use Cases
- Third-party SaaS apps restricting access by IP whitelist
- Securing staging servers via IP allowlist
- Lightweight CASB deployment
- Applying MFA/device controls to SaaS apps without native support

## Prerequisites
- Twingate Connector deployed (cloud-managed or self-hosted)
- Static IP address associated with Connector (Twingate-managed or infrastructure-specific)
- Target SaaS app/service must support IP-based access restrictions

## Configuration Approaches
| Scenario | Connector Type |
|----------|---------------|
| Twingate-managed IPs | Twingate cloud Connectors |
| Company-specific IPs | Self-deployed Connectors in private infra |
| AWS exit nodes | AWS-hosted Connectors |

## Related Guides
- Getting Started with SaaS App Gating
- Best Practices for Whitelisting Traffic to Public Resources
- Best Practices for SaaS App Gating
- IdP-specific: Google Workspace, JumpCloud, Entra ID, Okta, OneLogin
- AWS CloudFront gating
- Office 365 with Entra ID
- App Native IP Filtering with AWS Exit Nodes

## Gotchas
- Connector IP must be the one whitelisted in the target service — verify which IP the Connector egresses from before configuring allowlists
- Split tunnel behavior means only traffic to the defined resource routes through Twingate; misconfigured resource definitions will bypass the Connector
- Self-hosted Connectors require managing your own static IP assignment

## Related Docs
- Connector deployment documentation
- Audit logs export
- Best Practices for Whitelisting Traffic to Public Resources
---
source: https://www.twingate.com/docs/ip-based-access-use-case
type: docs
fetched: 2026-08-14
source_version: 1e692badee8adcbfab8dbf9b391894964b9f200c876f8220def3bdc169c99b4a
---

# Application Gating (IP-Based Access)

## Page Title
Application Gating / IP-Based Access Use Case

## Summary
Twingate enables IP address-based access control for SaaS apps and private services by routing traffic through Connectors with static or company-specific IPs. This allows organizations to whitelist Twingate Connector IPs at the application layer, enforcing access controls without a traditional VPN gateway.

## Key Information
- Routes only IP-restricted traffic through Connectors (split tunnel) — no performance bottleneck
- Connectors can use Twingate-managed static IPs or self-hosted Connectors with company IPs
- Adds security controls (MFA, device posture) to SaaS apps that lack native support
- Audit logs available for compliance/export
- Supported IdP integrations: Google Workspace, JumpCloud, Microsoft Entra ID, Okta, OneLogin

## Use Cases
- SaaS apps with IP allowlisting (e.g., Office 365, Google Workspace)
- Staging server access restriction
- Lightweight CASB deployment
- AWS CloudFront and AWS exit node gating

## Prerequisites
- Twingate account with admin access
- Twingate Connector deployed (cloud-managed or self-hosted)
- Target SaaS app must support IP-based access restrictions
- End users must install Twingate client

## Configuration Approach
1. Deploy a Connector (Twingate-managed for static IP, or self-hosted for company IP)
2. Note the Connector's egress IP address
3. Whitelist that IP in the target SaaS application's IP allowlist
4. Define the SaaS app's public IP/hostname as a Twingate Resource
5. Assign Resource access to appropriate Users/Groups
6. Users connect via Twingate client — traffic to that resource routes through Connector

## Gotchas
- Only traffic bound for the defined Resource routes through the Connector; general internet traffic is unaffected
- Self-hosted Connectors require stable/static outbound IP configuration on the host infrastructure
- Twingate-managed Connector IPs are managed by Twingate — verify IP stability before whitelisting in strict environments

## Related Docs
- Getting Started with SaaS App Gating
- Best Practices for Whitelisting Traffic to Public Resources
- Best Practices for SaaS App Gating
- IdP-specific guides: Google Workspace, JumpCloud, Entra ID, Okta, OneLogin
- SaaS App Gating with AWS Exit Nodes
- SaaS App Gating AWS CloudFront
- Office 365 gating with Microsoft Entra ID
- Deploy Connectors
- Audit Logs
# Getting Started with SaaS App Gating

## Page Title
Getting Started with Using Twingate for SaaS App Gating

## Summary
Twingate can gate SaaS application access by adding IP whitelisting rules at the identity provider (IdP) level rather than within individual SaaS apps. Users must route IdP authentication traffic through a Twingate Remote Network, so only authorized Twingate users can authenticate. This consolidates access control across both SaaS and private applications.

## Key Information
- Routes IdP authentication traffic through Twingate Connectors, exposing a consistent exit IP
- Works for SaaS apps that don't natively support IP whitelisting
- Consolidates IP whitelisting to IdP + Twingate instead of per-app settings
- Enables consistent device restrictions across platforms
- Authentication traffic volume is low (only IdP auth requests, not full SaaS traffic)

## Prerequisites
- Deployed Twingate Connectors with outbound internet access allowed
- A Remote Network designated for IdP traffic
- Known external exit IP(s) for that Remote Network
- Admin access to your IdP (Okta, JumpCloud, OneLogin, Entra ID, or Google Workspace)

## Step-by-Step Configuration

1. **Choose a Remote Network** for IdP authentication traffic to pass through
2. **Determine external exit IP** — add a resource like `*.whatsmyip.org` to the Remote Network, connect via Twingate, and check the displayed IP
3. **Use NAT gateway** (recommended if multiple Connectors) — present a single public IP to avoid managing multiple IPs
4. **Add IdP FQDN as a Resource** in the same Remote Network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply a Device-only Policy** to the IdP Resource to prevent authentication loops
6. **Configure IdP authentication policy** to only allow access from the determined external exit IP

## Configuration Values

| Component | Example Value |
|-----------|--------------|
| Okta FQDN | `tenant.okta.com` |
| Microsoft Entra FQDN | `login.microsoftonline.com` |
| Test IP resource | `*.whatsmyip.org` |
| Policy type for IdP resource | Device-only Policy |

## Gotchas

- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users can't authenticate with IdP because Twingate requires prior auth — apply Device-only Policy to break this circular dependency
- **Multiple Connectors**: Traffic is load-balanced across Connectors; use a NAT gateway to present a single exit IP, otherwise you must whitelist all Connector IPs at your IdP
- **Outbound internet required**: Connectors must allow outbound internet traffic, not just internal network access

## Related Docs
- [App Gating with Okta](#)
- [App Gating with JumpCloud](#)
- [App Gating with OneLogin](#)
- [App Gating with Microsoft Entra ID](#)
- [App Gating with Google Workspace](#)
- [App Gating Best Practices](#)
- Device-only Resource Policy documentation
- Connector deployment documentation
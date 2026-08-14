---
source: https://www.twingate.com/docs/saas-app-gating
type: docs
fetched: 2026-08-14
source_version: 3de7ea84f8c00be97274f582b8db779d0d33ad6decbbf679e0c5c03e8805720d
---

# SaaS App Gating with Twingate

## Page Title
Getting Started with Using Twingate for SaaS App Gating

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Twingate Connectors, then configuring the IdP to only allow logins from the Connector's public exit IP. This approach extends Twingate's authorization controls to SaaS apps without requiring native IP whitelisting support in each app.

## Key Information
- Only IdP authentication traffic routes through Twingate—not all SaaS traffic
- Works by IP-restricting the IdP itself, not individual SaaS apps
- Supports apps that don't natively support IP whitelisting
- Consolidates access control into IdP + Twingate configuration
- Enables consistent device policy enforcement across platforms

## Prerequisites
- Twingate Remote network configured with deployed Connectors
- Connectors must have outbound internet access
- Known public exit IP(s) for Connector traffic
- IdP that supports IP-based authentication policies (Okta, JumpCloud, OneLogin, Entra ID, Google Workspace)

## Step-by-Step Configuration

1. **Choose a Remote network** to route IdP authentication traffic through
2. **Determine external exit IP** — Add resource `*.whatsmyip.org` to the Remote network, connect via Twingate, visit the site to reveal the Connector's public IP
3. **Add IdP FQDN as a Resource** in the same Remote network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
4. **Apply a Device-only Policy** to the IdP Resource (prevents auth loop — users can reach IdP without needing prior IdP auth)
5. **Configure IdP authentication policy** to only permit logins from the Connector's public exit IP

## Configuration Values

| Item | Example Values |
|------|---------------|
| IdP Resource (Okta) | `tenant.okta.com` |
| IdP Resource (Entra ID) | `login.microsoftonline.com` |
| Test IP resource | `*.whatsmyip.org` |
| Policy type for IdP resource | Device-only Policy |

## Gotchas
- **Multiple Connectors**: Traffic load-balances across all Connectors in a Remote network — use a NAT gateway to present a single public IP, otherwise you must whitelist multiple IPs in the IdP
- **Auth loop risk**: Without a Device-only Policy on the IdP resource, users can't authenticate with the IdP because Twingate requires authentication first — always apply Device-only Policy to the IdP resource
- **Traffic origin**: Exit IP comes from the Connector host's network, not Twingate's infrastructure — verify the actual public IP using the whatsmyip method

## Related Docs
- App Gating with Okta
- App Gating with JumpCloud
- App Gating with OneLogin
- App Gating with Microsoft Entra ID
- App Gating with Google Workspace
- App Gating Best Practices
- Device-only Resource Policy documentation
- Twingate Connectors documentation
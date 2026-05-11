# SaaS App Gating with Twingate

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Twingate Connectors, then restricting IdP authentication policies to only allow the Connector's exit IP. This provides consistent access controls across both SaaS and private applications without configuring IP allowlists in each individual SaaS app.

## Key Information
- Traffic routed: Only IdP authentication requests pass through the Remote network (low volume)
- Connectors act as the exit point; their public IP becomes the allowlisted IP in IdP policies
- Works for SaaS apps that don't natively support IP whitelisting
- Consolidates access control to IdP + Twingate instead of per-app settings
- Device restrictions can be enforced consistently across platforms

## Prerequisites
- Twingate Connectors deployed with outbound internet access allowed
- An IdP (Okta, JumpCloud, OneLogin, Microsoft Entra ID, or Google Workspace)
- Ability to configure network/IP-based authentication policies in your IdP

## Step-by-Step Configuration

1. **Select a Remote network** to route IdP authentication traffic through; ensure Connectors have outbound internet access
2. **Determine exit IP** — add a resource like `*.whatsmyip.org` to the Remote network, connect via Twingate, and visit the site to reveal the public exit IP
3. **Use NAT if multiple Connectors** — place a NAT gateway in front of Connectors so all traffic presents a single public IP; avoids managing multiple IPs in IdP rules
4. **Add IdP FQDN as a Resource** in the same Remote network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply a Device-only Policy** to the IdP Resource to prevent authentication loops (users can reach IdP without needing prior Twingate auth)
6. **Configure IdP authentication policy** to only permit logins from the exit IP identified in step 2

## Configuration Values

| Item | Example Value |
|------|---------------|
| IdP Resource (Okta) | `tenant.okta.com` |
| IdP Resource (Entra ID) | `login.microsoftonline.com` |
| IP discovery resource | `*.whatsmyip.org` |
| Policy type for IdP resource | Device-only Policy |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP resource, users cannot authenticate with the IdP to gain Twingate access — creating a chicken-and-egg deadlock
- **Multiple Connectors = multiple IPs**: Without NAT, load-balanced traffic across Connectors produces multiple exit IPs that all need to be allowlisted in the IdP
- **Outbound internet required**: Connectors must be able to reach the internet; purely internal-only Connector deployments won't work

## Related Docs
- App Gating with Okta
- App Gating with JumpCloud
- App Gating with OneLogin
- App Gating with Microsoft Entra ID
- App Gating with Google Workspace
- App Gating Best Practices
- Device-only Resource Policy
- IP Whitelisting within SaaS applications (alternative approach)
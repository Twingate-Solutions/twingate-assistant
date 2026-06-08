# SaaS App Gating with Twingate

## Page Title
Getting Started with Using Twingate for SaaS App Gating

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Twingate Connectors, then configuring the IdP to only allow authentication from that Connector's public exit IP. This enables IP-based access control for SaaS apps even when the apps don't natively support IP whitelisting.

## Key Information
- Traffic routed: Only IdP authentication requests pass through the Remote network (low volume)
- Connectors serve as the exit point; their public IP is whitelisted in the IdP
- Multiple Connectors require NAT gateway to present a single public IP
- Supported IdPs: Okta, JumpCloud, OneLogin, Microsoft Entra ID, Google Workspace

## Prerequisites
- Twingate deployed with at least one Remote network and Connector
- Outbound internet traffic allowed from Connector hosts
- Admin access to your IdP to configure authentication/network policies

## Step-by-Step Configuration

1. **Select a Remote network** to route IdP authentication traffic through
2. **Determine external exit IP** — Add a resource like `*.whatsmyip.org` to the Remote network; access it via Twingate to reveal the Connector's public IP
3. **Configure NAT** (if multiple Connectors) — Use a NAT gateway so all Connectors share one public IP
4. **Add IdP FQDN as a Resource** in the same Remote network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply a Device-only Policy** to the IdP Resource — prevents authentication loop where Twingate auth is required before IdP auth completes
6. **Configure IdP policy** — Restrict SaaS app authentication to only the Connector's public exit IP

## Configuration Values

| Item | Example Value |
|------|---------------|
| Test resource for IP discovery | `*.whatsmyip.org` |
| Okta IdP FQDN | `tenant.okta.com` |
| Microsoft FQDN | `login.microsoftonline.com` |
| Policy type for IdP Resource | Device-only Policy |

## Gotchas

- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users may be unable to authenticate with Twingate (needed for IdP access) because IdP access requires Twingate (circular dependency)
- **Multiple Connectors = multiple IPs**: Without NAT, each Connector presents a different public IP, requiring multiple whitelist entries that must be maintained
- **Connector outbound internet required**: The Remote network's Connectors must be able to reach the internet, not just internal resources

## Related Docs
- App Gating with Okta
- App Gating with JumpCloud
- App Gating with OneLogin
- App Gating with Microsoft Entra ID
- App Gating with Google Workspace
- App Gating Best Practices
- Device-only Resource Policy (Twingate docs)
- Connector deployment documentation
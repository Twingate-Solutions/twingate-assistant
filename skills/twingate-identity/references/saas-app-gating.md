# SaaS App Gating with Twingate

## Page Title
Getting Started with using Twingate for SaaS App Gating

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Twingate Connectors, then restricting IdP auth policies to only allow the Connector's public exit IP. This enables IP whitelisting for SaaS apps that don't natively support it and consolidates access control into a single IdP+Twingate configuration.

## Key Information
- Only IdP authentication traffic routes through the Remote network (low bandwidth impact)
- Traffic exits to the internet via deployed Connectors—outbound internet must be permitted
- Multiple Connectors require NAT gateway to present a single public IP
- User traffic load-balances across all Connectors in a Remote network
- Supported IdPs: Okta, JumpCloud, OneLogin, Microsoft Entra ID, Google Workspace

## Prerequisites
- Twingate Connectors deployed with outbound internet access
- An existing Remote network to route IdP traffic through
- Admin access to your IdP to configure authentication policies
- Known public exit IP(s) for your Connector network

## Step-by-Step Configuration

1. **Choose a Remote network** to route IdP authentication traffic through
2. **Determine external exit IP** — Add a resource like `*.whatsmyip.org` to the Remote network, connect via Twingate, and visit the site to reveal the public IP
3. **Configure NAT (if multiple Connectors)** — Use a NAT gateway so all Connectors present a single public IP
4. **Add IdP FQDN as a Resource** in the same Remote network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply a Device-only Policy** to the IdP Resource to avoid authentication loops
6. **Configure IdP authentication policy** to only permit access from the Connector's public exit IP

## Configuration Values

| Parameter | Example Value |
|-----------|--------------|
| Okta IdP FQDN | `tenant.okta.com` |
| Entra ID FQDN | `login.microsoftonline.com` |
| IP discovery resource | `*.whatsmyip.org` |
| Policy type for IdP resource | Device-only Policy |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users cannot authenticate with the IdP because Twingate auth is required first—circular dependency
- **Multiple Connectors = multiple IPs**: Without NAT, you must whitelist every Connector's public IP in the IdP policy
- **Outbound internet required**: Connectors must be able to reach the internet; purely internal Connectors won't work

## Related Docs
- App Gating with Okta
- App Gating with JumpCloud
- App Gating with OneLogin
- App Gating with Microsoft Entra ID
- App Gating with Google Workspace
- App Gating Best Practices
- Device-only Resource Policy documentation
- Twingate Connectors deployment docs
# Getting Started with SaaS App Gating

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Twingate Connectors, then whitelisting only those Connector exit IPs in your IdP's authentication policy. This approach extends Twingate's authorization controls to SaaS apps without requiring each app to support native IP whitelisting.

## Key Information
- Authentication traffic (not application traffic) routes through the selected Remote network
- Only users authorized in Twingate can reach the IdP login endpoint, blocking unauthorized SaaS access
- Consolidates IP whitelisting into a single IdP+Twingate configuration
- Enables device-based restrictions across any platform

## Prerequisites
- Twingate Remote network with deployed Connectors (outbound internet allowed)
- Admin access to your IdP (Okta, JumpCloud, OneLogin, Microsoft Entra ID, or Google Workspace)
- Known external exit IP(s) for your Connector network

## Step-by-Step Configuration

1. **Choose a Remote network** to route IdP authentication traffic through
2. **Determine external exit IP** — Add a resource like `*.whatsmyip.org` to the Remote network; access it via Twingate to reveal the public IP
3. **Configure NAT (if multiple Connectors)** — Use a NAT gateway so all Connectors share a single public IP; avoids managing multiple IPs in IdP rules
4. **Add IdP FQDN as a Resource** in the same Remote network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply a Device-only Policy** to the IdP Resource — prevents authentication loops where Twingate auth is required before IdP auth can complete
6. **Configure IdP authentication policy** to only allow access from your Connector exit IP(s)

## Configuration Values

| Item | Example Values |
|------|---------------|
| Test resource for IP discovery | `*.whatsmyip.org` |
| Okta IdP FQDN | `tenant.okta.com` |
| Microsoft Entra FQDN | `login.microsoftonline.com` |
| Policy type for IdP resource | Device-only Policy |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP resource, users cannot authenticate with the IdP because Twingate itself requires prior IdP authentication — apply Device-only Policy to break this dependency
- **Multiple Connectors**: User traffic load-balances across all Connectors; without NAT, multiple exit IPs must all be whitelisted in the IdP
- **Traffic type**: Only IdP authentication requests transit this Remote network, not full SaaS app traffic

## Related Docs
- App Gating with Okta
- App Gating with JumpCloud
- App Gating with OneLogin
- App Gating with Microsoft Entra ID
- App Gating with Google Workspace
- App Gating Best Practices
- Device-only Resource Policy (Twingate docs)
- Twingate Connectors documentation
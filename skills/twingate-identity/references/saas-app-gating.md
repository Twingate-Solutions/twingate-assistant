# Getting Started with SaaS App Gating

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Twingate Connectors, then restricting IdP auth policies to only allow the Connector's exit IP. This enables IP whitelisting for SaaS apps that don't natively support it and consolidates access controls into a single IdP+Twingate configuration.

## Key Information
- Authentication traffic (not application traffic) routes through Twingate Connectors
- Connectors must have outbound Internet access
- Only IdP authentication requests pass through the Remote network — traffic volume is low
- User traffic load-balances across all Connectors in a Remote network
- Applies consistent device restrictions across SaaS and private apps

## Prerequisites
- Deployed Twingate Connectors with outbound Internet access
- A Remote network designated for IdP authentication traffic
- Known external exit IP(s) for that Remote network
- Access to configure IdP authentication/network policies

## Step-by-Step

1. **Choose a Remote network** to route IdP authentication traffic through
2. **Determine the external exit IP** — add `*.whatsmyip.org` as a Resource in the Remote network, connect via Twingate, and visit the site to reveal the public IP
3. **Use NAT gateway** (recommended if multiple Connectors) — present a single public IP to avoid managing multiple IPs in IdP policies
4. **Add IdP FQDN as a Resource** in the same Remote network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply a Device-only Policy** to the IdP Resource — prevents auth loop where Twingate access requires IdP auth, but IdP auth requires Twingate access
6. **Configure IdP authentication policy** to only permit access from the Connector exit IP

## Configuration Values
| Item | Example Value |
|------|---------------|
| Test Resource for IP discovery | `*.whatsmyip.org` |
| Okta IdP FQDN | `tenant.okta.com` |
| Microsoft Entra ID FQDN | `login.microsoftonline.com` |
| Resource Policy type | Device-only |

## Gotchas
- **Auth loop risk**: Without a Device-only Policy on the IdP Resource, users cannot authenticate with the IdP to gain Twingate access, which is required to reach the IdP — circular dependency
- **Multiple Connectors = multiple IPs**: Without NAT, you must whitelist all Connector exit IPs in your IdP; NAT simplifies this to one IP
- **Outbound Internet required**: Connectors must be able to reach the Internet, not just internal resources

## Related Docs
- App Gating with Okta
- App Gating with JumpCloud
- App Gating with OneLogin
- App Gating with Microsoft Entra ID
- App Gating with Google Workspace
- App Gating Best Practices
- Device-only Resource Policy
- Twingate Connectors documentation
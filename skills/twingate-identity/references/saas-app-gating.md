# Getting Started with SaaS App Gating

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Twingate Connectors, then configuring the IdP to only allow authentication from the Connector's public exit IP. This extends Twingate's authorization controls to SaaS apps without native IP whitelisting support and centralizes access control in one place.

## Key Information
- Traffic routed through Twingate exits via deployed Connectors; only IdP authentication requests pass through (low volume)
- Works by IP-whitelisting the Connector's public exit IP in the IdP authentication policy
- Supports apps that lack native IP whitelisting by enforcing at the IdP level
- Consolidates IP whitelisting from individual SaaS apps into a single IdP+Twingate config
- Device restrictions can be enforced consistently across platforms

## Prerequisites
- Twingate Connectors deployed with outbound internet access allowed
- A Remote Network designated for IdP authentication traffic
- Knowledge of (or ability to determine) the public exit IP of that Remote Network
- Multiple Connectors: use a NAT gateway to present a single public IP

## Step-by-Step Configuration

1. **Choose a Remote Network** to route IdP authentication traffic through
2. **Determine the public exit IP** — add a rule for `*.whatsmyip.org` in the Remote Network, connect via Twingate, and check the displayed IP
3. **Use NAT gateway** (if multiple Connectors) to ensure a single consistent public IP for all Connector traffic
4. **Add IdP authentication FQDN as a Resource** in the same Remote Network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply a Device-only Policy** to the IdP Resource to prevent authentication loops (users must reach IdP before Twingate auth completes)
6. **Configure IdP authentication policy** to only allow access from the determined public exit IP

## Configuration Values
| Item | Example Value |
|------|--------------|
| Test destination to find exit IP | `*.whatsmyip.org` |
| Okta IdP FQDN | `tenant.okta.com` |
| Microsoft Entra IdP FQDN | `login.microsoftonline.com` |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users can't authenticate with the IdP because Twingate requires IdP auth first — apply Device-only Policy to break this dependency
- **Multiple Connectors**: User traffic load-balances across Connectors; multiple exit IPs require managing multiple whitelist entries unless NAT consolidates them
- **Outbound internet must be allowed** from Connector hosts

## Related Docs
- App Gating with Okta
- App Gating with JumpCloud
- App Gating with OneLogin
- App Gating with Microsoft Entra ID
- App Gating with Google Workspace
- App Gating Best Practices
- Device-only Resource Policy
- Twingate Connectors
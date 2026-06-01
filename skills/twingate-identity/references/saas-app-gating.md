# Getting Started with SaaS App Gating

## Page Title
Getting Started with Using Twingate for SaaS App Gating

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Connectors and IP whitelisting the exit IP in your IdP's authentication policy. This extends Twingate's authorization controls to SaaS apps without native IP whitelisting support. Configuration requires adding your IdP's FQDN as a Twingate Resource with a Device-only Policy.

## Key Information
- Routes IdP authentication traffic through Twingate Connectors to enforce consistent access controls
- Works for SaaS apps lacking native IP whitelisting by centralizing restrictions at the IdP level
- Consolidates access control across both SaaS and private resources in one place
- Device-only Policy on the IdP Resource prevents authentication loops ("chicken-and-egg" problem)
- Only authentication requests pass through the Remote network — not full SaaS app traffic

## Prerequisites
- Existing Twingate Remote network with deployed Connectors
- Connectors must allow outbound Internet traffic
- Knowledge of your Connectors' public exit IP address
- Access to configure authentication policies in your IdP

## Step-by-Step Configuration

1. **Choose a Remote network** to route IdP authentication traffic through
2. **Determine external exit IP** — add a resource like `*.whatsmyip.org` to the Remote network and access it while connected to Twingate to reveal the public IP
3. **Configure NAT** (recommended if multiple Connectors) — use a NAT gateway to present a single public IP across all Connectors
4. **Add IdP authentication FQDN as a Resource** in the same Remote network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply a Device-only Policy** to the IdP Resource to prevent authentication dependency loops
6. **Configure IdP authentication policy** to only allow access from the identified external exit IP

## Configuration Values

| Value | Example |
|-------|---------|
| IdP Resource (Okta) | `tenant.okta.com` |
| IdP Resource (Microsoft) | `login.microsoftonline.com` |
| IP discovery resource | `*.whatsmyip.org` |
| Policy type for IdP Resource | Device-only Policy |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users cannot authenticate with the IdP because Twingate requires prior IdP authentication — apply Device-only Policy to break this cycle
- **Multiple Connectors**: Traffic is load-balanced across Connectors; without NAT, you must whitelist multiple IPs in your IdP
- **Traffic volume**: Only IdP auth requests traverse the Remote network, not full SaaS app traffic

## Related Docs
- App Gating with Okta
- App Gating with JumpCloud
- App Gating with OneLogin
- App Gating with Microsoft Entra ID (Azure AD)
- App Gating with Google Workspace
- App Gating Best Practices
- Device-only Resource Policy documentation
- Twingate Connectors documentation
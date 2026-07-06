# SaaS App Gating with Twingate

## Summary
Twingate can gate SaaS application access by routing IdP authentication traffic through Connectors and then IP-whitelisting only that exit IP in the IdP's authentication policy. This provides consistent access controls for SaaS apps that lack native IP whitelisting and consolidates policy management into a single IdP+Twingate configuration.

## Key Information
- Authentication traffic to IdP is routed through a Twingate Remote network/Connector
- IdP is configured to only allow authentication from the Connector's public exit IP
- Works with Okta, JumpCloud, OneLogin, Microsoft Entra ID, and Google Workspace
- Requires a **Device-only Policy** on the IdP Resource to prevent authentication loops

## Prerequisites
- Twingate Remote network with deployed Connectors
- Outbound internet access allowed from Connectors
- Admin access to your IdP to configure IP-based authentication policies
- Known public exit IP of your Connector infrastructure (single IP recommended)

## Step-by-Step Configuration

1. **Choose a Remote network** for IdP authentication traffic to route through
2. **Determine external exit IP** — Add a resource like `*.whatsmyip.org` to the Remote network; access it via Twingate to reveal the public IP
3. **Consolidate to single IP (recommended)** — Deploy a NAT gateway in front of Connectors so all Connectors share one public IP
4. **Add IdP FQDN as a Resource** in that Remote network (e.g., `tenant.okta.com`, `login.microsoftonline.com`)
5. **Apply Device-only Policy** to the IdP Resource (prevents auth loop)
6. **Configure IdP authentication policy** to only permit logins from the discovered exit IP

## Configuration Values

| IdP | Resource FQDN Example |
|-----|----------------------|
| Okta | `tenant.okta.com` |
| Microsoft Entra ID | `login.microsoftonline.com` |

**Test resource for IP discovery:** `*.whatsmyip.org`

## Gotchas
- **Auth loop risk**: Without a Device-only Policy on the IdP Resource, users cannot authenticate with the IdP because Twingate itself requires authentication first — apply Device-only Policy to break this dependency
- **Multiple Connectors = multiple IPs**: Traffic is load-balanced across Connectors; use NAT gateway to avoid managing multiple whitelisted IPs
- **Traffic routing**: Only IdP auth requests pass through this Remote network, not all SaaS traffic

## Related Docs
- [App Gating with Okta](#)
- [App Gating with JumpCloud](#)
- [App Gating with OneLogin](#)
- [App Gating with Microsoft Entra ID](#)
- [App Gating with Google Workspace](#)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [IP Whitelisting within SaaS applications](https://www.twingate.com/docs)
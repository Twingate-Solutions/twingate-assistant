# Twingate vs. Mesh VPNs

## Summary
Comparison of Twingate's zero-trust network access architecture against mesh VPN products (e.g., Tailscale, WireGuard-based solutions). Key differentiators are infrastructure compatibility, enterprise administration, and security feature depth. Twingate targets enterprises; mesh VPNs often require significant infrastructure changes to deploy.

## Key Differences

### Deployment
| Factor | Twingate | Mesh VPN |
|---|---|---|
| IP re-addressing required | No | Yes (unique IPs across entire network) |
| Overlapping IP support | ✅ | ❌ |
| Agent on servers | No (Connector only) | Yes (every device) |
| Co-exists with existing VPN | Yes | Typically requires replacement |

### Administration
- Twingate: Point-and-click admin console, consumer-grade UX
- Mesh VPN: Often requires JSON-based policy configuration
- Both offer APIs; Twingate API supports user provisioning automation and VPC server access provisioning

### Security Features (Twingate-specific)
- **Universal 2FA**: Applies 2FA to any resource type including SSH, no app changes needed
- **Device posture checks**: Access policies based on device attributes
- **Identity-indexed logs**: Network flow logs tied to user + device identity, centralized analytics

### Integrations
- IdP: Okta, OneLogin, Google Workspace, Entra ID (Azure AD), social SSO
- DNS filtering: Compatible with DNSFilter and similar tools
- Designed to coexist with existing security stack

## Prerequisites
- None for evaluation — Twingate deploys alongside existing infrastructure without changes

## Architecture Notes
- Twingate requires: Client agent (per end-user device) + Connector (lightweight, one per Remote Network)
- Mesh VPN requires: Agent on every device including servers

## Gotchas
- Mesh VPNs force IP uniqueness across all network segments — problematic for multi-segment networks with overlapping ranges
- Re-addressing in mesh VPN deployments requires full inventory + downstream updates (bookmarks, configs, user retraining)
- Mesh VPN agent-on-every-server model doesn't scale in dynamic cloud environments (VPCs with ephemeral instances)
- Mesh VPN admin UX varies widely — evaluate end-user client experience separately from admin experience

## Related Docs
- Twingate Connectors (Remote Networks)
- Universal 2FA configuration
- Device posture policies
- Identity provider integrations
- DNSFilter compatibility
- Administrative API reference
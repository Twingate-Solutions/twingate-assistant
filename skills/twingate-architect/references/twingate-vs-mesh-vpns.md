# Twingate vs. Mesh VPNs

## Summary
Twingate is an enterprise-first zero-trust access solution that differs from mesh VPNs primarily in deployment simplicity, network compatibility, and security feature depth. Unlike mesh VPNs, Twingate requires no network infrastructure changes, supports overlapping IP ranges, and installs only on client devices plus a single connector per network.

## Key Information

- **No IP re-addressing required**: Twingate supports overlapping IP address ranges across network segments; mesh VPNs require unique IPs across entire private network
- **Minimal agent footprint**: Twingate needs agents only on client devices + one Controller per Remote Network; mesh VPNs require agents on every device including servers
- **Co-existence capable**: Can run alongside existing VPNs for evaluation without rip-and-replace
- **Admin interface**: Point-and-click console vs. JSON-based policy configuration in some mesh VPN products
- **API available**: Full administrative API for automation (user provisioning, server access on VPC deployment)

## Security Features Beyond Basic Mesh VPN

- **Universal 2FA**: Applies 2FA to any private resource including non-app services (e.g., SSH), no application changes required
- **Device posture checks**: Access policies based on device attributes
- **Identity-indexed logging**: Network flow logs tied to user + device identity for centralized visibility

## Identity Provider Integrations

- Okta, OneLogin, Google Workspace, Entra ID (Azure AD), social SSO

## Compatibility Notes

- Works with DNS filtering tools (e.g., DNSFilter) for public internet protection
- Designed to interoperate with existing security stack components

## Gotchas

- Mesh VPNs require full network inventory and IP re-assignment before deployment—significant operational overhead
- IP re-addressing in mesh VPNs has cascading effects: bookmarks, settings, workflows, and end-user training all require updates
- Mesh VPN agent-on-every-device model becomes unmanageable at enterprise scale

## Deployment Comparison

| Factor | Twingate | Mesh VPN |
|---|---|---|
| Network changes | None | IP re-addressing required |
| Agent installation | Clients + 1 connector/network | Every device including servers |
| Overlapping IPs | Supported | Not supported |
| Policy interface | GUI | Often JSON/CLI |

## Related Docs

- Twingate Connector (Controller) setup documentation
- Remote Networks configuration
- Identity provider integration guides
- DNSFilter compatibility
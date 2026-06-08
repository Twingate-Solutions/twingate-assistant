# Twingate vs. Mesh VPNs

## Page Title
Twingate vs. Mesh VPNs

## Summary
Comparison page contrasting Twingate's enterprise-focused zero-trust architecture against mesh VPN products (e.g., Tailscale, WireGuard-based solutions). Key differentiators are infrastructure compatibility, deployment complexity, and enterprise security features. Intended for evaluators choosing between approaches.

## Key Information

**Architecture Differences:**
- Twingate: Controller per Remote Network + client agents only on user devices
- Mesh VPNs: Agent required on every device, including servers
- Twingate supports overlapping IP address ranges; mesh VPNs require unique IPs across entire network

**Deployment:**
- Twingate: Zero infrastructure changes required; can coexist with existing VPN
- Mesh VPNs: Typically require full network re-addressing before deployment
- Twingate deployable alongside existing solutions for risk-free evaluation

**Administration:**
- Twingate: GUI-based point-and-click admin console + extensive API
- Mesh VPNs: Often require JSON-based policy configuration
- Twingate API supports automation (user provisioning, server access on VPC deployment)

**Security Features (Twingate-specific):**
- Universal 2FA: Applies to any resource type including SSH, no app changes needed
- Device posture checks for access policy decisions
- Identity-indexed network flow logs across all users/devices

**Integrations:**
- IdPs: Okta, OneLogin, Google Workspace, Entra ID (Azure AD), social SSO
- DNS filtering: Compatible with DNSFilter for public internet protection

## Prerequisites
- None specific (comparison/evaluation content)

## Configuration Values
- No CLI flags, env vars, or API parameters documented on this page

## Gotchas
- Mesh VPN re-addressing has cascading effects: bookmarks, settings, workflows, and end-user habits must all be updated
- Mesh VPN server-side agents create scaling/maintenance burden in dynamic enterprise environments
- Mesh VPN admin policies written in JSON can introduce human error at scale

## Related Docs
- [DNSFilter integration](https://www.twingate.com/docs) (referenced but not linked inline)
- Remote Networks configuration
- Identity Provider integration guides (Okta, OneLogin, Google Workspace, Entra ID)
- Twingate API documentation
- Device posture/restrictions configuration
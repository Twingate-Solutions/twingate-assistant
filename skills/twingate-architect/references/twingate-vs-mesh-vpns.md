# Twingate vs. Mesh VPNs

## Summary
Comparison of Twingate against mesh VPN products (e.g., Tailscale, WireGuard-based solutions). Twingate is architected enterprise-first, emphasizing zero infrastructure changes, centralized administration, and compatibility with existing security stacks. Mesh VPNs require network re-addressing and per-device agent installation.

## Key Differences

### Deployment
- **Twingate**: No infrastructure changes, no IP re-addressing, supports overlapping IP ranges
- **Mesh VPNs**: Require unique IPs across entire private network; all resources must be re-addressed
- Twingate can coexist with existing VPN solutions—enables risk-free evaluation without disruption

### Agent Installation
- **Twingate**: Client agent on end-user devices only + one lightweight Connector per Remote Network
- **Mesh VPNs**: Agent required on every device including servers

### Administration
- **Twingate**: Point-and-click console, extensive API for automation
- **Mesh VPNs**: Often require JSON-based policy configuration; limited admin UX

## Security Features (Twingate-specific)
- **Universal 2FA**: Applies to any resource type including SSH—no application changes required
- **Device posture checks**: Access policies based on device attributes
- **Identity-indexed logs**: All network flow logs tied to user + device identity
- **IdP integrations**: Okta, OneLogin, Google Workspace, Entra ID (Azure AD), social SSO
- **DNS filtering compatibility**: Works with DNSFilter for public internet protection

## Prerequisites
- None specific to this comparison page—conceptual/architectural reference

## Gotchas
- Mesh VPNs require IP inventory and re-addressing before deployment—significant operational overhead in large environments
- Mesh VPN admin policies written in JSON (noted for at least one major product)—higher error risk vs. GUI
- Overlapping IP support is a hard requirement in many enterprise multi-segment networks; mesh VPNs don't support this

## Configuration Values
None—this is a conceptual comparison page, not a configuration reference.

## Related Docs
- Twingate Connectors (Remote Network setup)
- Identity Provider integrations (Okta, Entra ID, etc.)
- Device posture policies
- Universal 2FA configuration
- DNSFilter integration
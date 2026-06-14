# Twingate vs. Mesh VPNs

## Summary
Twingate is an enterprise-focused secure access solution that differs from mesh VPNs primarily in deployment approach, administration, and security features. Key architectural differences eliminate the need for network infrastructure changes, IP re-addressing, and per-server agent installation. Twingate is designed to coexist with existing solutions and security stacks.

## Key Differences: Twingate vs. Mesh VPNs

| Area | Twingate | Mesh VPN |
|------|----------|----------|
| IP addressing | Supports overlapping IPs, no re-addressing | Requires unique IPs across entire network |
| Infrastructure changes | None required | Typically required |
| Agent installation | Client devices + one Connector per Remote Network | Every device including servers |
| Policy configuration | Point-and-click UI | Often JSON/config files |
| 2FA | Universal (including SSH, non-app resources) | Application-level only |

## Architecture Highlights
- **No infrastructure changes**: Deploy alongside existing VPN without disruption
- **Overlapping IP support**: Multiple network segments with duplicate IP ranges work without modification
- **Connector model**: Only one lightweight component per Remote Network (not per server)
- **Identity-indexed logs**: All network flow logs tied to user + device identity

## Security Features (Beyond Basic Mesh VPN)
- **Universal 2FA**: Applies to any resource type (SSH, databases, etc.) without app changes
- **Device posture checks**: Access policies based on device attributes
- **Centralized logging**: Enterprise-wide network flow logs and analytics

## Integrations
- **Identity Providers**: Okta, OneLogin, Google Workspace, Entra ID (Azure AD), social SSO
- **DNS Filtering**: Compatible with DNSFilter for public internet protection
- **API**: Full administrative API for automation (user provisioning, server access on VPC deployment)

## Deployment Considerations
- Clients available for all major desktop and mobile platforms
- End users self-install with no configuration required
- Can be piloted without replacing existing access solution
- No need to re-inventory or re-address existing network resources

## Gotchas
- Mesh VPNs require IP uniqueness across your entire private network — auditing and re-addressing existing infrastructure is a significant undertaking before deployment
- Mesh VPN agents on every server create ongoing maintenance burden at scale
- Evaluate mesh VPN identity provider compatibility before committing — not all support enterprise IdPs

## Use Case Fit
- Regulated industries (healthcare, finance, legal) are explicitly supported
- Suitable for enterprises of all sizes, including rapidly scaling organizations
- Prosumer/home network use is possible but not the primary target

## Related Docs
- Twingate Connectors (Remote Network setup)
- Universal 2FA configuration
- Device posture policies
- Identity provider integration guides
- Administrative API reference
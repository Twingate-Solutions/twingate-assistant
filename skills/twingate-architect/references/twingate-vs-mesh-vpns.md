# Twingate vs. Mesh VPNs

## Summary
Twingate is an enterprise-first zero-trust access solution that differs from mesh VPNs primarily in deployment approach, administrative complexity, and security features. Key architectural differences mean Twingate requires no network infrastructure changes, while mesh VPNs typically require full IP re-addressing. Twingate targets enterprise environments with features beyond basic access control.

## Key Differences: Twingate vs. Mesh VPNs

### Deployment
- **Twingate**: No infrastructure changes required; supports overlapping IP ranges; no re-addressing of resources
- **Mesh VPNs**: Require unique IPs across entire network; full IP re-addressing often necessary; substantial knock-on effects to settings/workflows

### Software Installation
- **Twingate**: Client agent on user devices + single lightweight Connector per Remote Network
- **Mesh VPNs**: Agent required on every device including servers — problematic at scale

### Coexistence
- Twingate can run alongside existing VPN solutions, enabling low-risk evaluation without rip-and-replace

## Security Features (Beyond Mesh VPN Basics)
- **Universal 2FA**: Applies 2FA to any resource type including SSH, no application changes needed
- **Device posture checks**: Access policies based on device attributes
- **Identity-indexed network flow logs**: Centralized audit logs tied to user and device identity

## Integration Compatibility
- **Identity Providers**: Okta, OneLogin, Google Workspace, Entra ID (Azure AD), social SSO
- **DNS Filtering**: Compatible with DNSFilter and similar tools for public internet protection
- **Admin API**: Full API for automation (user provisioning, access assignment, server deployment workflows)

## Administration
- GUI-based point-and-click admin console (vs. some mesh VPN products requiring JSON policy configuration)
- API available for programmatic administration and automation

## Gotchas
- Mesh VPN IP re-addressing requirement is often underestimated — requires full network inventory before migration
- Mesh VPN agents on servers create ongoing maintenance burden in dynamic/large environments
- Evaluate mesh VPN identity provider and security tool compatibility before committing — not all support enterprise IdPs

## Prerequisites
- No special network prerequisites for Twingate deployment
- Existing network infrastructure (including overlapping subnets) can remain unchanged

## Related Docs
- Twingate Connectors (Remote Network setup)
- Universal 2FA configuration
- Device posture policies
- Identity provider integration guides (Okta, Entra ID, Google Workspace, OneLogin)
- Administrative API reference
- DNSFilter integration
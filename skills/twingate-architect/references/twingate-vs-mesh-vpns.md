# Twingate vs. Mesh VPNs

## Summary
Twingate and mesh VPNs both provide secure access to private resources, but differ significantly in architecture, deployment complexity, and enterprise feature set. Twingate requires no network infrastructure changes and no IP re-addressing, while mesh VPNs typically require both. Twingate targets enterprise use cases with additional security features beyond basic access control.

## Key Differences

### Deployment
| Factor | Twingate | Mesh VPN |
|--------|----------|----------|
| IP re-addressing | Not required | Typically required |
| Overlapping IP support | Yes | No |
| Agent installation | Clients + one Connector per network | Agent on every device including servers |
| Infra changes | None | Significant |
| Can coexist with existing VPN | Yes | Generally no |

### Administration
- Twingate: Point-and-click admin console, no JSON config required
- Mesh VPNs: Often require JSON-based policy configuration
- Both offer administrative APIs

### Security Features (Twingate-specific)
- **Universal 2FA**: Applies 2FA to any resource type (including SSH) without app changes
- **Device posture checks**: Access policies based on device attributes
- **Identity-indexed logs**: Network flow logs tied to user + device identity

### Identity Provider Support
- Okta, OneLogin, Google Workspace, Entra ID (Azure AD), social SSO

### DNS Filtering Compatibility
- Twingate integrates with DNSFilter for public internet traffic protection

## Prerequisites
- N/A (comparison/reference document)

## Gotchas
- Mesh VPNs require unique IPs across entire private network — overlapping subnets across network segments require full re-addressing before deployment
- IP re-addressing causes cascading updates: settings, bookmarks, workflows, and end-user retraining
- Mesh VPN agent-on-every-server model becomes unmanageable at enterprise scale

## Use Case Fit
- Twingate targets enterprises including regulated industries (healthcare, financial services, legal)
- Twingate can be piloted alongside existing VPN without disruption — reduces procurement risk

## Related Docs
- Twingate Connectors (Remote Network setup)
- Identity Provider integrations (Okta, OneLogin, Google Workspace, Entra ID)
- DNSFilter compatibility
- Administrative API documentation
- Device posture / access policies
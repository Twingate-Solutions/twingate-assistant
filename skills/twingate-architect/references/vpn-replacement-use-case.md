# VPN Replacement Use Case

## Page Title
VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs by providing zero-trust, application-level access to private corporate resources without requiring open network ports. It deploys in under 15 minutes via a lightweight Connector component and requires no hardware procurement or network reconfiguration.

## Key Information
- **No open ports required** — eliminates public internet attack surface present in VPN gateways
- **Split tunnel by default** — only traffic destined for internal resources routes through Twingate (vs VPN full-tunnel)
- **Granular access control** — application-level permissions vs VPN's broad network-level access
- **MFA + device posture checks** supported for third-party SaaS apps
- **Deployment time** — under 15 minutes with a single Connector host
- **IaC support** — Terraform, Kubernetes, Pulumi integrations for automation
- **Central Admin Console** for access management and activity monitoring

## Prerequisites
- A host within each target network to run the Twingate Connector
- Identity Provider (optional but recommended for fast rollout): Okta, JumpCloud, Entra ID (Azure AD), OneLogin, or Google

## Configuration Notes
- No hardware procurement needed
- No network configuration changes required
- Can coexist with existing VPN during testing/migration — no forced cutover

## Related Guides

### VPN Replacement
- How to Replace the AWS VPN with Twingate
- How to Secure Site-to-Site Connections with Twingate
- How to Manage Access for Vendors & Contractors

### Environment Deployment
- How to Secure Private Resources in AWS with Twingate
- How to Secure Private Resources in Azure with Twingate
- How to Secure Private Resources in GCP with Twingate

### Architecture Comparisons
- Twingate vs VPN
- Twingate vs MeshVPN

## Gotchas
- VPN gateways require frequent patching due to common CVEs — Twingate's no-open-port model removes this burden but the Connector host itself still needs maintenance
- Split tunnel is default behavior; full-tunnel routing is not the standard mode
- Traditional VPNs expose wide network access enabling lateral movement — Twingate restricts this by design, but resource definitions must be explicitly configured
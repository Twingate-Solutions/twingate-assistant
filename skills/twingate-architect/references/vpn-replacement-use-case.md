# VPN Replacement Use Case

## Page Title
Twingate VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs by providing zero-trust, application-level access to private corporate resources without requiring open network ports. It deploys in under 15 minutes using a lightweight Connector component with no hardware procurement or network reconfiguration needed.

## Key Information
- **No open ports required** — eliminates attack surface present in VPN gateways
- **Split tunnel by default** — only routes traffic destined for internal resources through the network (vs. VPN full tunnel)
- **Application-level access controls** — more granular than VPN's network-level access; reduces lateral movement risk
- **MFA and device posture checks** for third-party SaaS apps (not possible with traditional VPNs)
- **Deployment time**: under 15 minutes with a single Connector host
- **No hardware procurement or network config changes** required
- **Can run alongside existing VPN** — low-risk parallel testing before full cutover

## Prerequisites
- A host within each target network to run the Twingate Connector
- Identity Provider (supported: Okta, JumpCloud, Entra ID/Azure AD, OneLogin, Google)
- Admin Console access for managing resources and monitoring

## Deployment Environments (Guides Available)
- AWS
- Azure
- GCP
- Site-to-site connections
- Vendor/contractor access

## Configuration Values
| Component | Notes |
|-----------|-------|
| Connector | Lightweight, deployed on single host per network |
| Tunnel mode | Split tunnel (default) |
| IaC support | Terraform, Kubernetes, Pulumi |

## Gotchas
- Twingate is split tunnel by default — verify this aligns with your security policy before deployment
- No open ports needed, but the Connector host must have outbound connectivity
- VPN gateway patching burden is eliminated, but Connector updates still need to be managed

## Related Docs
- [How to Replace the AWS VPN with Twingate](#)
- [How to Secure Site-to-Site Connections with Twingate](#)
- [How to Manage Access for Vendors & Contractors](#)
- [How to Secure Private Resources in AWS/Azure/GCP](#)
- [Twingate vs VPN architecture comparison](#)
- [Twingate vs MeshVPN architecture comparison](#)
- [Identity Provider integrations](#)
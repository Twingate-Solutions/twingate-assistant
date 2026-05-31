# VPN Replacement Use Case

## Page Title
VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs by providing zero-trust, application-level access to private corporate resources across office networks, cloud VPCs, and mobile devices. It deploys in under 15 minutes without hardware procurement or network reconfiguration, and can coexist with existing VPN solutions during evaluation.

## Key Information
- **No open inbound ports** required — eliminates public internet attack surface present in VPN gateways
- **Split tunnel by default** — only private resource traffic routes through Twingate (vs. VPN full-tunnel)
- **Application-level access controls** — reduces lateral movement risk compared to VPN network-level access
- **MFA and device posture checks** supported for SaaS apps — not possible with traditional VPNs
- **Deployment time**: under 15 minutes using a single lightweight Connector host
- **Central Admin Console** for access management and activity monitoring
- **Automation support**: Terraform, Kubernetes, Pulumi

## Prerequisites
- A host within the target network to deploy the Connector
- Identity Provider (optional but recommended for fast rollout): Okta, JumpCloud, Entra ID (Azure AD), OneLogin, or Google

## Deployment Environments (Linked Guides)
- AWS private resources
- Azure private resources
- GCP private resources
- Site-to-site connections
- Vendor/contractor access management

## Gotchas
- Existing VPN does **not** need to be removed before testing Twingate — parallel deployment is supported
- Twingate is split tunnel by default; plan resource CIDR/DNS configuration accordingly
- VPN gateways require frequent patching for CVEs; Twingate Connectors have no exposed ports to patch against external threats

## Configuration Values
| Component | Notes |
|-----------|-------|
| Connector | Single host per network segment; no hardware required |
| Identity Provider | Integrates via OIDC/SAML with major IdPs |
| Admin Console | Web-based; centralized policy and audit |

## Related Docs
- [Twingate vs VPN](architecture comparison)
- [Twingate vs MeshVPN](architecture comparison)
- How to Replace the AWS VPN with Twingate
- How to Secure Site-to-Site Connections with Twingate
- How to Manage Access for Vendors & Contractors
- Identity Providers integration guides (Okta, JumpCloud, Entra ID, OneLogin, Google)
# VPN Replacement Use Case

## Page Title
VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs by providing zero-trust, application-level access to private corporate resources across office networks, cloud VPCs, and other infrastructure. It deploys in under 15 minutes without hardware procurement or network reconfiguration, and can coexist with existing VPN solutions during testing/migration.

## Key Information
- **No open network ports required** — eliminates public internet attack surface present in VPN gateways
- **Split tunnel by default** — only traffic destined for internal resources routes through Twingate (vs. VPN full-tunnel)
- **Application-level access control** — more granular than network-level VPN access; reduces lateral movement risk
- **MFA and device posture checks** supported for third-party SaaS apps
- **Deployment time**: under 15 minutes using a single lightweight Connector host
- **Infrastructure-as-code support**: Terraform, Kubernetes, Pulumi
- **Central Admin Console** for access management and activity monitoring

## Prerequisites
- A host within the target network to deploy the Connector component
- Identity Provider (IdP) for user authentication (supported: Okta, JumpCloud, Entra ID/Azure AD, OneLogin, Google)
- No hardware procurement or network configuration changes needed

## Deployment Environments
| Environment | Guide Available |
|-------------|----------------|
| AWS | Yes |
| Azure | Yes |
| GCP | Yes |
| Site-to-site | Yes |
| Vendor/contractor access | Yes |

## Gotchas
- Twingate is **split tunnel by default** — verify this aligns with policy requirements before full rollout
- Existing VPN does **not** need to be removed before testing Twingate — safe parallel deployment
- VPN gateways require frequent patching for vulnerabilities; Twingate's no-open-ports architecture avoids this maintenance burden

## Related Docs
- [How to Replace the AWS VPN with Twingate]
- [How to Secure Site-to-Site Connections with Twingate]
- [How to Manage Access for Vendors & Contractors]
- [How to Secure Private Resources in AWS / Azure / GCP]
- [Twingate vs VPN] (architecture comparison)
- [Twingate vs MeshVPN] (architecture comparison)
- Identity Provider integration docs: Okta, JumpCloud, Entra ID, OneLogin, Google
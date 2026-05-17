# VPN Replacement Use Case

## Page Title
VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs by providing zero-trust, application-level access to private corporate resources across office networks, cloud VPCs, and other infrastructure. It deploys in under 15 minutes without hardware procurement or network reconfiguration, and can coexist with existing VPN solutions during testing/migration.

## Key Information
- **No open network ports required** — eliminates common public internet attack vectors
- **Split tunnel by default** — only routes traffic destined for internal resources through corporate network (vs. VPN full tunnel)
- **Application-level access controls** — more granular than VPN's network-level access; reduces lateral movement risk
- **Deployment time**: Under 15 minutes using a single lightweight Connector host
- **MFA and device posture checks** supported for third-party SaaS apps
- **Central Admin Console** for access management and activity monitoring
- **Infrastructure-as-code support**: Terraform, Kubernetes, Pulumi

## Prerequisites
- A host within the target network to deploy the Connector
- Identity Provider (optional but recommended for rollout): Okta, JumpCloud, Entra ID (Azure AD), OneLogin, or Google

## Deployment Environments (Linked Guides)
- AWS
- Azure
- GCP
- Site-to-site connections
- Vendor/contractor access management

## Configuration Values
- No specific env vars or CLI flags listed on this page
- See environment-specific guides for configuration details

## Gotchas
- No need to remove existing VPN before testing — Twingate can run alongside current VPN solution
- VPNs require frequent patching for gateway vulnerabilities; Twingate avoids this by eliminating open ports
- Traditional VPNs expose full network access; Twingate scopes access per application/resource

## Related Docs
- [How to Replace the AWS VPN with Twingate]
- [How to Secure Site-to-Site Connections with Twingate]
- [How to Manage Access for Vendors & Contractors]
- [How to Secure Private Resources in AWS / Azure / GCP]
- [Twingate vs VPN] (architecture comparison)
- [Twingate vs MeshVPN] (architecture comparison)
- Identity Provider integrations: Okta, JumpCloud, Entra ID, OneLogin, Google
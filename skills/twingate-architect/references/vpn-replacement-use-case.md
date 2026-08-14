---
source: https://www.twingate.com/docs/vpn-replacement-use-case
type: docs
fetched: 2026-08-14
source_version: d95e4e9dcf2058bdc816f639a7d0d4450285d416172837b929b0e6073c533f10
---

# VPN Replacement Use Case

## Page Title
VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs for remote access to office networks, cloud VPCs, and private corporate resources. It offers zero open inbound ports, application-level access controls, and split-tunnel routing by default. Deployment takes under 15 minutes without hardware procurement or network reconfiguration.

## Key Information
- **No open network ports** required — eliminates public internet attack surface present in VPN gateways
- **Split tunnel by default** — only traffic destined for internal resources routes through Twingate (vs. VPN full-tunnel)
- **Application-level access controls** — more granular than network-level VPN access; reduces lateral movement risk
- **MFA and device posture checks** supported for third-party SaaS apps
- **Deployment time**: under 15 minutes using a single lightweight Connector host
- **No hardware procurement** or network configuration changes required
- **Can coexist with existing VPN** — no forced cutover required for testing
- **IDP integrations**: Okta, JumpCloud, Entra ID (Azure AD), OneLogin, Google

## Prerequisites
- A host within the target network to deploy the Connector
- Identity Provider (optional but recommended for fast rollout)
- Twingate account with Admin Console access

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Infrastructure-as-code support: Terraform, Kubernetes, Pulumi

## Related Docs
- [How to Replace the AWS VPN with Twingate]
- [How to Secure Site-to-Site Connections with Twingate]
- [How to Manage Access for Vendors & Contractors]
- [How to Secure Private Resources in AWS with Twingate]
- [How to Secure Private Resources in Azure with Twingate]
- [How to Secure Private Resources in GCP with Twingate]
- [Twingate vs VPN] (architecture comparison)
- [Twingate vs MeshVPN] (architecture comparison)
- Identity Provider setup: Okta, JumpCloud, Entra ID, OneLogin, Google

## Gotchas
- This page is overview/marketing-level; no implementation steps are provided here — follow linked guides for actual deployment
- VPN replacement does not require removing the existing VPN first; parallel operation is supported during migration
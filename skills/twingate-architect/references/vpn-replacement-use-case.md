# VPN Replacement Use Case

## Page Title
VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs by providing zero-trust, application-level access to private resources across office networks, cloud VPCs, and corporate infrastructure. It deploys in under 15 minutes without hardware procurement or network changes, and operates as split-tunnel by default for better performance.

## Key Information
- **No open ports required** — Connector architecture eliminates public internet attack surface
- **Split-tunnel by default** — only traffic destined for internal resources routes through Twingate (vs. VPN full-tunnel)
- **Application-level access controls** — more granular than network-level VPN access; reduces lateral movement risk
- **MFA and device posture checks** for third-party SaaS apps (not available with traditional VPNs)
- **Single Connector host** required per network — no hardware, no network reconfiguration
- **Coexists with existing VPN** — can be tested without removing current VPN solution

## Prerequisites
- A host within the target network to deploy the Connector
- Identity Provider integration (optional but recommended): Okta, JumpCloud, Entra ID, OneLogin, or Google
- Admin Console access for resource and user management

## Deployment Overview
1. Deploy lightweight Connector on a single host within target network
2. Configure resources in Admin Console
3. Integrate with existing Identity Provider for user rollout
4. Users download and install Twingate Client (no IT assistance required)
5. Total deployment time: ~15 minutes

## Configuration Values
- **Tunnel mode**: Split-tunnel (default)
- **Automation support**: Terraform, Kubernetes, Pulumi
- **Supported IdPs**: Okta, JumpCloud, Entra ID (Azure AD), OneLogin, Google

## Gotchas
- VPN gateways require open ports and frequent patching; Twingate does not — validate firewall rules won't interfere with Connector outbound connections
- Full-tunnel vs. split-tunnel behavior differs from VPN defaults; verify routing expectations with end users
- Device posture checks and MFA for SaaS apps require Twingate Client to be active

## Related Docs
- [How to Replace the AWS VPN with Twingate]
- [How to Secure Site-to-Site Connections with Twingate]
- [How to Manage Access for Vendors & Contractors]
- [How to Secure Private Resources in AWS / Azure / GCP]
- [Twingate vs VPN] (architecture comparison)
- [Twingate vs MeshVPN] (architecture comparison)
- Identity Provider integration guides (Okta, JumpCloud, Entra ID, OneLogin, Google)
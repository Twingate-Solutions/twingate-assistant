# VPN Replacement Use Case

## Page Title
VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs by providing zero-trust, application-level access to private resources across office networks, cloud VPCs, and corporate infrastructure. It deploys in under 15 minutes without hardware procurement or network reconfiguration, and operates as split-tunnel by default.

## Key Information
- **No open ports required** — eliminates public internet attack surface present in VPN gateways
- **Split-tunnel by default** — only traffic destined for internal resources routes through Twingate (vs. VPN full-tunnel)
- **Granular access controls** — application-level rather than network-level access, reducing lateral movement risk
- **MFA + device posture checks** — works for third-party SaaS apps, not possible with traditional VPNs
- **Can coexist with existing VPN** — test Twingate without removing current solution first

## Prerequisites
- Single host within target network to deploy the Connector
- Identity Provider (Okta, JumpCloud, Entra ID/Azure AD, OneLogin, or Google) for user rollout
- No hardware procurement or network config changes needed

## Deployment Environments
- AWS
- Azure
- GCP
- On-premise/office networks

## Architecture Advantages Over VPN

| Feature | Twingate | VPN |
|---|---|---|
| Open ports | None required | Required |
| Access scope | Application-level | Network-level |
| Tunnel mode | Split-tunnel | Full-tunnel |
| Patch burden | Low | High (frequent CVEs) |
| Deploy time | ~15 minutes | Hours/days |

## Related Docs
- [How to Replace the AWS VPN with Twingate]
- [How to Secure Site-to-Site Connections with Twingate]
- [How to Manage Access for Vendors & Contractors]
- [How to Secure Private Resources in AWS / Azure / GCP]
- [Twingate vs VPN] (architecture comparison)
- [Twingate vs MeshVPN] (architecture comparison)
- Identity Provider integrations: Okta, JumpCloud, Entra ID, OneLogin, Google

## Gotchas
- Deployment time claim (~15 min) assumes a single Connector on an existing host; complex multi-network environments will take longer
- Split-tunnel is default behavior — verify this aligns with your security policy before deployment
- No specific CLI flags, API params, or env vars documented on this page — see environment-specific guides for configuration details
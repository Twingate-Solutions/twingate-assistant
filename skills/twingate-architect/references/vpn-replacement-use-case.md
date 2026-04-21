## Page Title
VPN Replacement

## Summary
Overview of replacing a corporate VPN with Twingate. No open inbound ports required; split-tunnel by default; deploys in under 15 minutes without touching existing network infrastructure. Can be tested in parallel with an existing VPN before migration.

## Key Information
- No open inbound ports — Connector makes outbound connections only; no VPN gateway to patch
- Split-tunnel by default — only defined-resource traffic routes through Twingate
- Deploys alongside existing VPN for side-by-side testing before cutover
- Application-level access control replaces broad network-level VPN access, reducing lateral movement risk
- IdP integration for SSO rollout: Okta, JumpCloud, Entra ID, OneLogin, Google Workspace
- Admin Console centralizes resource, user, and policy management
- IaC support via Terraform, Kubernetes, Pulumi for automated administration
- Additional SaaS app protection via MFA and device posture checks (not possible with traditional VPN)

## Prerequisites
- Connector deployed within target network on a single host (no network reconfiguration)
- Identity Provider configured for user authentication (recommended for org-wide rollout)

## Step-by-Step
Not applicable on this page — see linked environment-specific guides.

## Configuration Values
None on this page.

## Gotchas
- Full-tunnel mode is available but not the default and is not recommended for most deployments
- Twingate does not require a public-facing gateway — eliminates VPN CVE exposure surface
- MFA and posture checks for SaaS apps require additional policy configuration and appropriate plan tier

## Related Docs
- `/docs/aws-vpn-replacement` — AWS-specific VPN replacement
- `/docs/site-2-site` — site-to-site connection replacement
- `/docs/twingate-vs-vpn` — detailed architectural comparison
- `/docs/twingate-vs-mesh-vpns` — comparison with mesh VPN alternatives
- `/docs/vendor-and-contractor-access-management` — non-employee access management

# VPN Replacement Use Case

## Page Title
VPN Replacement Use Case

## Summary
Twingate replaces traditional VPNs by providing zero-trust, application-level access to private corporate resources without requiring open network ports. It deploys in under 15 minutes via a lightweight Connector component with no hardware procurement or network reconfiguration needed.

## Key Information
- **No open ports required** — eliminates public internet attack surface present in VPN gateways
- **Split tunnel by default** — only traffic destined for internal resources routes through Twingate (vs. VPN full-tunnel)
- **Granular access controls** — application-level rather than network-level, reducing lateral movement risk
- **MFA + device posture checks** — extends protection to third-party SaaS apps (not possible with traditional VPNs)
- **Deployment time** — under 15 minutes with a single Connector host
- **IaC support** — Terraform, Kubernetes, Pulumi integrations for automation
- **Central Admin Console** — unified access management and activity monitoring

## Prerequisites
- A host within the target network to deploy the Connector
- Identity Provider integration (optional but recommended): Okta, JumpCloud, Entra ID (Azure AD), OneLogin, or Google

## Supported Deployment Environments
- AWS (replaces AWS VPN)
- Azure
- GCP
- Site-to-site connections
- Vendor/contractor access scenarios

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Connector is a single lightweight component deployed on one host per network segment

## Gotchas
- No need to remove existing VPN before testing — Twingate can run in parallel during evaluation
- No hardware procurement or network config changes required (contrast with VPN gateway deployments)
- VPN gateways require frequent patching for vulnerabilities; Twingate's architecture avoids this exposure

## Related Docs
- [How to Replace the AWS VPN with Twingate]
- [How to Secure Site-to-Site Connections with Twingate]
- [How to Manage Access for Vendors & Contractors]
- [How to Secure Private Resources in AWS/Azure/GCP]
- [Twingate vs VPN] (architecture comparison)
- [Twingate vs MeshVPN] (architecture comparison)
- Identity Provider integration guides: Okta, JumpCloud, Entra ID, OneLogin, Google
# Bastion Server Cloaking with Twingate

## Page Title
Bastion Server Cloaking / Bastion Replacement

## Summary
Twingate can replace or supplement bastion servers by making private resources completely invisible to the internet while providing stronger access controls. Unlike bastions, Twingate integrates natively with Identity Providers for real-time access synchronization and enforces SSO/2FA policies without client or server configuration changes.

## Key Information
- **Internet exposure eliminated**: Resources and Connectors do not need to be publicly accessible; all traffic is encrypted in-transit from user device to Connector
- **Real-time IdP sync**: Access is tied to active corporate accounts; deprovisioned users lose access immediately regardless of other credentials
- **SSO/2FA enforcement**: Any IdP authentication policy (including MFA) applies to any resource type at OSI Layer 4 without modifying clients or servers
- **Bastion weaknesses addressed**:
  - Bastion attack surface → Twingate resources are not internet-routable
  - SSH key management decoupled from IdP → Twingate enforces IdP identity
  - 2FA on SSH is difficult → Twingate applies SSO policies universally

## Prerequisites
- Twingate Connector deployed in the private network
- Identity Provider configured with Twingate
- Resources defined in Twingate admin console

## Bastion vs. Twingate Comparison

| Concern | Bastion | Twingate |
|---|---|---|
| Internet exposure | Publicly accessible | Fully hidden |
| IdP integration | Manual/difficult | Real-time sync |
| 2FA enforcement | Complex on SSH | Native via SSO policy |
| Access revocation | SSH key removal | IdP account deactivation |

## Gotchas
- Twingate does not require the Connector to have a public IP — ensure firewall/security group rules are not unnecessarily exposing the Connector
- Access control is enforced at the IdP level; ensure IdP provisioning/deprovisioning workflows are active to fully realize real-time sync benefits
- SSH access through Twingate still requires SSH key or password auth on the target server — Twingate handles network-layer authorization, not application-layer authentication

## Related Docs
- Connector deployment
- Identity Provider configuration
- Resource configuration
- SSO/2FA policy setup
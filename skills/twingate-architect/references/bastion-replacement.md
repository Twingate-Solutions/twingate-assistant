# Bastion Server Cloaking with Twingate

## Page Title
Bastion Server Cloaking / Bastion Replacement

## Summary
Twingate can replace or supplement bastion servers by making private resources completely invisible to the internet. It addresses core bastion weaknesses: internet exposure, IdP synchronization gaps, and 2FA enforcement difficulties.

## Key Information

- **Bastion use cases**: Security monitoring/hardening on single asset; single source IP for ingress whitelisting; centralized access management point
- **Bastion weaknesses Twingate solves**:
  - Bastions remain internet-exposed and vulnerable to exploits
  - SSH key management is hard to sync with Active Directory/IdP
  - Enforcing 2FA on SSH is difficult
- **Twingate advantages**:
  - Protected resources are **completely invisible** to the internet — no public exposure required
  - Connector does not need to be globally accessible
  - All traffic encrypted in-transit from user device to Connector
  - Real-time IdP sync: inactive corporate accounts lose access automatically
  - SSO policies (including 2FA) apply at OSI Layer 4 without client/server config changes
  - Auth policy can be scoped per Resource

## Prerequisites

- Twingate Connector deployed inside private network
- Identity Provider (IdP) configured with Twingate for SSO/2FA
- Resources defined in Twingate (replaces bastion-forwarded hosts)

## Architecture Notes

- No inbound firewall rules required for protected resources
- Connector initiates outbound connections only — no public IP needed on Connector
- Access control enforced at network layer (L4) via Twingate, not SSH key management

## Gotchas

- Twingate **guarantees** active-employee enforcement via IdP sync, but per-Resource permissions still need to be configured separately — IdP deactivation alone revokes all access, but granular Resource access requires explicit policy
- This page does not detail SSH key replacement — Twingate cloaks the bastion/resources but SSH keys may still be used for authentication *to* the destination server (Twingate handles network access, not application-layer auth)
- 2FA enforcement requires IdP to have 2FA policy configured; Twingate applies the IdP's existing policy

## Configuration Values

None specified on this page — implementation details are in Connector setup and Resource/Policy configuration docs.

## Related Docs

- Connector setup documentation
- Identity Provider integration
- Resource access policy configuration
- SSO configuration
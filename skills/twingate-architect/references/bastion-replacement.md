# Bastion Server Cloaking with Twingate

## Summary
Twingate can replace or augment traditional bastion servers by making private resources completely invisible to the internet. It addresses key bastion weaknesses: internet exposure, IdP synchronization gaps, and 2FA enforcement difficulties.

## Key Information

- **Bastion use cases Twingate replaces:**
  - Single ingress point for private network access
  - Centralized access management/revocation
  - Security monitoring consolidation

- **Twingate advantages over bastion:**
  - Resources and Connectors are not publicly accessible — no internet-exposed attack surface
  - All traffic encrypted in-transit from user device to destination Connector
  - Real-time IdP sync: deprovisioned users lose access immediately, regardless of SSH key status
  - SSO policies (including 2FA/MFA) apply to any resource type at OSI Layer 4, no client/server config changes required

## Bastion Limitations Addressed

| Bastion Problem | Twingate Solution |
|---|---|
| Internet-exposed attack surface | Resources fully hidden; no public endpoint |
| SSH key management decoupled from IdP | Real-time IdP synchronization |
| 2FA hard to enforce on SSH | SSO/2FA policy applied per-resource via IdP |

## Prerequisites

- Twingate Connector deployed inside private network
- Identity Provider (IdP) configured and synced with Twingate
- SSO policy configured in IdP (for 2FA enforcement)

## Implementation Notes

- No requirement to expose the Connector or any protected resource to the internet
- Access revocation in IdP propagates to Twingate access immediately
- Per-resource authentication policies configurable without modifying SSH client or server configuration

## Gotchas

- Twingate does **not** replace the bastion if the bastion itself performs session recording or command auditing — those functions require additional tooling
- SSH key management is bypassed conceptually, but existing SSH keys on target servers are not automatically removed; manual cleanup required when migrating off bastion
- Users must have an **active corporate account** in the IdP — permission to a Resource alone is insufficient

## Related Docs

- Connector setup
- Identity Provider integration
- Resource configuration
- Access policies / 2FA enforcement
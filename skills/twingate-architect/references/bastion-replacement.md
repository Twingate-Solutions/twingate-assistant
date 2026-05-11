# Bastion Server Cloaking with Twingate

## Page Title
Bastion Server Cloaking / Bastion Replacement

## Summary
Twingate can replace or augment bastion servers by making private resources completely invisible to the internet while providing stronger security controls. It addresses key bastion weaknesses: internet exposure, IdP synchronization gaps, and 2FA enforcement challenges.

## Key Information

- **Bastion servers serve two purposes**: security hardening focus + access management centralization
- **Twingate advantages over bastions**:
  - Resources and Connectors are not publicly accessible or discoverable on the internet
  - All traffic is encrypted in-transit from user device to destination Connector
  - Real-time sync with Identity Provider — deprovisioned accounts immediately lose access
  - SSO policies (including 2FA) apply to any resource type without client/server config changes
- Twingate operates at **OSI Layer 4** (network/transport), authorizing connections while integrating with IdP
- Access control applies regardless of individual resource permissions — active corporate account required

## Bastion Limitations Addressed

| Bastion Problem | Twingate Solution |
|---|---|
| Internet-exposed attack surface | Resources fully hidden from internet |
| SSH key management decoupled from IdP | Real-time IdP synchronization |
| 2FA difficult to enforce on SSH | Any SSO/2FA policy applicable to any resource |

## Prerequisites

- Twingate Connector deployed within private network
- Identity Provider configured with Twingate
- Existing bastion infrastructure (for migration scenario)

## Architecture Notes

- No inbound firewall rules needed — Connector initiates outbound connections
- Resources defined in Twingate are inaccessible without Twingate Client authentication
- IdP deprovisioning immediately revokes access (no manual SSH key rotation needed)

## Gotchas

- Twingate **replaces the access control function** of a bastion but does not replace SSH itself — users still SSH to target servers, just without going through a jump host
- "Invisible to the internet" requires no public IP or open inbound ports on protected resources — verify firewall rules block all direct inbound access
- 2FA enforcement is configured at the **IdP/SSO policy level**, not within Twingate directly

## Related Docs

- Connector deployment documentation
- Identity Provider integration (SSO/2FA configuration)
- Resource configuration
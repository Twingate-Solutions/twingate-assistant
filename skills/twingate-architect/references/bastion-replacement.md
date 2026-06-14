# Bastion Server Cloaking with Twingate

## Page Title
Bastion Server Cloaking / Bastion Replacement

## Summary
Twingate can replace or augment bastion servers by making private resources completely invisible to the internet. It addresses key bastion weaknesses: internet exposure, IdP synchronization gaps, and 2FA enforcement difficulties.

## Key Information

**Why bastions are used:**
- Centralize security monitoring/logging on a single exposed asset
- Single source IP to whitelist for ingress rules
- Single access management point (disable bastion access = disable all downstream access)

**Bastion limitations Twingate solves:**

| Bastion Problem | Twingate Solution |
|---|---|
| Bastion exposed to internet attacks | Resources + Connectors fully invisible/inaccessible from internet |
| SSH key management decoupled from IdP/AD | Real-time IdP sync; inactive accounts immediately lose access |
| 2FA on SSH is difficult to enforce | SSO policies (including 2FA) applied at network layer (OSI Layer 4) to any resource |

## Prerequisites
- Twingate Connector deployed in private network
- Identity Provider configured for Twingate SSO integration

## Architecture Notes
- Twingate Connector does **not** need to be publicly accessible
- All traffic is encrypted in-transit from user device to destination Connector
- Access control operates at OSI Layer 4 (network connections), not application layer
- No client or server configuration changes required to apply authentication policies

## Gotchas
- Twingate guarantees only **active** IdP accounts can access resources — but this applies regardless of resource-level permissions (IdP account status is a prerequisite gate)
- SSH key management is bypassed entirely; access authorization moves to IdP
- This is architectural replacement guidance, not a step-by-step migration guide — actual Connector setup is covered in separate docs

## Related Docs
- Connector deployment documentation
- Identity Provider integration/SSO setup
- Resource access policies
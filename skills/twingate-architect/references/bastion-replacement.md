# Bastion Server Cloaking with Twingate

## Summary
Twingate can replace or augment bastion servers by making private resources completely invisible to the internet. It addresses key bastion weaknesses: internet exposure, IdP synchronization gaps, and 2FA enforcement difficulties.

## Key Information

- **Bastion use cases Twingate replaces:**
  - Security monitoring/hardening focus point
  - Single ingress whitelist source
  - Centralized access management

- **Twingate advantages over bastions:**
  - Resources are fully invisible/inaccessible from the internet (no public exposure required)
  - Connectors do not need to be globally accessible
  - All traffic encrypted in-transit from user device to Connector
  - Real-time sync with Identity Provider — deprovisioned users lose access immediately
  - SSO policies (including 2FA) applied at OSI Layer 4 without client/server config changes

## Bastion Drawbacks Addressed

| Bastion Problem | Twingate Solution |
|---|---|
| Bastion exposed to internet attacks | No resource or Connector needs internet exposure |
| SSH key management decoupled from IdP | Real-time IdP sync; no active account = no access |
| 2FA on SSH is difficult | SSO/2FA policy applied to any resource type natively |

## Prerequisites

- Twingate Connector deployed in private network
- Identity Provider (Active Directory, Okta, etc.) configured with Twingate
- Users provisioned through IdP

## Gotchas

- Access is blocked for **any** user without an active corporate account, regardless of other permissions — ensure IdP sync is configured correctly before cutting over
- This is an architectural replacement/supplement, not a drop-in SSH proxy; evaluate whether direct resource access (without bastion hop) fits your workflow
- No client or server configuration changes required to apply SSO/2FA policies

## Related Docs

- Connector setup documentation
- Identity Provider integration
- Resource access configuration
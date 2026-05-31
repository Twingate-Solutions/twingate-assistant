# Bastion Server Cloaking with Twingate

## Page Title
Bastion Server Cloaking / Bastion Replacement

## Summary
Twingate can replace or augment bastion servers by making private resources completely invisible to the internet while providing stronger authentication integration. Unlike bastions, Twingate resources have no public internet exposure and integrate directly with Identity Providers for real-time access control and 2FA enforcement.

## Key Information
- **Resource invisibility**: Twingate-protected resources are not publicly accessible or discoverable; no public IP/port exposure required
- **Traffic encryption**: All traffic is encrypted in-transit from user device to destination Connector
- **Real-time IdP sync**: Access automatically revoked when employee account is disabled in Identity Provider
- **SSO/2FA support**: Any IdP authentication policy (including MFA) can be applied to any resource type without client/server config changes
- **OSI Layer 4 authorization**: Twingate authorizes network connections at the transport layer while integrating with IdP

## Problems Solved vs. Traditional Bastions

| Bastion Weakness | Twingate Solution |
|---|---|
| Bastion exposed to internet attacks | No public exposure; resources fully cloaked |
| SSH key management decoupled from IdP | Real-time IdP synchronization |
| Difficult to enforce 2FA on SSH | SSO/2FA policy applies to any resource type |

## Prerequisites
- Twingate Connector deployed in target private network
- Identity Provider configured with Twingate
- Users provisioned through IdP

## Implementation Notes
- The Twingate Connector does **not** need to be globally accessible via the internet
- No client or server configuration changes required to apply authentication policies
- Access control operates independently of resource-level permissions — IdP account status is a prerequisite gate

## Gotchas
- Twingate guarantees only *active* IdP accounts can connect, but resource-level permissions are separate — both must be configured correctly
- This page is conceptual; actual Connector deployment and Resource configuration are covered in separate docs

## Related Docs
- Connector setup documentation
- Identity Provider / SSO integration
- Resource access policies
- 2FA/MFA configuration
# Bastion Server Cloaking with Twingate

## Page Title
Bastion Server Cloaking / Bastion Replacement

## Summary
Twingate can replace or augment bastion servers by making protected resources completely invisible to the internet. It integrates with Identity Providers for real-time access control and applies SSO/2FA policies to any resource type without client or server configuration changes.

## Key Information
- **Internet invisibility**: Resources and Twingate Connectors require no public internet exposure; all traffic is encrypted in-transit from user device to Connector
- **Real-time IdP sync**: Access automatically revoked when employee account is deactivated in Identity Provider
- **SSO/2FA enforcement**: Any IdP authentication policy (including 2FA) can be applied at the network level (OSI Layer 4) to any resource
- **No config changes required**: SSO policies apply without modifying client or server configurations

## Problems Twingate Solves vs. Traditional Bastions

| Bastion Weakness | Twingate Solution |
|---|---|
| Publicly exposed attack surface | Resources fully cloaked from internet |
| SSH key management decoupled from IdP | Real-time IdP synchronization |
| 2FA difficult to enforce on SSH | IdP auth policies apply to all resource types |

## Prerequisites
- Twingate Connector deployed in private network
- Identity Provider (Active Directory, SAML/OIDC IdP) configured with Twingate
- Resources defined in Twingate admin console

## Gotchas
- Twingate does **not** eliminate the need for a bastion if workflows require it, but it can cloak the bastion itself from the public internet
- Access is blocked for users without active corporate accounts **regardless of any resource-level permissions** they may hold
- Security benefit requires Connector to remain unexposed publicly — deploying Connector on a publicly accessible host negates the cloaking advantage

## Use Cases
1. **Cloak existing bastion**: Place Twingate in front of bastion server, remove public IP exposure
2. **Replace bastion**: Define private servers directly as Twingate Resources, eliminating the bastion hop entirely
3. **Enforce 2FA on SSH**: Apply IdP 2FA policy to SSH resources without server-side configuration

## Related Docs
- Twingate Connector setup
- Identity Provider integration
- Resource configuration
- Access policies / SSO configuration
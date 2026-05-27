# Bastion Server Cloaking with Twingate

## Page Title
Bastion Server Cloaking / Bastion Replacement

## Summary
Twingate can replace or augment bastion servers by making private resources completely invisible to the internet while providing stronger access controls. It addresses core bastion weaknesses: internet exposure, IdP sync gaps, and 2FA enforcement challenges.

## Key Information

**Bastion server use cases (what Twingate replaces):**
- Focused security monitoring/logging on a single exposed asset
- Single source IP to whitelist for private network ingress
- Centralized access management point

**Bastion limitations Twingate solves:**
- **Internet exposure**: Bastion remains attackable; Twingate Resources and Connectors are fully dark to the internet
- **IdP coupling**: SSH key management decouples from Active Directory/IdP; Twingate syncs with IdP in real-time
- **2FA enforcement**: Native SSH 2FA is complex; Twingate applies SSO policies (including 2FA) at the network layer (OSI Layer 4) without client/server config changes

**Twingate advantages:**
- All forwarded traffic is encrypted in-transit from user device to destination Connector
- Real-time IdP sync ensures only active employees retain access regardless of resource-level permissions
- SSO/2FA policies apply to any resource type without requiring application changes

## Prerequisites
- Twingate Connector deployed in private network
- Identity Provider (IdP) configured for SSO integration
- Existing bastion or SSH-accessible private resources

## Architecture Notes
- Connector does **not** need to be publicly accessible
- No inbound firewall rules required for Twingate to function
- Access control operates at network layer — independent of application-level auth

## Gotchas
- Twingate does not eliminate the need for resource-level authentication (SSH keys, etc.) — it adds network-layer access control on top
- IdP sync means account deactivation in IdP immediately revokes Twingate access, but existing authenticated sessions behavior should be verified
- "Completely invisible" applies to Resources and Connectors — the Twingate control plane itself uses Twingate's cloud infrastructure

## Configuration Values
No specific env vars, CLI flags, or API parameters documented on this page. See Connector deployment docs for setup.

## Related Docs
- Connector setup documentation
- Identity Provider / SSO integration
- Resource configuration
- Network access policies / 2FA enforcement
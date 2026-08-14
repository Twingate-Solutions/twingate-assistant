---
source: https://www.twingate.com/docs/bastion-replacement
type: docs
fetched: 2026-08-14
source_version: f953b07397a26512084ad5b43e3d02e5d823c92d054fd325c71a8b181f7ac528
---

# Bastion Server Cloaking with Twingate

## Page Title
Bastion Server Cloaking / Bastion Replacement

## Summary
Twingate can replace or supplement bastion servers by making private resources completely invisible to the internet while providing stronger authentication and identity integration. Unlike bastions, Twingate resources cannot be directly attacked from the internet, and access control integrates natively with Identity Providers and 2FA policies.

## Key Information
- Twingate Connectors and protected resources require **no public internet exposure**
- All traffic is **encrypted in-transit** from user device to destination Connector
- Access integrates **real-time** with Identity Provider — revoked accounts immediately lose access
- SSO policies (including 2FA) apply at the **network layer (OSI Layer 4)** without client/server config changes
- Works for any resource type, not just SSH targets

## Bastion Limitations Addressed

| Bastion Problem | Twingate Solution |
|---|---|
| Publicly exposed to internet attacks | Resources fully hidden; no public IP required |
| SSH key management decoupled from IdP | Real-time IdP sync; no active account = no access |
| 2FA difficult to enforce on SSH | SSO/2FA policy applied to any resource via IdP |

## Prerequisites
- Twingate account with Connector deployed in target network
- Identity Provider configured for Twingate SSO integration
- Resources defined within Twingate (servers previously accessed via bastion)

## Implementation Approach
1. Deploy Twingate **Connector** inside the private network (does not need inbound internet access)
2. Define private servers as **Resources** in Twingate admin console
3. Assign **Access Policies** to Resources, specifying IdP authentication requirements (including 2FA)
4. Configure IdP sync to ensure real-time user directory updates
5. Remove or restrict public internet exposure of the bastion server
6. Users install Twingate client and authenticate via IdP to access Resources directly

## Configuration Values
- No specific CLI flags or env vars documented on this page
- Authentication policy configuration is done in Twingate admin console per Resource
- IdP integration configured separately (see Identity Provider docs)

## Gotchas
- Twingate does **not** replace the bastion's logging/monitoring role by itself — ensure audit logging is configured separately
- Access is blocked for any user without an active IdP account, regardless of other permissions — plan for service accounts or non-IdP users
- This page is conceptual; actual Connector deployment and Resource configuration require separate setup steps

## Related Docs
- Connector setup documentation
- Identity Provider integration guides
- Resource configuration
- Access Policy / 2FA enforcement setup
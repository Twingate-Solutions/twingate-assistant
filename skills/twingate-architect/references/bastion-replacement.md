# Bastion Server Cloaking with Twingate

## Summary
Twingate can replace or supplement bastion servers by making private resources completely invisible to the internet. It addresses key bastion weaknesses: internet exposure, identity provider coupling, and 2FA enforcement gaps.

## Key Information

- **Bastion use cases**: Security hardening focus point, single IP whitelist source, centralized access management
- **Bastion weaknesses Twingate solves**:
  - Bastions remain internet-exposed and vulnerable to exploits
  - SSH key management often decoupled from Active Directory/IdP
  - Enforcing 2FA on SSH is difficult
- **Twingate advantages**:
  - Resources and Connectors are **completely invisible** to the internet — no public exposure required
  - All traffic encrypted in-transit from user device to destination Connector
  - Real-time IdP sync — inactive corporate accounts lose access automatically
  - SSO policies (including 2FA) applied at network layer (OSI Layer 4) without client/server config changes

## Prerequisites

- Twingate Connector deployed in private network
- Identity Provider (IdP) configured with Twingate
- Existing bastion or private resources to protect

## Implementation Approach

1. Deploy Twingate Connector inside the private network (no public IP required)
2. Define private resources (servers, subnets) in Twingate admin
3. Assign access policies tied to IdP groups/users
4. Configure SSO/2FA policy in IdP — Twingate enforces it on resource access
5. Remove or firewall-restrict the bastion's public internet exposure
6. Revoke access by deactivating user in IdP — Twingate access revoked automatically

## Gotchas

- Twingate does **not** require the Connector to be internet-accessible — do not expose it publicly
- Access revocation is IdP-driven; ensure IdP sync is active and tested
- 2FA enforcement happens via IdP policy, not SSH config — no changes needed on target servers
- Resource invisibility only applies if underlying firewall rules also block direct access to resources

## Related Docs

- Connector deployment
- Identity Provider integration
- Resource configuration
- Access policies / SSO configuration
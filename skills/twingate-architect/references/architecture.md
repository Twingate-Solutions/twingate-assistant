# Twingate Architecture

## Summary
Twingate implements Zero Trust Networking (ZTN) for secure private resource access, treating all networks as untrusted and requiring authentication/authorization for every access attempt. The system uses four core components working together to enable secure connectivity without traditional VPN infrastructure.

## Key Information

- **Zero Trust model**: No implicit trust for any network (public or private); every access request requires authentication + authorization
- **Four core components**:
  - **Controller**: Central management/policy enforcement plane
  - **Clients**: Installed on user devices
  - **Connectors**: Deployed in private networks to expose resources
  - **Relay infrastructure**: Twingate-managed relay servers for connectivity fallback
- **Peer-to-peer connections**: Supported by default; no open inbound ports required; transparent to users and admins; available to all customers at no extra cost
- **DNS handling**: Client intercepts DNS queries transparently, enabling access to private DNS addresses without exposing the private DNS resolver

## Prerequisites

- None listed on this page (overview/conceptual page only)

## Component Roles

| Component | Location | Purpose |
|-----------|----------|---------|
| Controller | Twingate-managed | Auth, policy, orchestration |
| Client | User device | DNS interception, tunnel management |
| Connector | Customer network | Resource proxy, no inbound ports needed |
| Relay | Twingate-managed | Fallback when P2P not possible |

## Configuration Values
None defined on this page (architecture overview only).

## Gotchas

- P2P connections require **no additional deployment** for existing customers — enabled automatically
- DNS behavior is non-standard and unique to Twingate; review DNS docs before deployment to avoid conflicts with existing DNS infrastructure
- Zero Trust model means being on the corporate network provides no implicit access — all access is policy-controlled

## Related Docs

- [How Twingate Works](#) — detailed component communication
- [Connectors](#) — deployment guidance
- [Resources](#) — resource management
- [Users & Groups](#) — identity management
- [Policies](#) — access control configuration
- [Devices](#) — device management
- [DNS with Twingate](#) — DNS interception details
- [Peer-to-Peer Communication](#) — P2P connection details
- [Twingate vs. VPNs](#) — comparison guide
- [Twingate vs. Mesh VPNs](#) — comparison guide
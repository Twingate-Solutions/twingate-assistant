# Twingate Architecture

## Summary
Twingate implements Zero Trust Networking for secure access to private resources, operating on the principle that all networks and users are untrusted by default. The system uses four core components (Controller, Clients, Connectors, Relay infrastructure) to enforce authentication and authorization for every resource access attempt.

## Key Information
- **Zero Trust model**: Every access request requires authentication (who you are) and authorization (what you can access) regardless of network location
- **Four core components**:
  - **Controller**: Central management/policy enforcement
  - **Clients**: End-user software
  - **Connectors**: Deployed in private networks to expose resources
  - **Relay infrastructure**: Facilitates connectivity
- **Peer-to-peer connections**: Supported by default; no open inbound ports required; zero additional deployment needed; transparent to users and admins
- **DNS handling**: Client intercepts DNS transparently; users can resolve private DNS addresses without direct access to private DNS resolvers

## Prerequisites
- None specific to this overview page

## Configuration Values
None defined on this page (overview/architecture reference only)

## Management Areas
| Area | Purpose |
|------|---------|
| Connectors | Deploy in private networks |
| Resources | Define what users can access |
| Users & Groups | Identity management |
| Policies | Access control rules |
| Devices | Device trust configuration |

## Gotchas
- Twingate treats private networks with the same trust level as public internet — internal network access alone grants no implicit trust
- Peer-to-peer connectivity requires no inbound ports, which differs from traditional VPN assumptions
- DNS behavior is non-standard (client intercepts DNS queries); review DNS documentation before deployment to avoid conflicts with existing DNS infrastructure

## Related Docs
- [How Twingate Works](#) — detailed component communication
- [DNS with Twingate](#) — DNS interception mechanics
- [Peer-to-Peer Communication](#) — P2P connection details
- [Twingate vs. VPNs](#) — comparison guide
- [Twingate vs. Mesh VPNs](#) — comparison guide
- [Connectors documentation](#)
- [Resources documentation](#)
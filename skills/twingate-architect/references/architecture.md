# Twingate Architecture

## Summary
Twingate implements Zero Trust Networking for secure private resource access, assuming all networks and users are untrusted by default. The system uses four components (Controller, Clients, Connectors, Relay) to enforce authentication and authorization on every access attempt. Unlike VPNs, Twingate treats internal and external networks with equal distrust.

## Key Information
- **Zero Trust model**: Every resource access attempt requires authentication (who you are) and authorization (what you can access)
- **No network trust distinction**: Internal company networks treated same as public internet
- **Four core components**: Controller, Clients, Connectors, Relay infrastructure
- **Peer-to-peer connections**: Enabled by default, no open inbound ports required, transparent to users and admins
- **DNS integration**: Client intercepts DNS transparently; users can access private DNS addresses without direct access to private DNS resolver
- **P2P availability**: All customers, no additional deployment needed

## Prerequisites
None specified on this page — links out to component-specific docs.

## Core Components
| Component | Role |
|-----------|------|
| Controller | Central management/policy enforcement |
| Client | Installed on user devices; handles DNS interception |
| Connector | Deployed in private networks to proxy resource access |
| Relay | Facilitates connections when direct P2P isn't possible |

## Configuration Areas
- **Connectors**: Deployment and management
- **Resources**: Define what private resources are accessible
- **Users & Groups**: Identity management
- **Policies**: Access control rules
- **Devices**: Device trust configuration

## Gotchas
- DNS behavior is non-standard — Twingate Client intercepts DNS queries transparently; review DNS docs before deploying if you have complex DNS requirements
- P2P connections require no inbound ports, but fallback to Relay infrastructure occurs automatically when P2P isn't possible

## Related Docs
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works) — detailed component communication
- [DNS with Twingate](https://www.twingate.com/docs/dns) — DNS interception mechanics
- [Peer-to-Peer Communication](https://www.twingate.com/docs/peer-to-peer) — P2P connection details
- [Connectors](https://www.twingate.com/docs/connectors)
- [Twingate vs. VPNs](https://www.twingate.com/docs/twingate-vs-vpn)
- [Twingate vs. Mesh VPNs](https://www.twingate.com/docs/twingate-vs-mesh-vpn)
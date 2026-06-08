# Twingate Architecture Overview

## Page Title
Architecture

## Summary
Twingate implements Zero Trust Networking to provide secure access to private resources, assuming all networks and users are untrusted by default. The system uses four core components (Controller, Clients, Connectors, Relay infrastructure) to enforce authentication and authorization on every resource access attempt.

## Key Information
- **Zero Trust model**: Every access attempt requires authentication (who you are) and authorization (what you can access) — no implicit trust for any network, public or private
- **Four core components**: Controller, Clients, Connectors, Relay infrastructure
- **Peer-to-peer connections**: Supported by default with no open inbound ports required; available to all customers with no additional deployment
- **DNS handling**: Client transparently intercepts DNS; users can resolve private DNS addresses without direct access to private DNS resolvers
- **No VPN required**: Replaces traditional VPN and mesh VPN approaches

## Prerequisites
- None listed on this page (overview/reference document)

## Component Reference
| Component | Role |
|-----------|------|
| Controller | Central management/policy enforcement |
| Client | Installed on user devices; handles DNS and connections |
| Connector | Deployed in private networks; proxies resource access |
| Relay | Twingate-managed infrastructure for connection brokering |

## Configuration Areas
- **Connectors**: Deployment and management
- **Resources**: Define private resources to protect
- **Users & Groups**: Identity and access management
- **Policies**: Access control rules
- **Devices**: Device trust configuration

## Gotchas
- Peer-to-peer connections require **no open inbound ports** — no firewall changes needed
- DNS behavior is unique to Twingate; review DNS documentation before deployment to understand resolver interactions
- Zero Trust means even users on the corporate LAN are not implicitly trusted

## Related Docs
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works) — detailed component communication
- [DNS with Twingate](https://www.twingate.com/docs/dns) — private DNS resolution behavior
- [Peer-to-Peer Communication](https://www.twingate.com/docs/peer-to-peer)
- [Connectors](https://www.twingate.com/docs/connectors)
- [Twingate vs. VPNs](https://www.twingate.com/docs/twingate-vs-vpns)
- [Twingate vs. Mesh VPNs](https://www.twingate.com/docs/twingate-vs-mesh-vpns)
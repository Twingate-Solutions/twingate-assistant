# Twingate Architecture Overview

## Page Title
Architecture

## Summary
Twingate implements Zero Trust Networking for secure access to private resources, assuming all networks and users are untrusted by default. The system uses four core components (Controller, Clients, Connectors, Relay infrastructure) to enforce authentication and authorization on every resource access attempt.

## Key Information
- **Zero Trust model**: Every access attempt requires authentication (who you are) and authorization (what you can access) regardless of network location
- **Four core components**: Controller, Clients, Connectors, Relay infrastructure
- **Peer-to-peer connections**: Supported by default with no open inbound ports required; no additional deployment needed
- **DNS integration**: Client transparently intercepts DNS to enable private DNS address resolution without exposing the private DNS resolver
- **No network trust distinctions**: Public internet and private corporate networks treated identically from a trust perspective

## Prerequisites
None specified on this page — this is an architectural overview/index page.

## Component Reference

| Component | Role |
|-----------|------|
| Controller | Central management and policy enforcement |
| Client | End-user agent; handles DNS interception |
| Connector | Deployed in private networks; proxies resource access |
| Relay | Infrastructure for NAT traversal and connection brokering |

## Configuration Values
None specified on this page.

## Gotchas
- Peer-to-peer connections require **no inbound ports** — eliminates need for firewall rule changes
- DNS behavior is non-standard; private DNS addresses are accessible without direct access to the private resolver — review DNS guide before deployment to avoid unexpected behavior

## Related Docs
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works) — detailed component communication
- [DNS with Twingate](https://www.twingate.com/docs/dns) — DNS interception mechanics
- [Peer-to-Peer Communication](https://www.twingate.com/docs/peer-to-peer) — P2P connection details
- [Connectors](https://www.twingate.com/docs/connectors)
- [Resources](https://www.twingate.com/docs/resources)
- [Users & Groups](https://www.twingate.com/docs/users)
- [Policies](https://www.twingate.com/docs/policies)
- [Devices](https://www.twingate.com/docs/devices)
- [Twingate vs. VPNs](https://www.twingate.com/docs/twingate-vs-vpns)
- [Twingate vs. Mesh VPNs](https://www.twingate.com/docs/twingate-vs-mesh-vpns)
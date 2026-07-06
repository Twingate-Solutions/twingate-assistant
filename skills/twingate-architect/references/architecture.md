# Twingate Architecture

## Page Title
Architecture Overview

## Summary
Twingate implements Zero Trust Networking for secure private resource access, assuming all networks and users are untrusted by default. The system uses four core components (Controller, Clients, Connectors, Relay infrastructure) to enforce authentication and authorization on every access attempt. It operates transparently to end users via DNS integration and peer-to-peer connections.

## Key Information
- **Zero Trust model**: Every resource access attempt requires authentication + authorization regardless of network location (public or private)
- **Four core components**:
  - **Controller**: Central management/policy enforcement
  - **Clients**: End-user devices
  - **Connectors**: Deploy in private networks to expose resources
  - **Relay infrastructure**: Facilitates connectivity
- **DNS integration**: Clients transparently intercept DNS to enable private DNS address resolution without exposing private DNS resolvers
- **Peer-to-peer connections**: Supported by default; no open inbound ports required; zero additional deployment needed

## Prerequisites
None for reading; deployment prerequisites covered in component-specific docs.

## Configuration / Components
| Component | Purpose |
|-----------|---------|
| Controller | Auth, policy, management plane |
| Client | Installed on user devices |
| Connector | Deployed in private network/cloud |
| Relay | NAT traversal / connection brokering |

## Gotchas
- Twingate does **not** treat internal network connections as inherently trusted — zero trust applies even when on-premises
- Peer-to-peer works **without inbound port changes** to existing infrastructure
- DNS behavior is non-standard/unique — review DNS guide before deployment to avoid conflicts

## Related Docs
- [How Twingate Works](#) — detailed component communication architecture
- [Connectors](#) — deployment guide
- [Resources](#) — resource configuration
- [Users & Groups](#) — identity management
- [Policies](#) — access control rules
- [Devices](#) — device management
- [DNS with Twingate](#) — DNS interception explained
- [Peer-to-Peer Communication](#) — P2P connection details
- [Twingate vs. VPNs](#) — comparison guide
- [Twingate vs. Mesh VPNs](#) — comparison guide
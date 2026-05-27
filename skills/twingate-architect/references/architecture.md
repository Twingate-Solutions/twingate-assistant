# Twingate Architecture

## Summary
Twingate implements Zero Trust Networking to provide secure access to private resources, assuming all networks and users are untrusted by default. The system uses four core components to enforce authentication and authorization on every resource access attempt.

## Key Information

- **Zero Trust model**: Every access attempt requires authentication (who you are) and authorization (what you can access) — no implicit trust for private networks
- **Four core components**:
  - **Controller**: Central management/policy enforcement
  - **Clients**: Installed on user devices
  - **Connectors**: Deployed in private networks alongside resources
  - **Relay infrastructure**: Twingate-managed relay servers for connectivity
- **Peer-to-peer connections**: Supported by default; no open inbound ports required, transparent to users and admins
- **DNS handling**: Client intercepts DNS transparently, allowing access to private DNS addresses without exposing the private DNS resolver

## Prerequisites
- None listed on this page (overview/reference page)

## Core Components

| Component | Role |
|-----------|------|
| Controller | Authentication, authorization, policy management |
| Client | End-user device agent |
| Connector | Deployed in private network, proxies resource access |
| Relay | Fallback/intermediary for connections when P2P not possible |

## Configuration Values
- No specific env vars or CLI flags on this page

## Gotchas
- Zero Trust means users on a corporate LAN receive **no implicit trust** — same verification applies as remote users
- Peer-to-peer requires no additional deployment for existing customers

## Related Docs
- [How Twingate Works](#) — detailed component communication flow
- [Connectors](#) — deployment and management
- [Resources](#) — defining protected resources
- [Users & Groups](#) — access management
- [Policies](#) — authorization rules
- [Devices](#) — device management
- [DNS with Twingate](#) — private DNS behavior
- [Peer-to-Peer Communication](#) — P2P connection details
- [Twingate vs. VPNs](#) / [vs. Mesh VPNs](#) — comparison guides
---
source: https://www.twingate.com/docs/architecture
type: docs
fetched: 2026-08-14
source_version: 7086a41b7f61d30df9662031653711e9b5b22bb5a10906a51a4e7759a2c37696
---

# Twingate Architecture

## Page Title
Architecture Overview

## Summary
Twingate implements Zero Trust Networking (ZTN) for secure private resource access, assuming all networks and users are untrusted by default. The system uses four core components to enforce authentication and authorization on every access attempt. It operates without traditional VPN infrastructure and supports peer-to-peer connections without open inbound ports.

## Key Information

- **Zero Trust model**: No implicit trust for any network (public or private); every access attempt requires authentication + authorization
- **Four core components**:
  - **Controller** – central management/policy enforcement
  - **Clients** – end-user software
  - **Connectors** – deployed in private networks to expose resources
  - **Relay infrastructure** – facilitates connectivity when direct connection isn't possible
- **DNS integration**: Client transparently intercepts DNS to enable private DNS resolution without exposing the private DNS resolver to users
- **Peer-to-peer connections**: Supported by default for all customers; no open inbound ports required, no additional deployment needed, transparent to users and admins

## Prerequisites
- None listed on this page (overview/conceptual content only)

## Configuration Values
- None specified on this page

## Management Areas (Links to Primary Docs)
- Connectors
- Resources
- Users & Groups
- Policies
- Devices

## Gotchas
- Peer-to-peer connectivity requires **no open inbound ports** — existing deployments get this automatically without reconfiguration
- DNS behavior is unique to Twingate's Client implementation; users can reach private DNS addresses even without access to the private DNS resolver itself
- Zero Trust means **on-network users are not implicitly trusted** — same verification applies regardless of network location

## Related Docs
- How Twingate Works (detailed component communication)
- How DNS Works with Twingate
- Peer-to-peer communication guide
- Twingate vs. VPNs
- Twingate vs. Mesh VPNs
- "Architecting Network Connectivity for a Zero Trust Future" (blog)
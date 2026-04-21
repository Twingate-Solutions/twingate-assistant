## Page Title
Architecture

## Summary
Navigation hub for Twingate's architecture documentation. Covers the Zero Trust Networking model, the four core components (Controller, Clients, Connectors, Relay), DNS handling, and peer-to-peer connections. Use this to orient to the technical design before reading component-specific guides.

## Key Information
- **Zero Trust model**: every access attempt is authenticated and authorized regardless of network location; no implicit trust for internal network users
- **Four components**:
  - **Controller**: cloud-hosted control plane; manages auth, policy enforcement, and orchestration
  - **Clients**: end-user apps (desktop/mobile) that intercept and route traffic
  - **Connectors**: lightweight proxies deployed in private networks; make outbound-only connections
  - **Relay**: Twingate-managed relay infrastructure for traffic that cannot establish P2P
- **DNS**: Twingate Client intercepts DNS lookups for private resource addresses and resolves them transparently without exposing the private DNS resolver to users
- **Peer-to-peer (P2P)**: direct connections between Client and Connector without open inbound ports; uses NAT traversal (QUIC); available to all plans; zero configuration required
- No open inbound ports on Connectors — all connections are outbound from Connector to Controller/Relay

## Prerequisites
None — reference/overview page.

## Step-by-Step
Not applicable.

## Configuration Values
None on this page.

## Gotchas
- The Relay is used as fallback only when P2P cannot be established (e.g. symmetric NAT); it does not see plaintext traffic — data is end-to-end encrypted
- "Controller" is Twingate's cloud service — it is not deployed by the customer
- Clients and Connectors authenticate to the Controller but do not route data through it

## Related Docs
- `/docs/how-twingate-works` — detailed component interaction
- `/docs/how-dns-works-with-twingate` — DNS interception mechanics
- `/docs/peer-to-peer-communication-in-twingate` — P2P connection detail
- `/docs/understanding-relays` — Relay infrastructure
- `/docs/how-nat-traversal-works` — NAT traversal mechanics
- `/docs/twingate-vs-vpn` — architectural comparison with VPN

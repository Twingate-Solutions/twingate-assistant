## Page Title
Understanding Relays

## Summary
Explains what Twingate Relays do, how the global Relay network is structured for low latency and redundancy, and the data privacy guarantees. Relays facilitate Client-Connector connection establishment and serve as encrypted fallback transport — they cannot decrypt traffic passing through them.

## Key Information
- **Role**: Relays facilitate the initial Client-Connector TLS tunnel setup and serve as encrypted fallback transport when P2P NAT traversal is not possible
- **End-to-end encryption**: TLS tunnel is between Client and Connector — Relay is a hop, not an endpoint; Relay cannot decrypt traffic
- **No data stored**: Relays do not store traffic or network-identifiable information; pass-through only; no connections terminated at Relay
- **Latency**: each Connector connects to geographically nearest Relay automatically
- **Redundancy**: each location has a cluster of multiple Relays; if one fails, another in the same cluster takes over; if a cluster fails, next-nearest cluster is used automatically
- **Relay cluster locations (Google Cloud)**: Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia (NA); Sao Paulo (SA); Eemshaven, Finland, Frankfurt, London, Zurich (EU); Tel Aviv (ME); Johannesburg (AF); Mumbai, Singapore, Tokyo (AS); Sydney (AU)
- **Relay cluster locations (DigitalOcean)**: Atlanta, NYC, San Francisco, Toronto (NA); Amsterdam, Frankfurt, London (EU); Bengaluru, Singapore (AS); Sydney (AU)

## Prerequisites
None — Relays are Twingate-managed infrastructure; no customer configuration required.

## Step-by-Step
Not applicable — fully automatic.

## Configuration Values
None — Connector-to-Relay assignment is automatic based on geography.

## Gotchas
- Connectors connect to the nearest Relay on startup — if that Relay cluster goes down, automatic failover to next-nearest occurs without manual intervention
- The Relay cluster location list reflects current Twingate infrastructure; check the live doc for additions

## Related Docs
- `/docs/how-twingate-works` — Relay's role in the four-component architecture
- `/docs/peer-to-peer-communication-in-twingate` — P2P vs Relay transport selection
- `/docs/how-nat-traversal-works` — how Relay enables NAT traversal
- `/docs/detailed-client-connection-flow` — how Relay is used during connection setup

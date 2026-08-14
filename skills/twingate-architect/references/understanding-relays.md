---
source: https://www.twingate.com/docs/understanding-relays
type: docs
fetched: 2026-08-14
source_version: bfdd5d8e822861a094f9b1a3d5aeb202865971f4046079870ce34032ce04a1d0
---

# Understanding Relays

## Summary
Relays facilitate connection establishment between Twingate Clients and Connectors for accessing Resources. They act as intermediaries in the end-to-end encrypted TLS tunnel and may route encrypted traffic when direct connections aren't possible. Relays do not store or terminate data connections.

## Key Information
- Relays serve two functions: connection establishment facilitation and optional traffic routing between Clients and Connectors
- All traffic is end-to-end encrypted via certificate-pinned TLS tunnel before passing through a Relay
- Relays never terminate connections or store traffic/network-identifiable information
- Each Connector connects to the geographically nearest available Relay to minimize latency
- Relay clusters provide redundancy: failure within a location fails over to another Relay in same cluster; full cluster failure fails over to next nearest cluster

## Relay Cluster Locations

**Google Cloud:** Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia (NA); São Paulo (SA); Eemshaven, Finland, Frankfurt, London, Zurich (EU); Tel Aviv (ME); Johannesburg (AF); Hong Kong, Mumbai, Singapore, Taiwan, Tokyo (Asia); Sydney (AU)

**DigitalOcean:** Atlanta, Richmond VA, NYC, San Francisco, Toronto (NA); Amsterdam, Frankfurt, London (EU); Bengaluru, Singapore (Asia); Sydney (AU)

## Architecture Notes
- Authorization flow: Controller authorizes Client → Client establishes connection to Connector via Relay
- Connection type: End-to-end encrypted, certificate-pinned TLS tunnel
- Relay involvement in data path: transient only; no connection termination at Relay

## Gotchas
- Relays are Twingate-managed infrastructure — no self-hosting or configuration required by operators
- Traffic through Relays is already encrypted; Relays cannot inspect payload data
- Relay routing is automatic; no manual Relay selection is available

## Related Docs
- Twingate Controllers (authorization component)
- Connectors (the component that connects to Relays)
- Twingate Client configuration
---
source: https://www.twingate.com/docs/understanding-relays
type: docs
fetched: 2026-08-05
source_version: 69e77ac39097deee75d722573b8152850b8fd7a4e0860b1bf3a35759748e969a
---

# Understanding Relays

## Page Title
Understanding Relays

## Summary
Relays facilitate secure connection establishment between Twingate Clients and Connectors for Resource access. They act as intermediaries in the end-to-end encrypted TLS tunnel, and may route encrypted traffic when direct connections aren't possible. Relays are stateless and do not store traffic or network-identifiable data.

## Key Information
- Relays facilitate (not terminate) connections between Clients and Connectors
- Connections use certificate-pinned TLS tunnels — encryption is end-to-end
- Relays may serve as a routing hop when direct Client↔Connector connection isn't possible
- Traffic passing through Relays is already encrypted; Relays cannot read it
- No data is stored at Relays — purely transient pass-through
- Connectors automatically connect to the geographically nearest available Relay

## Relay Cluster Locations

**Google Cloud:** Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia, São Paulo, Eemshaven, Finland, Frankfurt, London, Zurich, Tel Aviv, Johannesburg, Hong Kong, Mumbai, Singapore, Taiwan, Tokyo, Sydney

**DigitalOcean:** Atlanta, Richmond (VA), New York City, San Francisco, Toronto, Amsterdam, Frankfurt, London, Bengaluru, Singapore, Sydney

## Redundancy Model
- Each Relay location runs a **cluster** of multiple Relays
- Failure of one Relay → failover to another Relay in same cluster
- Failure of entire cluster → automatic failover to next nearest cluster

## Prerequisites
- No direct configuration required — Relay selection is automatic
- Connectors handle Relay connection without user intervention

## Gotchas
- Relays are Twingate-managed infrastructure; you cannot self-host or select specific Relays
- Relay routing only occurs "when necessary" — direct peer-to-peer is preferred when available
- Relay involvement does not break end-to-end encryption; the encrypted tunnel passes *through* the Relay, not to it
- Latency impact is minimized by geo-proximity selection, but cross-region Connector deployments may incur higher latency

## Configuration Values
None — Relay selection and failover are fully automatic. No environment variables, CLI flags, or API parameters apply to Relay configuration.

## Related Docs
- Twingate Connectors documentation
- Twingate Controller documentation
- Network architecture / Client connection flow docs
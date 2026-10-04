---
source: https://help.twingate.com/articles/4995810632-connector-cannot-connect-to-the-twingate-relay
type: help
fetched: 2026-10-04
source_version: 19631e67ac76b001377e2ae555571c4cd97dfebfe38f0de3d7b60472d6a2f830
trust: official
---

# Connector Cannot Connect to Twingate Relay

## Page Title
Connector Cannot Connect to the Twingate Relay

## Summary
When a Twingate Connector has only a public IPv6 address (no IPv4), it cannot establish connections to the Twingate Relay infrastructure. This causes all Resource connections to fail despite the Client working normally and general internet connectivity being functional.

## Key Information
- **Affected component:** Twingate Connector
- **Root cause:** Connector VM has only a public IPv6 address; no public IPv4 address assigned
- **Effect:** All Resource connections fail; Client appears functional

## Symptoms
- Connector passes general outbound internet connectivity checks
- All network requirements are otherwise met
- No connections to Resources succeed
- Twingate Administrator console shows Connector unable to connect to Resources

## Error Messages in Connector Logs
```
[Timestamp][Connector]: [ERROR] [libsdwan] listen::channel_event: Failed to preconnect a relay listener "ice://any": 110 (Connection timed out)

[Timestamp][Connector]: [ERROR] [libsdwan] listen::maintain_relay_connectivity: relay [IP address and port] is not available, disconnect
```
Also may appear: `resource temporarily unavailable`

## Resolution
Assign a public IPv4 address to the Connector VM instance.

- Check your cloud provider's networking settings (AWS: Elastic IP / public IP assignment; GCP: External IP; Azure: Public IP resource) and ensure the Connector's network interface has a public IPv4 address
- IPv6-only network configurations are not supported for Connector-to-Relay communication

## Gotchas
- The Connector may appear healthy (outbound connectivity works, no obvious failures) while IPv6-only prevents Relay connections specifically
- Logs may initially appear as generic timeout or "resource temporarily unavailable" errors — check for the `libsdwan` relay-specific messages to confirm this cause

## Related Docs
- [Twingate Network Requirements](https://help.twingate.com/articles/network-requirements)
- Twingate Administrator Console connection diagnostics
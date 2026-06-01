# Connector Details

## Page Title
Connector Details (Metadata & Status Information)

## Summary
Twingate Connectors report metadata back to the Controller providing operational status, network information, and diagnostic data. This information is used for monitoring Connector health and troubleshooting connectivity issues.

## Key Information

- **Uptime/Downtime**: Reflects Connector state as seen by the Controller — not the host machine state. Connector downtime with a running host machine indicates a configuration/connectivity issue
- **Time Offset**: Difference between Connector and Controller clocks; maximum tolerance is **±5 seconds**. Values near limits cause intermittent connection failures
- **STUN Discovery**: Required for peer-to-peer connections. Uses STUN to determine public IP/port behind NAT layers. If unavailable, P2P connections fail entirely
- **Hostname**: Reports the running process's hostname (e.g., Docker container hostname, not physical host)
- **Public IP**: Most recent IP seen by Controller; may change in multi-path routing setups
- **Private IP**: All private IPs visible to the Connector process. Docker containers report `172.0.0.0/16` subnet addresses, not the physical host's IPs

## Prerequisites
- Connector must be deployed and registered with the Controller
- NTP or time synchronization configured on host machine (critical for staying within ±5s offset)
- STUN traffic must be permitted through firewall/NAT for P2P connections

## Gotchas

- **Docker networking**: Private IP will show container network addresses (`172.0.0.0/16`), not physical machine IPs — expected behavior, not a bug
- **Downtime ≠ machine down**: Connector showing downtime while host is running points to Connector process or network issues, not host failure
- **Time drift**: Offsets approaching ±5s cause *intermittent* (not total) failures, making it harder to diagnose
- **Public IP changes**: In environments with multiple egress paths, public IP reported may be inconsistent
- **STUN unavailability**: Falls back from P2P to relay connections — connections still work but performance degrades

## Configuration Values
None directly configurable from this page. Time synchronization is an OS-level concern (NTP).

## Related Docs
- Connector Best Practices (linked for uptime/downtime troubleshooting)
- Twingate Knowledge Base: Time Synchronization Issues
- STUN protocol documentation
- NAT traversal documentation
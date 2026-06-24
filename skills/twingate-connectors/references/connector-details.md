# Connector Details

## Page Title
Connector Details

## Summary
Twingate Connectors report metadata back to the Controller including uptime/downtime, time synchronization, STUN discovery status, and network information. This data is used for monitoring Connector health and troubleshooting connectivity issues.

## Key Information

- **Uptime/Downtime**: Reflects Connector state as seen by the Controller — not the host machine status. A running machine can still show Connector downtime.
- **Time Offset**: Difference between Connector clock and Controller clock. Max tolerance is **±5 seconds**. Values outside this range cause intermittent connection failures.
- **STUN Discovery**: Required for peer-to-peer connections. Used to determine public IP/port behind NAT layers. If unavailable, P2P connections fail entirely.
- **Hostname**: Reports the hostname of the machine/container running the Connector (e.g., Docker container hostname, not host machine).
- **Public IP**: Most recently seen IP from the Controller's perspective — may change in multi-path routing setups.
- **Private IP**: All private IPs visible to the Connector process. Docker containers report container-network addresses (e.g., `172.0.0.0/16`), not the physical host's IPs.

## Prerequisites
- A deployed Twingate Connector
- Network access from Connector to Twingate Controller

## Configuration Values
- **Time offset limit**: `±5 seconds` (hard tolerance)
- **Docker private IP subnet**: `172.0.0.0/16` (container networking — does not reflect physical host)

## Gotchas

- **Downtime ≠ host offline**: Connector downtime only reflects Controller visibility. A healthy host machine can still register Connector downtime — check best practices if this occurs.
- **Time sync is critical**: Offsets near ±5s cause *intermittent* issues that may be hard to diagnose. Ensure NTP is configured and running on the Connector host.
- **STUN unavailability**: Blocks all P2P connections. Clients will fall back to relay if available, but P2P performance is lost.
- **Docker IP reporting**: Private IPs shown for containerized Connectors reflect container network interfaces only — physical host IPs are not visible from inside the container.
- **Public IP is not static**: In environments with multiple egress paths, the reported public IP may not be consistent.

## Related Docs
- Connector Best Practices (linked in page)
- Twingate Knowledge Base: Time Synchronization Issues (linked in page)
- STUN protocol documentation
- NAT traversal overview
---
source: https://www.twingate.com/docs/connector-details
type: docs
fetched: 2026-11-13
source_version: 45d95cd0f5494b02966b529f72c97c38493f170ca58ff0b777a11bcd914acadf
trust: official
---

# Connector Details

## Summary
Twingate Connectors report metadata to the Controller, covering Connector status and the host machine it runs on. This data is shown in the Admin Console and helps troubleshoot connectivity, time sync, and networking issues.

## Key Information
- **Uptime/Downtime**: Shows how long the Connector has been online or offline *as seen by the Controller*. It does not necessarily reflect whether the host machine is up.
- **Time offset**: Difference between Connector and Controller clocks.
  - Negative = Connector is "in the past"; positive = "in the future".
  - Controller tolerates a maximum of **+/- 5 seconds**.
  - Offsets near the limit can cause intermittent connection issues.
- **STUN discovery**: Connectors must complete STUN discovery to establish peer-to-peer connections with Clients. Twingate uses STUN to learn the Connector's public IP and port when it is behind one or more NAT layers. If STUN is unavailable, peer-to-peer connections fail.
- **Hostname**: Hostname of the machine running the Connector. In Docker this is the container's hostname, not the physical host's.
- **Public IP**: Most recent public IP the Controller saw the Connector on. It can change, especially if traffic is routed through multiple egress IPs.
- **Private IP**: All private IPs visible to the Connector's machine. In Docker, expect addresses in `172.17.0.0/16`. The physical host's IPs are not visible from the container.

## Prerequisites
- A deployed Twingate Connector reporting to a Controller.
- Network access that allows STUN discovery (for peer-to-peer).
- Accurate system clock on the Connector host (e.g., via NTP).

## Step-by-Step (Troubleshooting Flow)
1. If the Connector shows downtime while the host is running, review Twingate's Connector best practices.
2. If connections are intermittent, check the time offset and sync the host clock if it is near +/- 5 seconds.
3. If peer-to-peer connections fail, verify the Connector can complete STUN discovery (check egress/firewall rules).
4. Use the hostname and IP data to confirm which machine or container the Connector is running on.

## Configuration Values
None. This page describes reported metadata only, with no env vars, CLI flags, or API parameters. The one numeric threshold is the +/- 5 second time offset tolerance.

## Gotchas
- Downtime reflects Controller visibility, not host state.
- Time offsets within the tolerance but close to the limit can still cause intermittent issues.
- Containerized Connectors report container hostnames and Docker-internal private IPs, not the host's.
- The public IP may change between observations.
- Blocked STUN silently prevents peer-to-peer connectivity.

## Related Docs
- Connector best practices
- Twingate Knowledge Base article on time synchronization troubleshooting
- Twingate documentation on STUN and NAT/peer-to-peer connectivity
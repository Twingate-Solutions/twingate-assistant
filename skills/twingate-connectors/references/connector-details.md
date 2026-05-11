# Connector Details

## Page Title
Connector Details

## Summary
Twingate Connectors report metadata back to the Controller providing status information and host machine details. This data helps monitor Connector health and troubleshoot connectivity issues. Metrics include uptime, time sync, STUN discovery status, and network addressing.

## Key Information
- **Uptime/Downtime**: Reflects Controller's view of Connector state, not host machine status — Connector can show downtime while host is running
- **Time Offset**: Maximum tolerance is **±5 seconds** between Connector and Controller; values near limits cause intermittent connection issues
- **STUN Discovery**: Required for peer-to-peer Client↔Connector connections; used to determine public IP/port behind NAT layers
- **Hostname**: Reports container hostname in Docker deployments, not physical host hostname
- **Public IP**: Most recently seen IP by Controller; may change in multi-path routing setups
- **Private IP**: All visible private IPs on the Connector's machine; Docker containers report `172.0.0.0/16` subnet, not physical host IPs

## Prerequisites
- Connector deployed and registered with Controller
- For STUN discovery: Connector must have outbound access to STUN servers

## Gotchas
- **Docker networking**: Private IP reflects container network (`172.0.0.0/16`), not physical machine IP — don't use this for host-level debugging
- **Downtime ≠ host down**: Connector downtime reported by Controller may indicate configuration issues rather than machine failure; review best practices if host is running but Connector shows downtime
- **Time sync is critical**: Keep host clock synchronized (NTP); offsets approaching ±5s cause intermittent failures before hard cutoff
- **STUN unavailable = no P2P**: Without STUN discovery, all traffic falls back through relay — impacts performance
- **Public IP instability**: In environments with multiple egress paths, public IP field may not be reliable for allowlisting

## Configuration Values
None directly configurable on this page — these are read-only reported metrics visible in the Twingate admin console.

## Related Docs
- Connector best practices (linked inline)
- Twingate Knowledge Base: Time synchronization troubleshooting
- STUN protocol documentation
- NAT traversal concepts
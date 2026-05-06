# Connector Details

## Page Title
Connector Details

## Summary
Twingate Connectors report metadata to the Controller for status monitoring and troubleshooting. Key metrics include uptime/downtime, time synchronization, STUN discovery status, and network information. This data is viewable in the Twingate admin console.

## Key Information

- **Uptime/Downtime**: Reflects Connector state as seen by the Controller—not the host machine state. Connector downtime with a running host machine indicates a configuration issue
- **Time Offset**: Difference between Connector and Controller clocks. Maximum tolerance is **±5 seconds**. Values near limits cause intermittent connection issues
- **STUN Discovery**: Required for peer-to-peer connections. Used to determine public IP/port behind NAT layers. If unavailable, P2P connections fail entirely
- **Hostname**: Reports the container/process hostname, not necessarily the physical host (e.g., Docker container hostname)
- **Public IP**: Most recently observed IP by Controller; may change in multi-path routing setups
- **Private IP**: All private IPs visible to the Connector process. Docker containers report `172.0.0.0/16` addresses, not the host machine's physical IPs

## Prerequisites
- Running Twingate Connector
- Network access to Twingate Controller
- NTP or equivalent time sync configured on host

## Gotchas

- **Time sync is critical**: Offsets beyond ±5 seconds will break connectivity. Ensure NTP is running on the Connector host
- **Docker networking**: Private IP reporting shows container IPs (`172.x.x.x`), not physical host IPs—don't use these for network diagnostics of the underlying host
- **STUN blocked**: If firewalls block STUN, peer-to-peer connections will fail; traffic falls back through relay (higher latency)
- **Downtime ≠ host down**: Connector downtime with an active host suggests a process/configuration problem, not a machine failure—consult Twingate best practices docs

## Configuration Values
None directly configurable on this page—these are read-only reported metrics.

## Related Docs
- Twingate Connector Best Practices
- Twingate Knowledge Base: Time Synchronization Issues
- STUN protocol documentation
- NAT traversal concepts
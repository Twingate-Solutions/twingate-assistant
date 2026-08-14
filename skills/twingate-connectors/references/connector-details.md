---
source: https://www.twingate.com/docs/connector-details
type: docs
fetched: 2026-08-14
source_version: af1193c7a09156f57f0913d4b73cc5ff71f4e7f1af5fa28d5128594fac41e422
---

# Connector Details

## Page Title
Connector Details

## Summary
Twingate Connectors report metadata back to the Controller including uptime, time synchronization, STUN discovery status, and network information. This data is viewable in the admin console and is primarily useful for monitoring Connector health and troubleshooting connectivity issues.

## Key Information
- **Uptime/Downtime**: Reflects Controller's view of Connector state, not the host machine's actual uptime
- **Time Offset**: Difference between Connector and Controller clocks; max tolerance is **±5 seconds**
- **STUN Discovery**: Required for peer-to-peer connections; failure means P2P is unavailable, falling back to relay
- **Hostname**: Reports the process/container hostname, not necessarily the physical host
- **Public IP**: Most recent IP seen by Controller; may change in multi-path routing setups
- **Private IP**: All private IPs visible to the Connector process; Docker containers report container subnet (e.g., `172.0.0.0/16`), not host IPs

## Prerequisites
- A deployed and registered Twingate Connector
- Access to Twingate admin console to view Connector details

## Configuration Values
| Parameter | Value/Limit |
|-----------|-------------|
| Max time offset tolerance | ±5 seconds |
| Docker container subnet example | `172.0.0.0/16` |

## Gotchas
- **Downtime ≠ host offline**: Connector can show downtime while the host machine is running — check best practices for misconfiguration
- **Time offset issues**: Offsets near ±5s cause *intermittent* (not total) connection failures — harder to diagnose
- **Docker hostname/IP mismatch**: Connector reports container hostname and container network IPs, not the physical host's values; don't use these to identify the underlying host
- **Public IP instability**: In multi-path or load-balanced setups, reported public IP may not be consistent
- **STUN unavailability**: If STUN fails (e.g., firewall blocking UDP), P2P connections fail entirely — all traffic routes through relay, increasing latency

## Troubleshooting Steps
1. **Connector offline but host running** → Review Twingate Connector best practices
2. **Time offset issues** → Ensure NTP is configured and syncing on the Connector host; check Twingate KB article on time synchronization
3. **STUN discovery unavailable** → Verify outbound UDP is not blocked to Twingate STUN servers; check firewall/NAT rules

## Related Docs
- Twingate Connector Best Practices
- STUN protocol documentation
- NAT traversal documentation
- Twingate Knowledge Base: Time synchronization troubleshooting
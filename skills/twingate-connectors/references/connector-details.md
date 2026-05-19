# Connector Details

## Page Title
Connector Details

## Summary
Twingate Connectors report metadata to the Controller for status monitoring and troubleshooting. This includes uptime/downtime tracking, time synchronization, STUN discovery status, and network information. These details are viewable in the Twingate admin console.

## Key Information
- **Uptime/Downtime**: Reflects Connector state as seen by Controller — not the host machine's actual uptime
- **Time Offset**: Difference between Connector and Controller clocks; max tolerance is **±5 seconds**
- **STUN Discovery**: Required for peer-to-peer connections; used to determine public IP/port behind NAT
- **Hostname**: Reports the running process's hostname (e.g., Docker container hostname, not physical host)
- **Public IP**: Most recently seen IP from Controller's perspective; may change dynamically
- **Private IP**: All private IPs visible to the Connector process; Docker containers report `172.0.0.0/16` subnet addresses, not the physical host's IPs

## Prerequisites
- A deployed and running Twingate Connector
- Connector must have network access to Twingate Controller

## Configuration Values
| Parameter | Value/Limit |
|-----------|-------------|
| Max time offset tolerance | ±5 seconds |
| Docker private subnet (typical) | `172.0.0.0/16` |

## Gotchas
- **Downtime ≠ machine down**: If Connector shows downtime but the host is running, check Twingate best practices — the issue is with the Connector process or its connection to the Controller
- **Time drift causes intermittent failures**: Offsets near ±5 seconds cause connection issues before the hard limit is hit; ensure NTP is configured on the host
- **Docker networking caveat**: Private IP reporting reflects the container's network view — the physical host's IP is not visible from inside the container
- **STUN required for P2P**: Without STUN discovery, all traffic routes through relays instead of peer-to-peer; verify outbound STUN access is not blocked
- **Public IP may change**: Dynamic routing setups can cause the reported public IP to shift; account for this in firewall rules

## Troubleshooting Reference
- Connector shows downtime but machine is up → review Connector best practices
- Time synchronization issues → Twingate Knowledge Base article on time sync
- STUN unavailable → check firewall/NAT rules blocking STUN protocol outbound

## Related Docs
- Twingate Connector best practices
- STUN protocol documentation
- NAT traversal overview
- Twingate Knowledge Base (time synchronization)
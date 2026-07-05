# Connector Details

## Page Title
Connector Details

## Summary
Twingate Connectors report metadata to the Controller for status monitoring and troubleshooting. Key metrics include uptime/downtime, time synchronization, STUN discovery status, and network information. This data is visible in the Twingate admin console.

## Key Information

- **Uptime/Downtime**: Reflects Connector state as seen by the Controller — not the host machine state. Connector downtime ≠ host machine downtime
- **Time Offset**: Difference between Connector clock and Controller clock; max tolerance is **±5 seconds**
- **STUN Discovery**: Required for peer-to-peer connections; used to determine public IP/port behind NAT layers
- **Hostname**: Reports the process's hostname (e.g., Docker container hostname, not physical host)
- **Public IP**: Most recent IP the Controller observes; may change in multi-path routing setups
- **Private IP**: All private IPs visible to the Connector process; Docker containers report container subnet (e.g., `172.0.0.0/16`), not host IPs

## Gotchas

- **Time offset near ±5s** causes intermittent connection issues — ensure NTP is properly configured on Connector hosts
- **Downtime ≠ host down**: If Connector shows downtime but host is running, review Twingate best practices (misconfiguration, not hardware failure)
- **STUN unavailable** = no peer-to-peer connections possible; clients fall back to relay or fail
- **Docker networking**: Private IP will show container network addresses, not physical machine IPs — don't use for host network troubleshooting
- **Public IP is not static**: In multi-homed or load-balanced setups, the reported IP may rotate

## Configuration Values

| Parameter | Value/Limit |
|-----------|-------------|
| Max time offset | ±5 seconds |
| Docker private subnet (typical) | `172.0.0.0/16` |

## Related Docs

- Twingate Connector Best Practices
- STUN protocol documentation
- NAT traversal documentation
- Twingate Knowledge Base: Time synchronization troubleshooting
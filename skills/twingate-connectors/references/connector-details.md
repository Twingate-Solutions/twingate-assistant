# Connector Details

## Page Title
Connector Details

## Summary
Twingate Connectors report metadata back to the Controller including uptime/downtime, time synchronization, STUN discovery status, and network information. This data is used for monitoring Connector health and troubleshooting connectivity issues.

## Key Information

- **Uptime/Downtime**: Reflects Connector state as seen by the Controller — not the host machine state. Connector can show downtime while the host is running
- **Time Offset**: Difference between Connector clock and Controller clock; maximum tolerance is **±5 seconds**
- **STUN Discovery**: Required for peer-to-peer connections; used to determine public IP/port behind NAT layers
- **Hostname**: Reports the container or process hostname, not necessarily the physical machine hostname
- **Public IP**: Most recently seen IP by the Controller; may change in multi-path routing setups
- **Private IP**: All private IPs visible to the Connector process; Docker containers report `172.0.0.0/16` subnet, not the host machine's IPs

## Gotchas

- Connector downtime ≠ host machine downtime; if host is up but Connector shows downtime, review best practices
- Time offset values near ±5 seconds cause **intermittent connection issues**, not immediate failure
- Negative time offset = Connector clock is behind Controller; positive = Connector clock is ahead
- Docker deployments report container hostname and `172.0.0.0/16` private IPs — physical host addresses are **not visible** from the container
- If STUN discovery is unavailable, peer-to-peer connections **will not work** (falls back to relay)
- Public IP is not static — can change in setups with dynamic routing

## Troubleshooting Reference

| Symptom | Likely Cause | Action |
|---|---|---|
| Connector shows downtime, host is running | Connector process issue | Review best practices doc |
| Intermittent connection drops | Time offset near ±5s limit | Fix NTP/time sync on host |
| No peer-to-peer connections | STUN discovery failing | Check firewall/UDP access |

## Related Docs
- Twingate Connector Best Practices
- Time Synchronization Knowledge Base article
- STUN protocol documentation
- NAT traversal configuration
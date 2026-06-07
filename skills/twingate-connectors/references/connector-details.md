# Connector Details

## Page Title
Connector Details (Metadata & Status Information)

## Summary
Twingate Connectors report metadata back to the Controller including uptime, time sync, network discovery status, and IP addresses. This information is used for monitoring Connector health and troubleshooting connectivity issues.

## Key Information

- **Uptime/Downtime**: Reflects Controller's view of Connector state — not host machine state. Connector can show downtime even if the host is running.
- **Time Offset**: Difference between Connector and Controller clocks. Max tolerance is **±5 seconds**. Values outside this range cause intermittent connection issues.
- **STUN Discovery**: Required for peer-to-peer connections. Without it, Clients cannot establish direct connections to the Connector. Used to determine public IP/port behind NAT.
- **Hostname**: Reports the runtime hostname (e.g., Docker container hostname, not physical host).
- **Public IP**: Most recent IP seen by Controller — may change in multi-path routing setups.
- **Private IP**: All private IPs visible to the Connector process. Docker containers report container network addresses (e.g., `172.0.0.0/16`), not the host machine's IPs.

## Prerequisites
- Connector must be deployed and registered with the Controller
- NTP or equivalent time sync configured on host machine
- STUN access not blocked by firewall

## Configuration Values / Limits

| Parameter | Value |
|-----------|-------|
| Max time offset tolerance | ±5 seconds |
| Docker private subnet (typical) | `172.0.0.0/16` |

## Gotchas

- **Downtime ≠ host down**: Connector showing downtime while host is running indicates a Connector process or network issue, not a machine failure. Check best practices doc.
- **Time offset near limits**: Values approaching ±5s cause *intermittent* issues, not hard failures — harder to diagnose.
- **Docker IP reporting**: Private IP reflects container network, not physical host. Do not use this to identify host machine addresses in containerized deployments.
- **Public IP instability**: Reported public IP may differ across requests if routing varies (e.g., load balancers, multiple egress paths).
- **STUN unavailable**: Blocks all peer-to-peer connections; traffic will fall back through relay (if available) or fail entirely.

## Related Docs
- Twingate Connector Best Practices
- Time Synchronization Troubleshooting (Twingate Knowledge Base)
- STUN protocol documentation
- NAT traversal concepts
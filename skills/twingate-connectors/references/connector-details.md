# Connector Details

## Page Title
Connector Details (Metadata & Diagnostics)

## Summary
Twingate Connectors report metadata to the Controller including uptime/downtime, time offset, STUN discovery status, and network information. This data is used for monitoring Connector health and troubleshooting connectivity issues.

## Key Information

- **Uptime/Downtime**: Reflects Controller's view of Connector state — not the host machine's state. Connector can show downtime while host is running
- **Time Offset**: Difference between Connector clock and Controller clock; max tolerance is **±5 seconds**
- **STUN Discovery**: Required for peer-to-peer connections; used to determine public IP/port behind NAT layers
- **Hostname**: Reports the running process's hostname (e.g., Docker container hostname, not physical host)
- **Public IP**: Most recent IP seen by Controller; may change in multi-path routing setups
- **Private IP**: All private IPs visible to the Connector process; Docker containers report `172.0.0.0/16` subnet, not the physical host's IPs

## Prerequisites
- Connector deployed and registered with a Twingate Controller
- STUN access required for peer-to-peer functionality

## Gotchas

- **Time sync is critical**: Offsets near ±5 seconds cause intermittent connection failures; ensure NTP is configured on the Connector host
- **Docker networking**: Private IP will show container network addresses (`172.x.x.x`), not the physical machine's IP — don't use reported private IP to infer host network location
- **Downtime ≠ host down**: A Connector showing downtime does not mean the machine is offline; check Connector process health and best practices
- **STUN unavailable = no P2P**: If STUN discovery fails, all connections fall back through relays (no direct peer-to-peer)
- **Public IP instability**: In environments with multiple egress paths, public IP may not be stable

## Related Docs
- Connector best practices
- Twingate Knowledge Base: Time synchronization issues
- STUN protocol documentation
- NAT traversal
## Connector Details

Metadata and diagnostics that Twingate Connectors report back to the Controller, visible in the Admin Console Connector management page.

**Reported Fields:**
- **Uptime / Downtime** -- how long the Connector has been online/offline as seen by the Controller (not necessarily the host machine status)
- **Time offset** -- time difference between Connector and Controller; must stay within +/- 5 seconds; values near the limit cause intermittent connection issues; negative = Connector clock is behind
- **STUN discovery** -- whether the Connector can determine its public IP/port for P2P; if unavailable, peer-to-peer connections cannot be established
- **Hostname** -- hostname of the machine running the Connector (may be a Docker container's hostname, not the physical host)
- **Public IP** -- most recent public IP the Controller sees the Connector from; can change if routing varies
- **Private IP** -- all private IPs visible on the Connector's machine; Docker containers report their container network IPs (e.g., 172.x.x.x), not the host machine's IPs

**Troubleshooting Notes:**
- Connector downtime with host running: review connector best practices (firewall, outbound connectivity)
- Time offset near limits: check NTP/clock sync on the Connector host

**Related Docs:**
- /docs/connector-best-practices -- Network requirements and connectivity checks
- /docs/connector-health-checks -- Direct health check commands

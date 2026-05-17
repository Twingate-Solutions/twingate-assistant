# Connector Failures Troubleshooting

## Summary
Covers three main Connector failure scenarios: offline/flapping status, online but can't reach Resources, and online with poor performance. Connectors are gateways to Remote Network Resources; a failed Connector affects all Resources in that network unless a backup Connector exists.

## Key Information
- Connector offline → all Resources in that Remote Network fail
- Admin Console Connector details page shows `Status` and `Time Offset` values
- Time Offset >5 seconds in either direction causes auth token rejection and flapping
- `chronyd` recommended over `ntpd` for clock sync
- Multiple Connectors sharing the same tokens causes conflicts
- Resource addresses/FQDNs are resolved from the **Connector's perspective**, not the client's

## Prerequisites
- Access to Admin Console
- SSH access to Connector host (or `docker exec` for containers)
- Connector software up to date
- Host meets hardware/OS requirements

## Configuration Values

| Item | Value |
|------|-------|
| `TWINGATE_LOG_LEVEL` | `7` (detailed logging) |
| Outbound TCP | Port 443 (Controller + Relay) |
| Outbound TCP | Ports 30000–31000 (Relay fallback) |
| Outbound | UDP/QUIC for HTTP/3 |

## Diagnostic Commands

```bash
# View logs (systemd)
journalctl -u twingate-connector -f

# View logs (Docker)
docker logs <CONTAINER_NAME> -f

# Test TCP connectivity to Resource
nc -zv <RESOURCE_ADDRESS> <PORT>

# Test DNS resolution
nslookup <RESOURCE_FQDN>

# Get Connector's private IP
hostname -I
```

## Error Patterns

| Error | Cause |
|-------|-------|
| `Invalid token` / `failed to get an access token` | Clock drift; check Time Offset in Admin Console |
| `Gone, code 410` | Token/auth issue |
| `too many open files` | `ulimit` file descriptor limit too low |
| `Failed to preconnect a relay listener` + `Connection timed out` | Firewall blocking outbound to Twingate Relay |
| `failed to connect` / `could not be reached` | Connector can't reach Resource on its local network |

## Gotchas
- Clock skew >5s breaks auth even if network is fine — always check Time Offset first when flapping
- Running duplicate Connector instances with same tokens causes silent failures
- Security groups/NSGs must allow Connector's **private IP** to reach Resource ports
- Application-level IP filtering (pg_hba.conf, SSH AllowUsers, WAF) can block Connector even when network is open
- ICMP failures while TCP works = host OS blocking outbound ICMP, not a Twingate issue
- Peer-to-peer failure silently degrades to Relay routing, increasing latency

## Related Docs
- Connector Logging
- Firewall Failures
- Peer-to-peer troubleshooting guide
- Hardware and OS requirements
- Resources configuration
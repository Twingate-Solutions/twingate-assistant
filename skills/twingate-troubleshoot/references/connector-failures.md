# Connector Failures Troubleshooting

## Page Title
Connector Failures

## Summary
Covers three failure scenarios for Twingate Connectors: offline/flapping status, online but unable to reach Resources, and online with poor performance. A failed Connector affects all Resources in its Remote Network unless a backup Connector exists. Diagnostics focus on logs, Admin Console metrics, and network-layer testing.

## Key Information
- Connector offline → all Resources in that Remote Network fail for all users
- Three failure categories: offline/flapping, reachable but Resource access fails, degraded performance
- Traffic routes peer-to-peer when possible; falls back to Relay (higher latency)
- Resource addresses/FQDNs are resolved from the **Connector host's** perspective

## Prerequisites
- Access to Admin Console (Connector details page)
- SSH or `docker exec` access to Connector host
- `nc`, `nslookup`, `hostname` available on host

## Step-by-Step Diagnostics

### Offline/Flapping
1. Check Admin Console → Remote Network → Connector details
   - `Time Offset > 5s` → fix NTP (use `chronyd`, not `ntpd`)
   - Status `Offline` → host down or no internet
2. Enable detailed logging: `TWINGATE_LOG_LEVEL=7`
3. Check logs for error patterns (see table below)
4. Verify only one Connector instance uses a given token set
5. Confirm outbound connectivity to Twingate infrastructure

### Resource Unreachable (Connector Online)
1. SSH into Connector host; test reachability directly:
   ```bash
   nc -zv <RESOURCE_ADDRESS> <PORT>
   nslookup <RESOURCE_FQDN>
   ```
2. Check VPC/VNet routing (peering, transit gateways, route tables)
3. Check cloud security groups / on-prem firewalls between Connector and Resource
4. Check application-level IP allowlists; get Connector IP: `hostname -I`
5. Verify Resource config address/ports match what's actually reachable

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `TWINGATE_LOG_LEVEL` | `7` (detailed logging) |
| Outbound TCP | Port `443` (Controller + Relay) |
| Outbound TCP | Ports `30000–31000` (Relay fallback) |
| Outbound | UDP/QUIC for HTTP/3 |

## Log Commands
```bash
# systemd
journalctl -u twingate-connector -f

# Docker
docker logs <CONTAINER_NAME> -f
```

## Error Reference

| Error | Cause |
|-------|-------|
| `Invalid token` / `failed to get an access token` | Clock drift; `Time Offset > 5s` |
| `Gone, code 410` | Likely token/version issue |
| `too many open files` | `ulimit` (file descriptor limit) too low |
| `Failed to preconnect a relay listener` + `Connection timed out` | Firewall blocking outbound to Relay; no public IPv4 |

## Gotchas
- **Clock skew**: Authentication fails if host clock drifts >5 seconds; use `chronyd`
- **Duplicate tokens**: Multiple Connectors sharing same token set causes conflicts
- **ICMP**: Ping failures while TCP works = host OS blocking outbound ICMP (not Twingate-controlled)
- **Resource address resolution**: FQDN Resources must be resolvable from the Connector host, not the client
- **Port restrictions**: Twingate forwards all TCP/UDP by default; if ports are restricted in Resource config, only those ports forward

## Related Docs
- Firewall Failures
- Connector Logging
- Peer-to-peer troubleshooting guide
- Hardware and OS requirements
- Resources configuration
- Connector software updates
---
source: https://www.twingate.com/docs/connector-failures
type: docs
fetched: 2026-11-08
source_version: 83b5ace2ec9ad480e82b33f4cffe79b1743a07edb54d7ba312c45ed8c323f8c8
trust: official
---

# Connector Failures

## Page Title
Connector Failures — Troubleshooting Guide

## Summary
Covers three failure scenarios for Twingate Connectors: offline/flapping status, online but unable to reach Resources, and online with poor performance. A failed Connector affects all Resources in its Remote Network unless a secondary Connector exists. Diagnostic approach combines Admin Console inspection, host-level testing, and log analysis.

## Key Information
- Clock skew >5 seconds causes `Invalid token` errors and flapping; use `chronyd` (preferred over `ntpd`) on the Connector host
- Multiple Connector instances sharing the same tokens cause conflicts
- Resource addresses/FQDNs are resolved from the **Connector host's** perspective, not the client's
- Peer-to-peer (UDP) failure silently falls back to Relay, increasing latency

## Prerequisites
- Access to Admin Console (Connector details page)
- SSH access to Connector host (or `docker exec` for containers)
- Network tools: `curl`, `nc`, `nslookup`, `hostname`

## Step-by-Step Diagnostics

### Offline/Flapping
1. Check Admin Console → Remote Network → Connector → **Time Offset** (must be <5s)
2. Verify tokens are correct and not regenerated without reconfiguration
3. Confirm only one instance runs per token set
4. Enable verbose logging: set `TWINGATE_LOG_LEVEL=7`
5. Test Controller reachability from Connector host:
   ```
   curl -v --connect-timeout 10 https://<NETWORK_NAME>.twingate.com/api/v1/public_keys
   ```
6. Verify outbound firewall rules (see Configuration Values)

### Cannot Reach Resources
1. SSH into Connector host; test TCP: `nc -zv <RESOURCE_ADDRESS> <PORT>`
2. Test DNS: `nslookup <RESOURCE_FQDN>`
3. Verify routing (VPC peering, transit gateways, subnet route tables)
4. Check cloud security groups (AWS/Azure/GCP) allow inbound from Connector's private IP
5. Check app-level allowlists (`pg_hba.conf`, SSH `AllowUsers`, WAF rules)
6. Get Connector's private IP: `hostname -I`

### Poor Performance
1. Check if peer-to-peer is establishing (see peer-to-peer troubleshooting guide)
2. Review host resource utilization (CPU, memory, bandwidth)
3. Confirm Connector is deployed geographically close to Resources

## Configuration Values
| Parameter | Value | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `7` | Enable detailed logging |
| Outbound TCP | `443` | Controller + Relay communication |
| Outbound TCP | `30000–31000` | Relay fallback (no peer-to-peer) |
| Outbound UDP/QUIC | HTTP/3 | Peer-to-peer + Relay |

## Log Commands
```bash
# systemd
journalctl -u twingate-connector -f

# Docker
docker logs <CONTAINER_NAME> -f
```

## Error Reference
| Error | Cause |
|---|---|
| `failed to get public keys` | Firewall blocking TCP 443 to `*.twingate.com` |
| `Invalid token` | Clock drift on host |
| `too many open files` | `ulimit` file descriptor limit too low |
| `Failed to preconnect a relay listener` | No public IPv4 or firewall blocking Relay ports |

## Gotchas
- Testing Relay reachability does **not** confirm Controller reachability — test both separately
- Relay success ≠ auth success; they use different addresses
- ICMP failures while TCP/UDP succeed = host OS blocking outbound ICMP (not a Twingate setting)
- Port restrictions on a Resource override the default (all TCP/UDP forwarded)

## Related Docs
- Connector Logging
- Firewall Failures
- Peer-to-peer troubleshooting guide
- Hardware and OS requirements
- Connector software updates
- Resources configuration
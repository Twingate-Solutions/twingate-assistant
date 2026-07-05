# Connector Failures Troubleshooting

## Page Title
Connector Failures - Troubleshooting Guide

## Summary
Covers three failure scenarios for Twingate Connectors: offline/flapping status, online but unable to reach Resources, and online with poor performance. Connectors are gateways to Remote Networks—if one fails and no backup exists, all Resources on that network become inaccessible.

## Key Information
- Connector offline = all Resources on that Remote Network fail (unless another Connector covers it)
- Three failure categories: offline/flapping, reachability failures, performance issues
- Resource addresses/FQDNs are resolved **from the Connector's perspective**, not the client's

## Prerequisites
- Access to Admin Console (Connector details page)
- SSH access to Connector host (or `docker exec` for containers)
- Ability to check host firewall, security groups, and network routing

## Step-by-Step Diagnostics

### Offline/Flapping Connector
1. Check Admin Console → Remote Network → Connector details
2. Check **Time Offset** — if >5 seconds, clock drift is causing auth failures; fix with `chronyd`
3. Verify tokens are correct and not duplicated across multiple instances
4. Check logs for error patterns (see table below)
5. Verify outbound connectivity requirements are met

### Cannot Reach Resources
1. SSH into Connector host, test TCP: `nc -zv <RESOURCE_ADDRESS> <PORT>`
2. Test DNS: `nslookup <RESOURCE_FQDN>`
3. Verify network routing (VPC peering, route tables, transit gateways)
4. Check cloud security groups / NSGs / GCP firewall rules
5. Check application-level IP filtering (SSH, PostgreSQL `pg_hba.conf`, RDP, WAF)
6. Get Connector's private IP: `hostname -I` — add to allowlists as needed
7. Verify Resource address/port config in Admin Console matches actual service

### Performance Issues
1. Check if peer-to-peer is establishing (see peer-to-peer troubleshooting guide)
2. Assess Connector host resources (CPU, memory, bandwidth)
3. Check geographic proximity of Connector to Resources
4. For ICMP failures only: verify host OS allows outbound ICMP

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `TWINGATE_LOG_LEVEL` | `7` (detailed logging) |
| Outbound TCP | Port 443 (Controller + Relay) |
| Outbound TCP | Ports 30000–31000 (Relay fallback) |
| Outbound | UDP/QUIC for HTTP/3 |

**Log commands:**
- systemd: `journalctl -u twingate-connector -f`
- Docker: `docker logs <CONTAINER_NAME> -f`

## Error Reference

| Error | Cause |
|-------|-------|
| `Invalid token` / `failed to get an access token` | Clock drift — check Time Offset in Admin Console |
| `Gone, code 410` | Token/auth issue |
| `too many open files` | `ulimit` (file descriptors) too low on host |
| `Failed to preconnect a relay listener` + `Connection timed out` | Firewall blocking outbound to Twingate Relay |
| `failed to connect` / `could not be reached` | Connector cannot route to Resource |

## Gotchas
- **Clock drift** is a common hidden cause — Time Offset >5s breaks auth entirely
- Running **multiple Connectors with same tokens** causes conflicts
- `chronyd` preferred over `ntpd` for time sync
- Peer-to-peer failure silently falls back to Relay, increasing latency
- ICMP/ping failures don't indicate TCP failure — controlled at host OS level, not Twingate

## Related Docs
- Connector Logging
- Firewall Failures
- Peer-to-peer troubleshooting guide
- Resources configuration
- Hardware and OS requirements
- Connector software updates
# Connector Failures Troubleshooting

## Page Title
Connector Failures - Troubleshooting Guide

## Summary
Covers three failure scenarios for Twingate Connectors: offline/flapping status, online but unable to reach Resources, and online with poor performance. Connectors are gateways to Remote Network Resources; a failed Connector affects all Resources in that network unless a backup Connector exists.

## Key Information
- Connector offline → all Resources in that Remote Network fail
- Clock skew >5 seconds causes token rejection and flapping
- `chronyd` recommended over `ntpd` for time sync
- Resource addresses resolve from the **Connector's** perspective, not the client's
- Default: all TCP/UDP ports forwarded unless port restrictions configured on Resource

## Prerequisites
- Access to Admin Console (Connector details page)
- SSH access to Connector host (or `docker exec` for containers)
- Correct tokens configured; each token set used by only one Connector instance

## Step-by-Step Diagnostics

### Offline/Flapping
1. Check Admin Console → Remote Network → Connector details
2. Verify **Time Offset** < 5 seconds; if not, fix NTP (`chronyd`)
3. Confirm tokens are current and not duplicated across instances
4. Check logs for error patterns (see table below)
5. Verify outbound connectivity requirements are met

### Cannot Reach Resources
1. SSH into Connector host; test TCP: `nc -zv <RESOURCE_ADDRESS> <PORT>`
2. Test DNS: `nslookup <RESOURCE_FQDN>`
3. Check routing (VPC peering, transit gateways, route tables)
4. Check cloud security groups / NSGs / on-prem firewalls
5. Check app-level IP allowlists; get Connector IP: `hostname -I`
6. Verify Resource address/port config in Admin Console matches actual service

### Poor Performance
1. Check if peer-to-peer is establishing (see peer-to-peer troubleshooting guide)
2. Assess Connector host resources (CPU, memory, bandwidth)
3. Consider deploying additional Connectors on same Remote Network for load balancing

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
| `Invalid token` / `failed to get an access token` | Clock drift; check Time Offset in Admin Console |
| `Gone, code 410` | Connector token/version issue |
| `too many open files` | `ulimit` file descriptor limit too low |
| `Failed to preconnect a relay listener` + `Connection timed out` | Firewall blocking outbound to Relay; no public IPv4 |
| `failed to connect` / `could not be reached` | Network/firewall between Connector and Resource |

## Gotchas
- Running **multiple Connectors with the same tokens** causes conflicts
- ICMP (ping) failures while TCP works = host OS blocking outbound ICMP (not Twingate-controlled)
- Resource FQDN must resolve from Connector host, not client
- Security groups must allow Connector's **private IP** to reach Resource instances

## Related Docs
- Connector Logging
- Firewall Failures
- Resources configuration
- Peer-to-peer troubleshooting guide
- Hardware and OS requirements
- Connector software updates
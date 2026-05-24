# Connector Failures Troubleshooting

## Summary
Covers three failure scenarios for Twingate Connectors: offline/flapping status, online but unable to reach Resources, and online but poor performance. Connectors are critical gateways; if one fails, all Resources on that Remote Network are inaccessible unless a backup Connector exists.

## Key Information
- Offline Connector = entire Remote Network affected for all users
- Time Offset >5 seconds causes authentication token rejection and flapping
- `chronyd` recommended over `ntpd` for time sync
- Same tokens used by multiple Connector instances causes conflicts
- Resource addresses/FQDNs are resolved from the **Connector's perspective**, not the client's

## Prerequisites
- Access to Admin Console (Connector details page)
- SSH or `docker exec` access to Connector host
- Correct Connector tokens (regenerate if needed)

## Diagnostic Steps

### Offline/Flapping
1. Check Admin Console → Remote Network → Connector details for Status and **Time Offset**
2. If Time Offset >5s, fix NTP on host (`chronyd`)
3. Verify tokens are correct and only one instance uses each token set
4. Check logs for error patterns (see table below)
5. Verify outbound connectivity requirements

### Cannot Reach Resources
1. SSH into Connector host; test TCP: `nc -zv <RESOURCE_ADDRESS> <PORT>`
2. Test DNS: `nslookup <RESOURCE_FQDN>`
3. Verify routing between Connector subnet and Resource subnet (VPC peering, route tables)
4. Check cloud security groups/NSGs/firewall rules for inbound traffic from Connector IP
5. Check app-level IP allowlists (SSH, PostgreSQL `pg_hba.conf`, RDP, WAFs)
6. Get Connector private IP: `hostname -I`
7. Confirm Resource address/port config in Admin Console matches actual service

### Poor Performance
1. Check if peer-to-peer is failing (forcing relay routing) → see P2P troubleshooting guide
2. Review Connector host resources (CPU, memory, bandwidth)
3. Consider deploying additional Connectors on same Remote Network for load balancing

## Configuration Values

| Variable | Value | Purpose |
|----------|-------|---------|
| `TWINGATE_LOG_LEVEL` | `7` | Enable detailed logging |

**Log commands:**
```bash
journalctl -u twingate-connector -f   # systemd
docker logs <CONTAINER_NAME> -f        # Docker
```

**Required outbound ports:**
- TCP 443 (Controller + Relay)
- TCP 30000–31000 (Relay fallback)
- UDP/QUIC for HTTP/3

## Error Reference

| Error | Cause |
|-------|-------|
| `Invalid token` / `failed to get an access token` | Clock drift; check Time Offset in Admin Console |
| `Gone, code 410` | Token/auth issue |
| `too many open files` | Host `ulimit` (file descriptor limit) too low |
| `Failed to preconnect a relay listener` + `Connection timed out` | Outbound firewall blocking Relay ports |
| `failed to connect` / `could not be reached` | Network path issue between Connector and Resource |

## Gotchas
- ICMP/ping failures while SSH/HTTP work = host OS blocking outbound ICMP (not a Twingate issue)
- Connector in different VPC/subnet than Resource with no route = silent failure (Connector shows Online)
- Port restrictions on Resource config override default all-TCP/UDP forwarding

## Related Docs
- Firewall Failures
- Connector Logging
- Peer-to-peer troubleshooting guide
- Hardware and OS requirements
- Resources configuration
- Connector software updates
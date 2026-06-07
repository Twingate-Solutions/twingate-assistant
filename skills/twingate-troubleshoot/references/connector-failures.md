# Connector Failures Troubleshooting

## Summary
Covers three Connector failure scenarios: offline/flapping status, online but unable to reach Resources, and online with poor performance. Connectors failing affects all Resources in their Remote Network unless a backup Connector exists.

## Key Information
- Offline Connector = all Resources in that Remote Network unreachable for all users
- Two Connectors per Remote Network recommended for redundancy
- Resource addresses/FQDNs are resolved from the **Connector's perspective**, not the client's

## Failure Scenario 1: Offline or Flapping

### Common Causes & Fixes
- **Clock skew**: Time Offset >5 seconds in Admin Console → run `chronyd` (preferred over `ntpd`) on host
- **Invalid tokens**: Regenerate and reconfigure; never run multiple Connectors with same tokens
- **Outdated software**: Update Connector to latest version
- **Outbound firewall blocking**: Requires TCP 443, TCP 30000-31000, UDP/QUIC for HTTP/3

### Log Commands
```bash
# systemd
journalctl -u twingate-connector -f

# Docker
docker logs <CONTAINER_NAME> -f
```

### Log Error Reference
| Error | Cause |
|-------|-------|
| `Invalid token` / `failed to get an access token` | Clock drift |
| `Gone, code 410` | Token/auth issue |
| `too many open files` | `ulimit` too low |
| `Failed to preconnect a relay listener` + timeout | No outbound connectivity to Relay |

## Failure Scenario 2: Online but Cannot Reach Resources

### Diagnostic Commands (run on Connector host)
```bash
# Test TCP connectivity
nc -zv <RESOURCE_ADDRESS> <PORT>

# Test DNS resolution
nslookup <RESOURCE_FQDN>

# Get Connector's private IP
hostname -I
```

### Checklist
- [ ] Connector host can route to Resource subnet (VPC peering, transit gateways, route tables)
- [ ] Cloud security groups allow inbound traffic from Connector IP on required ports (AWS/Azure/GCP)
- [ ] Application-level IP allowlists include Connector's private IP (`pg_hba.conf`, SSH `AllowUsers`, WAF rules, etc.)
- [ ] Resource address/FQDN in Admin Console matches what's reachable from Connector
- [ ] Port restrictions on Resource config match what the service listens on (default: all TCP/UDP)

## Failure Scenario 3: Poor Performance

### Common Causes
- Peer-to-peer not establishing → traffic relayed (higher latency) — check UDP connectivity on both Client and Connector networks
- Connector geographically distant from Resources → deploy in same region/VPC/subnet
- Host resource constraints (CPU/memory/bandwidth) → scale up or add Connectors for load balancing

### ICMP Note
Ping failures while SSH/HTTP work = host OS blocking outbound ICMP (not a Twingate setting)

## Configuration Values
| Setting | Value |
|---------|-------|
| `TWINGATE_LOG_LEVEL` | `7` (detailed logging) |
| Required outbound TCP | `443`, `30000-31000` |
| Required outbound | UDP/QUIC (HTTP/3) |
| Max clock skew allowed | 5 seconds |

## Gotchas
- Running multiple Connectors with identical tokens causes conflicts — each Connector needs unique tokens
- `ntpd` is less reliable than `chronyd` for preventing clock drift
- Default port behavior forwards all TCP/UDP; port restrictions on Resource config silently block other ports

## Related Docs
- Connector Logging
- Firewall Failures
- Peer-to-peer troubleshooting guide
- Hardware and OS requirements
- Resources configuration
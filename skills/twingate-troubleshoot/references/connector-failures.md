---
source: https://www.twingate.com/docs/connector-failures
type: docs
fetched: 2026-08-14
source_version: d2f8d0e5d857e53f733b53fb0f7bf32e4fe67978e1dd5f2dd5239d5aa6c3ab1d
---

# Connector Failures - Troubleshooting Guide

## Summary
Covers three failure scenarios for Twingate Connectors: offline/flapping status, online but cannot reach Resources, and online with poor performance. Connectors are gateways to Remote Networks; a failed Connector impacts all Resources in that network unless a redundant Connector exists.

## Key Information
- Connector offline = all Resources in that Remote Network fail for all users
- Multiple Connectors on same Remote Network provide redundancy/load balancing
- Resource addresses are resolved from the **Connector's perspective**, not the client

## Failure Scenario 1: Offline or Flapping

### Common Causes & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `Invalid token` | Clock drift >5 seconds | Enable `chronyd` on host |
| `too many open files` | Low `ulimit` file descriptor limit | Increase ulimit on host |
| `Failed to preconnect a relay listener` | Firewall blocking outbound ports | Open TCP 443, 30000-31000 |
| `Gone, code 410` | Token conflict or stale instance | Ensure single Connector per token set |

### Diagnostic Steps
1. Check Admin Console → Remote Network → Connector details
2. Verify **Time Offset** < 5 seconds (clock skew causes auth failures)
3. Confirm tokens are current (regenerated tokens require reconfiguration)
4. Verify only **one** Connector instance runs per token set
5. Check logs:
   - systemd: `journalctl -u twingate-connector -f`
   - Docker: `docker logs <CONTAINER_NAME> -f`

### Required Outbound Ports
- TCP 443 (Controller + Relay)
- TCP 30000-31000 (Relay fallback)
- UDP/QUIC for HTTP/3

## Failure Scenario 2: Online but Cannot Reach Resources

### Diagnostic Steps
1. SSH into Connector host (or `docker exec`) and test directly:
   ```bash
   nc -zv <RESOURCE_ADDRESS> <PORT>      # TCP connectivity
   nslookup <RESOURCE_FQDN>               # DNS resolution
   hostname -I                            # Get Connector's private IP
   ```
2. Check network segmentation (VPC peering, transit gateways, route tables)
3. Check cloud security groups (AWS/Azure/GCP) — must allow inbound from Connector's IP
4. Check application-level IP allowlists (SSH, PostgreSQL `pg_hba.conf`, RDP, WAF rules)
5. Verify Resource address/ports in Admin Console match actual service

## Failure Scenario 3: Poor Performance

### Common Causes
- Peer-to-peer not established → traffic relaying through Twingate Relay (higher latency)
- Connector geographically distant from Resources
- Connector host resource-constrained (CPU/memory/bandwidth)

### Fixes
- Debug P2P with peer-to-peer troubleshooting guide
- Deploy Connectors in same region/VPC as Resources
- Scale up host or add Connectors to same Remote Network for load balancing

## Configuration Values
- `TWINGATE_LOG_LEVEL=7` — Enable detailed logging

## Gotchas
- **Clock drift** is a frequent silent failure cause — always check Time Offset first
- Running **duplicate Connectors with same tokens** causes conflicts
- ICMP (ping) failures while TCP works = host OS blocking outbound ICMP (not Twingate)
- If `nc`/`nslookup` fail from Connector host, problem is network-level, not Twingate

## Related Docs
- Firewall configuration
- Peer-to-peer troubleshooting guide
- Connector logging
- Hardware/OS requirements
- Resource configuration
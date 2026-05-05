## Connector Failures (Troubleshooting)

Diagnostic playbook for **three Connector failure modes**: offline/flapping, online-but-can't-reach-Resources, and online-but-poor-performance.

### Failure Mode 1: Connector Offline or Flapping

**Symptoms:**
- All Resources in a Remote Network unreachable
- Admin Console shows status `Offline` or alternating Online/Offline
- Connector logs: `Invalid token`, `failed to get an access token`, `Gone, code 410`, `Failed to preconnect a relay listener` with `Connection timed out`

**Diagnose via Admin Console -> Connector detail page:**

| Indicator | Cause |
|---|---|
| Status: Offline | Host down or no internet |
| **Time Offset > +/-5 sec** | **Clock drift** -- single most common cause of flapping; auth tokens get rejected |

**Time Offset Fix**: confirm host runs a time sync service. **`chronyd` recommended over `ntpd`**. Host-level config, not Twingate.

**Other checks:**
- Tokens correct? (regenerated tokens require Connector reconfigure)
- Only ONE Connector instance running with each token pair (running multiples with same tokens causes conflicts)
- Connector software up to date (very old versions blocked)
- Host meets [hardware/OS requirements](/docs/connector-best-practices)

**Connector Logs (set `TWINGATE_LOG_LEVEL=7` for detail):**
```
journalctl -u twingate-connector -f          # systemd
docker logs <container> -f                   # Docker
```

| Error Pattern | Cause |
|---|---|
| `Invalid token` | Clock drift (check Time Offset) |
| `too many open files` | Host file descriptor limit too low; raise `ulimit` |
| `Failed to preconnect a relay listener` | Outbound block to Twingate Relay infrastructure |

**Outbound prerequisites:**
- TCP 443 to `*.twingate.com` (Controller + Relay)
- TCP 30000-31000 (Relay fallback)
- UDP + QUIC (HTTP/3) -- ALL destinations

### Failure Mode 2: Connector Online but Cannot Reach Resources

**Symptoms:**
- Connector shows Online; specific Resources fail for users
- Connector logs: `failed to connect`, `could not be reached` for specific Resource addresses
- Some Resources work, others don't

**Test from Connector host (SSH or `docker exec`):**
```
nc -zv <RESOURCE_ADDRESS> <PORT>     # TCP reachability
nslookup <RESOURCE_FQDN>             # DNS resolution
```

If these fail FROM THE CONNECTOR HOST, problem is in the network path (not in Twingate).

**Check:**
1. **Network segmentation** -- Connector + Resource in same VPC/VNet, or peering/transit gateway between
2. **Route tables** include route to Resource's subnet
3. **Cloud security groups / NSGs** -- allow inbound from Connector's private IP on required ports
4. **Application-layer IP filtering**:
   - SSH: `AllowUsers`, `AllowGroups`, `iptables`, `ufw`
   - PostgreSQL: `pg_hba.conf` source IP rules
   - RDP: Windows Firewall + NLA
   - Web apps: WAF, reverse proxy ACLs
5. **Resource configuration** -- FQDN/IP correct, ports match the actual service ports

**Critical**: Resource addresses are resolved **from the Connector's perspective**. FQDNs must be resolvable by the Connector's DNS; IPs must be routable from the Connector's network.

Find Connector's private IP: `hostname -I` on the Connector host.

### Failure Mode 3: Online but Performance Is Poor

**Symptoms:** slow / unreliable connections, Connector healthy

**Causes:**
- **P2P not establishing** -- traffic falls back to Relay (higher latency). See /docs/troubleshooting-p2p
- **Connector is geographically far** from Resources -- deploy Connectors in same region/VPC as Resources
- **Resource-constrained Connector host** -- review hardware recommendations; scale up or add Connectors

**ICMP/ping**: if ping fails to Resources but other connections (SSH/HTTP) work -- check the Connector host's outbound ICMP rules; this is host-level, not Twingate.

### Decision Notes

- **Always run 2+ Connectors per Remote Network** -- single Connector failure = total outage for that Remote Network
- **Time Offset > 5s = silent kill** -- check this FIRST when triaging flapping
- **Test from the Connector host** -- it's the source of truth for "is the path open?"
- For AWS: NAT Gateways often break P2P; consider self-hosted NAT instances or Marketplace alternatives

### Related Docs

- /docs/connector-details, /docs/connector-real-time-logs -- Connector inspection
- /docs/connector-best-practices -- Hardware + outbound requirements
- /docs/troubleshooting-p2p -- P2P performance issues
- /docs/firewall-failures -- Sibling: outbound firewall issues
- /docs/dns-failures -- DNS issues (sibling failure class)
- /docs/how-to-troubleshoot -- Top-level troubleshooting decision tree

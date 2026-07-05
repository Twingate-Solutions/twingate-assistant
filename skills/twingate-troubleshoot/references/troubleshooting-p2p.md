# Troubleshooting Peer-to-Peer Connections

## Summary
Twingate uses NAT traversal for peer-to-peer connections between Clients and Connectors. Several network conditions can prevent P2P from working, requiring no open inbound firewall ports but specific outbound UDP/QUIC capabilities. When P2P fails, Twingate falls back to relay transport.

## Key Information
- P2P requires no inbound firewall ports, but needs specific outbound UDP/QUIC access
- Four root causes for P2P failure: UDP/QUIC blocked, IP/port restrictions, double NAT, incompatible NAT type
- Both Client AND Connector must support endpoint-independent NAT for P2P to work
- QUIC issues are almost never on the Client side — start troubleshooting at the Connector

## Prerequisites
- Outbound UDP/QUIC unrestricted on both Client and Connector sides
- Single NAT device in path (no double NAT)
- Endpoint-independent NAT on both ends
- Review [network prerequisites doc](https://www.twingate.com/docs) before troubleshooting

## Diagnostic Steps

### 1. Verify UDP/QUIC Not Blocked
- Test QUIC support at `https://quic.nginx.org/`
- Start with Connector-side analysis (QUIC rarely blocked client-side)

### 2. Verify Outbound Rules
- Connectors must send UDP to **all IP addresses** (client public IPs are dynamic)
- UDP must be allowed to **any port** (NAT devices assign random ports)

### 3. Check for Double NAT
- Double NAT: two NAT devices in front of a single device
- Common when user adds own router on top of ISP-provided equipment
- UDP's stateless nature makes double NAT incompatible with P2P

### 4. Check NAT Type

**Connector side** — Admin Console → Connectors → verify `STUN Discovery: Available`

**Client side** — search logs for:
```
[INFO] [libsdwan] stun_nat_type: endpoint-independent
```
Required value: `endpoint-independent`

## Configuration Values / Diagnostics

| Check | Location | Expected Value |
|-------|----------|----------------|
| Connector NAT type | Admin Console → Connectors | `STUN Discovery: Available` |
| Client NAT type | Client logs, `stun_nat_type` | `endpoint-independent` |

## Gotchas
- **AWS NAT Gateways** are incompatible — known to break NAT traversal
- Endpoint-dependent NAT assigns different ports per destination, making the Connector's port unpredictable to Clients
- Double NAT creates complex/brittle port mappings that break P2P

## Known Incompatibilities & Workarounds

| Issue | Workaround |
|-------|-----------|
| AWS NAT Gateway | Use Cohesive cloud NAT, fck-nat, alterNAT, or custom NAT gateway |
| Sonicwall | Enable "Consistent NAT" |
| PaloAlto | Configure "Persistent NAT" |
| OPNSense | Add Outbound NAT rule with endpoint-independent config |

## Related Docs
- [How NAT traversal works](https://www.twingate.com/docs) — deep dive on mechanics
- [Network prerequisites](https://www.twingate.com/docs) — required outbound rules
- [Relay transport](https://www.twingate.com/docs) — fallback mechanism
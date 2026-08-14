---
source: https://www.twingate.com/docs/troubleshooting-p2p
type: docs
fetched: 2026-08-14
source_version: 9d79915787babf9b0877b4886d24729f4b0532a696326cbf5cf52c563709366d
---

# Troubleshooting Peer-to-Peer Connections

## Page Title
How to Troubleshoot Peer-to-Peer (P2P) Connections

## Summary
Twingate uses two transport mechanisms: peer-to-peer (via NAT traversal) and relays. Neither requires open inbound firewall ports. P2P failures are caused by four main issues: blocked UDP/QUIC, restricted outbound rules, double NAT, or incompatible NAT types.

## Key Information

- No inbound firewall ports required for either transport mechanism
- P2P uses UDP/QUIC via NAT traversal; relays route through intermediate servers
- Both Client and Connector must support endpoint-independent NAT for P2P to work
- Falling back to relay transport is automatic when P2P fails

## Four Root Causes of P2P Failure

1. **UDP/QUIC blocked** — Check Connector side first; QUIC is rarely blocked client-side
2. **Outbound IP/port restrictions** — Connector must send UDP to all IPs/any port; Client must do the same
3. **Double NAT** — Two NAT devices in front of Client or Connector breaks stateless UDP traversal
4. **Incompatible NAT type** — Endpoint-dependent NAT assigns different ports per destination, breaking hole-punching

## Diagnostics

### Check QUIC support
Visit `https://quic.nginx.org/` from the affected machine/network.

### Check Connector NAT type
In Admin Console → Connectors → verify **STUN Discovery** shows **Available**.

### Check Client NAT type
Search Client logs for:
```
[INFO] [libsdwan] stun_nat_type: endpoint-independent
```
Any value other than `endpoint-independent` indicates incompatible NAT.

## Prerequisites
- UDP and QUIC must be unblocked on both Client and Connector networks
- Outbound UDP to all IP addresses and all ports must be permitted on both sides
- Single NAT device in front of each endpoint (no double NAT)
- Endpoint-independent NAT on both sides

## Known Incompatibilities & Workarounds

| Issue | Workaround |
|---|---|
| AWS NAT Gateways | Use [Cohesive Cloud NAT](https://cohesivenetworks.com/), [fck-nat](https://github.com/AndrewGuenther/fck-nat), [alterNAT](https://github.com/1debit/alternat), or build your own |
| SonicWall | Enable "Consistent NAT" |
| Palo Alto | Configure "Persistent NAT" |
| OPNSense | Add Outbound NAT rule for endpoint-independent mapping |

## Gotchas

- Connectors behind AWS NAT Gateways **will not** support P2P without a workaround
- Double NAT is common when users add personal routers on top of ISP-provided equipment
- Endpoint-dependent NAT silently breaks P2P — the Connector's reported port differs between Relay and Client communication, so hole-punching never succeeds
- QUIC blocking by enterprise firewalls is a frequent overlooked cause

## Related Docs
- [How NAT traversal works](https://www.twingate.com/docs/how-nat-traversal-works)
- [Connector network requirements](https://www.twingate.com/docs/connector-requirements)
- Relay transport documentation
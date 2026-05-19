# Troubleshooting Peer-to-Peer Connections

## Summary
Twingate uses NAT traversal for peer-to-peer connections between Clients and Connectors. Four primary conditions can prevent P2P from working: blocked UDP/QUIC, blocked IP/port ranges, double NAT, or incompatible NAT types. When P2P fails, Twingate falls back to relay transport.

## Key Information
- No inbound firewall ports required for either P2P or relay transport
- P2P uses QUIC (UDP-based) for NAT traversal
- Both Client AND Connector must meet all requirements for P2P to work
- Failure to establish P2P results in fallback to relay (not a broken connection)

## Four Root Causes

### 1. UDP/QUIC Blocked
- QUIC runs over UDP; blocking either breaks NAT traversal
- More commonly blocked on Connector side than Client side
- **Test**: Visit `https://quic.nginx.org/` to verify QUIC support on a given machine/network

### 2. Outbound Rules Too Restrictive
- Connectors must send UDP to **all IP addresses** (Client IPs are not predictable)
- Both sides must allow UDP to **any port** (NAT devices assign random ports)
- Verify prerequisites documented in the network requirements article

### 3. Double NAT
- Two NAT devices in front of a single Client/Connector
- Common when users add their own router on top of ISP-provided equipment
- UDP's stateless nature makes multi-layer NAT mappings brittle and unreliable

### 4. Incompatible NAT Type
- Requires **endpoint-independent NAT** on both sides
- Endpoint-dependent NAT assigns different ports per destination, breaking port discovery
- **Check Connector**: Admin Console → Connector details → `STUN Discovery` must show `Available`
- **Check Client**: Search logs for `stun_nat_type: endpoint-independent`

## Known Incompatible Devices
| Device | Issue |
|--------|-------|
| AWS NAT Gateways | Not NAT traversal-friendly |

### AWS NAT Gateway Workarounds
- [Cohesive's cloud NAT](https://cohesive.net/)
- [fck-nat](https://github.com/AndrewGuenther/fck-nat)
- [alterNAT](https://github.com/1debit/alternat)
- Build your own NAT gateway

## Firewall Configuration for Endpoint-Independent NAT
| Firewall | Setting |
|----------|---------|
| SonicWall | "Consistent NAT" configuration |
| PaloAlto | "Persistent NAT" implementation |
| OPNSense | Outbound NAT rule |

## Diagnostic Steps
1. Test QUIC at `https://quic.nginx.org/` on Connector host
2. Verify outbound UDP rules allow all IPs and all ports
3. Check for double NAT on network topology (especially Client side)
4. Admin Console: confirm Connector shows `STUN Discovery: Available`
5. Client logs: confirm `stun_nat_type: endpoint-independent`

## Gotchas
- Start debugging on the Connector side first (QUIC blocking rarely occurs on Client side)
- Both endpoints must independently satisfy all requirements — one incompatible side blocks P2P
- Double NAT most commonly appears on Client side when users add home routers behind ISP equipment
- Endpoint-dependent NAT silently breaks P2P with no obvious error

## Related Docs
- How NAT traversal works (Twingate internal article)
- Twingate network/firewall prerequisites article
- Firewall vendor docs for consistent/persistent NAT configuration
# Troubleshooting Peer-to-Peer Connections

## Summary
Twingate uses NAT traversal for peer-to-peer (P2P) connections between Clients and Connectors. Several network conditions can prevent P2P from working, including blocked UDP/QUIC, restrictive outbound rules, double NAT, or incompatible NAT types. Relay transport is the fallback when P2P fails.

## Key Information
- P2P and Relay are the two transport mechanisms; neither requires inbound firewall ports opened
- P2P uses NAT traversal over UDP/QUIC
- Both Client and Connector must support endpoint-independent NAT for P2P to work
- QUIC is rarely blocked on Client side; start troubleshooting on Connector side

## Four Root Causes of P2P Failure

1. **UDP/QUIC blocked** — on either Client or Connector side
2. **Outbound IP/port restrictions** — Connectors must send UDP to any IP/any port; Clients similarly
3. **Double NAT** — two NAT devices in front of Client or Connector breaks stateless UDP traversal
4. **Incompatible NAT type** — endpoint-dependent NAT assigns different ports per destination, breaking traversal

## Diagnostic Steps

### 1. Verify QUIC/UDP Not Blocked
- Test QUIC support: visit `https://quic.nginx.org/`
- Prioritize checking Connector-side firewall first

### 2. Verify Outbound Rules
- Connectors must allow UDP to **all IP addresses** and **any port**
- Clients need same outbound UDP flexibility
- Confirm prerequisites from Twingate network requirements doc

### 3. Check for Double NAT
- Occurs when two NAT devices exist in front of a device (e.g., ISP router + personal router)
- Double NAT on Client side typically prevents P2P entirely

### 4. Check NAT Type
**Connector side (Admin Console):**
- Navigate to Connectors → verify `STUN Discovery` shows `Available`

**Client side (logs):**
```
[INFO] [libsdwan] stun_nat_type: endpoint-independent
```
- Required value: `endpoint-independent`
- `endpoint-dependent` = P2P will fail

## Configuration Values
| Check | Location | Required Value |
|-------|----------|----------------|
| STUN Discovery | Admin Console → Connectors | `Available` |
| `stun_nat_type` | Client logs | `endpoint-independent` |

## Known Incompatibilities & Workarounds

**AWS NAT Gateways** — incompatible NAT type. Workarounds:
- [Cohesive's cloud NAT](https://cohesivenetworks.com/)
- [fck-nat](https://github.com/AndrewGuenther/fck-nat)
- [alterNAT](https://github.com/1debit/alternat)
- Build custom NAT gateway

**Enterprise Firewalls** — can configure endpoint-independent NAT:
- **SonicWall**: Enable "Consistent NAT"
- **PaloAlto**: Implement "persistent NAT"
- **OPNSense**: Add outbound NAT rule with endpoint-independent setting

## Gotchas
- Both **Client AND Connector** must be behind endpoint-independent NAT — one incompatible side breaks P2P
- Double NAT is most common on Client side (ISP modem + personal router)
- P2P failure silently falls back to Relay; users may not notice degraded performance until investigated
- QUIC blocked by default on some enterprise firewalls — often overlooked

## Related Docs
- [How NAT traversal works](https://www.twingate.com/docs/how-nat-traversal-works)
- [Twingate network requirements](https://www.twingate.com/docs/connector-requirements)
- Firewall-specific NAT configuration guides (SonicWall, PaloAlto, OPNSense)
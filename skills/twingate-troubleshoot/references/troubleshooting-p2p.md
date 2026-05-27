# Troubleshooting Peer-to-Peer Connections

## Summary
Twingate uses NAT traversal for peer-to-peer (P2P) connections between Clients and Connectors, requiring no open inbound firewall ports. Four main conditions can prevent P2P connections from working. When P2P fails, traffic falls back to Relay transport.

## Key Information
- P2P uses UDP/QUIC for NAT traversal
- No inbound ports need to be opened on either side
- Both Client and Connector must support endpoint-independent NAT
- Failure causes fallback to Relay (not a hard failure, but impacts performance)

## Four Root Causes of P2P Failure

### 1. UDP/QUIC Blocked
- QUIC (UDP-based) is required for NAT traversal
- Overzealous firewalls often block QUIC by default
- Start by checking the **Connector side** (Client side rarely blocks QUIC)
- **Test:** Visit `https://quic.nginx.org/` to verify QUIC support

### 2. Outbound Rules Too Restrictive
- Connectors must send UDP packets to **any IP address** (client IPs are unknown in advance)
- Outbound rules must allow UDP to **any port** (NAT devices assign random ports)
- Verify prerequisites documented in Twingate network requirements

### 3. Double NAT
- Occurs when two NAT devices exist in front of a Client or Connector
- Common when users add their own router on top of ISP-provided equipment
- UDP's stateless nature makes multi-layer NAT mappings brittle and unreliable
- Generally breaks P2P entirely

### 4. Incompatible NAT Type (Endpoint-Dependent NAT)
- Required: **Endpoint-independent NAT** on BOTH Client and Connector sides
- Problem: Endpoint-dependent NAT assigns different public ports per destination, so the Client cannot predict the correct Connector port

## Verification Steps

**Check Connector NAT type:**
- Admin Console → Connectors → verify `STUN Discovery` shows `Available`

**Check Client NAT type:**
- Search Client logs for:
```
[INFO] [libsdwan] stun_nat_type: endpoint-independent
```

## Known Incompatibilities & Workarounds

| Device | Issue | Workaround |
|--------|-------|------------|
| AWS NAT Gateway | Incompatible NAT type | Use Cohesive Cloud NAT, fck-nat, alterNAT, or build custom NAT gateway |

## Firewall Configuration for Endpoint-Independent NAT

| Firewall | Setting |
|----------|---------|
| SonicWall | Enable "Consistent NAT" |
| Palo Alto | Implement "Persistent NAT" |
| OPNSense | Add Outbound NAT rule |

## Gotchas
- Double NAT is most common on the **Client side** (user-added router + ISP router)
- AWS NAT Gateways are explicitly incompatible — requires third-party replacement
- Both ends must have endpoint-independent NAT; one incompatible side breaks P2P
- QUIC blocking is more common on Connector (corporate/cloud network) side than Client side

## Related Docs
- How NAT traversal works (Twingate internal article)
- Twingate network requirements/prerequisites
- Relay transport documentation
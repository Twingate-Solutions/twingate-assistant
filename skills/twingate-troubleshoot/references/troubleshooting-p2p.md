# Troubleshooting Peer-to-Peer Connections

## Summary
Twingate uses NAT traversal for peer-to-peer connections between Clients and Connectors. Four main conditions prevent P2P from working: blocked UDP/QUIC, blocked outbound IPs/ports, double NAT, or incompatible NAT types. No inbound firewall ports are required for either P2P or relay transport.

## Key Information
- P2P uses UDP/QUIC for NAT traversal; neither side needs open inbound ports
- Both Client and Connector must be behind **endpoint-independent NAT** for P2P to work
- Relay transport is the fallback when P2P fails
- QUIC is more commonly blocked on Connector side than Client side

## Four Root Causes (in order)

### 1. UDP/QUIC Blocked
- Verify QUIC is not blocked on either side (start with Connector side)
- Test tool: https://quic.nginx.org/

### 2. Outbound Rules Blocking Traffic
- Connectors must send UDP to **any IP address and any port** (Client public IPs are unknown in advance, ports are random)
- Verify prerequisites per [network requirements docs]

### 3. Double NAT
- Two NAT devices in front of a single device breaks P2P
- Common when users add personal routers on top of ISP equipment
- UDP is stateless—multiple NAT layers create unmaintainable port mappings

### 4. Incompatible NAT Type
- Requires **endpoint-independent NAT** on both sides
- **Endpoint-dependent NAT** assigns different ports per destination, breaking P2P

## Verification Steps

**Check Connector NAT type:**
- Admin Console → Connectors → verify `STUN Discovery` shows `Available`

**Check Client NAT type:**
- Search Client logs for:
```
[INFO] [libsdwan] stun_nat_type: endpoint-independent
```

## Known Incompatibilities & Workarounds

| Device | Issue | Fix |
|--------|-------|-----|
| AWS NAT Gateway | Incompatible NAT type | Use Cohesive Cloud NAT, fck-nat, alterNAT, or custom NAT gateway |
| SonicWall | Default NAT type | Enable "Consistent NAT" |
| PaloAlto | Default NAT type | Configure "Persistent NAT" |
| OPNSense | Default NAT type | Add Outbound NAT rule |

## Gotchas
- QUIC (not raw UDP) is what Twingate uses—firewalls blocking QUIC specifically will break P2P even if UDP is allowed
- AWS NAT Gateways are a **known incompatibility**—cannot be fixed with configuration alone; requires replacement
- Both sides must have compatible NAT—fixing only the Connector side is insufficient if Client is behind endpoint-dependent NAT
- Double NAT is common in home setups (ISP modem + personal router)

## Related Docs
- How NAT traversal works (Twingate internal article)
- Network/firewall prerequisites documentation
- Twingate relay transport overview
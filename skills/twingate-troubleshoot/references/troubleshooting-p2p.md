# Troubleshooting Peer-to-Peer Connections

## Summary
Twingate uses NAT traversal for peer-to-peer connections between Clients and Connectors. Four main conditions can prevent P2P from working: blocked UDP/QUIC, blocked IP/port ranges, double NAT, or incompatible NAT types. No firewall ports need to be opened inbound for either P2P or relay traffic.

## Key Information
- P2P uses UDP/QUIC; relay traffic uses TCP to a shared relay server
- Both Client and Connector must have endpoint-independent NAT for P2P to function
- If P2P fails, Twingate falls back to relay transport automatically
- QUIC is more commonly blocked on the Connector side than Client side

## Four Root Causes

### 1. UDP/QUIC Blocked
- QUIC (UDP-based) must be allowed on both sides
- Test QUIC support: https://quic.nginx.org/
- Start troubleshooting on the Connector side

### 2. Outbound Rules Too Restrictive
- Connectors must send UDP to **any IP address** (client IPs unknown in advance)
- Must allow UDP to **any port** (NAT devices assign random ports)
- Verify prerequisites from the network requirements doc

### 3. Double NAT
- Two NAT devices in front of a single Client breaks P2P
- Common when users add their own router on top of ISP-provided equipment
- UDP's stateless nature makes multi-layer NAT mappings brittle

### 4. Incompatible NAT Type
- Requires **endpoint-independent NAT** on both sides
- Endpoint-dependent NAT assigns different ports per destination — breaks P2P

## Verification Steps

**Check Connector NAT type (Admin Console):**
- Navigate to Connectors → verify `STUN Discovery` shows `Available`

**Check Client NAT type (Client logs):**
```
[INFO] [libsdwan] stun_nat_type: endpoint-independent
```

## Known Incompatible Appliances

| Appliance | Issue | Workaround |
|-----------|-------|------------|
| AWS NAT Gateway | Incompatible NAT type | Use Cohesive cloud NAT, fck-nat, alterNAT, or custom NAT gateway |

## Firewall Configuration for Endpoint-Independent NAT

| Firewall | Setting |
|----------|---------|
| SonicWall | Enable "Consistent NAT" |
| PaloAlto | Implement "Persistent NAT" |
| OPNSense | Add Outbound NAT rule |

## Gotchas
- Both sides (Client **and** Connector) must satisfy all conditions — one incompatible end breaks P2P for all sessions
- QUIC being blocked is often silent; test explicitly with quic.nginx.org
- Double NAT is easy to miss when users add home routers behind ISP equipment
- P2P failure doesn't break connectivity (relay fallback exists) but may degrade performance

## Related Docs
- How NAT Traversal Works (Twingate internal article)
- Network Requirements / Prerequisites
- Twingate Relay documentation
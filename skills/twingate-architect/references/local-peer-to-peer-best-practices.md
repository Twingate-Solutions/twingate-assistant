# Best Practices for Local Peer-to-Peer Connections

## Summary
Twingate's local P2P feature enables direct connections between users and Connectors within the same network, bypassing central gateway routing. This guide covers recommended network topology (dual-VLAN design) and firewall configurations to optimize performance while maintaining Zero Trust security. Connectors serve as the only permitted bridge between user and resource VLANs.

## Key Information
- Local P2P keeps traffic within the local network, reducing latency and external bandwidth usage
- Only authenticated/authorized users can initiate P2P connections (Zero Trust enforcement)
- Recommended: deploy **two Connectors** in the resource VLAN for redundancy
- All user-to-resource traffic must pass through Connectors — no direct VLAN-to-VLAN access

## Recommended Network Topology

| VLAN | Contents |
|------|----------|
| VLAN 1 (Resources) | Servers, applications, 2x Twingate Connectors |
| VLAN 2 (Users) | End-user devices, DHCP, DNS |

## Firewall Rules (Applied Top-to-Bottom)

```
Source  | Destination | IP/Port      | Action
VLAN 2  | VLAN 1      | 10.0.0.2:*   | Allow   (Connector IP only)
VLAN 2  | VLAN 1      | *:*          | Block
VLAN 1  | VLAN 2      | *:*          | Block
```

## Firewall-Specific Configuration Steps

**Palo Alto NGFW:**
1. Define VLANs and assign interfaces
2. Create security zones per VLAN
3. Create security policy: VLAN 2 → Connector IPs in VLAN 1
4. Add PBF rules if needed
5. Use Strata Cloud Manager for policy validation

**Fortinet FortiGate:**
1. Create VLANs via Network > VLAN, assign VIDs and interfaces
2. Create firewall policy: source VLAN 2 → destination Connector IP(s)
3. Apply security profiles; add deny-all rule for remaining inter-VLAN traffic

**Sophos XG:**
1. Network > Interfaces > Add Interface > Add VLAN (set VLAN ID, IP, zone)
2. Rules and Policies: permit VLAN 2 → Connector IP(s) in VLAN 1
3. Block all other inter-VLAN traffic explicitly

**Barracuda CloudGen:**
1. Configure VLAN interfaces on physical/virtual ports
2. Firewall Admin > Configuration > Firewall: create allow rule (VLAN 2 source → Connector IP destination)
3. Add default deny rule for all other inter-VLAN traffic
4. Test connectivity after applying

## Gotchas
- Firewall rules are **order-dependent** — place allow rules for Connector IPs before the broad deny rule
- VLAN 1 → VLAN 2 traffic is also blocked (bidirectional restriction)
- Only the Connector's private IP should be whitelisted, not entire VLAN 1 subnet
- Requires two Connectors in VLAN 1 (HA/redundancy best practice)

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Peer-to-Peer Communication](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting P2P](https://www.twingate.com/docs/troubleshooting-p2p)
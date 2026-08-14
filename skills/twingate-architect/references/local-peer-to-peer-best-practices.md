---
source: https://www.twingate.com/docs/local-peer-to-peer-best-practices
type: docs
fetched: 2026-08-14
source_version: b0db6802587736f74551f54f9661e23f10d833186f08efb681563bdf1c6d19f6
---

# Best Practices for Local Peer-to-Peer Connections

## Summary
Guide for designing internal networks to leverage Twingate's local peer-to-peer (P2P) connections. Recommends a two-VLAN topology with Connectors mediating all cross-VLAN traffic. Covers firewall configuration for Palo Alto, FortiGate, Sophos XG, and Barracuda CloudGen.

## Key Information
- Local P2P: direct communication between users and Resources on the same network without routing through a central gateway
- Reduces latency by minimizing hops compared to traditional VPN
- Only authenticated/authorized users can initiate P2P connections (Zero Trust enforcement)
- Recommended: 2 Connectors per Remote Network for redundancy
- Connectors act as the sole bridge between user VLAN and resource VLAN

## Recommended Network Topology

**Two-VLAN Design:**
| VLAN | Contents |
|------|----------|
| VLAN 1 (Resources) | Servers, systems, 2x Twingate Connectors |
| VLAN 2 (Users) | End-user devices, DHCP, DNS |

**Firewall Rules (applied top-to-bottom):**
```
Source  | Destination | IP/Port      | Action
VLAN 2  | VLAN 1      | 10.0.0.2:*   | Allow  (Connector IP only)
VLAN 2  | VLAN 1      | *:*          | Block
VLAN 1  | VLAN 2      | *:*          | Block
```

## Firewall Configuration by Platform

**Palo Alto Networks NGFW:**
- Create VLANs → define security zones → create security policies allowing VLAN 2 → Connector IPs only → optionally add PBF rules

**Fortinet FortiGate:**
- Network > VLAN → add VLANs with VIDs → Policy & Objects → create policy with source VLAN, destination = Connector IP(s) only

**Sophos XG:**
- Network > Interfaces > Add VLAN → Rules and Policies → permit VLAN 2 to Connector IPs in VLAN 1, block all other inter-VLAN traffic

**Barracuda CloudGen:**
- Configure VLAN interfaces → Firewall Admin > Configuration > Firewall → allow VLAN 2 source to Connector IP destination → add default deny rule for all other traffic

## Gotchas
- Firewall rules are order-dependent; place specific allow rules before broad block rules
- Only Connector private IPs should be allowed through inter-VLAN firewall — not the entire VLAN 1 subnet
- Blocking VLAN 1 → VLAN 2 traffic is intentional; users must initiate via Twingate client
- Two Connectors in VLAN 1 required for HA — ensure firewall allows both Connector IPs from VLAN 2
- DNS/DHCP for users should stay in VLAN 2; do not mix with resource infrastructure

## Prerequisites
- Twingate Connectors deployed (minimum 2 recommended) in resource VLAN
- Managed switch/router supporting VLAN tagging
- Firewall capable of inter-VLAN policy enforcement (Palo Alto, FortiGate, Sophos XG, or Barracuda CloudGen examples provided)

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Peer-to-Peer Communication in Twingate](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting P2P](https://www.twingate.com/docs/troubleshooting-p2p)
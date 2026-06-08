# Best Practices for Local Peer-to-Peer Connections

## Summary
Twingate supports local peer-to-peer (P2P) connections where users communicate directly with Connectors on the same network, bypassing central gateways. This guide covers network topology design using VLAN segregation to optimize performance while enforcing Zero Trust access controls.

## Key Information
- Local P2P keeps traffic within the local network, reducing latency and external bandwidth usage
- Only authenticated/authorized users can initiate P2P connections
- Recommended topology: single physical network with two VLANs (Resources vs. Users)
- Two Connectors should be deployed in the Resource VLAN for redundancy

## Recommended Network Topology

**VLAN 1 (Resources):** Servers, systems, and Twingate Connectors  
**VLAN 2 (Users):** End-user devices, DHCP, DNS

## Firewall Rules

```
Source | Destination | IP/Port     | Action
VLAN 2 | VLAN 1      | 10.0.0.2:* | Allow   ← Connector IP only
VLAN 2 | VLAN 1      | *:*         | Block
VLAN 1 | VLAN 2      | *:*         | Block
```
Rules are evaluated top-to-bottom; only Connector IPs in VLAN 1 are reachable from VLAN 2.

## Firewall-Specific Configuration Notes

| Firewall | Key Steps |
|----------|-----------|
| **Palo Alto NGFW** | Create security zones per VLAN → define security policies allowing VLAN2→Connector IPs → optionally use PBF rules |
| **FortiGate** | Network > VLAN config → Policy & Objects > new policy with explicit destination IP (Connector) → block all other inter-VLAN traffic |
| **Sophos XG** | Network > Interfaces > Add VLAN → Rules and Policies permitting VLAN2→Connector IP only |
| **Barracuda CloudGen** | Configure VLAN interfaces → Firewall Admin > Configuration > access rules (VLAN2 source, Connector IP destination) → default deny rule |

## Connector Placement
- Deploy **two Connectors** in VLAN 1 (Resource VLAN)
- Connectors mediate all requests from VLAN 2 users to VLAN 1 resources
- Only Connector private IPs should be reachable from VLAN 2

## Gotchas
- All inter-VLAN traffic must be blocked **except** to Connector IP addresses — misconfigured rules allowing broader access defeat Zero Trust enforcement
- Firewall rules are order-dependent; place allow rules for Connector IPs **before** the blanket block rule
- VLAN 1→VLAN 2 traffic is blocked in the example config — verify this matches your operational requirements
- Replace `10.0.0.2` in examples with actual Connector IP(s); adjust if deploying two Connectors (add a second allow rule)

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Peer-to-Peer Communication](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting P2P](https://www.twingate.com/docs/troubleshooting-p2p)
# Best Practices for Local Peer-to-Peer Connections

## Summary
Twingate supports local peer-to-peer (P2P) connections where users and Connectors are on the same physical network, enabling direct low-latency access without routing through a central gateway. The recommended topology uses two VLANs with strict firewall rules that force all user traffic through Twingate Connectors.

## Key Information
- Local P2P keeps traffic within the local network, reducing latency and external bandwidth usage
- Only authenticated/authorized users can initiate P2P connections (Zero Trust enforcement)
- Two Connectors in the resource VLAN provide redundancy
- All inter-VLAN access is mediated by Twingate security protocols

## Recommended Network Topology

**Single physical network, two VLANs:**
- **VLAN 1 (Resources):** Servers, systems, 2x Twingate Connectors
- **VLAN 2 (Users):** End-user devices, DHCP, DNS

## Firewall Rules

```
Source | Destination        | Action
VLAN 2 | Connector IP (e.g. 10.0.0.2):* | Allow
VLAN 2 | VLAN 1 *:*         | Block
VLAN 1 | VLAN 2 *:*         | Block
```
Rules are evaluated top-to-bottom; only Connector IPs in VLAN 1 are reachable from VLAN 2.

## Firewall-Specific Configuration Steps

| Firewall | Key Steps |
|----------|-----------|
| **Palo Alto NGFW** | Create VLANs → define security zones → create security policies (src zone=VLAN2, dst=Connector IPs) → optional PBF rules |
| **FortiGate** | Network > VLAN (assign VIDs/interfaces) → Policy & Objects > new policy (src VLAN, dst=Connector IPs) → default deny for all other inter-VLAN |
| **Sophos XG** | Network > Interfaces > Add VLAN → Rules and Policies > permit VLAN2→Connector IPs, block all else |
| **Barracuda CloudGen** | Configure VLAN interfaces → Firewall Admin > Configuration > access rules (src=VLAN2 range, dst=Connector IP) → default deny rule |

## Gotchas
- Firewall rules are **order-dependent**; the allow rule for Connector IPs must precede the block-all rule
- Only Connector private IPs should be permitted through inter-VLAN firewall—not entire VLAN 1 subnet
- Two Connectors are recommended; if using multiple, each Connector IP needs an explicit allow rule
- Block traffic in **both directions** (VLAN1→VLAN2 and VLAN2→VLAN1) except through Connectors

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Peer-to-Peer Communication in Twingate](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting P2P](https://www.twingate.com/docs/troubleshooting-p2p)
# Best Practices for Local Peer-to-Peer Connections

## Summary
Guide for designing internal networks to leverage Twingate's local peer-to-peer (P2P) connections. Recommends a two-VLAN architecture with Connectors mediating all inter-VLAN traffic. Covers firewall configuration for Palo Alto, FortiGate, Sophos XG, and Barracuda CloudGen.

## Key Information
- Local P2P: direct communication between users and Resources on the same physical network, routed through Connectors
- Benefits: reduced latency, bandwidth optimization, Zero Trust enforcement
- Recommended topology: single physical network, two VLANs, two Connectors in resource VLAN
- All user-to-resource traffic must pass through Connector IPs — no direct inter-VLAN access

## Recommended Network Topology

| VLAN | Contents |
|------|----------|
| VLAN 1 (Resources) | Servers, systems, 2x Twingate Connectors |
| VLAN 2 (Users) | End-user devices, DHCP, DNS |

## Firewall Rules (Applied Top-to-Bottom)

| Source | Destination | IP/Port | Action |
|--------|-------------|---------|--------|
| VLAN 2 | VLAN 1 | `<ConnectorIP>:*` | Allow |
| VLAN 2 | VLAN 1 | `*:*` | Block |
| VLAN 1 | VLAN 2 | `*:*` | Block |

> Only Connector private IP addresses are whitelisted. All other VLAN 2 → VLAN 1 traffic is denied.

## Firewall-Specific Configuration Notes

- **Palo Alto NGFW**: Create security zones per VLAN → define security policies allowing VLAN 2 → Connector IPs → use PBF rules for routing; use Strata Cloud Manager for policy validation
- **FortiGate**: Network > VLAN setup → Policy & Objects > create policy with source VLAN and destination = Connector IP(s) only
- **Sophos XG**: Network > Interfaces > Add VLAN → Rules and Policies > permit VLAN 2 to Connector IPs in VLAN 1; block all other inter-VLAN traffic
- **Barracuda CloudGen**: Configure VLAN interfaces → Firewall Admin > Configuration > Firewall rules → set source = VLAN 2 range, destination = Connector IP only → add default deny rule

## Prerequisites
- Two Twingate Connectors deployed in VLAN 1
- Managed switch supporting 802.1Q VLANs
- Firewall capable of inter-VLAN policy enforcement

## Gotchas
- Firewall rules are order-dependent (top-to-bottom); allow rules for Connector IPs must precede the block-all rule
- VLAN 1 → VLAN 2 traffic is also blocked by default in this design — verify Connector-initiated return traffic is handled correctly
- Two Connectors recommended for redundancy; only specific Connector IPs should be whitelisted, not entire VLAN 1 subnet

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Peer-to-Peer Communication](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting P2P](https://www.twingate.com/docs/troubleshooting-p2p)
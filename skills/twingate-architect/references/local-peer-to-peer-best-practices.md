# Best Practices for Local Peer-to-Peer Connections

## Summary
Twingate supports local peer-to-peer (P2P) connections where users and Connectors are on the same physical network, enabling direct secure access without routing through external gateways. The recommended topology uses two VLANs with strict firewall segregation, where all user access to resources is mediated exclusively through Twingate Connectors.

## Key Information
- Local P2P keeps traffic within the local network, reducing latency and external bandwidth usage
- Only authenticated/authorized users can initiate P2P connections (Zero Trust enforcement)
- Two Connectors recommended in the resource VLAN for redundancy
- Firewall rules are ordered: allow Connector IPs first, then block all other inter-VLAN traffic

## Recommended Network Topology

**VLAN 1 (Resources):** Servers, applications, and 2x Twingate Connectors  
**VLAN 2 (Users):** End-user devices, DHCP, DNS

## Firewall Rules

```
Source  | Destination | IP/Port    | Action
VLAN 2  | VLAN 1      | 10.0.0.2:* | Allow   ← Connector IP only
VLAN 2  | VLAN 1      | *:*        | Block
VLAN 1  | VLAN 2      | *:*        | Block
```

Rules applied top-to-bottom; Connector IP must be explicitly allowed before the blanket block.

## Configuration by Firewall Vendor

| Firewall | Key Config Location |
|----------|-------------------|
| Palo Alto NGFW | Security Zones → Security Policies → PBF rules |
| FortiGate | Network > VLAN → Policy & Objects > Firewall Policy |
| Sophos XG | Network > Interfaces > Add VLAN → Rules and Policies |
| Barracuda CloudGen | Configuration tab > Firewall section > Access Rules |

**General pattern for all vendors:**
1. Create VLAN interfaces with correct IDs and IP assignments
2. Create allow rule: VLAN 2 source → Connector IP(s) in VLAN 1, any port
3. Create default deny rule: all other inter-VLAN traffic blocked

## Gotchas
- Firewall rule order is critical — allow Connector IPs must precede the block-all rule
- Block traffic in both directions (VLAN 1→VLAN 2 and VLAN 2→VLAN 1) except through Connectors
- Using a single Connector IP in the example (`10.0.0.2`) — replace with actual Connector IPs for both Connectors
- Users cannot directly reach VLAN 1 resources at all without Twingate authentication

## Prerequisites
- Two Twingate Connectors deployed in VLAN 1
- VLAN-capable switch/firewall infrastructure
- Static/known IP addresses for Connectors (required for firewall rules)

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Peer-to-Peer Communication in Twingate](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting P2P](https://www.twingate.com/docs/troubleshooting-p2p)
# Best Practices for Local Peer-to-Peer Connections

## Summary
Guide for designing internal networks to leverage Twingate's local peer-to-peer (P2P) connections. Covers recommended VLAN topology and firewall rules to enable direct, secure user-to-resource connections while maintaining Zero Trust access control.

## Key Information
- Local P2P allows direct communication between users and resources on the same network without routing through external gateways
- Reduces latency by minimizing hops; keeps traffic local to save external bandwidth
- All connections still require Twingate authentication/authorization regardless of topology

## Recommended Network Topology

**Single physical network, two VLANs:**
- **VLAN 1 (Resources):** Servers, systems, and 2x Twingate Connectors
- **VLAN 2 (Users):** End-user devices, DHCP, DNS

**Traffic rules (applied top-to-bottom):**
```
Source  | Destination | IP/Port     | Action
VLAN 2  | VLAN 1      | 10.0.0.2:*  | Allow  (Connector IP only)
VLAN 2  | VLAN 1      | *:*         | Block
VLAN 1  | VLAN 2      | *:*         | Block
```

## Firewall Configuration Rules

**Core logic:**
```
allow traffic from VLAN2 to Connector_IPs on VLAN1 on required ports
block all other traffic between VLAN1 and VLAN2
```

**Supported firewall platforms with vendor-specific guidance:**
- **Palo Alto NGFW:** Security zones + security policies + PBF rules; use Strata Cloud Manager
- **Fortinet FortiGate:** Network > VLAN config + Policy & Objects firewall rules with destination IP restriction
- **Sophos XG:** Network > Interfaces > Add VLAN + Rules and Policies
- **Barracuda CloudGen:** VLAN interfaces + access rules in Firewall Admin > Configuration tab

## Gotchas
- Only the Connector's private IP addresses should be permitted across VLANs—no broad inter-VLAN routing
- Two Connectors recommended in VLAN 1 (implied redundancy)
- Firewall rules are order-dependent; place allow rules for Connector IPs before broad deny rules
- VLAN 1 → VLAN 2 traffic is blocked in both directions in the example config (verify this matches your use case)

## Prerequisites
- Managed switch/router supporting 802.1Q VLANs
- Twingate Connectors deployed in resource VLAN (VLAN 1)
- Firewall capable of inter-VLAN rule enforcement

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Peer-to-Peer Communication](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting P2P](https://www.twingate.com/docs/troubleshooting-p2p)
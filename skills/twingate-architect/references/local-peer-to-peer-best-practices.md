## Best Practices for Local Peer-to-Peer Connections

Guide to designing internal network topology that maximizes Twingate's local P2P performance while enforcing Zero Trust segmentation. The recommended pattern uses two VLANs (Resources + Connectors on VLAN 1, Users on VLAN 2) with firewall rules that allow VLAN 2 traffic only to Connector private IPs on VLAN 1, blocking all other inter-VLAN traffic.

**Key Information**
- Local P2P: Twingate Client connects directly to the Connector on the same LAN, avoiding relay hops
- Benefit: lower latency, higher throughput, reduced external bandwidth vs relay-based connections
- Recommended topology: single physical network, two VLANs -- VLAN 1 (Resources + 2 Connectors), VLAN 2 (Users + DHCP)
- Firewall rule order: allow VLAN 2 -> Connector IPs on VLAN 1 (any port); block all other VLAN 1 <-> VLAN 2 traffic
- Two Connectors in VLAN 1 provide HA and load balancing
- Applies to on-premises networks; same principle extends to cloud VPCs with security groups

**Prerequisites**
- Managed switch or router supporting VLANs
- Firewall capable of inter-VLAN policy rules

**Firewall Rules (example)**
```
Source  | Destination        | Action
VLAN 2  | Connector IPs:*    | Allow
VLAN 2  | VLAN 1 (any other) | Block
VLAN 1  | VLAN 2             | Block (or Allow if needed for return traffic)
```

**Supported Firewall Platforms**
- Palo Alto Networks NGFW: security zones + security policies + optional PBF
- Fortinet FortiGate: VLAN interfaces + firewall policies specifying destination IP
- Sophos XG: VLAN interfaces + rules and policies
- Barracuda CloudGen: VLAN interfaces + access rules with default deny

**Gotchas**
- All users in VLAN 2 must authenticate through Twingate to reach VLAN 1 -- direct inter-VLAN routing must be completely blocked except to Connector IPs
- Place both Connectors in VLAN 1 (not VLAN 2) so they can directly reach Resources without traversing the firewall policy
- If users and Resources are on the same VLAN with no segmentation, local P2P still works but Zero Trust enforcement is weaker

**Related Docs**
- /docs/peer-to-peer-communication-in-twingate
- /docs/how-nat-traversal-works
- /docs/connector-placement-best-practices
- /docs/troubleshooting-p2p

# Best Practices for Local Peer-to-Peer Connections

## Summary
Twingate supports local peer-to-peer (P2P) connections that allow users to communicate directly with Connectors without routing through a central gateway. This guide covers recommended network topology using dual VLANs with strict traffic segregation to optimize performance and security. All user access to resources is mediated through Twingate Connectors.

## Key Information
- Local P2P keeps traffic within the local network, reducing latency and external bandwidth usage
- Recommended topology: two VLANs on a single physical network
  - **VLAN 1**: Resources (servers, systems) + two Twingate Connectors
  - **VLAN 2**: Users, DHCP, DNS, end-user devices
- Only Connector private IPs in VLAN 1 are reachable from VLAN 2
- Two Connectors recommended for redundancy in VLAN 1

## Firewall Rules (Apply Top-to-Bottom)

| Source | Destination | IP/Port | Action |
|--------|------------|---------|--------|
| VLAN 2 | VLAN 1 | `<ConnectorIP>:*` | Allow |
| VLAN 2 | VLAN 1 | `*:*` | Block |
| VLAN 1 | VLAN 2 | `*:*` | Block |

> Note: VLAN 1 → VLAN 2 blocking is implied; adjust if return traffic needs to flow.

## Supported Firewall Platforms
Configuration guidance provided for:
- **Palo Alto NGFW** – Security zones, security policies, PBF rules; reference Strata Cloud Manager
- **Fortinet FortiGate** – VLAN creation via GUI → Network → VLAN; policies via Policy & Objects
- **Sophos XG** – Network → Interfaces → Add VLAN; Rules and Policies for inter-VLAN control
- **Barracuda CloudGen** – VLAN interfaces on physical/virtual ports; access rules via Firewall Admin → Configuration

## Prerequisites
- Two Twingate Connectors deployed in VLAN 1
- Managed switch supporting 802.1Q VLANs
- Firewall capable of inter-VLAN policy enforcement

## Gotchas
- Firewall rules are order-dependent; allow Connector IPs **before** the broad block rule
- Users cannot reach any VLAN 1 resource directly—only through Connectors; plan DNS accordingly
- The example allows traffic from VLAN 2 to a single Connector IP (`10.0.0.2`)—update rules for both Connectors
- VLAN 1 → VLAN 2 block in the example table conflicts with return traffic; verify stateful firewall behavior on your platform

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Peer-to-Peer Communication](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting P2P](https://www.twingate.com/docs/troubleshooting-p2p)
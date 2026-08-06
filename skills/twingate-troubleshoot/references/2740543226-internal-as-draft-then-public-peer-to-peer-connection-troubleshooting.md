---
source: https://help.twingate.com/articles/2740543226-internal-as-draft-then-public-peer-to-peer-connection-troubleshooting
type: help
fetched: 2026-08-06
source_version: 84ad88efe2103724d96086fa74ab561dfe963881116a53b537b84711aff0bb43
---

# Peer-to-Peer Connection Troubleshooting

## Page Title
Peer-to-Peer Connection Troubleshooting (Client & Connector)

## Summary
Twingate prefers peer-to-peer (P2P) data transport but falls back to relay when P2P cannot be established. This guide covers firewall and NAT requirements that must be met on both the Client and Connector sides for P2P to work. Both endpoints must satisfy all conditions simultaneously.

## Key Information
- P2P requires compatible conditions on **both** Client and Connector sides
- Fallback to Twingate Relay occurs automatically when P2P fails
- P2P uses UDP; QUIC protocol is involved
- AWS NAT Gateway explicitly **does not** support NAT traversal

## Prerequisites
Both Client and Connector must meet:

### Firewall Requirements
- Allow outbound **UDP on ANY port** to **ANY public IP**
- No filtering of **P2P or QUIC** at any layer:
  - OS-level firewall
  - Network inspection/security software
  - Modem/router L7 filtering
  - ISP-level filtering

### NAT Requirements
- **No double NAT**
- NAT must use **Endpoint Independent Mapping (EIM)** — same external IP/port used for all connections from a host using the same internal port
- **Hairpin NAT** likely required when Client and Connector are on the same local network

## Configuration Values / Environment Notes
- **AWS NAT Gateway**: Not supported for P2P — place Connectors in **public subnets behind an Internet Gateway** instead

## Determining NAT Type

### Tool: pystun3
```bash
pip install pystun3
pystun3
```

**Example output:**
```
NAT Type: Full Cone
External IP: x.x.x.x
External Port: 54320
```

- `Full Cone` NAT = EIM-compatible = P2P friendly
- If external port changes between STUN queries, NAT is **not** EIM and P2P will fail

## Gotchas
- **Both** the Client NAT **and** the Connector NAT must be P2P-compatible; one incompatible side breaks P2P
- AWS NAT Gateway is a known blocker — must use Internet Gateway for Connector deployments
- Security software performing network inspection can silently block QUIC/UDP even if OS firewall rules appear correct
- ISP-level filtering can block P2P regardless of local configuration
- Double NAT (e.g., ISP modem + local router) will prevent P2P

## Related Docs
- Twingate complete firewall rules (linked in source)
- [AWS VPC Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
- [Wikipedia: Network Address Translation](https://en.wikipedia.org/wiki/Network_address_translation)
- [Tailscale: How NAT Traversal Works](https://tailscale.com/blog/how-nat-traversal-works)
- [pystun3 GitHub](https://github.com/talkiq/pystun3)
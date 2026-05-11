# How Firewalls Work with Twingate

## Summary
Twingate replaces the traditional VPN+firewall combination for user flows by handling both connectivity and access control in a single solution. Unlike VPNs, Twingate never grants users a network presence—traffic to unauthorized Resources never leaves the device. Firewalls remain recommended for machine-to-machine flows within the same network.

## Key Information

- **VPN model**: Connectivity only; firewalls add access control on top via IP-based rules
- **Twingate model**: Connectivity + access control unified; users never get a local IP on the private network
- **Lateral movement prevention**: User devices cannot scan or probe the network—unauthorized traffic is blocked at the client before leaving the device
- **Machine-to-machine flows**: Protected via Twingate Service Accounts for cross-environment communication; firewalls still recommended for same-network app-to-app traffic
- **Logging**: Real-time connection logs capture identity, source IP, Resource, protocol, port, Connector, Remote Network, and timestamp
- **Admin Console security**: Dedicated Security Policy for admin access + Admin Actions Report (full audit trail of create/delete/edit/connect events)

## VPN vs. Twingate Firewall Role Comparison

| Concern | VPN + Firewall | Twingate |
|---|---|---|
| User connectivity | VPN | Twingate Client |
| User access control | Firewall (IP rules) | Resources + Security Policies |
| Lateral movement risk | High without firewall rules | Virtually eliminated |
| Machine-to-machine (cross-env) | Firewall rules | Service Accounts |
| Machine-to-machine (same network) | Firewall | **Still use firewall** |
| Anomaly detection | Firewall alerts | Real-time connection logs → SIEM |

## Configuration Values

- **Resources**: Define with specific protocols and ports (not broad network ranges)
- **Security Policies**: Applied per Resource; configure auth frequency, 2FA requirements
- **Admin Console Policy**: Dedicated Security Policy with stricter re-authentication
- **Logging integration**: Export real-time connection logs to a SIEM

## Gotchas

- Twingate does **not** replace firewalls for same-network machine-to-machine flows—firewalls still needed there
- Resources should be **tightly scoped** (specific IPs, protocols, ports)—broad Resource definitions undermine access control benefits
- Only traffic through authorized Connector connections is logged; blocked attempts never reach the network and won't appear in network-layer logs
- Admin Console is a high-value target; apply a strict dedicated Security Policy to it

## Prerequisites

- Resources defined with specific protocols/ports
- Security Policies configured per Resource and for Admin Console
- SIEM integration recommended for real-time monitoring of connection logs

## Related Docs

- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Real-time Connection Logs](https://www.twingate.com/docs/real-time-logs)
- [Admin Actions Report](https://www.twingate.com/docs/admin-actions-report)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
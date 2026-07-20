# How Firewalls Work with Twingate

## Summary
Twingate replaces the traditional VPN+firewall combination for user access control by handling both connectivity and access control in a single solution. Unlike VPNs, Twingate never places users on the private network, preventing lateral movement attacks. Firewalls remain recommended for machine-to-machine flows within the same network.

## Key Information

- **VPN model**: Connectivity only — firewalls must be added separately for access control
- **Twingate model**: Connectivity + access control unified — traffic never leaves the device if user lacks authorization for a Resource
- Users are never assigned a local IP on the private network (eliminates lateral movement/port scanning risk)
- Twingate replaces firewall role for **user flows**; firewalls still recommended for **machine-to-machine flows on the same network**
- Machine-to-machine flows across separate environments can use **Service Accounts**
- Real-time connection logs available for SecOps/SIEM integration

## VPN vs Twingate Firewall Role Comparison

| Concern | VPN Setup | Twingate |
|---|---|---|
| User connectivity | VPN | Twingate Client |
| User access control | Firewall | Twingate (Resources + Security Policies) |
| M2M (cross-environment) | Firewall | Service Accounts |
| M2M (same network) | Firewall | Firewall (still needed) |
| Anomaly detection | Separate tooling | Real-time connection logs → SIEM |

## Configuration Values / Features

- **Resources**: Define with specific protocols and ports (tightly scoped)
- **Security Policies**: Control access per Resource; separate policy available for Admin Console
- **Service Accounts**: For machine-to-machine cross-environment access
- **Real-time connection logs** include: user identity, device info, public IP, Resource requested, protocol, port, Connector, Remote Network, timestamp, event type

## Gotchas

- Unauthorized connection attempts **never reach the network** — they are blocked at the device level and therefore **cannot be logged** (no network traffic generated)
- Only traffic through authorized Connectors appears in connection logs
- Admin Console requires its own Security Policy — treat it as a high-value target
- Twingate does **not** replace firewalls for same-network machine-to-machine segmentation

## Admin Console Security

- Dedicated Security Policy for Admin Console (enforce 2FA, frequent re-authentication)
- **Admin Actions Report**: Full audit trail of all admin actions (create/delete/edit/connect) across all objects (Connectors, Devices, Groups, API Keys, Remote Networks, Resources, Service Accounts, Users)

## Related Docs

- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Real-time Connection Logs](https://www.twingate.com/docs/real-time-logs)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
- [Admin Actions Report](https://www.twingate.com/docs/admin-actions-report)
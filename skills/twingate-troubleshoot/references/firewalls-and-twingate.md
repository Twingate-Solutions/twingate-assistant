# How Firewalls Work with Twingate

## Summary
Twingate replaces the traditional VPN+firewall combination for user access control by managing both connectivity and access control in a single solution. Unlike VPNs, Twingate never assigns users a network presence, making lateral movement and scanning attacks virtually impossible. Firewalls remain recommended for machine-to-machine flows within the same network.

## Key Information

- **VPN model**: Handles connectivity only; firewalls add access control on top via IP-based rules
- **Twingate model**: Handles both connectivity AND access control; traffic never leaves the device if user lacks authorization
- Users are never assigned a local IP address on the private network — no network presence = no lateral movement risk
- Each Twingate Resource should be tightly defined with specific protocols and ports
- Machine-to-machine flows across separate environments can be protected via **Service Accounts**
- Firewalls are still recommended for machine-to-machine flows **within the same network**

## VPN + Firewall vs. Twingate Comparison

| Concern | VPN + Firewall | Twingate |
|---|---|---|
| User connectivity | VPN | Twingate Client |
| User access control | Firewall (IP rules) | Resources + Security Policies |
| Lateral movement risk | High (user on network) | Eliminated (no network presence) |
| M2M across environments | Firewall rules | Service Accounts |
| M2M same network | Firewall | Still use firewall |
| Anomaly detection | Firewall alerts | Real-time connection logs + SIEM |

## Configuration Values / Features

- **Security Policies**: Control Resource access per user/group
- **Service Accounts**: Protect machine-to-machine flows across separate environments
- **Real-time connection logs** capture per-connection:
  - User identity, device info, public IP
  - Resource requested, protocol, port
  - Connector and Remote Network path
  - Timestamp and event type

## Gotchas

- Connection attempts to unauthorized Resources never leave the device — these attempts **cannot be logged** at the network level
- Only traffic flowing through Connectors (authorized connections) appears in logs
- Twingate does **not** replace firewalls for same-network machine-to-machine traffic
- Admin Console requires its own Security Policy — treat it as a high-value target

## Admin Console Security

- Dedicated Security Policy for Admin Console (enforce 2FA, frequent re-authentication)
- **Admin Actions Report**: Timestamped audit trail of all admin actions (create/delete/edit/connect) across all objects

## Related Docs

- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Real-time Connection Logs](https://www.twingate.com/docs/real-time-logs)
- [Admin Actions Report](https://www.twingate.com/docs/admin-actions-report)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
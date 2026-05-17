# How Firewalls Work with Twingate

## Summary
Twingate replaces the traditional VPN+firewall combination for user flows by handling both connectivity and access control in a single solution. Unlike VPNs, Twingate never places users on the private network, making lateral movement and scanning attacks impossible. Firewalls remain recommended for machine-to-machine flows within the same network.

## Key Information

- **VPN limitation**: VPNs handle connectivity only; firewalls must be added separately to enforce access control
- **Twingate difference**: Users are never assigned a local IP or placed on the private network — unauthorized traffic never leaves the device
- **Resource model**: Each Resource should be tightly defined with specific protocols and ports (replaces firewall rules for user flows)
- **Machine-to-machine flows**: Twingate Service Accounts protect cross-environment M2M communication; firewalls still recommended for same-network M2M flows
- **Logging**: Real-time connection logs capture user identity, device info, source IP, Resource, protocol, port, Connector, Remote Network, and timestamp
- **Admin Console security**: Dedicated Security Policy for admin access + Admin Actions Report (full audit trail of all create/delete/edit/connect events)

## Prerequisites

- Twingate Resources defined with specific protocols and ports
- Security Policies configured per user group or Resource
- For M2M: Service Accounts configured
- For monitoring: SIEM integration recommended

## Architecture Comparison

| Concern | VPN Approach | Twingate Approach |
|---|---|---|
| Connectivity | VPN | Twingate Client |
| User access control | Firewall rules on IP ranges | Security Policies + Resource definitions |
| M2M (cross-environment) | Firewall | Service Accounts |
| M2M (same network) | Firewall | Firewall (still recommended) |
| Anomaly detection | Firewall alerts | Real-time connection logs → SIEM |

## Gotchas

- Twingate only logs traffic through authorized connections via Connectors — unauthorized attempts never reach the network so they won't appear in logs
- Same-network M2M flows are **not** covered by Twingate; firewalls still required there
- Resources must be tightly scoped (specific ports/protocols) to replicate firewall-level granularity — broad Resource definitions reduce security benefit
- Admin Console is a high-value target; apply a stricter Security Policy with frequent re-auth and enforce 2FA

## Configuration Values

- **Security Policy**: Assign one specifically for Admin Console access
- **Real-time connection logs fields**: user email, device info, public IP, Resource, protocol, port, Connector, Remote Network, timestamp, event type
- **Admin Actions Report**: covers all Twingate objects (Connector, Device, Group, API Keys, Remote Network, Resource, Service Account, User)

## Related Docs

- Security Policies
- Real-time Connection Logs
- Service Accounts
- Admin Actions Report
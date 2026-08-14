---
source: https://www.twingate.com/docs/firewalls-and-twingate
type: docs
fetched: 2026-08-14
source_version: a3e42b2e3b513d1b9c0507412f94b024ab1eba7b5f28b7a0e3d9e376fd35ee66
---

# How Firewalls Work with Twingate

## Summary
Twingate replaces the traditional VPN+firewall combination for user access flows by handling both connectivity and access control in a single solution. Unlike VPNs, Twingate never places users on the private network, making lateral movement and scanning attacks virtually impossible. Firewalls remain recommended for machine-to-machine flows within the same network.

## Key Information

- **VPN model**: Provides connectivity only; firewalls must be layered on top for access control
- **Twingate model**: Handles both connectivity AND access control natively
- **Critical difference**: Twingate Client blocks unauthorized traffic at the device level—packets never leave the device if the user lacks authorization for that Resource
- **User flows**: Twingate replaces firewall role; no local IP assignment means no lateral movement risk
- **Machine-to-machine flows**: Protected via Twingate Service Accounts (especially cross-environment communication); firewalls still recommended for same-network app-to-app traffic
- **Logging**: Real-time connection logs capture identity, source IP, Resource requested, protocol, port, Connector, Remote Network, and timestamp
- **Admin Console security**: Dedicated Security Policy for console access + Admin Actions Report audit trail

## Prerequisites

- Twingate Resources must be defined with specific protocols AND specific ports (not broad network ranges)
- Users must be explicitly authorized per Resource via Security Policies
- Service Accounts required for machine-to-machine flows across separate environments

## Configuration Values

| Component | Purpose |
|-----------|---------|
| Security Policies | Control Resource access + Admin Console authentication requirements |
| Service Accounts | Machine-to-machine authentication across environments |
| Real-time connection logs | Network access monitoring |
| Admin Actions Report | Administrative audit trail |

## Gotchas

- **Twingate does NOT replace firewalls for same-network machine-to-machine flows**—firewalls still needed between co-located apps/services
- Only authorized traffic flowing through Connectors is logged; blocked/unauthorized attempts never reach the network and generate no network-side logs
- Resources must be tightly scoped (specific protocol + port)—broad Resource definitions undermine the access control model
- Admin Console is a high-value target; configure its dedicated Security Policy with frequent re-authentication and mandatory 2FA

## Related Docs

- Security Policies
- Real-time connection logs
- Admin Actions Report
- Service Accounts
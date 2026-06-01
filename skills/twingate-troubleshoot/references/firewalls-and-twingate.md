# How Firewalls Work with Twingate

## Summary
Twingate replaces the firewall's role in controlling user flows by enforcing access control at the device level before traffic leaves the endpoint. Unlike VPNs (which provide connectivity only and rely on firewalls for access control), Twingate handles both connectivity and access control in a single solution. Firewalls remain recommended for machine-to-machine flows within the same network.

## Key Information
- **VPN model**: Connectivity only → firewalls add access control layer on top
- **Twingate model**: Connectivity + access control combined; unauthorized traffic never leaves the user's device
- Users connected to Twingate are **not** placed on the private network; explicit Resource authorization is required
- Lateral movement and port scanning are effectively prevented since devices never receive a local IP address
- Machine-to-machine flows can be protected via **Service Accounts** (especially cross-environment)
- Firewalls still recommended for machine-to-machine flows **within the same network**

## Twingate vs. VPN + Firewall Architecture

| Concern | VPN + Firewall | Twingate |
|---|---|---|
| User connectivity | VPN | Twingate Client |
| User access control | Firewall rules | Security Policies + Resource definitions |
| Lateral movement prevention | Network segmentation | Traffic blocked at device |
| M2M cross-environment | Manual firewall rules | Service Accounts |
| M2M same-network | Firewall | Still use firewall |

## Configuration Values
- Each **Resource** should define specific protocols and specific ports (tight scope is critical)
- **Security Policy** for Admin Console: enforce 2FA, frequent re-authentication
- Real-time connection logs fields: user identity, device public IP, email, Resource requested, protocol, port, Connector info, Remote Network, timestamp, event type

## Monitoring & SecOps
- Real-time connection logs available for all authorized traffic through Connectors
- Unauthorized connection attempts never leave the device → not logged (no noise from scanning)
- **Recommended**: pipe real-time connection logs to a SIEM for alerting and investigation
- Admin Actions Report: timestamped audit trail of all admin actions (create/delete/edit/connect) across all objects

## Admin Console Security
- Dedicated Security Policy for Admin Console access
- Admin Actions Report covers: Connectors, Devices, Groups, API Keys, Remote Networks, Resources, Service Accounts, Users

## Gotchas
- Twingate does **not** replace firewalls for same-network machine-to-machine flows
- Resources must be tightly scoped (protocol + port) to replicate firewall-level precision
- Only traffic through authorized Connectors is logged; blocked attempts produce no server-side logs

## Related Docs
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Real-time Connection Logs](https://www.twingate.com/docs/real-time-logs)
- [Admin Actions Report](https://www.twingate.com/docs/admin-actions-report)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
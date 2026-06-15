# How Firewalls Work with Twingate

## Summary
Twingate replaces the firewall's role in controlling user-to-application flows by enforcing access control at the device level before traffic leaves the endpoint. Unlike VPNs (which handle connectivity only and rely on firewalls for access control), Twingate handles both connectivity and access control in a single solution. Firewalls remain recommended for machine-to-machine flows within the same network.

## Key Information
- **VPN model**: Connectivity only → requires firewall layered on top for access control
- **Twingate model**: Connectivity + access control combined; unauthorized traffic never leaves the user's device
- Users in Twingate are never assigned a local IP or given network presence — eliminates lateral movement and port scanning risks
- Machine-to-machine flows across separate environments can use **Service Accounts**
- Firewalls still recommended for M2M flows between services **co-existing on the same network**
- Real-time connection logs capture all authorized connection events through Connectors

## Twingate vs VPN + Firewall Comparison

| Concern | VPN + Firewall | Twingate |
|---|---|---|
| User connectivity | VPN | Twingate Client |
| User access control | Firewall rules (IP-based) | Resources + Security Policies |
| Lateral movement prevention | Network segmentation + firewall | Traffic blocked at device |
| M2M (cross-environment) | Firewall/VPN | Service Accounts |
| M2M (same network) | Firewall | Firewall (still recommended) |

## Configuration Values / Components
- **Resources**: Define with specific protocols AND specific ports (tightly scoped)
- **Security Policies**: Control access to Resources and Admin Console
- **Service Accounts**: Handle machine-to-machine authentication across environments
- **Real-time connection logs**: Fields include user identity, device info, public IP, Resource requested, protocol, port, Connector info, Remote Network, timestamp

## Monitoring & SecOps
- Connection logs only capture traffic flowing through authorized Connectors (unauthorized attempts never reach the network)
- Integrate real-time logs with a **SIEM** for alerting and forensic investigation
- **Admin Actions Report**: Timestamped audit trail of all admin actions (create/delete/edit/connect) across all Twingate objects

## Admin Console Security
- Dedicated Security Policy for Admin Console access (enforce 2FA, frequent re-auth)
- Admin Actions Report covers: Connector, Device, Group, API Keys, Remote Network, Resource, Service Account, User events

## Gotchas
- Each Twingate Resource should be **tightly defined** with specific protocols and ports — overly broad Resources undermine Twingate's access control model
- Twingate does **not** replace firewalls for same-network M2M traffic
- Anomaly detection via Twingate only covers authorized connections; blocked attempts are invisible to logs (by design — they never leave the device)

## Related Docs
- Security Policies
- Service Accounts
- Real-time connection logs
- Admin Actions Report
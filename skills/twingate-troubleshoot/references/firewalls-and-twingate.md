# How Firewalls Work with Twingate

## Summary
Twingate replaces the firewall's role for user flows by combining connectivity and access control into a single solution. Unlike VPNs (which only handle connectivity and require firewalls for access control), Twingate prevents unauthorized traffic from leaving the device entirely. Firewalls remain recommended for machine-to-machine flows within the same network.

## Key Information

- **VPN model**: Provides connectivity only; users get local IP addresses and network presence; firewalls required separately for access control
- **Twingate model**: Handles both connectivity and access control; users never get a local IP or network presence
- **Lateral movement prevention**: Unauthorized traffic never leaves the user's device, making port scanning and lateral attacks virtually impossible
- **Machine-to-machine flows**: Twingate Service Accounts protect cross-environment M2M communication; traditional firewalls still recommended for same-network M2M flows
- **Resource definition**: Each Resource should be tightly defined with specific protocols and ports to maximize access control granularity

## VPN + Firewall vs. Twingate Comparison

| Concern | VPN + Firewall | Twingate |
|---|---|---|
| Connectivity | VPN | Twingate |
| User access control | Firewall | Twingate (built-in) |
| M2M cross-environment | Firewall | Service Accounts |
| M2M same-network | Firewall | Firewall (still recommended) |
| Anomaly detection | Firewall alerts | Real-time connection logs |

## Configuration Values

- **Security Policies**: Applied per Resource to enforce access control and re-authentication requirements
- **Admin Console Security Policy**: Dedicated policy for admin access (enforce 2FA, frequent re-auth)
- **Real-time connection logs**: Log fields include user identity, device public IP, email, Resource requested, protocol, port, Connector info, Remote Network, timestamp

## Monitoring & SecOps

- Real-time connection logs available for all authorized connections through Connectors
- Unauthorized connection attempts never leave the device (not logged at network level)
- **Recommended**: Forward logs to a SIEM for real-time alerting and forensic investigation
- **Admin Actions Report**: Full audit trail of all admin actions (create/delete/edit/connect) across all Twingate objects

## Gotchas

- Twingate does **not** replace firewalls for same-network machine-to-machine flows
- Only traffic through authorized Connectors is loggable; blocked/unauthorized attempts generate no network-level logs
- Admin Console access requires its own dedicated Security Policy — treat it as a high-value target
- Resource definitions must include specific protocols and ports; overly broad Resources reduce zero-trust effectiveness

## Related Docs

- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Real-time Connection Logs](https://www.twingate.com/docs/real-time-logs)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
- [Admin Actions Report](https://www.twingate.com/docs/admin-actions-report)
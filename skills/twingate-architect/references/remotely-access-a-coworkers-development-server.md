# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to development servers on private home networks without exposing the network to the internet. Unlike port forwarding or VPN, Twingate requires no router reconfiguration and restricts access to only the specific resource.

## Key Information
- Access is scoped to individual resources, not the entire home network
- No router ports need to be opened
- No VPN server deployment required
- Existing home network configuration remains unchanged
- Access is restricted to explicitly granted coworkers only

## Prerequisites
- Twingate account with admin access
- Development server (physical or virtual) on the home network
- Ability to install Twingate Connector on the development server

## Implementation Steps

1. **Deploy a Connector** on the development server (the machine being shared)
2. **Add the development server as a Resource** in Twingate admin console
3. **Grant access** to specific coworkers via Twingate's access controls

## Why Not Alternatives

| Method | Problem |
|--------|---------|
| Port forwarding | Exposes home network elements to internet |
| VPN server | Requires deployment, exposes network surface |
| Twingate | No network exposure, resource-scoped access |

## Gotchas
- The Connector must be installed directly on the development server (or a machine on the same network with access to it)
- The server owner is responsible for keeping the Connector running — if the machine is off or the Connector stops, coworkers lose access

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connector)
- [Adding a Resource](https://www.twingate.com/docs/resources)
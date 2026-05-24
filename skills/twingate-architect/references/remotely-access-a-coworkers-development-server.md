# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to development servers on private home networks without exposing the network to the internet. Unlike port forwarding or VPN, only the specific development server resource is made accessible to authorized coworkers.

## Key Information
- Designed for developers hosting servers on home networks who need to share access with coworkers
- No router port forwarding required
- No VPN server deployment required
- No reconfiguration of existing home network
- Access is narrowly scoped to individual resources (not the entire network)
- Only explicitly authorized users can access the resource

## Prerequisites
- Twingate account with admin access to configure resources
- Development server with ability to install Twingate Connector
- Coworkers must be added as Twingate users and granted access

## Implementation Steps
1. **Deploy a Connector** on the development server (the machine being shared)
2. **Add the development server as a Resource** in Twingate
3. **Grant access** to specific coworkers via Twingate's access controls

## Why Not Port Forwarding or VPN
| Method | Problem |
|--------|---------|
| Port forwarding | Exposes home network elements to internet |
| VPN server | Requires deployment, exposes network elements |
| Twingate | No network exposure, resource-scoped access |

## Gotchas
- The Connector must be installed directly on the development server (or on a device on the same network with network-level access to the server)
- The home network owner/developer must set up and maintain the Connector
- Access control is managed through Twingate admin, not the developer's local network settings

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connectors)
- [Adding Resources](https://www.twingate.com/docs/resources)
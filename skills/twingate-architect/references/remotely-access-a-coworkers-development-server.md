# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to a coworker's development server on a private home network without exposing the network to the internet. Unlike port forwarding or VPN setups, Twingate requires no router reconfiguration and restricts access to only the specific resource.

## Key Information
- Access is limited to individual resources (the dev server), not the entire home network
- No router ports need to be opened
- No VPN server deployment required
- Existing home network requires zero reconfiguration
- Access can be restricted to specific coworkers who are explicitly granted permission

## Use Case Context
- Developers with servers on home networks (post-COVID office closures, under-desk servers)
- Sharing in-progress work for testing/review without others spinning up their own servers
- Avoids risks of port forwarding and traditional VPN (which expose home network elements to the internet)

## Implementation Steps
1. Deploy a **Connector** on the development server
2. Add the development server as a **Resource** in Twingate
3. Grant specific coworkers access to that resource

## Why Not Port Forwarding or VPN
| Method | Problem |
|--------|---------|
| Port Forwarding | Exposes home network elements to the internet |
| VPN Server | Requires deployment, exposes network, heavier security burden |
| Twingate | No exposure, no reconfiguration, resource-level access control |

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs)
- [Adding a Resource](https://www.twingate.com/docs)
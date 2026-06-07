# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to a developer's local/home development server without exposing the home network to the internet. Unlike port forwarding or VPN setups, Twingate restricts access to only the specific resource, not the entire network.

## Key Information
- Use case: Share access to a development server on a private/home network with specific coworkers
- No router port forwarding required
- No VPN server deployment required
- No existing home network reconfiguration needed
- Access is narrowly scoped to individual resources, not the whole network
- Only explicitly authorized users can access the resource

## Prerequisites
- Twingate account with ability to deploy Connectors and configure Resources
- Access to the development server machine (to install the Connector)
- Coworkers must be granted explicit access in Twingate

## Implementation Steps
1. **Deploy a Connector** on the development server machine
2. **Add the development server as a Resource** in Twingate
3. **Grant access** to specific coworkers via Twingate's access controls

## Why Not Alternatives
| Method | Problem |
|--------|---------|
| Port forwarding | Exposes home network elements to the internet |
| Self-hosted VPN | Exposes home network, requires VPN server deployment and maintenance |

## Gotchas
- The Connector must run on or have network access to the development server
- Access is per-resource, not network-wide — ensure the resource is defined correctly to cover only the intended server/port
- Physical network location of the server (office vs. home) doesn't affect the setup process

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connectors)
- [Adding a Resource](https://www.twingate.com/docs/resources)
# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to development servers on private home networks without exposing the network to the internet. Unlike port forwarding or VPN setups, Twingate requires no router reconfiguration and restricts access to specific resources only.

## Key Information
- Target use case: sharing local/home development servers with coworkers
- Access is scoped to individual resources, not entire networks
- No router port forwarding required
- No VPN server deployment needed
- No changes to existing home network configuration
- Access is restricted to explicitly authorized users only

## Prerequisites
- Twingate account with ability to deploy Connectors and create Resources
- Development server must be able to run a Twingate Connector
- Coworkers must have Twingate client installed and be granted access

## Implementation Steps
1. Deploy a **Twingate Connector** on the development server
2. Add the development server as a **Resource** in Twingate
3. Grant specific coworkers access to that Resource

## Why Not Alternatives
| Method | Problem |
|--------|---------|
| Port forwarding | Exposes home network elements to internet |
| VPN server | Requires deployment, exposes network, heavier security burden |
| Twingate | No network exposure, resource-scoped access |

## Gotchas
- Connector must run on or have network access to the development server
- Access control must be configured explicitly — coworkers are not auto-granted access
- This doc is conceptual; refer to Connector deployment and Resource configuration docs for technical steps

## Related Docs
- [Deploy a Connector](https://www.twingate.com/docs/connector)
- [Add a Resource](https://www.twingate.com/docs/resources)
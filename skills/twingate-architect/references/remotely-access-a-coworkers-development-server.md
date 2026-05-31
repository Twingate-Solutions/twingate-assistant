# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to a developer's private development server (e.g., on a home network) without exposing the network to the internet. Unlike port forwarding or VPN, Twingate restricts access to specific resources only, with no router or network reconfiguration required.

## Key Information
- Access is scoped to individual resources, not the entire network
- No router ports need to be opened
- No VPN server deployment required
- Existing home network configuration is unchanged
- Access is granted only to explicitly authorized coworkers

## Use Case Context
- Developer's physical server relocated from office to home network
- Need to share in-progress work for testing/review without others spinning up their own servers
- Avoids risks of port forwarding (exposes home network to internet) and traditional VPN setup

## Prerequisites
- Twingate account with admin access to create resources
- Ability to install a Twingate Connector on the development server
- Coworkers must be added as Twingate users and granted access to the resource

## Implementation Steps
1. **Deploy a Connector** on the development server (the machine being shared)
2. **Add the development server as a Resource** in the Twingate admin console
3. **Grant access** to specific coworkers via Twingate's access controls

## Gotchas
- The Connector must run on or have network access to the development server
- Access control is managed at the resource level — ensure only intended users are granted access
- Coworkers need the Twingate client installed to connect

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connectors)
- [Adding a Resource](https://www.twingate.com/docs/resources)
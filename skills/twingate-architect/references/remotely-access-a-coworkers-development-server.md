# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to development servers on private home networks without exposing the network to the internet. Unlike port forwarding or VPN setups, Twingate requires no router reconfiguration and restricts access to specific resources only.

## Key Information
- Access is scoped to individual resources (not the entire home network)
- No router ports need to be opened
- No VPN server deployment required
- No changes to existing home network configuration
- Access is explicitly granted per-user per-resource

## Use Case Context
- Developers with servers on home networks (post-COVID office closures)
- Sharing in-progress work for testing/review without coworkers spinning up their own servers
- Alternative to port forwarding and home VPN setups, both of which expose home network elements to the internet

## Prerequisites
- Twingate account with admin access
- Development server (physical or VM) to install Connector on
- Coworkers who need access must have Twingate client installed

## Implementation Steps
1. **Deploy a Connector** on the development server
2. **Add the development server as a Resource** in Twingate
3. **Grant access** to specific coworkers for that resource

## Gotchas
- The Connector must run on a machine that has network access to the target resource (running it directly on the dev server is simplest)
- Access control is explicit — coworkers must be granted access before they can connect

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connectors)
- [Adding a Resource](https://www.twingate.com/docs/resources)
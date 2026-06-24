# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to development servers on private home networks without exposing the network to the internet. Unlike port forwarding or VPN solutions, Twingate restricts access to specific resources only for explicitly authorized users.

## Key Information
- Access is scoped to individual resources (not the entire network)
- No router ports need to be opened
- No VPN server deployment required
- No reconfiguration of existing home network needed
- Home network remains invisible to the internet and third parties
- Access is restricted to coworkers explicitly granted permission

## Use Case Context
- Developer's server on home network needs to be accessible to remote coworkers
- Replaces risky workarounds: port forwarding and personal VPN servers
- Both alternatives expose elements of the home network to the internet

## Implementation Steps
1. Deploy a **Twingate Connector** on the development server
2. Add the development server as a **Resource** in Twingate
3. Grant specific coworkers access to that resource

## Prerequisites
- Twingate account with admin access
- Development server to act as the resource host
- Ability to install the Connector on the development server

## Configuration Values
None specified on this page — refer to Connector deployment and Resource configuration docs.

## Gotchas
- The Connector must run on or have network access to the development server
- Access control is managed at the resource level; verify only intended users are granted access

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connectors)
- [Adding a Resource](https://www.twingate.com/docs/resources)
# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to development servers on private home networks without exposing the network to the internet. No port forwarding or VPN server setup is required, and access is restricted to specific resources for specific users.

## Key Information
- Use case: share in-progress dev work for testing/review without requiring others to spin up their own servers
- Works for servers on home networks (common post-COVID scenario)
- Access is scoped to individual resources, not entire networks
- No router port changes or network reconfiguration needed
- Third parties cannot see or access the home network

## Why Not Port Forwarding or VPN
- **Port forwarding**: exposes home network elements to the internet
- **VPN server**: also exposes network elements, heavier security burden on developer

## Prerequisites
- Twingate account with ability to deploy Connectors and manage Resources
- A development server to share access to
- Coworkers who need access must be granted explicit permissions in Twingate

## Implementation Steps
1. Deploy a **Twingate Connector** on the development server
2. Add the development server as a **Resource** in Twingate
3. Grant specific coworkers access to that Resource

## Architecture Notes
- Twingate does not require inbound internet exposure
- Connector initiates outbound connections; no open router ports needed
- Access control is per-resource, not per-network

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connector)
- [Adding a Resource](https://www.twingate.com/docs/resources)
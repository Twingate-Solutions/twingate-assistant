# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to development servers on private home networks without exposing the network to the internet. Unlike port forwarding or VPNs, it restricts access to specific resources and requires no router reconfiguration.

## Key Information
- Target use case: sharing home-hosted dev servers with coworkers for collaboration (testing, review)
- No router ports need to be opened
- No VPN server deployment required
- No changes to existing home network configuration
- Access is restricted to specific resources, not the entire network
- Only explicitly authorized coworkers can access the resource

## Prerequisites
- Twingate account with ability to deploy Connectors and add Resources
- Development server (physical or virtual) to act as the Connector host

## Step-by-Step

1. **Deploy a Connector** on the development server
2. **Add the development server as a Resource** in Twingate
3. **Grant access** to specific coworkers via Twingate access controls

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Refer to Connector deployment docs for configuration parameters

## Gotchas
- Connector must run on or alongside the development server on the same local network
- Access control must be explicitly configured — coworkers are not granted access by default

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connector)
- [Adding a Resource](https://www.twingate.com/docs/resources)
# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to a developer's personal server (home or office) without exposing the home network to the internet. Unlike port forwarding or VPN setups, Twingate restricts access to specific resources only, with no router reconfiguration required.

## Key Information
- Use case: Share in-progress work for testing/review without coworkers spinning up their own servers
- Access is narrowly scoped — only the development server is accessible, not the entire home network
- No router ports need to be opened
- No VPN server deployment required
- No changes to existing home network configuration
- Access is explicitly granted per-user to specific resources

## Prerequisites
- Twingate account with ability to create Networks/Connectors
- Developer must have admin access to their development server (to install Connector)
- Coworkers must have Twingate client installed and be granted access

## Step-by-Step
1. **Deploy a Connector** on the development server (see Connector deployment docs)
2. **Add the development server as a Resource** in the Twingate Admin Console
3. **Grant access** to specific coworkers via Twingate's access controls

## Architecture Notes
- Connector runs on the same machine as the development server
- Outbound-only connections — no inbound firewall rules needed
- Only users explicitly granted access can reach the resource

## Gotchas
- The Connector must remain running on the development server for remote access to work
- If the developer's home internet goes down, the resource becomes unreachable
- Access control must be managed in Twingate Admin Console — not handled at the network level

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connector)
- [Adding a Resource](https://www.twingate.com/docs/resources)
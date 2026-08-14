---
source: https://www.twingate.com/docs/remotely-access-a-coworkers-development-server
type: docs
fetched: 2026-08-14
source_version: 93882d68e5ea57bd6910b495d22ff4f742f0085f82951f395b747bec8aeaef3c
---

# Remotely Access a Coworker's Development Server

## Summary
Twingate enables secure access to development servers on private home networks without exposing the network to the internet. Unlike port forwarding or VPNs, only the specific development server is accessible to explicitly authorized coworkers.

## Key Information
- Solves the problem of sharing home-network development servers with coworkers
- No router port forwarding required
- No VPN server deployment needed
- No changes to existing home network configuration
- Access is scoped to individual resources (not the entire network)
- Coworker access is explicitly granted per-resource

## Prerequisites
- Twingate account with admin access
- Development server to share
- Coworkers must be added as Twingate users with explicit access grants

## Step-by-Step

1. **Deploy a Connector** on the development server (the machine being shared)
2. **Add the development server as a Resource** in the Twingate admin console
3. **Grant access** to specific coworkers for that resource

## Architecture Notes
- Connector on the dev server initiates outbound connections to Twingate's network — no inbound ports needed
- Access is narrowly scoped: only the configured resource is reachable, not the broader home network
- Third parties cannot discover or reach the home network

## Gotchas
- The Connector must run on or have network access to the development server
- Home network remains private, but the server running the Connector must stay online for access to work
- Access grants must be explicitly configured — coworkers do not get access by default

## Related Docs
- [Deploying a Connector](https://www.twingate.com/docs/connector)
- [Adding a Resource](https://www.twingate.com/docs/resources)
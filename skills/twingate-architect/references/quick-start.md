## Page Title
Quick Start

## Summary
Three-step guide to get Twingate running: define a Remote Network, deploy a Connector into it, then install the Client and access resources. Estimated setup time: 15 minutes.

## Key Information
- **Three steps**: Remote Network → Connector → Client install
- **Remote Network**: logical container created in the Admin Console; select location (e.g. "AWS")
- **Resource definition**: add FQDN, IP, or CIDR address; must assign to a Group before it's accessible (Everyone group available by default)
- **Connector deployment**: deployed behind firewall on a host that can reach the target resources; supports Docker, native Linux service, and other options; must reach the Twingate Controller and Relay
- **Peer-to-peer connections**: recommended to enable for better user experience and to stay within Fair Use Policy bandwidth limits
- **Client install**: download from `get.twingate.com`; after auth, resources are immediately accessible

## Prerequisites
- Twingate account (free tier available)
- Permission to deploy Docker container or native Linux service on the target host
- Target host must be able to reach the resources you want to expose

## Step-by-Step
1. Admin Console → Network → Remote Networks → Add → select location → name it
2. Click the new Remote Network → Deploy Connector → select deployment method → run on target host
3. Wait for Connector to show "connected" in Admin Console (connects to both Controller and Relay)
4. Network → Add Resource → enter address → assign to a Group
5. Install Client from `get.twingate.com` → authenticate → access the resource

## Configuration Values
- Connector deployment: Docker or native Linux service (exact token/command shown in Admin Console)
- Client download: `get.twingate.com`

## Gotchas
- A Resource must be assigned to at least one Group — it will be inaccessible otherwise
- The Connector host must be able to resolve and route to the resources you define (Connector does the DNS lookup)
- Two Connectors per Remote Network recommended for HA — single Connector is a single point of failure
- The "Connection Status" sidebar in Admin Console updates in real-time as Connector comes online

## Related Docs
- `/docs/remote-networks` — Remote Network concept
- `/docs/resources` — resource types (FQDN, IP, CIDR, wildcard)
- `/docs/architecture` — component overview

---
source: https://www.twingate.com/docs/quick-start
type: docs
fetched: 2026-08-05
source_version: 1e841a0d49d1d8f30dffb4c21c43ffdac38f061832545861dffa34c3a6d87419
---

# Twingate Quick Start

## Summary
Step-by-step guide to configure a Twingate network by defining a Remote Network, deploying a Connector, and installing the Client to access private Resources. Covers the minimum configuration required to make a Resource accessible to users.

## Key Information
- Three core components: Remote Network (logical grouping), Connector (deployed agent), Client (end-user app)
- Resources must be assigned to at least one Group or they are inaccessible
- Default group available is "Everyone"; custom Groups enable access restriction
- Connector must be deployed on a host that can reach the target Resources
- Client installation available at `get.twingate.com`
- Connector status updates automatically once deployment initiates

## Prerequisites
- Active Twingate account (free tier available)
- Permissions to deploy Docker container or native Linux service on the target Remote Network host

## Step-by-Step

1. **Define Remote Network**
   - Navigate to Network → Remote Networks → Add
   - Select location (e.g., AWS, GCP, on-prem)
   - Name it (e.g., "AWS Production VPC") → Add Remote Network

2. **Define Resource**
   - Network → Add Resource
   - Enter address/name details → Add Resource
   - Assign to a Group (e.g., "Everyone") → Add 1 Group
   - ⚠️ Must assign to a Group or Resource is unreachable

3. **Deploy Connector**
   - Open Remote Network → Deploy Connector
   - Choose deployment method (Docker, Linux service, etc.)
   - Run generated deployment command on target host
   - Verify Connection Status sidebar shows successful link to Controller and Relay

4. **Install Client**
   - Visit `get.twingate.com` on end-user device
   - Authenticate → access Resources directly by hostname/IP

## Configuration Values
- No explicit env vars in this doc; deployment tokens/commands are generated in the Admin Console per Connector
- See [Deploying Connectors](https://www.twingate.com/docs/deploying-connectors) for environment-specific flags

## Gotchas
- Skipping Group assignment makes the Resource completely inaccessible — no error is shown
- Connector host must have network-level access to the Resources it serves
- Peer-to-peer connections should be enabled to stay within the Fair Use Policy for bandwidth
- If a Remote Network was auto-created during signup, you can skip step 1

## Related Docs
- [Resource Definition](https://www.twingate.com/docs/resource-definition) — allowed address formats
- [Deploying Connectors](https://www.twingate.com/docs/deploying-connectors) — environment-specific deployment
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Services (CI/CD)](https://www.twingate.com/docs/services)
- [Security Policies](https://www.twingate.com/docs/security-policies)
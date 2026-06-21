# Twingate Quick Start

## Summary
Step-by-step guide to configure a Twingate network by defining a Remote Network, deploying a Connector, and installing the Client. Covers the minimum setup required to protect and access private resources. Suitable for first-time setup.

## Key Information
- Four core steps: define Remote Network → define Resource → deploy Connector → install Client
- Resources must be assigned to at least one Group to be accessible
- Default group available is "Everyone"; custom Groups enable access restriction
- Connector must be deployed on a host with network access to the target Resources
- Peer-to-peer connections are recommended for performance and Fair Use Policy compliance
- Connector status updates automatically in the UI once deployment is initiated

## Prerequisites
- Twingate account (free tier available)
- Permissions to deploy Docker container or native Linux service on the target Remote Network host

## Step-by-Step

1. **Define Remote Network**: Network → Add (next to Remote Networks) → select location (e.g., AWS) → name it → click "Add Remote Network"
2. **Define Resource**: Network → Add Resource → enter address details → Add Resource → assign to Group (e.g., "Everyone") → click "Add 1 Group"
3. **Deploy Connector**: Navigate to Remote Network → Deploy Connector → select deployment method → run on target host → confirm status shows connection to Controller and Relay
4. **Install Client**: Download from `get.twingate.com` → authenticate → access configured Resources

## Configuration Values
- Connector deployment options vary by environment (Docker, Linux native, others) — select in UI during deployment flow
- Resource addresses: see [Resource Definition](https://www.twingate.com/docs/resource-definition) for allowed formats

## Gotchas
- **Resource not accessible?** Most common cause: Resource not added to any Group. Must explicitly assign Group.
- Connector host must have direct network access to the Resources it serves — placement matters
- Remote Network may already exist post-signup; skip creation step if so
- Custom Groups must be created before they appear as assignment options for Resources

## Related Docs
- [Resource Definition](https://www.twingate.com/docs/resource-definition) — allowed address formats
- [Deploying Connectors](https://www.twingate.com/docs/deploy-connectors) — environment-specific deployment details
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer) — setup guide
- [Services](https://www.twingate.com/docs/services) — CI/CD and automated process access
- Client download: `get.twingate.com`
# Twingate Quick Start

## Page Title
Quick Start - Configure Twingate Network for Private Resource Access

## Summary
Sets up a functional Twingate network by defining a Remote Network, deploying a Connector, and installing the Client application. Covers the minimum configuration required to grant users authenticated access to private resources behind a firewall.

## Key Information
- Four core components: Remote Network, Resource, Connector, Client
- Resources must be assigned to at least one Group or they are inaccessible
- Connector must be deployed on a host with network access to the target Resources
- Connector status updates automatically in the UI once deployment initiates
- Peer-to-peer connections recommended to improve performance and comply with Fair Use Policy

## Prerequisites
- Active Twingate account (free tier available)
- Permissions to deploy Docker container or native Linux service on the target Remote Network host

## Step-by-Step

### 1. Define a Remote Network
1. Navigate to **Network** in the nav bar
2. Click **Add** next to Remote Networks
3. Select location (e.g., AWS)
4. Enter a name (e.g., "AWS Production VPC") → click **Add Remote Network**

### 2. Define a Resource
1. Click **Network** → **Add Resource**
2. Enter resource address/details → click **Add Resource**
3. Assign to a Group (e.g., "Everyone") → click **Add 1 Group**

> ⚠️ Resource MUST be added to a Group to be accessible

### 3. Deploy a Connector
1. Inside the Remote Network, click **Deploy Connector**
2. Select deployment method for your environment (Docker, Linux service, etc.)
3. Run the generated deployment command on the target host
4. Monitor **Connection Status** sidebar — ready when connected to both Controller and Relay

### 4. Install the Client
1. Visit `get.twingate.com`
2. Install and authenticate
3. Access configured resources directly by hostname/IP

## Configuration Values
- No explicit env vars listed on this page
- Deployment tokens/commands are generated per-Connector in the UI
- See [Deploying Connectors](https://www.twingate.com/docs/connectors) for environment-specific flags

## Gotchas
- Skipping Group assignment makes the Resource completely inaccessible — no warning during resource creation
- Connector host must have direct network access to the Resources (not just internet access)
- Existing Remote Networks from signup may already exist — check before creating duplicates
- Peer-to-peer support requires additional configuration; not enabled by default

## Related Docs
- [Resource Definition](https://www.twingate.com/docs/resource-definition) — allowed address formats
- [Deploying Connectors](https://www.twingate.com/docs/connectors) — environment-specific deployment
- [Groups/Access Control](https://www.twingate.com/docs/groups) — custom group creation
- [Services](https://www.twingate.com/docs/services) — CI/CD and automated process access
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
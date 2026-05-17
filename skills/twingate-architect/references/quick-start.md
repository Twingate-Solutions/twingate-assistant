# Twingate Quick Start

## Page Title
Quick Start Guide

## Summary
Walks through the minimum steps to configure a Twingate network: create a Remote Network, deploy a Connector, define a Resource, and install the Client. Covers the complete flow from account setup to accessing a private resource.

## Key Information
- Four core components: Remote Networks, Connectors, Resources, and Groups
- Resources must be assigned to at least one Group or they are inaccessible
- Connectors must be deployed on a host with network access to the target Resources
- Client installation available at `get.twingate.com`

## Prerequisites
- Active Twingate account (free tier available)
- Sufficient permissions to deploy Docker container or native Linux service on the target Remote Network host

## Step-by-Step

### 1. Define a Remote Network
1. Click **Network** in navigation bar
2. Click **Add** next to Remote Networks
3. Select location (e.g., AWS, GCP)
4. Enter name (e.g., "AWS Production VPC") → click **Add Remote Network**

### 2. Define a Resource
1. Click **Network** → **Add Resource**
2. Enter resource address details → click **Add Resource**
3. Assign to a Group (minimum: "Everyone") → click **Add 1 Group**

### 3. Deploy a Connector
1. Navigate to the Remote Network
2. Click **Deploy Connector**
3. Select deployment method (Docker, Linux service, etc.)
4. Run generated deployment command on target host
5. Confirm status sidebar shows connection to both Controller and Relay

### 4. Install the Client
1. Visit `get.twingate.com`
2. Install and authenticate
3. Access configured Resources directly from device

## Configuration Values
- Connector deployment options: Docker container, native Linux service, and others (environment-dependent)
- Deployment tokens/commands are generated in the Admin Console per Connector

## Gotchas
- **Resource must be added to a Group** — skipping this step makes the resource inaccessible to all users
- Connector host must have direct network access to the Resources being proxied
- Peer-to-peer connections are recommended to stay within Fair Use Policy bandwidth limits — requires additional configuration
- Default group is "Everyone"; custom Groups required to restrict per-user access

## Related Docs
- [Resource Definition](https://www.twingate.com/docs/resource-definition) — allowed address formats
- [Deploying Connectors](https://www.twingate.com/docs/deploying-connectors) — full deployment options
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer) — setup guide
- [Services (CI/CD)](https://www.twingate.com/docs/services) — automated process access
- Security Policies, Groups management — in Admin Console docs
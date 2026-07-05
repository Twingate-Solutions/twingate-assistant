# Twingate Quick Start

## Page Title
Quick Start: Configure Twingate Network for Private Resource Access

## Summary
Sets up a functional Twingate network by defining a Remote Network, deploying a Connector, and installing the Client app. Covers the minimum configuration needed to grant users authenticated access to private resources behind a firewall.

## Prerequisites
- Active Twingate account (free tier available)
- Sufficient permissions to deploy Docker container or native Linux service on the target Remote Network host

## Key Information
- **Remote Network**: Logical grouping for protected resources (e.g., "AWS Production VPC")
- **Connector**: Deployed behind your firewall; must be on a host that can reach target Resources
- **Resources must be added to a Group** — unassigned Resources are inaccessible to users
- Default group is "Everyone"; create custom Groups to restrict access
- Connector status updates automatically in sidebar; ready when connected to both Controller and Relay
- Peer-to-peer connections recommended for better performance and Fair Use Policy compliance

## Step-by-Step

### 1. Define Remote Network
1. Navigate to **Network** in nav bar
2. Click **Add** next to Remote Networks
3. Select location (e.g., AWS, GCP)
4. Enter name → **Add Remote Network**

### 2. Define a Resource
1. **Network** → **Add Resource**
2. Enter resource address details → **Add Resource**
3. Assign to a Group (e.g., "Everyone") → **Add 1 Group**

> ⚠️ Resource must be added to a Group or it will not be accessible.

### 3. Deploy a Connector
1. Open Remote Network → click **Deploy Connector**
2. Select deployment method for your environment
3. Run deployment on remote host
4. Verify sidebar shows successful connection to Controller and Relay

### 4. Install Client
- Visit **get.twingate.com**
- Authenticate → access configured Resources from any network

## Configuration Values
- Connector deployment options vary by environment (Docker, native Linux service, others)
- Resource addresses: see [Resource Definition](https://www.twingate.com/docs) for allowed formats

## Gotchas
- **Connector host must have network access to the Resources** it will serve — placement matters
- Skipping Group assignment makes Resource unreachable even if correctly configured
- Existing Remote Networks from signup can be reused; no need to create duplicates

## Related Docs
- [Resource Definition](https://www.twingate.com/docs) — allowed address formats
- [Deploying Connectors](https://www.twingate.com/docs) — environment-specific options
- [Peer-to-peer connections](https://www.twingate.com/docs) — bandwidth optimization
- [Services](https://www.twingate.com/docs) — CI/CD and automated process access
- [Security Policies](https://www.twingate.com/docs)
- Client install: **get.twingate.com**
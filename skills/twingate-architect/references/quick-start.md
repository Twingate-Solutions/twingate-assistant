# Twingate Quick Start

## Page Title
Quick Start: Configure Twingate Network for Private Resource Access

## Summary
Step-by-step guide to set up a Twingate network by defining a Remote Network, deploying a Connector, and installing the Client. Covers the minimum configuration needed to grant users access to protected private resources.

## Key Information
- Three core components: Remote Network (logical boundary), Connector (encrypted proxy), Client (end-user access)
- Resources must be assigned to at least one Group to be accessible
- Default available group is "Everyone"; custom Groups required for restricted access
- Connector must be deployed on a host with network access to target Resources
- Client download available at `get.twingate.com`

## Prerequisites
- Active Twingate account (free tier available)
- Permissions to deploy Docker container or native Linux service on the target Remote Network host

## Step-by-Step

### 1. Define Remote Network
1. Navigate to **Network** in navbar
2. Click **Add** next to Remote Networks
3. Select location (e.g., AWS)
4. Enter name (e.g., "AWS Production VPC") → click **Add Remote Network**

### 2. Define a Resource
1. **Network** → **Add Resource**
2. Enter resource address details → **Add Resource**
3. Assign to a Group (e.g., "Everyone") → **Add 1 Group**
   - ⚠️ Resource is inaccessible until assigned to a Group

### 3. Deploy a Connector
1. Open target Remote Network → click **Deploy Connector**
2. Select deployment method (Docker, native Linux, etc.)
3. Run deployment command on target host
4. Verify: "Connection Status" sidebar shows successful connection to both Twingate Controller and Relay

### 4. Install Client
1. Visit `get.twingate.com`, install on end-user device
2. Authenticate → access configured Resources directly by hostname

## Configuration Values
- Resource address formats: see [Resource Definition](https://www.twingate.com/docs) for allowed syntax
- Connector deployment options: Docker, native Linux, and others (environment-specific commands generated in UI)

## Gotchas
- **Group assignment is mandatory**: Resources not added to any Group will not be accessible to any user
- Connector host must have direct network reachability to the Resources it serves
- Peer-to-peer connections required to stay within Fair Use Policy for bandwidth; must be explicitly configured
- Existing Remote Networks may already exist from signup flow — check before creating duplicates

## Related Docs
- [Resource Definition](https://www.twingate.com/docs/resource-definition) — allowed address formats
- [Deploying Connectors](https://www.twingate.com/docs/deploying-connectors) — full deployment options
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer) — setup guide
- [Services](https://www.twingate.com/docs/services) — CI/CD and automated process access
- Security Policies, Groups management, Use Cases — available in main docs
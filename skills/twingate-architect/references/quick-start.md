# Twingate Quick Start

## Page Title
Quick Start – Configure Twingate Network for Private Resource Access

## Summary
Sets up a functional Twingate network by defining a Remote Network, deploying a Connector, creating a Resource, and installing the Client. Covers the minimal configuration path from account creation to accessing a protected Resource.

## Key Information
- Four-step process: Remote Network → Resource → Connector → Client
- Resources must be assigned to at least one Group or they are inaccessible to all users
- Connector must be deployed on a host with network access to the target Resources
- Client is installed from `get.twingate.com`
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
2. Enter Resource address details → click **Add Resource**
3. Assign to a Group (minimum: "Everyone") → click **Add 1 Group**

### 3. Deploy a Connector
1. Open the Remote Network → click **Deploy Connector**
2. Select deployment method (Docker, Linux service, etc.)
3. Run deployment on the remote host
4. Confirm status sidebar shows successful connection to Controller and Relay

### 4. Install the Client
1. Visit `get.twingate.com`
2. Install and authenticate
3. Access configured Resources directly from the device

## Configuration Values
- No explicit env vars documented on this page
- Connector deployment options: Docker container or native Linux service (environment-specific tokens shown during UI flow)

## Gotchas
- **Resource must be added to a Group** — omitting this step makes the Resource unreachable
- Connector host must have direct network access to target Resources (not just internet access)
- Remote Networks may already exist post-signup; check before creating a duplicate
- Peer-to-peer connections not enabled by default — requires additional configuration to avoid Fair Use Policy violations

## Related Docs
- [Resource Definition](#) – allowed address formats for Resources
- [Deploying Connectors](#) – all connector deployment environments
- [Support Peer-to-Peer Connections](#)
- [Services (CI/CD)](#) – automated/non-human access
- [Security Policies](#)
# Twingate Quick Start

## Page Title
Quick Start Guide

## Summary
Configure a Twingate network to provide secure access to private resources. Involves three core steps: define a Remote Network, deploy a Connector, and install the Client application.

## Prerequisites
- Active Twingate account (free tier available)
- Permissions to deploy Docker container or native Linux service on the target Remote Network

## Step-by-Step

### 1. Define a Remote Network
1. Navigate to **Network** in the navigation bar
2. Click **Add** next to Remote Networks
3. Select location (e.g., AWS, GCP)
4. Enter a name (e.g., "AWS Production VPC") → click **Add Remote Network**

### 2. Define a Resource
1. Navigate to **Network** → click **Add Resource**
2. Enter resource address details → click **Add Resource**
3. Assign to a Group (minimum: "Everyone") → click **Add 1 Group**

### 3. Deploy a Connector
1. Open the Remote Network → click **Deploy Connector**
2. Select deployment method for your environment
3. Run deployment on a host that can reach your target Resources
4. Verify **Connection Status** sidebar shows successful connection to Controller and Relay

### 4. Install the Client
1. Visit `get.twingate.com` and install the Client
2. Authenticate → access configured Resources directly

## Key Information
- Connectors deploy behind your firewall and provide encrypted connectivity
- Multiple deployment options available (Docker, native Linux, others)
- Connection Status sidebar updates automatically during Connector provisioning
- Connector must successfully connect to both **Controller** and **Relay** to be operational

## Configuration Values
- Resource addresses: see [Resource Definition](https://www.twingate.com/docs/resource-definition) for allowed formats
- Client download: `get.twingate.com`

## Gotchas
- **Resource must be added to a Group** or it will be inaccessible to users — this step is mandatory
- Connector host **must have network access to the Resources** it will serve
- Enable peer-to-peer connections to improve performance and stay within Fair Use Policy bandwidth limits
- Pre-existing Remote Networks may exist from signup; skip creation step if so

## Related Docs
- [Resource Definition](https://www.twingate.com/docs/resource-definition)
- [Deploying Connectors](https://www.twingate.com/docs/deploying-connectors)
- [Twingate Client Application](https://www.twingate.com/docs/client)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Services (CI/CD)](https://www.twingate.com/docs/services)
- [Security Policies](https://www.twingate.com/docs/security-policies)
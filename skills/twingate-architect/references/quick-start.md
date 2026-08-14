---
source: https://www.twingate.com/docs/quick-start
type: docs
fetched: 2026-08-14
source_version: 08841fcb183fe3c0268d001f87c2829d3b3d2b0e0c89d50cba1716403668cc04
---

# Twingate Quick Start

## Summary
Configure a Twingate network by defining a Remote Network, deploying a Connector behind your firewall, adding Resources, and installing the Client app. The setup enables encrypted access to private resources regardless of user network location.

## Key Information
- Four core components: Remote Networks, Connectors, Resources, and Groups
- Resources must be assigned to at least one Group to be accessible
- Connectors must be deployed on a host that can reach the target Resources
- Connector status updates automatically in the admin UI once deployed
- Peer-to-peer connections recommended to improve performance and comply with Fair Use Policy

## Prerequisites
- Twingate account (free tier available)
- Permissions to deploy Docker container or native Linux service on the target Remote Network host

## Step-by-Step

### 1. Define a Remote Network
1. Click **Network** in navigation bar
2. Click **Add** next to Remote Networks
3. Select location (e.g., AWS)
4. Enter name (e.g., "AWS Production VPC") → click **Add Remote Network**

### 2. Define a Resource
1. Click **Network** → **Add Resource**
2. Enter Resource address details → click **Add Resource**
3. Assign to a Group (e.g., "Everyone") → click **Add 1 Group**

> ⚠️ Resource must be added to a Group or it will not be accessible to any users.

### 3. Deploy a Connector
1. Navigate to the Remote Network
2. Click **Deploy Connector**
3. Select deployment method (Docker, Linux service, etc.)
4. Run generated deployment command on target host
5. Monitor **Connection Status** sidebar — ready when connected to both Controller and Relay

### 4. Install the Client
1. Visit [get.twingate.com](https://get.twingate.com)
2. Install and authenticate
3. Access configured Resources directly from device

## Configuration Values
- Connector deployment options: Docker container, native Linux service, and others (environment-dependent)
- Resource address formats: See [Resource Definition docs](https://www.twingate.com/docs/resource-definition)

## Gotchas
- Connector host **must** have network access to the Resources it will serve — placement matters
- Skipping Group assignment on a Resource means zero users can access it
- Existing Remote Networks from signup may be reused — no need to create duplicates
- Peer-to-peer connections require additional configuration; not enabled by default

## Related Docs
- [Resource Definition](https://www.twingate.com/docs/resource-definition)
- [Deploying Connectors](https://www.twingate.com/docs/deploying-connectors)
- [Twingate Client](https://www.twingate.com/docs/client)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Services (CI/CD)](https://www.twingate.com/docs/services)
- [Security Policies](https://www.twingate.com/docs/security-policies)
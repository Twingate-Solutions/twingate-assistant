# Twingate Quick Start

## Summary
Configure a Twingate network by defining a Remote Network, deploying a Connector, and installing the Client. This establishes encrypted access to private resources behind a firewall without exposing them publicly.

## Prerequisites
- Active Twingate account (free tier available)
- Admin permissions to deploy Docker container or Linux service on target Remote Network host
- Host machine that can reach the target Resources

## Step-by-Step

### 1. Define a Remote Network
1. Navigate to **Network** in the nav bar
2. Click **Add** next to Remote Networks
3. Select location (e.g., AWS, GCP)
4. Enter a name (e.g., "AWS Production VPC") → click **Add Remote Network**

### 2. Define a Resource
1. Click **Network** → **Add Resource**
2. Enter resource address details → click **Add Resource**
3. Assign to a Group (minimum: **Everyone**) → click **Add 1 Group**

> **Required:** Resource must be added to at least one Group or it will be inaccessible.

### 3. Deploy a Connector
1. Open the Remote Network → click **Deploy Connector**
2. Select deployment method (Docker, Linux service, etc.)
3. Run deployment on host that has network access to your Resources
4. Verify **Connection Status** sidebar shows successful connection to both Controller and Relay

### 4. Install the Client
- Download from `get.twingate.com`
- Authenticate → access Resources directly by hostname from any network

## Key Information
- Resources are accessed by private hostname/IP (e.g., `redis-a.prod.beamreach.int`)
- Connectors deploy **behind your firewall** — they initiate outbound connections only
- Multiple deployment environments supported (Docker, native Linux, cloud-specific options)
- Connector is ready when both **Controller** and **Relay** connections show green in the dashboard
- Peer-to-peer connections recommended to improve performance and comply with Fair Use Policy bandwidth limits

## Configuration Values
| Item | Notes |
|------|-------|
| Resource address formats | See [Resource Definition](https://www.twingate.com/docs/resource-definition) for allowed formats |
| Connector tokens | Auto-generated during Deploy Connector flow in the UI |

## Gotchas
- Connector host **must** have network-level access to the Resources it serves — placement matters
- Skipping Group assignment leaves the Resource unreachable even if it's defined
- If Remote Network already exists from signup, skip to Resource creation step

## Related Docs
- [Resource Definition](https://www.twingate.com/docs/resource-definition)
- [Deploying Connectors](https://www.twingate.com/docs/deploying-connectors)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Services (CI/CD)](https://www.twingate.com/docs/services)
- [Security Policies](https://www.twingate.com/docs/security-policies)
# Twingate Quick Start

## Summary
Configure a Twingate network by defining a Remote Network, deploying a Connector, and installing the Client. Provides encrypted access to private resources behind a firewall without exposing them publicly.

## Prerequisites
- Twingate account (free tier available)
- Admin permissions to deploy Docker container or Linux service on the target Remote Network host
- Host machine that can reach the private Resources you want to protect

## Step-by-Step

### 1. Define a Remote Network
- Navigate to **Network** → **Remote Networks** → **Add**
- Select location (e.g., AWS, GCP, on-prem)
- Name the network (e.g., "AWS Production VPC") → **Add Remote Network**

### 2. Define a Resource
- **Network** → **Add Resource**
- Enter resource address/CIDR details → **Add Resource**
- Assign to a Group (minimum: "Everyone") → **Add 1 Group**
- ⚠️ Resource must be added to at least one Group to be accessible

### 3. Deploy a Connector
- Inside your Remote Network, click **Deploy Connector**
- Select deployment method (Docker, native Linux, etc.)
- Run generated deployment command on a host that can reach your Resources
- Verify: "Connection Status" sidebar shows successful connection to both Controller and Relay

### 4. Install the Client
- Visit **get.twingate.com** to download the Client
- Authenticate → access protected Resources directly from any network

## Key Information
- Connectors deploy behind your firewall; no inbound firewall rules required
- Resources are defined by address (IP, CIDR, hostname) — see Resource Definition docs for full syntax
- Groups control access authorization; create custom Groups to restrict per-user access
- Peer-to-peer connections improve performance and reduce bandwidth against Fair Use Policy limits

## Configuration Values
| Item | Notes |
|------|-------|
| Connector deploy target | Must have network-level access to the Resources |
| Group assignment | Required — no Group = no access |
| Deployment options | Docker, native Linux service, and others (shown in UI) |

## Gotchas
- Skipping Group assignment is the most common reason a Resource is unreachable after setup
- The Connector host must have direct network access to the Resources — it acts as the network proxy
- Enable peer-to-peer support to avoid Fair Use Policy bandwidth limits

## Related Docs
- Resource Definition (allowed address formats)
- Deploying Connectors (all deployment environments)
- Supporting Peer-to-Peer Connections
- Services (for CI/CD / automated processes)
- Security Policies
- Custom Groups
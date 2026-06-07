# Twingate Quick Start

## Page Title
Quick Start Guide

## Summary
Step-by-step guide to configure a Twingate network by setting up a Remote Network, deploying a Connector, defining Resources, and installing the Client. Covers the minimum configuration needed for users to access protected private resources.

## Key Information
- Four core components: Remote Networks, Connectors, Resources, and Groups
- Resources must be assigned to at least one Group to be accessible
- Connector must be deployed on a host with network access to the target Resources
- Client app available at `get.twingate.com`
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Prerequisites
- Active Twingate account (free tier available)
- Permissions to deploy Docker container or native Linux service on the target Remote Network host

## Step-by-Step

### 1. Define a Remote Network
- Navigate to **Network** → click **Add** next to Remote Networks
- Select location (e.g., AWS, GCP)
- Name the network (e.g., "AWS Production VPC") → click **Add Remote Network**

### 2. Define a Resource
- Navigate to **Network** → click **Add Resource**
- Enter resource address/details → click **Add Resource**
- Assign to a Group (minimum: "Everyone") → click **Add 1 Group**

### 3. Deploy a Connector
- Within the Remote Network, click **Deploy Connector**
- Select deployment method for your environment
- Run deployment on remote host; monitor **Connection Status** sidebar
- Connector is ready when connected to both Twingate Controller and Relay

### 4. Install the Client
- Visit `get.twingate.com` and install on end-user device
- Authenticate and connect to access configured Resources

## Configuration Values
- No specific env vars listed in this page; deployment-specific values shown during Connector setup in the Admin Console

## Gotchas
- **Resource not accessible?** Must explicitly add Resource to a Group — skipping this step means no users can reach it
- Connector host must have direct network access to the Resources it serves
- Peer-to-peer connections should be configured to avoid Fair Use Policy violations on bandwidth

## Related Docs
- [Resource Definition](#) — full details on allowed address formats
- [Deploying Connectors](#) — all deployment environment options
- [Support Peer-to-Peer Connections](#)
- [Security Policies](#)
- [Services (CI/CD use cases)](#)
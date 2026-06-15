# Securing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploying Twingate Connectors in Azure to access private VMs without public IP addresses. Covers subnet preparation, Connector deployment via Container instances, Resource creation, and client access.

## Key Information
- Azure Container instances cannot share subnets with VMs — a dedicated subnet is required for the Connector
- Resources can be defined by IP address, DNS name, or both; users can only access via the defined address type(s)
- Internal DNS names resolve automatically if the zone is configured for the Connector — no additional Twingate zone config needed
- Connector status visible in Twingate Admin Console (green = healthy)

## Prerequisites
- Azure tenant with an existing Virtual Network
- Sufficient address space available in the VNet for a new subnet
- Twingate Admin Console access
- Resource Group, VNet, and Subnet details ready before Connector deployment

## Step-by-Step

### Prepare the Network
1. Go to **Virtual Networks** page in Azure
2. Add address space to the VNet
3. Go to **Subnets** page
4. Create a new subnet using the new address space (dedicated for Container instances)

### Deploy the Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs) with your Resource Group, VNet, and Subnet info
6. Verify container service is running in Azure
7. Confirm Connector shows green status in Twingate Admin Console

### Create Resources
8. Create Resources using internal DNS names or internal IPs of target VMs
9. Assign Resources to the Remote Network associated with the Connector

### Access Resources
10. Connect via Twingate Client (Windows/macOS tray, Android/iOS/ChromeOS app, or Linux CLI)
11. Resources appear in client; access via SSH, HTTP, or other protocols as configured

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Resource address: IP, DNS name, or both (determines how users must connect)

## Gotchas
- **Subnet isolation required**: Containers and VMs cannot share the same Azure subnet — skipping this step will break deployment
- **Address type restriction**: If a Resource is defined only by IP, DNS name access won't work and vice versa — define both if needed
- **DNS resolution**: Works automatically if DNS zone is configured at the Connector/network level; no Twingate-specific zone config required
- Troubleshooting available within the Admin Console deployment workflow screen

## Related Docs
- Azure Connector Deployment Guide (referenced but URL not provided)
- Twingate Client installation docs
- Connector troubleshooting (within Admin Console deployment workflow)
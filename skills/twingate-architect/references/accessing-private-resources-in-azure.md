# Accessing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploying Twingate Connectors in Azure to access private VMs without public IPs. Covers subnet preparation, Connector deployment as a Container instance, and Resource creation for SSH/HTTP servers.

## Key Information
- Azure Containers cannot share subnets with VMs — a dedicated subnet is required for the Connector
- Resources can be defined by DNS name, IP address, or both — users can only access via the defined address type(s)
- Internal DNS resolution works without explicit zone configuration in Twingate, as long as DNS is configured on the Connector's network
- Connector status visible in Twingate Admin Console (green = healthy)

## Prerequisites
- Azure tenant with an existing Virtual Network
- Twingate Admin Console access
- Resource Group identified for Connector deployment
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare Network
1. Navigate to **Virtual Networks** in Azure portal
2. Add address space to the virtual network
3. Navigate to **Subnets**
4. Create a new subnet using the new address space (dedicated for Container instances only)

### Deploy Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs) with your Resource Group, VNet, and Subnet details
6. Verify Connector shows green status in Twingate Admin Console

### Create Resources
7. Create Resources using internal DNS names or private IP addresses
8. Assign Resources to the Remote Network associated with the deployed Connector

### Access Resources
9. Connect via Twingate Client (tray menu on Windows/macOS, app on Android/iOS/ChromeOS, CLI on Linux)
10. Access private resources using defined addresses (SSH, HTTP, etc.)

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource Group | Existing Azure RG for Connector container |
| VNet | Virtual network containing private resources |
| Subnet | Dedicated container-only subnet (new, separate from VM subnets) |
| Resource address | IP, DNS name, or both — determines how users connect |

## Gotchas
- **Subnet isolation required**: Azure Container instances cannot coexist in subnets with VMs — failure to create a dedicated subnet will block deployment
- **Address type lock-in**: If a Resource is defined by IP only, DNS access won't work, and vice versa — define both if needed
- **DNS zones**: No explicit zone configuration needed in Twingate; relies on Connector's network DNS settings

## Related Docs
- Azure Connector Deployment Guide
- Twingate Client installation
- Twingate Admin Console (Remote Networks and Resources configuration)
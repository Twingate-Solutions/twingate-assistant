# Accessing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploying Twingate to access private Azure resources (VMs, servers) without public IP addresses. Covers subnet preparation, Connector deployment, Resource creation, and client access.

## Key Information
- Azure Container instances cannot share a subnet with VMs — a dedicated subnet is required for the Connector
- Resources can be defined by IP address, DNS name, or both — users can only access via the defined address type(s)
- Internal DNS resolution works without explicit zone configuration in Twingate, as long as DNS is configured for the Connector's network
- Connector health visible in Twingate Admin Console (green status indicator)

## Prerequisites
- Azure account with an existing Virtual Network
- Permission to create subnets and Container instances in Azure
- Twingate Admin Console access (to create Remote Network and generate Connector tokens)
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare Network
1. Navigate to **Virtual Networks** in Azure portal
2. Add address space to the virtual network
3. Navigate to **Subnets**
4. Create a new subnet using the new address space (dedicated for Containers only)

### Deploy Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs/azure-connector) with your Resource Group, VNet, and Subnet details
6. Verify Connector shows green status in Twingate Admin Console

### Create Resources
7. In Admin Console, create Resources using internal DNS names or IP addresses
8. Assign Resources to the Remote Network associated with the deployed Connector

### Access Resources
9. Connect via Twingate Client (tray menu on Windows/macOS, app on Android/iOS/ChromeOS, CLI on Linux)
10. Access Resources using their defined addresses (SSH, HTTP, etc.)

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource Group | Existing Azure RG for Connector Container instance |
| VNet | Target virtual network |
| Subnet | Dedicated Container-only subnet (new) |
| Resource address | IP, DNS name, or both — determines how users connect |

## Gotchas
- **Subnet isolation required**: Azure Containers cannot coexist in subnets with VMs — skipping this step will cause deployment failure
- **Address type matters**: If a Resource is defined by DNS only, IP access won't work, and vice versa
- **DNS zones**: No explicit Twingate zone config needed — DNS resolution is handled at the Connector network level

## Related Docs
- [Azure Connector Deployment Guide](https://www.twingate.com/docs/azure-connector)
- Twingate Client installation (Windows, macOS, Android, iOS, ChromeOS, Linux)
- Twingate Admin Console — Remote Networks and Resources configuration
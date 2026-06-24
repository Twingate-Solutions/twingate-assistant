# Accessing Private Resources in Azure with Twingate

## Summary
Guide for deploying Twingate to access private Azure resources (VMs, servers) without public IP addresses. Covers subnet preparation, Connector deployment, Resource creation, and client access.

## Key Information
- Azure Container instances cannot share subnets with VMs — a dedicated subnet is required for the Connector
- Resources can be defined by DNS name, IP address, or both; users can only access via the defined address type(s)
- Internal DNS resolution works automatically if the zone is defined for the Connector — no explicit zone config needed in Twingate

## Prerequisites
- Azure Virtual Network with available address space
- Resource Group identified for Connector deployment
- Twingate Admin Console access
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare Network
1. Navigate to Azure Virtual Networks page
2. Add address space to the virtual network
3. Navigate to Subnets page
4. Create a new subnet using the new address space (dedicated for Containers only)

### Deploy Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs) with your Resource Group, VNet, and Subnet details
6. Verify: container service visible in Azure + Connector status shows green in Twingate Admin Console

### Create Resources
7. In Twingate Admin Console, create Resources using internal DNS names or private IPs
8. Assign Resources to the deployed Connector

### Access Resources
9. Connect via Twingate Client (tray menu on Windows/macOS, app on Android/iOS/ChromeOS, CLI on Linux)
10. Access Resources using their defined addresses (SSH, HTTP, etc.)

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource Group | Existing Azure RG for Connector deployment |
| VNet | Target virtual network |
| Subnet | Must be Container-only subnet (new, dedicated) |
| Resource address | IP, DNS name, or both |

## Gotchas
- **Subnet isolation required**: Azure enforces that Container instances cannot coexist in subnets with VMs or other resource types — always create a dedicated subnet
- **Address type locks access method**: If a Resource is defined by IP only, users cannot reach it by DNS name and vice versa
- **DNS zones**: No Twingate-side zone configuration needed; resolution works if the zone is configured at the Connector's network level

## Related Docs
- Azure Connector Deployment Guide (linked in admin console deployment workflow)
- Twingate Client installation docs
- Connector troubleshooting (available in deployment workflow screen)
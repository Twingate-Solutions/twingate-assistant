# Accessing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploying Twingate Connectors in Azure to provide access to private VMs and resources without public IP addresses. Covers subnet preparation, Connector deployment, Resource creation, and client access.

## Key Information
- Azure Container Instances **cannot share a subnet with VMs** — a dedicated subnet is required for the Connector
- Resources can be defined by IP address, DNS name, or both; users can only access via the defined address type(s)
- Internal DNS resolution works automatically if the zone is defined for the Connector — no explicit zone configuration in Twingate needed
- Connector health visible in Twingate Admin Console (green status indicator)

## Prerequisites
- Azure tenant with an existing Virtual Network
- Sufficient address space available to add a new subnet
- Twingate Admin Console access
- Azure resource group with permissions to deploy Container Instances
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare the Network
1. Navigate to **Virtual Networks** in Azure portal
2. Add address space to the virtual network
3. Navigate to **Subnets**
4. Create a new subnet using the new address space (dedicated for Containers only)

### Deploy the Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs) with your Resource Group, VNet, and Subnet details
6. Verify Connector shows green status in Twingate Admin Console

### Create Resources
7. In Twingate Admin Console, create Resources using internal DNS names or private IP addresses
8. Assign Resources to the Remote Network associated with the Connector

### Access Resources
9. Connect via Twingate Client (tray menu on Windows/macOS, app on Android/iOS/ChromeOS, CLI on Linux)
10. Resources appear in client; access via SSH, HTTP, or other protocols as normal

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource Group | Existing or new Azure RG for the Container Instance |
| VNet | Must match VNet containing target VMs |
| Subnet | Dedicated Container-only subnet; cannot mix with VMs |
| Resource address | Internal IP or internal DNS name (or both) |

## Gotchas
- **Subnet isolation required**: Azure enforces that Container Instances must be in their own subnet — deploying into a VM subnet will fail
- **Address type restriction**: If a Resource is defined only by IP, DNS-based access won't work (and vice versa) — define both if needed
- **No public IPs needed**: Target VMs require no public IP or inbound firewall rules
- **Connector subnet must use new address space**: Ensure the new subnet CIDR doesn't overlap existing subnets

## Related Docs
- Azure Connector Deployment Guide
- Twingate Client installation
- Connector troubleshooting (available in Admin Console deployment workflow screen)
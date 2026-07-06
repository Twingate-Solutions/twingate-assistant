# Securing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploying Twingate Connectors and accessing private Azure resources (VMs without public IPs) via SSH, HTTP, or DNS. Covers subnet preparation, Connector deployment, and Resource creation for Azure virtual networks.

## Key Information
- Azure Container Instances **cannot share a subnet** with VMs — a dedicated subnet is required for the Connector
- Resources can be defined by IP address, DNS name, or both — users can only access via the defined address type(s)
- Internal DNS names resolve automatically if the zone is defined for the Connector — no additional zone configuration in Twingate needed
- Connector status visible in Twingate Admin Console (green = healthy)

## Prerequisites
- Azure tenant with an existing Virtual Network
- Permissions to create subnets and deploy Container Instances in Azure
- Twingate Admin Console access (to create Remote Network, generate Connector tokens)
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare Network
1. Navigate to **Virtual Networks** in Azure Portal
2. Add address space to the virtual network
3. Navigate to **Subnets**
4. Create a new subnet using the new address space (dedicated for Containers only)

### Deploy Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs/deploy-azure) with:
   - Resource Group name
   - VNet name
   - Subnet name (the dedicated container subnet)
6. Verify Container Instance is running in Azure Portal
7. Confirm Connector status shows green in Twingate Admin Console

### Create Resources
8. In Admin Console, create Resources using internal IP addresses or internal DNS names
9. Assign Resources to the Remote Network associated with the deployed Connector

### Access Resources
10. Connect via Twingate Client (tray menu on Windows/macOS, app on Android/iOS/ChromeOS, CLI on Linux)
11. Access resources using the defined address (IP or DNS)

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource Group | Existing Azure RG for Connector deployment |
| VNet | Target virtual network |
| Subnet | Must be dedicated to Containers (no VMs) |
| Resource address | IP, FQDN, or both — determines how users connect |

## Gotchas
- **Subnet isolation required**: Azure enforces that Container Instances cannot coexist with VMs in the same subnet — always create a separate subnet
- **Address type lock-in**: If a Resource is defined by DNS name only, IP access won't work (and vice versa) — define both if needed
- **DNS resolution**: Works automatically for internal zones without explicit Twingate zone config, as long as the Connector can reach the DNS server

## Related Docs
- [Azure Connector Deployment Guide](https://www.twingate.com/docs/deploy-azure)
- [Twingate Client Installation](https://www.twingate.com/docs/client)
- Twingate Admin Console — Remote Networks and Resources configuration
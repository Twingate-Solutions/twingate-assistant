# Securing Private Resources in Azure with Twingate

## Page Title
How to Secure Private Resources in Azure with Twingate

## Summary
Step-by-step guide for deploying Twingate Connectors in Azure to access private resources without public IP addresses. Covers subnet creation, Connector deployment as a Container instance, and Resource configuration for VMs and services.

## Key Information
- Connectors deploy as Azure Container instances
- Azure Container instances **cannot share subnets with VMs** — requires a dedicated subnet
- Resources can be defined by IP address, DNS name, or both
- Users can only access a Resource via the address(es) explicitly defined in Twingate
- Internal DNS names resolve via the Connector without explicit zone configuration in Twingate

## Prerequisites
- Azure Virtual Network (VNet) already configured
- Resource Group available
- Address space available to carve out a new subnet for Containers
- Twingate Admin Console access
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare the Network
1. Go to **Virtual Networks** in Azure portal
2. Add address space to the VNet (needed for the new Container subnet)
3. Go to **Subnets** page
4. Create a new subnet using the added address space (dedicated for Containers)

### Deploy the Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs) with your Resource Group, VNet, and subnet details
6. Verify: Container service appears in Azure AND Connector status shows **green** in Twingate Admin Console

### Create Resources
7. In Admin Console, create Resources using internal DNS names or internal IPs
8. Assign Resources to the Remote Network associated with the deployed Connector

### Access Resources
9. Connect via Twingate Client (tray menu on Windows/macOS, app on Android/iOS/ChromeOS, CLI on Linux)
10. Resources appear in client; connect via defined address (SSH, HTTP, etc.)

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource Group | Required for Connector deployment |
| VNet name | Must match network containing target VMs |
| Subnet | Must be dedicated Container subnet (no VMs) |
| Resource address | IP, DNS name, or both — defines how users connect |

## Gotchas
- **Subnet isolation required**: Azure enforces that Container instances cannot coexist in subnets with VMs or other resource types — always create a separate subnet
- **Address definition is access definition**: If a Resource is defined only by IP, users cannot reach it via DNS name, and vice versa
- **DNS zone config not required**: Internal DNS names resolve through the Connector automatically if the zone is configured at the network/DNS level — no Twingate-side zone setup needed
- Check the Admin Console troubleshooting section if Connector status doesn't turn green after deployment

## Related Docs
- Azure Connector Deployment Guide
- Twingate Client installation
- Remote Network configuration
- Hybrid deployment concepts
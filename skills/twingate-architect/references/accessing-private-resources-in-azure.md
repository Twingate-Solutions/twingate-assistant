# Accessing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploying Twingate Connectors in Azure to access private VMs and services without public IP addresses. Covers subnet creation, Connector deployment, and Resource configuration for Azure virtual networks.

## Key Information
- Azure Container instances **cannot share a subnet with VMs** — a dedicated subnet is required for the Connector
- Resources can be defined by IP address, DNS name, or both — users can only access via the defined method(s)
- Internal DNS names resolve automatically if the zone is configured on the Connector's network — no extra Twingate config needed
- Connector status visible in Twingate Admin Console (green = healthy)

## Prerequisites
- Azure subscription with an existing Virtual Network
- Twingate Admin Console access
- Resource Group, VNet, and Subnet details ready before Connector deployment
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare the Network
1. Navigate to **Virtual Networks** in Azure portal
2. Add address space to the virtual network
3. Navigate to **Subnets**
4. Create a new subnet using the new address space (Container-only subnet)

### Deploy the Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs) using the Resource Group, VNet, and Subnet from above
6. Confirm container service is running in Azure
7. Reload Twingate Admin Console — Connector indicator should be green

### Create Resources
8. In Admin Console, create Resources using internal DNS names or private IPs
9. Assign Resources to the Remote Network associated with the deployed Connector

### Access Resources
10. Connect via Twingate Client (Windows/macOS tray, Android/iOS app, Linux CLI)
11. Resources appear in the client; access via SSH, HTTP, or other protocols as normal

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource address | Internal IP or internal DNS name (or both) |
| Subnet type | Must be Container-dedicated (no VMs in same subnet) |
| Connector deployment | Via Azure Container Instances |

## Gotchas
- **Subnet isolation is mandatory**: Azure enforces that Container instances cannot coexist in subnets with VMs or other resource types
- **Resource address locks access method**: If only an IP is defined, DNS name access won't work, and vice versa
- **DNS zones don't need Twingate configuration**: Zone resolution works if defined at the network/Connector level

## Related Docs
- Azure Connector Deployment Guide (linked in Admin Console deployment workflow)
- Twingate Client installation docs
- Connector troubleshooting (available in deployment workflow screen in Admin Console)
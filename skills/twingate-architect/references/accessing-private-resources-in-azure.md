# Accessing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploying Twingate Connectors in Azure to access private VMs without public IP addresses. Covers subnet preparation, Connector deployment as a Container instance, and Resource creation for SSH/HTTP servers.

## Key Information
- Azure Containers cannot share a subnet with VMs — a dedicated subnet is required for the Connector
- Connector deploys as an Azure Container Instance
- Resources can be defined by internal DNS name or internal IP address
- Users can only access a Resource via the address type(s) defined (IP, DNS, or both)
- No explicit DNS zone configuration needed in Twingate — names resolve if defined for the Connector

## Prerequisites
- Existing Azure Virtual Network
- Resource Group available for Connector deployment
- Twingate Admin Console access
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare the Network
1. Navigate to **Virtual Networks** in Azure portal
2. Add address space to the virtual network
3. Navigate to **Subnets**
4. Create a new subnet using the new address space (dedicated for Container instances only)

### Deploy the Connector
1. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs/azure-connector) with your Resource Group, VNet, and Subnet details
2. Verify deployment: container service visible in Azure + Connector status green in Twingate Admin Console

### Create Resources
1. In Twingate Admin Console, create Resources using internal DNS names or internal IPs
2. Assign Resources to the Remote Network backed by the deployed Connector

### Access Resources
1. Connect via Twingate Client (desktop tray, mobile app, or Linux CLI)
2. Resources appear in client; access via defined address (SSH, HTTP, etc.)

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource Group | Existing or new Azure RG for Connector |
| VNet | Target virtual network |
| Subnet | Dedicated Container-only subnet |
| Resource address | Internal IP or internal DNS name |

## Gotchas
- **Subnet isolation required**: Azure restricts Container Instances to subnets containing only other Containers — do not place the Connector in an existing VM subnet
- **Address type lock-in**: If a Resource is defined by IP only, users cannot reach it via DNS (and vice versa); define both if needed
- **Connector status**: If status doesn't turn green after deployment, use the troubleshooting section in the Admin Console deployment workflow screen

## Related Docs
- [Azure Connector Deployment Guide](https://www.twingate.com/docs/azure-connector)
- Twingate Client setup (Windows, macOS, Android, iOS, ChromeOS, Linux)
- Hybrid deployment documentation
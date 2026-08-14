---
source: https://www.twingate.com/docs/accessing-private-resources-in-azure
type: docs
fetched: 2026-08-14
source_version: 9c4f22f8e7e94eba81702dbb494de8a4012565d97f7cfdad7ef661adc2a59433
---

# Accessing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploy Twingate Connectors in Azure to access private VMs without public IP addresses. Covers subnet preparation, Connector deployment, Resource creation, and client access. Applicable to simple or hybrid Azure deployments.

## Key Information
- Azure Container instances **cannot share a subnet with VMs** — a dedicated subnet is required for the Connector
- Resources can be defined by IP address, DNS name, or both — users can only access via the defined address type(s)
- Internal DNS zones don't need explicit Twingate configuration; names resolve as long as the Connector can reach the DNS server
- Connector status visible in Twingate Admin Console (green = healthy)

## Prerequisites
- Azure Virtual Network with available address space
- Permissions to create subnets, resource groups, and container instances in Azure
- Twingate Admin Console access
- Twingate Client installed on end-user devices

## Step-by-Step

### 1. Prepare the Network
1. Navigate to **Azure Virtual Networks**
2. Add address space to the existing virtual network
3. Go to **Subnets** → add new subnet using the new address space (name it distinctly, e.g., `twingate-connector`)

### 2. Deploy the Connector
1. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs/connector-deployment-azure)
2. Provide: Resource Group, VNet name, Subnet name from step 1
3. Verify: container service running in Azure + Connector shows green in Admin Console

### 3. Create Resources
1. In Admin Console, create Resources using internal DNS names or private IP addresses
2. Assign Resources to the Remote Network associated with the deployed Connector

### 4. Access Resources
1. Connect via Twingate Client (Windows/macOS tray, Android/iOS/ChromeOS app, or Linux CLI)
2. Resources appear in client; access via SSH, HTTP, or other protocols using defined addresses

## Configuration Values
| Parameter | Notes |
|---|---|
| Subnet | Must be dedicated to containers only (no VMs) |
| Resource address | IP, DNS name, or both — defines how users connect |
| Connector network | Assigned to the Azure Remote Network in Admin Console |

## Gotchas
- **Subnet isolation required**: Azure enforces that container instances and VMs cannot coexist in the same subnet — skipping this step will cause deployment failure
- **Address type locks access method**: If a Resource is defined by IP only, DNS-based access won't work, and vice versa
- **DNS zone config not needed in Twingate**: Internal DNS resolves via the Connector's network access, not Twingate-side zone configuration
- Troubleshooting guidance is available in the deployment workflow screen in Admin Console

## Related Docs
- [Azure Connector Deployment Guide](https://www.twingate.com/docs/connector-deployment-azure)
- Twingate Client installation (Windows, macOS, Android, iOS, ChromeOS, Linux)
- Hybrid deployment documentation
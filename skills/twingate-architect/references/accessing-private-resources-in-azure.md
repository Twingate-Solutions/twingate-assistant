# Accessing Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploy Twingate Connectors in Azure and expose private VM resources (no public IPs) to authorized users. Covers subnet creation, Connector deployment, Resource definition, and client access.

## Key Information
- Azure Container Instances **cannot share a subnet with VMs** — a dedicated subnet is required for the Connector
- Resources can be defined by internal DNS name or private IP address
- Users can only access Resources via the address type defined (IP, DNS, or both)
- DNS resolution works automatically if the zone is configured on the Connector's network — no explicit Twingate zone config needed

## Prerequisites
- Azure Virtual Network with available address space
- Permissions to create subnets, resource groups, and container instances in Azure
- Twingate account with Admin Console access
- Twingate Client installed on end-user devices

## Step-by-Step

### Prepare the Network
1. Navigate to **Virtual Networks** in Azure Portal
2. Add address space to the VNet (to accommodate new subnet)
3. Navigate to **Subnets**
4. Create a new subnet using the new address space (dedicated for Container Instances)

### Deploy the Connector
5. Follow the [Azure Connector Deployment Guide](https://www.twingate.com/docs/azure-connector) using the Resource Group, VNet, and new subnet details
6. Verify: container service running in Azure + Connector status shows **green** in Twingate Admin Console

### Create Resources
7. In Admin Console, create Resources using either:
   - Internal DNS name (e.g., `vm.internal.corp`)
   - Private IP address
8. Assign Resources to a Twingate Group

### Access Resources
9. Connect via Twingate Client (Windows/macOS tray, mobile app, or Linux CLI)
10. Resources appear in client; access via SSH, HTTP, etc. using defined addresses

## Configuration Values
| Item | Notes |
|------|-------|
| Subnet delegation | Must be dedicated to Container Instances |
| Resource address | IP, DNS hostname, or both — users limited to defined type |
| Connector visibility | Admin Console shows green status on successful deploy |

## Gotchas
- **Subnet isolation required**: VMs and Container Instances cannot coexist in the same Azure subnet — failure to separate will block Connector deployment
- **Address type lock-in**: If a Resource is defined only by IP, DNS access won't work (and vice versa) — define both if needed
- **DNS zones**: No Twingate-side zone configuration needed; relies on DNS being resolvable from the Connector's subnet

## Related Docs
- [Azure Connector Deployment Guide](https://www.twingate.com/docs/azure-connector)
- [Twingate Client Setup](https://www.twingate.com/docs/client)
- Azure Connector troubleshooting (within deployment workflow screen in Admin Console)
## Page Title
How to Secure Private Resources in Azure with Twingate

## Summary
Step-by-step guide to deploying a Twingate Connector in Azure Container Instances and creating Resources to access private Azure VMs with no public IP addresses. Covers the Azure-specific requirement that Container instances must be in a dedicated subnet separate from VMs.

## Key Information
- **Azure Container constraint**: Twingate Connector runs as a Container Instance; Azure requires Container instances to be in a subnet that contains *only* containers -- VMs cannot share the subnet
- **Dedicated subnet required**: Must add a new subnet to the VNet specifically for the Connector container
- **Resources can be DNS or IP**: Define Resources by internal DNS name (if private DNS exists in the VNet) or by private IP address; users can only access the Resource at the defined address

## Prerequisites
- Azure subscription with a Virtual Network
- Twingate account with a Remote Network created

## Step-by-Step
1. Go to Virtual Networks > select VNet > add address space
2. Go to Subnets > add a new subnet using the new address space (for Container instances only)
3. Deploy Connector to the new subnet following the Azure Connector Deployment Guide
4. Verify Connector status is green in the Admin Console
5. Create Resources: use internal DNS name (e.g., `vm.internal.example.com`) or private IP
6. Connect with the Twingate Client -- Resources accessible via private address/DNS

## Configuration Values
None specific -- standard VNet, subnet, and Connector deployment.

## Gotchas
- Container subnet must be dedicated -- cannot contain VMs or other non-container resources; attempting mixed subnet deployment will fail
- If defining Resources by DNS name, the DNS name must be resolvable from the Connector's subnet via the VNet's private DNS

## Related Docs
- `/docs/azure` -- Azure Connector deployment guide (referenced in this doc)
- `/docs/connectors` -- general Connector deployment
- `/docs/resources` -- Resource configuration
- `/docs/private-dns-best-practices` -- private DNS in Azure VNets

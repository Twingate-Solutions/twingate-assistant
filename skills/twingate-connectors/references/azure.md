# Deploy a Connector on Azure

## Summary
Covers multiple deployment methods for Twingate Connectors on Azure: VM (Linux/Docker), Container Instances (ACI), AKS, and IaC. Azure Container Instances is the recommended approach, with deployment commands generated directly from the Admin Console.

## Key Information
- Azure Container Instances (ACI) is the recommended deployment method
- Admin Console generates a complete Azure CLI deployment command
- Container Instances typically require their own dedicated subnet
- Custom DNS servers in VNet are **not** automatically recognized by ACI — must specify manually
- Docker Hub rate limiting can cause `RegistryErrorResponse` errors on ACI deployments
- Connector tokens are instance-specific; never reuse tokens across Connector instances

## Prerequisites (ACI Deployment)
- Azure resource group name
- Virtual network name
- Subnet name (dedicated subnet recommended for ACI)
- DNS server IPs (if using custom DNS on VNet)
- Docker Hub account (optional but strongly recommended)
- Register ACI provider if first-time use: `az provider register --namespace Microsoft.ContainerInstance`

## Step-by-Step (ACI Deployment)
1. Admin Console → Remote Networks → select Remote Network → Add Connector
2. Click the new Connector → Deployment page → select **Azure** option
3. Generate tokens (requires re-authentication)
4. Fill in Azure environment details (resource group, VNet, subnet, optional DNS/Docker Hub)
5. Copy generated command → run in **Azure Cloud CLI**

## Configuration Values

**Docker Hub rate limit bypass flags:**
```bash
--registry-username "Docker Hub username" \
--registry-password "Docker Hub password" \
--registry-login-server index.docker.io
```
- Use a Personal Access Token (PAT) instead of password if using SSO login (Google/GitHub) to Docker Hub

## Deployment Options Summary
| Method | Notes |
|--------|-------|
| Azure VM | Follow standard Linux deployment docs; supports Docker or systemd (Ubuntu, Fedora, Debian, CentOS) |
| ACI | Recommended; Admin Console generates CLI command |
| AKS | Use official Twingate Helm chart |
| IaC | Terraform, Pulumi, or Twingate API |

## Gotchas
- Subnet must have **outbound Internet access** for image pulls and Twingate connectivity
- ACI does not inherit custom VNet DNS — configure DNS manually in deployment
- ACI typically requires a **dedicated subnet** (not shared with VMs or other resources)
- First ACI deployment in an Azure environment requires registering the `Microsoft.ContainerInstance` provider
- SSO Docker Hub users **must** use PAT instead of password

## Updates
- **VM/systemd**: Manual (package manager) or scheduled task; stagger updates across Connectors
- **ACI**: Update via Azure CLI — see Azure Connector Update Guide

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Twingate Helm Chart (AKS)](https://www.twingate.com/docs/kubernetes)
- [Azure Connector Update Guide](https://www.twingate.com/docs/update-azure-connector)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- Terraform / Pulumi / Twingate API deployment docs
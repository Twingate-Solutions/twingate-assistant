# Deploy a Connector on Azure

## Summary
Covers multiple deployment methods for Twingate Connectors on Azure: VM, Container Instance (ACI), AKS, and IaC. The recommended approach is Azure Container Instance (ACI) using the Admin Console's built-in Azure CLI command generator.

## Key Information
- Subnet must have outbound Internet access for image download and Twingate connectivity
- Docker-based deployment works on any 64-bit Linux Docker-compatible distro
- systemd service supported on Ubuntu, Fedora, Debian, CentOS only
- ACI recommended over VM deployment for simplicity
- Container Instances typically require a dedicated subnet in Azure
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Prerequisites (ACI Deployment)
- Azure Resource group name
- Virtual network name
- Subnet name (dedicated subnet strongly recommended for ACI)
- DNS servers (if using custom VNet DNS — must specify manually via "Custom DNS" option)
- Docker Hub account (optional but highly recommended to avoid rate limiting)

## Step-by-Step (ACI via Admin Console)
1. Admin Console → Remote Networks → select Remote Network → Add Connector
2. Click new Connector → Deployment page → select **Azure** option
3. Generate tokens (requires re-authentication)
4. Fill in Azure environment details (resource group, VNet, subnet, DNS, optional features)
5. Copy generated command → run in **Azure Cloud CLI**

## Configuration Values

**Docker Hub rate limit workaround** (append to deploy command):
```bash
--registry-username "Docker Hub username" \
--registry-password "Docker Hub password" \
--registry-login-server index.docker.io
```
- Use a Personal Access Token (PAT) instead of password if Docker Hub login uses SSO (Google/GitHub)

**Register ACI provider** (first-time ACI users):
```bash
az provider register --namespace Microsoft.ContainerInstance
```

## Gotchas
- Docker Hub rate limiting causes `RegistryErrorResponse` on ACI — use a Docker Hub account or PAT
- Custom VNet DNS servers are **not** automatically recognized by ACI; must configure "Custom DNS" manually
- Connector tokens are instance-specific — never reuse tokens across multiple Connector instances
- ACI typically requires its own dedicated subnet; create a new subnet within an existing VNet

## Deployment Options Summary
| Method | Notes |
|--------|-------|
| Azure VM | Follow Linux Connector guide; Docker or systemd |
| Azure Container Instance | Recommended; Admin Console generates CLI command |
| AKS | Use official Twingate Helm chart |
| IaC | Terraform, Pulumi, or Twingate API |

## Updates
- **VM (systemd):** Manual via package manager or scheduled task; stagger updates across Connectors
- **ACI:** Upgrade via Azure CLI — see [Azure Connector Update Guide]

## Related Docs
- Linux Connector Deployment
- Connector Best Practices (hardware recommendations for Azure)
- Azure Connector Update Guide
- Twingate Helm Chart (AKS)
- Kubernetes Best Practices Guide
- Terraform / Pulumi / Twingate API (IaC)
- Support peer-to-peer connections guide
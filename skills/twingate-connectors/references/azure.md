# How to Deploy a Connector on Azure

## Summary
Covers deploying Twingate Connectors on Azure via Virtual Machine, Azure Container Instance (ACI), or AKS. The recommended method is ACI using an Azure CLI command generated from the Admin Console. Subnet outbound internet access is required for all deployment types.

## Key Information
- Three deployment options: Azure VM (Linux), Azure Container Instance (recommended), AKS (Helm chart)
- IaC options: Terraform, Pulumi, or Twingate API
- Each Connector instance requires its own unique tokens — never reuse tokens across instances
- ACI typically requires a dedicated subnet (not shared with other resources)
- First-time ACI users may need to register the provider: `az provider register --namespace Microsoft.ContainerInstance`

## Prerequisites (ACI Deployment)
- Azure resource group name
- Virtual network name
- Subnet name (dedicated subnet recommended for ACI)
- DNS servers (if using custom VNet DNS — must be specified manually in Connector config)
- Docker Hub account (highly recommended to avoid rate limiting)

## Step-by-Step (ACI via Admin Console)
1. Admin Console → Remote Networks → select Remote Network → Add Connector
2. Click the new Connector → select **Azure** option on deployment page
3. Generate tokens (requires re-authentication)
4. Fill in Azure environment details (resource group, VNet, subnet, optional DNS/Docker Hub)
5. Copy generated CLI command → run in Azure Cloud CLI

## Configuration Values

**Docker Hub rate limit workaround** (append to deploy command):
```bash
--registry-username "Docker Hub username" \
--registry-password "Docker Hub password" \
--registry-login-server index.docker.io
```
- Use a Personal Access Token (PAT) instead of password if Docker Hub SSO is enabled (Google/GitHub login requires PAT)

**VM deployment**: Supports Docker on any 64-bit Linux; systemd service supported on Ubuntu, Fedora, Debian, CentOS

**AKS**: Use official Twingate Helm chart

## Gotchas
- Custom DNS servers on VNet are **not** auto-recognized by ACI — must specify manually via "Custom DNS" option
- Docker Hub rate limiting causes `RegistryErrorResponse` errors in ACI without a Docker Hub account
- ACI requires its own dedicated subnet in most Azure configurations
- Connector tokens are instance-specific; create separate definitions per Connector

## Updates
- VM (systemd): Manual via Linux package manager or scheduled task; stagger updates across Connectors
- ACI: Update via Azure CLI — see Azure Connector Update Guide

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [AKS / Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes)
- [Azure Connector Update Guide](https://www.twingate.com/docs/azure-connector-update)
- [Terraform/Pulumi/API Deployment](https://www.twingate.com/docs/deployment-automation)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
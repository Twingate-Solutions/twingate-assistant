# Deploy a Connector on Azure

## Summary
Covers multiple deployment options for Twingate Connectors on Azure: VM (Linux), Container Instance (ACI), AKS, and IaC. Azure Container Instance is the recommended approach with a built-in Admin Console deployment workflow.

## Key Information
- Subnet requires outbound Internet access for image download and Twingate connectivity
- ACI is the recommended deployment method; Admin Console generates the full CLI command
- Container Instances typically require a **dedicated subnet** (not shared with other resources)
- Each Connector instance needs its own unique tokens — never reuse tokens across instances
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Prerequisites (ACI Deployment)
- Azure Resource Group name
- Virtual Network name
- Subnet name (dedicated subnet recommended)
- DNS servers (if using custom VNet DNS — must specify manually)
- Docker Hub account (highly recommended to avoid rate limit errors)
- First-time ACI users must register the provider: `az provider register --namespace Microsoft.ContainerInstance`

## Step-by-Step (ACI Deployment)
1. Admin Console → Remote Networks → select network → **Add Connector**
2. Click the new Connector → deployment page → select **Azure** option
3. Scroll to Step 2 → generate tokens (requires re-authentication)
4. Scroll to Step 3 → fill in Resource Group, VNet, Subnet, optional DNS/Docker Hub settings
5. Scroll to Step 4 → copy generated command → run in **Azure Cloud CLI**

## Configuration Values

| Parameter | Description |
|---|---|
| `--registry-username` | Docker Hub username |
| `--registry-password` | Docker Hub password or PAT |
| `--registry-login-server` | `index.docker.io` |

> If Docker Hub SSO is used (Google/GitHub), a **Personal Access Token (PAT)** is required instead of a password.

## Deployment Options Summary

| Method | Notes |
|---|---|
| Azure VM | Follow general Linux instructions; Docker or systemd (Ubuntu, Fedora, Debian, CentOS) |
| Azure Container Instance | Recommended; Admin Console generates deploy command |
| AKS | Use official Twingate Helm chart |
| IaC | Terraform, Pulumi, or Twingate API |

## Gotchas
- Custom VNet DNS servers are **not** automatically recognized by ACI — specify manually via "Custom DNS" option
- Docker Hub rate limiting causes `RegistryErrorResponse` errors — use a Docker Hub account to avoid this
- ACI generally requires its own dedicated subnet — create a new one within existing VNet
- Must register `Microsoft.ContainerInstance` provider in Azure before first ACI deployment

## Updates
- **systemd (VM):** Manual via Linux package manager or scheduled task; stagger updates across Connectors
- **ACI:** Upgrade via Azure CLI — see Azure Connector Update Guide

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [AKS / Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes)
- [Twingate Helm Chart](https://www.twingate.com/docs/helm)
- [Azure Connector Update Guide](https://www.twingate.com/docs/update-connectors-azure)
- [Terraform/Pulumi/API deployment](https://www.twingate.com/docs/deployment-automation)
# Deploy a Connector on Azure

## Summary
Covers multiple methods for deploying Twingate Connectors on Azure: Virtual Machines (Linux), Azure Container Instances (ACI), and AKS. The recommended approach for most users is ACI via the Admin Console's guided deployment workflow with Azure CLI.

## Key Information
- Subnet requires outbound Internet access for container image download and Twingate connectivity
- ACI is the recommended deployment method; Admin Console generates the CLI command automatically
- Container Instances typically require their own dedicated subnet
- Docker Hub rate limiting can cause `RegistryErrorResponse` errors with ACI deployments
- Tokens are Connector-specific — never reuse tokens across Connector instances

## Prerequisites (ACI Deployment)
- Azure Resource Group name
- Virtual Network name
- Subnet name (dedicated subnet recommended for Container Instances)
- DNS servers (if using custom DNS on VNet — must be specified manually)
- Docker Hub account (optional but strongly recommended to avoid rate limits)
- ACI provider registered: `az provider register --namespace Microsoft.ContainerInstance`

## Step-by-Step (ACI Deployment)
1. Admin Console → Remote Networks → select Remote Network → **Add Connector**
2. Click the new Connector → deployment page → select **Azure** option
3. Scroll to Step 2 → generate tokens (re-authentication required)
4. Scroll to Step 3 → fill in Azure environment details and optional settings
5. Scroll to Step 4 → copy generated command → run in **Azure Cloud CLI**

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `--registry-username` | Docker Hub username |
| `--registry-password` | Docker Hub password or PAT |
| `--registry-login-server` | `index.docker.io` |

## Deployment Options Summary

| Method | Notes |
|--------|-------|
| Azure VM | Follow standard Linux deployment; supports Docker or systemd (Ubuntu, Fedora, Debian, CentOS) |
| Azure Container Instance | Recommended; Admin Console generates CLI command |
| AKS | Use official Twingate Helm chart |
| IaC | Terraform, Pulumi, or Twingate API |

## Gotchas
- Custom DNS servers on VNet are **not** automatically recognized by Container Instance service — must specify manually using "Custom DNS" option
- Docker Hub SSO users (Google/GitHub) **must** use a Personal Access Token (PAT), not a password
- First-time ACI users in an Azure environment need to register the provider namespace
- ACI typically cannot share a subnet with other resource types — create a dedicated subnet

## Updating Connectors
- **VM (systemd):** Manual via Linux package manager or scheduled task; stagger updates across Connectors
- **Container:** Use Azure CLI — see Azure Connector Update Guide

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Twingate Helm Chart (AKS)](https://www.twingate.com/docs/kubernetes)
- [Azure Connector Update Guide](https://www.twingate.com/docs/update-azure-connector)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- Terraform / Pulumi / Twingate API deployment docs
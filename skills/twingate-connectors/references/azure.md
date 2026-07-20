# Deploy a Connector on Azure

## Summary
Covers multiple deployment methods for Twingate Connectors on Azure: VM (Linux/Docker), Azure Container Instances (ACI), AKS, and IaC. ACI is the recommended approach with Admin Console generating the deployment command automatically.

## Key Information
- ACI is the recommended deployment method
- Admin Console generates the Azure CLI deployment command automatically
- Subnet must have outbound internet access for image pull and Twingate connectivity
- ACI requires a **dedicated subnet** (separate from other resources)
- Docker Hub rate limiting can cause `RegistryErrorResponse` errors on ACI deployments
- Connector tokens are unique per instance — never reuse tokens

## Prerequisites (ACI Deployment)
- Azure Resource group name
- Virtual network name
- Subnet name (dedicated subnet recommended for ACI)
- Optional: Custom DNS server IPs (if VNet uses custom DNS, must specify manually)
- Optional but recommended: Docker Hub account or PAT to avoid rate limiting
- First-time ACI users must register the provider:
  ```bash
  az provider register --namespace Microsoft.ContainerInstance
  ```

## Step-by-Step (ACI Deployment)
1. Admin Console → Remote Networks → select network → Add Connector
2. Click the new Connector → select **Azure** option on deployment page
3. Generate tokens (re-authentication required)
4. Fill in Azure environment details (resource group, VNet, subnet, optional DNS/Docker Hub)
5. Copy generated command → run in Azure Cloud CLI

## Configuration Values

**Docker Hub rate limit workaround** (append to generated command):
```bash
--registry-username "Docker Hub username" \
--registry-password "Docker Hub password" \
--registry-login-server index.docker.io
```
> Use a Personal Access Token (PAT) instead of password if using SSO (Google/GitHub)

## Deployment Options Summary

| Method | Notes |
|--------|-------|
| Azure VM | Follow Linux Connector docs; Docker or systemd (Ubuntu, Fedora, Debian, CentOS) |
| Azure Container Instance | Recommended; Admin Console generates CLI command |
| AKS | Use official Twingate Helm chart |
| IaC | Terraform, Pulumi, or Twingate API |

## Gotchas
- Custom DNS on VNet is **not** auto-recognized by ACI — must specify DNS servers manually via "Custom DNS" option
- Docker Hub anonymous pulls may hit rate limits → always use a Docker Hub account for ACI
- PAT required (not password) when Docker Hub login uses SSO
- ACI typically requires its own dedicated subnet; create a new one within existing VNet
- Do not reuse Connector tokens across instances
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- [Linux Connector Deployment](#)
- [Connector Best Practices](#)
- [Azure Connector Update Guide](#)
- [Systemd Connector Update Guide](#)
- [Twingate Helm Chart (AKS)](#)
- [Kubernetes Best Practices Guide](#)
- [Terraform / Pulumi / API Deployment](#)
- [Peer-to-Peer Connections](#)
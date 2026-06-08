# Deploy a Connector on Azure

## Summary
Covers multiple deployment options for Twingate Connectors on Azure: VM (Linux/Docker), Azure Container Instance (ACI), and AKS. The Admin Console provides an Azure CLI command generator for ACI deployments. Subnet must have outbound internet access.

## Key Information
- **Recommended method**: Azure Container Instance (ACI) via Admin Console-generated CLI command
- **VM options**: Docker (any 64-bit Linux) or systemd service (Ubuntu, Fedora, Debian, CentOS)
- **AKS**: Use official Twingate Helm chart
- **IaC**: Terraform, Pulumi, or Twingate API supported
- Each Connector instance requires its own unique tokens — never reuse tokens across instances

## Prerequisites (ACI Deployment)
- Azure Resource Group name
- Virtual Network name
- Subnet name (dedicate a new subnet to Container Instances — Azure typically requires this)
- DNS servers (if using custom VNet DNS; must be specified manually)
- Docker Hub account (highly recommended to avoid rate limit errors)
- First-time ACI users must register the service:
  ```bash
  az provider register --namespace Microsoft.ContainerInstance
  ```

## Step-by-Step: ACI Deployment
1. Admin Console → Remote Networks → select Remote Network → Add Connector
2. Click new Connector → Deployment page → select **Azure** option
3. Generate tokens (re-authentication required)
4. Fill in Azure environment details (resource group, VNet, subnet, optional DNS/Docker Hub)
5. Copy generated command → run in **Azure Cloud CLI**

## Configuration Values

**Docker Hub rate limit workaround** (append to deployment command):
```bash
--registry-username "DockerHub_username" \
--registry-password "DockerHub_password_or_PAT" \
--registry-login-server index.docker.io
```
> If using SSO (Google/GitHub) for Docker Hub, use a Personal Access Token (PAT) instead of password.

## Gotchas
- Custom DNS servers on a VNet are **not** automatically recognized by ACI — must specify DNS servers manually using "Custom DNS" option
- ACI deployment requires a **dedicated subnet** in most Azure environments
- `RegistryErrorResponse` error = Docker Hub rate limit; fix with Docker Hub credentials
- Docker Hub SSO users **must** use PAT, not password
- Stagger Connector updates across instances to avoid downtime

## Updating Connectors
- **systemd (VM)**: Manual via Linux package manager or scheduled task; see Systemd Connector Update Guide
- **ACI**: Via Azure CLI; see Azure Connector Update Guide

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices) — hardware recommendations for Azure
- [Azure Connector Update Guide](https://www.twingate.com/docs/azure-connector-update)
- [Twingate Helm Chart](https://www.twingate.com/docs/kubernetes) — AKS deployments
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- Terraform / Pulumi / Twingate API — IaC deployment
# Deploy a Connector on Azure

## Summary
Twingate Connectors can be deployed on Azure via Virtual Machines, Container Instances (ACI), AKS, or Infrastructure-as-Code tools. The recommended method is Azure Container Instances (ACI) using the Admin Console deployment workflow. Subnets must have outbound internet access.

## Key Information
- **Recommended deployment**: Azure Container Instances (ACI) via Admin Console
- **VM deployment**: Supports any 64-bit Linux + Docker; `systemd` service on Ubuntu, Fedora, Debian, CentOS
- **AKS**: Use official Twingate Helm chart
- **IaC options**: Terraform, Pulumi, Twingate API
- Container Instances typically require a **dedicated subnet**
- Peer-to-peer connections recommended for bandwidth Fair Use Policy compliance

## Prerequisites (ACI Deployment)
- Azure Resource Group name
- Virtual Network name
- Subnet name (dedicated subnet recommended)
- DNS server(s) — required if using custom VNet DNS (not auto-recognized by ACI)
- Docker Hub account (highly recommended to avoid rate limit errors)

## Step-by-Step (ACI Deployment)
1. Admin Console → Remote Networks → select Remote Network → Add Connector
2. Click new Connector → Deployment page → select **Azure** option
3. Generate tokens (requires re-authentication)
4. Fill in Azure environment details (resource group, VNet, subnet, optional DNS/Docker Hub)
5. Copy generated command → run in **Azure Cloud CLI**

## Configuration Values

**Register ACI provider (first-time only):**
```bash
az provider register --namespace Microsoft.ContainerInstance
```

**Docker Hub rate limit bypass parameters (append to deploy command):**
```bash
--registry-username "Docker Hub username" \
--registry-password "Docker Hub password" \
--registry-login-server index.docker.io
```
> Use a Personal Access Token (PAT) instead of password if Docker Hub SSO (Google/GitHub) is used — PAT is **required** in that case.

## Gotchas
- **Custom VNet DNS**: ACI does not inherit custom DNS servers automatically — must specify DNS manually using the "Custom DNS" option during deployment
- **Docker Hub rate limiting**: ACI deployments may fail with `RegistryErrorResponse` without a Docker Hub account
- **Dedicated subnet**: Azure usually requires Container Instances in their own subnet — create a new one within an existing VNet
- **Don't reuse Connector tokens**: Each Connector instance needs its own tokens/task definition
- **First-time ACI users**: Must register `Microsoft.ContainerInstance` provider before deploying

## Updating Connectors
- **VM (systemd)**: Manual via Linux package manager or scheduled task; stagger updates across Connectors
- **ACI**: Upgrade via Azure CLI — see Azure Connector Update Guide

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Twingate Helm Chart (AKS)](https://www.twingate.com/docs/kubernetes)
- [Terraform/Pulumi/API Deployment](https://www.twingate.com/docs/deployment-automation)
- [Azure Connector Update Guide](https://www.twingate.com/docs/azure-connector-update)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
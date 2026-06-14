# Deploy a Connector on Azure

## Summary
Covers multiple methods for deploying Twingate Connectors on Azure: VM (Linux/Docker), Container Instance (ACI), AKS, and IaC options. Azure Container Instance is the recommended approach, with a guided workflow in the Admin Console that generates a deployment command.

## Key Information
- Subnet must have outbound Internet access for image pulls and Twingate connectivity
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits
- ACI is the recommended deployment method
- Docker Hub rate limiting can cause `RegistryErrorResponse` errors on ACI deployments
- Container Instances typically require their own dedicated subnet in Azure

## Prerequisites (ACI Deployment)
- Azure Resource Group name
- Virtual network name
- Subnet name (dedicated subnet recommended)
- Docker Hub account (highly recommended to avoid rate limiting)
- Microsoft.ContainerInstance provider registered in Azure

## Step-by-Step (ACI Deployment)
1. Admin Console → Remote Networks → select Remote Network → Add Connector
2. Click new Connector → select **Azure** option on deployment page
3. Generate tokens (requires re-authentication)
4. Fill in Azure environment details (resource group, VNet, subnet, optional DNS/Docker Hub)
5. Copy generated command and run in **Azure Cloud CLI**

## Configuration Values

### Register ACI Provider (first-time only)
```bash
az provider register --namespace Microsoft.ContainerInstance
```

### Docker Hub Rate Limit Bypass Parameters
```
--registry-username "Docker Hub username"
--registry-password "Docker Hub password or PAT"
--registry-login-server index.docker.io
```

## Gotchas
- **Custom DNS**: VNet custom DNS servers are NOT automatically recognized by Container Instance service — must manually specify DNS servers using the "Custom DNS" option during deployment
- **Docker Hub SSO users** (Google/GitHub login): Must use a Personal Access Token (PAT), not a password
- **Subnet isolation**: Azure requires Container Instances in their own subnet in most cases — create a dedicated subnet before deploying
- **Token reuse**: Never reuse Connector tokens across instances; create separate task definitions per Connector
- **Updates (systemd/VM)**: Stagger updates across Connectors to avoid downtime

## Deployment Methods Summary
| Method | Notes |
|--------|-------|
| Azure VM | Follow standard Linux deployment; Docker or systemd (Ubuntu, Fedora, Debian, CentOS) |
| Azure Container Instance (ACI) | Recommended; Admin Console generates CLI command |
| AKS | Use official Twingate Helm chart |
| IaC | Terraform, Pulumi, or Twingate API |

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Twingate Helm Chart / AKS](https://www.twingate.com/docs/kubernetes)
- [Azure Connector Update Guide](https://www.twingate.com/docs/update-azure-connector)
- [Terraform/Pulumi/API Deployment](https://www.twingate.com/docs/deployment-automation)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
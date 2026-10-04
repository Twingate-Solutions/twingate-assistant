---
source: https://www.twingate.com/docs/azure
type: docs
fetched: 2026-10-04
source_version: 475a5df630a2d7bc1212c43aaac11d501bf66f6fa119d563e38565def736616d
trust: official
---

# How to Deploy a Connector on Azure

## Summary
Covers multiple deployment options for Twingate Connectors on Azure: VM (Linux), Container Instance (ACI), AKS, and IaC. The recommended path is Azure Container Instance (ACI) using a CLI command generated from the Admin Console.

## Key Information
- Subnet requires outbound Internet access for image download and Twingate connectivity
- ACI deployment is the recommended approach; Admin Console generates the full CLI command
- AKS deployment uses the official Twingate Helm chart
- IaC options: Terraform, Pulumi, or Twingate API
- Docker Hub rate limiting can cause `RegistryErrorResponse`; use a Docker Hub account to mitigate

## Prerequisites (ACI Deployment)
- Azure Resource group name
- Virtual network name
- Subnet name (dedicated subnet recommended for Container Instances)
- Optional: Custom DNS servers (must be specified manually if VNet uses non-default DNS)
- Optional but recommended: Docker Hub account or PAT (to avoid rate limit errors)
- First-time ACI users must register the provider:
  ```
  az provider register --namespace Microsoft.ContainerInstance
  ```

## Step-by-Step (ACI Deployment)
1. Admin Console → Remote Networks → select network → Add Connector
2. Click the new Connector → Deployment page → select **Azure** option
3. Generate tokens (re-authentication required)
4. Fill in Azure environment details (resource group, VNet, subnet, optional DNS/Docker Hub)
5. Copy the generated command and run it in Azure Cloud CLI

## Configuration Values

### Docker Hub Rate Limit Mitigation (append to deploy command)
```
--registry-username "Docker Hub username"
--registry-password "Docker Hub password or PAT"
--registry-login-server index.docker.io
```
> SSO users (Google/GitHub) **must** use a PAT instead of password.

## Gotchas
- **Dedicated subnet required**: Azure typically requires ACI to be in its own subnet; create a new subnet within an existing VNet
- **Custom DNS**: VNet custom DNS servers are not automatically inherited by Container Instances — specify them manually via the "Custom DNS" option
- **Token reuse**: Connector tokens are instance-specific; create separate definitions per Connector instance — never reuse tokens
- **Docker Hub SSO**: Must use a Personal Access Token (PAT), not a password

## Updates
- **VM (systemd)**: Manual via Linux package manager or scheduled task; see Systemd Connector Update Guide
- **ACI**: Updated via Azure CLI; see Azure Connector Update Guide
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- Connector Best Practices (hardware recommendations for Azure)
- Peer-to-peer connections guide
- AKS / Kubernetes Best Practices Guide
- Twingate Helm chart
- Azure Connector Update Guide
- Terraform / Pulumi / Twingate API deployment docs
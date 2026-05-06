# Deploy a Connector on Azure

## Summary
Covers deployment options for Twingate Connectors on Azure including Virtual Machines, Container Instances (ACI), and AKS. The recommended approach is Azure Container Instance (ACI) using the Admin Console's built-in Azure CLI command generator.

## Key Information
- Three deployment methods: Azure VM (Linux), Azure Container Instance (ACI), AKS (Helm chart)
- ACI deployment is recommended; Admin Console generates the full CLI command
- Subnet must have outbound Internet access for image download and Twingate connectivity
- Connector tokens are instance-specific — never reuse tokens across Connector instances

## Prerequisites (ACI Deployment)
- Azure resource group name
- Virtual network name
- Subnet name (dedicated subnet strongly recommended for ACI)
- DNS servers (if using custom VNet DNS — must specify manually via "Custom DNS" option)
- Docker Hub account (optional but highly recommended to avoid rate limiting)
- Register ACI provider if first-time ACI user:
  ```bash
  az provider register --namespace Microsoft.ContainerInstance
  ```

## Step-by-Step (ACI Deployment)
1. Admin Console → Remote Networks → select Remote Network → **Add Connector**
2. Click new Connector → Deployment page → select **Azure** option
3. Scroll to Step 2 → generate tokens (re-authentication required)
4. Scroll to Step 3 → fill in Azure environment details and optional settings
5. Scroll to Step 4 → copy generated command → run in **Azure Cloud CLI**

## Configuration Values

**Docker Hub rate limit workaround** (append to deployment command):
```bash
--registry-username "Docker Hub username" \
--registry-password "Docker Hub password" \
--registry-login-server index.docker.io
```
> Use a Personal Access Token (PAT) instead of password if Docker Hub login uses SSO (Google/GitHub).

## Gotchas
- Custom DNS servers on VNet are **not** automatically recognized by ACI — must specify manually
- Docker Hub rate limiting causes `RegistryErrorResponse` errors — use a Docker Hub account to avoid
- ACI typically requires a **dedicated subnet** (separate from other resources)
- `systemd` service support limited to: Ubuntu, Fedora, Debian, CentOS
- Stagger Connector updates across instances to avoid downtime

## Updates
- **VM/systemd**: Manual via Linux package manager or scheduled task → [Systemd Connector Update Guide]
- **ACI**: Via Azure CLI → [Azure Connector Update Guide]

## Related Docs
- [Linux Connector Deployment](#)
- [Connector Best Practices](#)
- [AKS / Helm Chart Deployment](#)
- [Terraform / Pulumi / API Deployment](#)
- [Peer-to-peer connections](#)
- [Fair Use Policy](#)
---
source: https://www.twingate.com/docs/azure
type: docs
fetched: 2026-08-14
source_version: 7104f96eaa3481601055080fc02726e8f43f68611ad134f5fa47b484b3a4d6ac
---

# Deploy a Connector on Azure

## Summary
Covers multiple methods for deploying Twingate Connectors on Azure: VM (Linux-based), Azure Container Instance (ACI), AKS, and IaC. ACI is the recommended approach, with deployment commands generated directly from the Admin Console.

## Key Information
- Subnet must have outbound internet access for image download and Twingate connectivity
- Peer-to-peer connections recommended for bandwidth Fair Use Policy compliance
- ACI is the recommended deployment method
- Docker Hub rate limiting can cause `RegistryErrorResponse` errors with ACI deployments

## Prerequisites (ACI Deployment)
- Azure Resource Group name
- Virtual Network name
- Subnet name (dedicated subnet required for Container Instances in most cases)
- DNS servers (if using custom VNet DNS — must specify manually, not auto-detected)
- Docker Hub account (optional but strongly recommended to avoid rate limiting)

## Step-by-Step (ACI)

1. Admin Console → **Remote Networks** → select network → **Add Connector**
2. Click new Connector → deployment page → select **Azure** option
3. Generate tokens (requires re-authentication)
4. Fill in Azure environment details (resource group, VNet, subnet, DNS, Docker Hub)
5. Copy generated command → run in **Azure Cloud CLI**

## Configuration Values

**Register ACI provider (first-time only):**
```bash
az provider register --namespace Microsoft.ContainerInstance
```

**Docker Hub rate limit bypass parameters:**
```bash
--registry-username "Docker Hub username" \
--registry-password "Docker Hub password or PAT" \
--registry-login-server index.docker.io
```

## Gotchas
- Container Instances must be deployed into a **dedicated subnet** — create a new subnet within an existing VNet
- Custom VNet DNS servers are **not** auto-recognized by ACI; must use "Custom DNS" option and specify manually
- Docker Hub SSO users (Google/GitHub) **must** use a Personal Access Token (PAT), not a password
- Connector tokens are instance-specific — **do not reuse tokens** across multiple Connectors; create separate task definitions per instance
- First ACI deployment in an environment requires registering `Microsoft.ContainerInstance` provider

## VM-Specific Notes
- Docker: any 64-bit Linux Docker-compatible distro
- systemd service: Ubuntu, Fedora, Debian, CentOS only
- Updates via Linux package manager or scheduled task; stagger updates across Connectors to avoid downtime

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [AKS / Helm Chart Deployment](https://www.twingate.com/docs/kubernetes)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Azure Connector Update Guide](https://www.twingate.com/docs/azure-connector-update)
- [Terraform / Pulumi / API deployment](https://www.twingate.com/docs/infrastructure-as-code)
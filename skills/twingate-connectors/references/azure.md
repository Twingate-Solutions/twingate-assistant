## Deploy Connector on Azure

Multiple deployment options for Twingate Connectors on Azure: Azure VM (Linux), Azure Container Instance (ACI), and AKS.

**Azure VM Deployment:**
- Follow standard Linux Connector deployment instructions (Docker or systemd)
- Supported on any 64-bit Linux distro (Docker) or Ubuntu/Fedora/Debian/CentOS (systemd)

**Azure Container Instance (recommended):**
- Admin Console → Connector → Azure option → Generate Tokens → fill environment info → copy and run Azure CLI command
- Required info: Resource group name, Virtual network name, Subnet name
- Optional: custom DNS servers, Docker Hub credentials

**Prerequisites for ACI:**
- Container Instances typically require their own dedicated subnet — create a new subnet in an existing VNet
- If first-time ACI deployment: `az provider register --namespace Microsoft.ContainerInstance`
- If using custom DNS servers on your VNet: specify them via the Custom DNS option at deploy time (Container Instance does not inherit VNet DNS automatically)

**Docker Hub Rate Limiting:**
- ACI pulls from Docker Hub and may hit rate limits (`RegistryErrorResponse`)
- Workaround: add `--registry-username`, `--registry-password`, `--registry-login-server index.docker.io` to the deploy command
- If using SSO to Docker Hub (Google/GitHub): use a Personal Access Token instead of a password

**AKS Deployment:**
- Use the official Twingate Helm chart; see Kubernetes Best Practices Guide

**IaC:**
- Terraform, Pulumi, or Twingate API

**Gotchas:**
- Subnet requires outbound internet access
- Do not reuse tokens across Connector instances

**Related Docs:**
- /docs/connectors-on-linux -- Linux deployment details
- /docs/connector-best-practices -- Best practices and hardware recommendations

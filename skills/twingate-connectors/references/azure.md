---
source: https://www.twingate.com/docs/azure
type: docs
fetched: 2026-11-13
source_version: cd08fd0dd59e0ff41e34ec19f20028c2d0523376c5315ec7583831e61e41d7de
trust: official
---

# How to Deploy a Connector on Azure

## Summary
Twingate Connectors can be deployed on Azure via Container Instances (recommended), custom Linux VMs, AKS (Helm), or IaC tools. The Admin Console generates an Azure CLI command for Container Instance deployment. The Connector subnet needs outbound Internet access.

## Key Information
- **Azure Container Instance (ACI)** is the recommended method. The Admin Console deployment page generates a ready-to-run `az` command.
- **Azure VM**: follow the general Linux Connector instructions. Docker deployment works on any 64-bit Linux distro Docker supports. The `systemd` service is supported on Ubuntu, Fedora, Debian, and CentOS.
- **AKS**: use the official Twingate Helm chart (see Kubernetes Best Practices Guide).
- **IaC**: Terraform, Pulumi, or the Twingate API.
- Enable peer-to-peer connections to improve user experience and stay within the Fair Use Policy on bandwidth.
- Azure generally requires Container Instances to be in their own subnet. Create a new subnet in an existing VNet.

## Prerequisites
- Resource group name
- Virtual network name
- Subnet name (dedicated to the Container Instance)
- Outbound Internet access from the subnet (to pull the container image and reach Twingate)
- Optional: custom DNS server addresses
- Optional but highly recommended: Docker Hub account

## Step-by-Step (ACI)
1. If this is your first ACI deployment, register the provider: `az provider register --namespace Microsoft.ContainerInstance`
2. In the Admin Console, go to Remote Networks, select the Remote Network, and click **Add Connector**.
3. Open the new Connector and choose the **Azure** option at the top of the deployment page.
4. In step 2, click the button to generate tokens (you will re-authenticate and return to the page).
5. In step 3, enter your Azure environment details and configure optional features.
6. In step 4, copy the completed command and run it in Azure Cloud CLI.

## Configuration Values
Add these parameters to the deployment command to authenticate to Docker Hub:
```
--registry-username "<Docker Hub username>" --registry-password "<password or PAT>" --registry-login-server index.docker.io
```
- A personal access token (PAT) can replace the password.
- SSO users (Google, GitHub) **must** use a PAT.

## Gotchas
- Docker Hub rate limiting can cause a `RegistryErrorResponse` error; authenticating to Docker Hub avoids it.
- ACI does not automatically recognize custom DNS servers configured on the VNet. Use the "Custom DNS" option in the deployment form and specify servers manually.
- Do not reuse Connector tokens. Tokens are per running Connector, so create a separate deployment for each instance.
- Stagger updates across multiple Connectors to avoid downtime.
- ACI may fail if not deployed in its own subnet.

## Updating
- **systemd on a VM**: update via the Linux package manager or a scheduled task (see Systemd Connector Update Guide).
- **ACI**: upgrade through the Azure CLI (see Azure Connector Update Guide).

## Related Docs
- Best Practices for Connectors (including Azure hardware recommendations)
- Linux Connector deployment
- Peer-to-peer connections
- Kubernetes Best Practices Guide / Twingate Helm chart
- Terraform, Pulumi, Twingate API
- Systemd Connector Update Guide
- Azure Connector Update Guide
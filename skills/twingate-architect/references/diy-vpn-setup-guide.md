---
source: https://www.twingate.com/docs/diy-vpn-setup-guide
type: docs
fetched: 2026-11-22
source_version: 5384fa5b42f02c526f3a28048d298a9e798210fee02d762a04cc693ad2f8dc60
trust: official
---

# Complete DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Guide for building a self-hosted, globally distributed VPN (exit nodes) using Twingate Exit Networks and DigitalOcean. Three deployment paths are offered: Minikube (local), DigitalOcean Droplets (Terraform), and DigitalOcean Kubernetes (Terraform + Helm). Code lives in the Twingate-Community/diy-vpn repository (https://github.com/Twingate-Community/diy-vpn).

## Key Information
- For personal or internal use only. Do not offer a commercial VPN service. Bandwidth through Twingate infrastructure is subject to the Fair Use Policy (https://www.twingate.com/terms/sa).
- Methods: Minikube (free, beginner, testing), Droplets (low cost, small teams), DOKS (medium-high cost, auto-scaling, enterprise).
- Droplet regions: tor1, nyc1, nyc3, sfo1, sfo3, ams3, fra1, lon1, sgp1, blr1, syd1.
- Verification in the Twingate Admin Console: Internet Security → Exit Networks (Minikube); Remote Networks such as `do_tor1`, `do_nyc1` (Droplets). Connectors should show "Connected".
- Client check: exit nodes appear under "Route all traffic through Twingate".

## Prerequisites
- Twingate Home or another plan that includes Exit Networks (not available on the free Starter plan)
- DigitalOcean account, GitHub account, Twingate Client installed
- Local: macOS, Linux, or Windows with WSL2; 4GB+ RAM (8GB+ for Kubernetes); 10GB+ disk; Docker Desktop (for Minikube)
- Tools: minikube, kubectl, helm (Method 1); terraform (Method 2); terraform, doctl, kubectl, helm (Method 3)

## Step-by-Step
1. **Twingate API token**: Admin Console → Settings → API → Generate API Token, with Read, Write, and Provision permissions. It is shown only once.
2. **DigitalOcean token**: Control Panel → API → Generate New Token, with Full Access scope (customizable).
3. **Network name**: the subdomain of your Twingate URL (`mycompany` for `mycompany.twingate.com`).
4. Clone the repo: `git clone https://github.com/Twingate-Community/diy-vpn.git`
5. **Minikube**:
   - `cd diy-vpn/minikube`
   - `minikube start --cpus=2 --memory=4096 --driver=docker`
   - `cp values-example.yaml values.yaml`, edit it, then run `./deploy.sh`
6. **Droplets**:
   - `cd diy-vpn/digital_ocean/droplet`
   - `cp terraform.tfvars.example terraform.tfvars`, edit it
   - `terraform init && terraform plan && terraform apply`
7. **DOKS**:
   - `cd diy-vpn/digital_ocean/kubernetes`
   - Same tfvars and Terraform steps as Droplets
   - `doctl kubernetes cluster kubeconfig save <cluster>`

## Configuration Values
- **Minikube `values.yaml`** (under `twingate-operator.twingateOperator`): `network`, `apiKey`, `remoteNetworkId` (from `https://{network}.twingate.com/exit-networks/{remoteNetworkId}`), `logFormat: "json"`, `logVerbosity: "debug"`
- **Terraform vars**: `do_token`, `tg_api_token`, `tg_network`, `environment`
- **`droplets` map**: `region`, `size` (e.g. `s-1vcpu-1gb`), `count`, `image` (`ubuntu-24-04-x64`)
- **`clusters` map**: `region`, `node_size`, `node_count`, or `min_count`/`max_count`/`auto_scale`

## Gotchas
- Network name must match exactly, and the API token needs the correct permissions, or the Connector won't appear.
- Terraform failures: check that the DO token has write access, region availability, and no state lock.
- Minikube: ensure Docker is running; if resources are short, use `--memory=8192 --cpus=4`, or reset with `minikube delete && minikube start`.
- Keep tokens and tfvars files out of version control.
- Use `terraform destroy` to avoid charges from test environments.
- The Ubuntu install steps in the source include pipe-to-shell and download commands from third-party hosts. Follow the official Helm, Minikube, and kubectl install docs instead.

## Related Docs
- Exit Networks (https://www.twingate.com/docs/exit-networks)
- Remote Networks (https://www.twingate.com/docs/remote-networks)
- Devices (https://www.twingate.com/docs/devices)
- Analytics (https://www.twingate.com/docs/analytics)
- Connector troubleshooting (https://www.twingate.com/docs/troubleshooting)
- API overview (https://www.twingate.com/docs/api-overview)
- Twingate plans (https://www.twingate.com/pricing)
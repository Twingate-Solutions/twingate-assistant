---
source: https://www.twingate.com/docs/diy-vpn-setup-guide
type: docs
fetched: 2026-08-14
source_version: 41eace518134887d3d660f9ea41d35825360e1f9ee2647281e771ca64055b4a5
---

# DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Step-by-step guide to deploy a self-managed VPN using Twingate's zero-trust networking on DigitalOcean infrastructure. Offers three deployment methods (Minikube, DO Droplets, DO Kubernetes) with Terraform and Helm. For personal/internal use only—commercial VPN services are prohibited.

## Key Information
- Three deployment paths: local Minikube (free/beginner), DigitalOcean Droplets (low cost/medium), DigitalOcean Kubernetes (enterprise/auto-scaling)
- Uses Twingate Exit Networks feature—requires **Home plan or higher** (not available on free Starter)
- Source repo: `github.com/Twingate-Community/diy-vpn`
- Twingate network name = subdomain of your Twingate URL (e.g., `mycompany` from `mycompany.twingate.com`)

## Prerequisites
- Twingate account (Home plan+), DigitalOcean account, GitHub account
- Twingate API token with **Read, Write, and Provision** permissions
- DigitalOcean API token with **Full Access**
- Docker Desktop (Minikube method)
- Tools by method:
  - Minikube: `minikube`, `kubectl`, `helm`
  - Droplets: `terraform`
  - Kubernetes: `terraform`, `doctl`, `kubectl`, `helm`

## Configuration Values

### Minikube (`values.yaml`)
```yaml
twingate-operator:
  twingateOperator:
    network: "your-company"
    apiKey: "your_twingate_api_key"
    remoteNetworkId: ""
    logFormat: "json"
    logVerbosity: "debug"
```

### Droplets (`terraform.tfvars`)
```hcl
do_token     = "dop_v1_..."
tg_api_token = "..."
tg_network   = "your-network-name"
droplets = {
  "toronto-vpn" = { region = "tor1", size = "s-1vcpu-1gb", count = 1, image = "ubuntu-24-04-x64" }
}
environment = "production"
```

### Kubernetes (`terraform.tfvars`)
```hcl
do_token     = "..."
tg_api_token = "..."
tg_network   = "..."
clusters = {
  "nyc-cluster" = { region = "nyc1", node_size = "s-2vcpu-4gb", min_count = 1, max_count = 3, auto_scale = true }
}
```

## Step-by-Step (Minikube)
1. `git clone https://github.com/Twingate-Community/diy-vpn.git && cd diy-vpn/minikube`
2. `minikube start --cpus=2 --memory=4096 --driver=docker`
3. `cp values-example.yaml values.yaml` → edit credentials
4. `./deploy.sh`
5. Verify: `kubectl get pods -n twingate` and check Admin Console → Internet Security → Exit Networks

## Step-by-Step (Droplets/Kubernetes)
1. `cd diy-vpn/digital_ocean/droplet` (or `kubernetes`)
2. `cp terraform.tfvars.example terraform.tfvars` → edit credentials
3. `terraform init && terraform plan && terraform apply`
4. Verify connectors in Twingate Admin Console → Remote Networks

## Gotchas
- Exit Networks not available on free Starter plan
- API token shown only once at creation—store immediately
- Network name must match exactly (case-sensitive)
- Minikube: increase resources if failing (`--memory=8192 --cpus=4`); reset with `minikube delete && minikube start`
- Terraform locked state will block `apply`—check DigitalOcean API token write permissions
- Bandwidth subject to Twingate Fair Use Policy

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twin
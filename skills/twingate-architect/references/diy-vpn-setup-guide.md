# DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Step-by-step guide for deploying a self-managed VPN using Twingate zero-trust networking on DigitalOcean infrastructure. Offers three deployment methods (Minikube, DO Droplets, DO Kubernetes) with Terraform/Helm/Kubernetes tooling. For personal/internal use only—commercial VPN services are prohibited.

## Key Information
- Three deployment methods: Minikube (local/free), DigitalOcean Droplets (low cost), DigitalOcean Kubernetes (enterprise)
- Requires Twingate Home plan or higher (Exit Networks not available on free Starter plan)
- Source repo: `github.com/Twingate-Community/diy-vpn`
- Twingate network name = subdomain from `https://<name>.twingate.com`

## Prerequisites
- Twingate account (Home plan minimum), DigitalOcean account, GitHub account
- Twingate Client installed on connecting device
- Docker Desktop (required for Minikube method)
- 4GB+ RAM (8GB+ for Kubernetes), 10GB+ disk, macOS/Linux/WSL2

## API Key Setup
**Twingate:** Admin Console → Settings → API → Generate Token → grant **Read, Write, and Provision** permissions

**DigitalOcean:** Control Panel → API → Generate New Token → **Full Access**

## Step-by-Step by Method

### Method 1: Minikube
```bash
git clone https://github.com/Twingate-Community/diy-vpn.git
cd diy-vpn/minikube
minikube start --cpus=2 --memory=4096 --driver=docker
cp values-example.yaml values.yaml
# Edit values.yaml, then:
./deploy.sh
```

### Method 2: DigitalOcean Droplets
```bash
cd diy-vpn/digital_ocean/droplet
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars, then:
terraform init && terraform plan && terraform apply
```

### Method 3: DigitalOcean Kubernetes
```bash
cd diy-vpn/digital_ocean/kubernetes
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform plan && terraform apply
```

## Configuration Values

| Variable | Description |
|---|---|
| `tg_network` / `network` | Twingate network subdomain |
| `tg_api_token` / `apiKey` | Twingate API token |
| `do_token` | DigitalOcean API token |
| `remoteNetworkId` | From `https://{network}.twingate.com/exit-networks/{id}` |
| `region` | DO region code (e.g., `tor1`, `nyc1`, `fra1`, `sgp1`) |
| `node_size` | DO droplet/node size (e.g., `s-1vcpu-1gb`) |
| `auto_scale` | Boolean; requires `min_count`/`max_count` |

## Gotchas
- Exit Networks require paid plan—won't work on Starter
- API token shown only once at creation—store immediately
- Network name must match exactly (case-sensitive)
- Minikube requires Docker Desktop running before `minikube start`
- Terraform state lock can block re-runs if prior apply failed
- Bandwidth subject to Twingate Fair Use Policy

## Troubleshooting
- Connector missing: verify API token permissions, check network name spelling
- Terraform fails: confirm DO token has write permissions, check region availability
- Minikube: increase resources with `--memory=8192 --cpus=4`; reset with `minikube delete && minikube start`

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs/connector-issues)
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [DigitalOcean Terraform Provider](https://registry.terraform.io/providers/digitalocean/digitalocean/latest/docs
# DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Step-by-step guide for deploying a self-managed VPN using Twingate zero-trust networking on DigitalOcean infrastructure. Offers three deployment methods: local Minikube, DigitalOcean Droplets (Terraform), and DigitalOcean Kubernetes. For personal/internal use only—commercial VPN offerings are prohibited.

## Key Information
- Three deployment methods with increasing complexity: Minikube → Droplets → Kubernetes
- Requires Twingate Home plan or higher (Exit Networks not available on free Starter plan)
- Source repo: `https://github.com/Twingate-Community/diy-vpn`
- Twingate network name = subdomain from your Twingate URL (e.g., `mycompany` from `mycompany.twingate.com`)

## Prerequisites
- **Accounts**: Twingate (Home+ plan), DigitalOcean, GitHub
- **Software**: Twingate Client, Docker Desktop (Minikube), Terraform (Droplets/K8s), kubectl, Helm, doctl (K8s only)
- **System**: 4GB+ RAM (8GB+ for K8s), 10GB+ disk, macOS/Linux/WSL2

## API Key Setup
**Twingate**: Settings → API → Generate API Token → grant **Read, Write, and Provision** permissions

**DigitalOcean**: API → Generate New Token → **Full Access** scope

## Step-by-Step by Method

### Method 1: Minikube
```bash
git clone https://github.com/Twingate-Community/diy-vpn.git && cd diy-vpn/minikube
minikube start --cpus=2 --memory=4096 --driver=docker
cp values-example.yaml values.yaml  # edit with credentials
./deploy.sh
kubectl get pods -n twingate
```

### Method 2: DigitalOcean Droplets
```bash
cd diy-vpn/digital_ocean/droplet
cp terraform.tfvars.example terraform.tfvars  # edit with credentials
terraform init && terraform plan && terraform apply
```

### Method 3: DigitalOcean Kubernetes
```bash
cd diy-vpn/digital_ocean/kubernetes
cp terraform.tfvars.example terraform.tfvars  # edit with credentials
terraform init && terraform plan && terraform apply
doctl kubernetes cluster kubeconfig save <cluster-name>
```

## Configuration Values

| Variable | Description |
|---|---|
| `tg_network` / `network` | Twingate network subdomain |
| `tg_api_token` / `apiKey` | Twingate API token |
| `do_token` | DigitalOcean API token |
| `remoteNetworkId` | Exit network ID from Twingate console |
| `node_size` | DO droplet size (e.g., `s-1vcpu-1gb`) |
| `auto_scale` | Enable K8s autoscaling (bool) |
| `min_count` / `max_count` | K8s node scaling bounds |

## Gotchas
- Twingate API token is shown **only once**—copy immediately
- Free Starter plan does **not** include Exit Networks; requires Home plan minimum
- Minikube requires Docker Desktop running before `minikube start`
- Terraform state lock can block redeployment if prior apply failed
- Network name in config must **exactly match** Twingate subdomain (case-sensitive)
- Bandwidth subject to Twingate Fair Use Policy

## Troubleshooting
- Connector missing in console → verify API token permissions, check network name spelling
- `terraform apply` fails → verify DO token has write permissions, check region availability
- Minikube issues → increase resources: `minikube start --memory=8192 --cpus=4`
- K8s problems → `kubectl logs -n twingate deployment/twingate-operator`

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs/connector-issues)
- [Twingate API Reference
# DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Step-by-step guide for deploying a self-managed VPN using Twingate's zero-trust networking on DigitalOcean infrastructure. Offers three deployment methods: local Minikube (learning), DigitalOcean Droplets (simple production), and DigitalOcean Kubernetes (enterprise). Internal/personal use only — not for commercial VPN services.

## Key Information
- Three deployment methods: Minikube, DO Droplets (Terraform), DO Kubernetes (Terraform)
- Requires Twingate Home plan or higher (Exit Networks not available on free Starter plan)
- Repository: `github.com/Twingate-Community/diy-vpn`
- Twingate network name = subdomain from `https://<networkname>.twingate.com`

## Prerequisites
- Accounts: Twingate (Home+), DigitalOcean, GitHub
- Twingate Client installed on connecting devices
- System: macOS/Linux/WSL2, 4GB+ RAM (8GB+ for Kubernetes), 10GB+ disk
- Docker Desktop required for Minikube method

## API Token Requirements
- **Twingate**: Settings → API → Generate token with **Read, Write, and Provision** permissions
- **DigitalOcean**: API → Generate token with **Full Access**

## Deployment Methods

### Method 1: Minikube
```bash
git clone https://github.com/Twingate-Community/diy-vpn.git
cd diy-vpn/minikube
minikube start --cpus=2 --memory=4096 --driver=docker
cp values-example.yaml values.yaml
# Edit values.yaml, then:
./deploy.sh
```

### Method 2: DigitalOcean Droplets (Terraform)
```bash
cd diy-vpn/digital_ocean/droplet
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform plan && terraform apply
```

### Method 3: DigitalOcean Kubernetes (Terraform)
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
| `remoteNetworkId` | From Exit Networks URL |
| `region` | DO region slug (e.g., `tor1`, `nyc1`, `fra1`) |
| `node_size` / `size` | Droplet size (e.g., `s-1vcpu-1gb`) |
| `auto_scale` | Boolean, Kubernetes only |
| `min_count` / `max_count` | Auto-scale bounds, Kubernetes only |

## Verification Commands
```bash
kubectl get pods -n twingate
kubectl get twingateconnectors -n twingate
kubectl logs -f -l app.kubernetes.io/name=twingate-operator -n twingate
terraform output
```

## Gotchas
- API token not shown again after creation — copy immediately
- Connector not appearing: verify token permissions and exact network name match
- Minikube reset: `minikube delete && minikube start`
- `terraform destroy` test environments to avoid unnecessary costs
- Terraform state lock can block reapply if prior run failed

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs/connector-issues)
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [DigitalOcean Terraform Provider](https://registry.terraform.io/providers/digitalocean/digitalocean/latest/docs)
- [Twingate Plans Comparison](https://www.twingate.com/pricing)
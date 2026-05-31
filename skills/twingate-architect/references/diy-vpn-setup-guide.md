# DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Build a self-managed VPN using Twingate zero-trust networking and DigitalOcean cloud infrastructure. Three deployment methods are offered: local Minikube (learning), DigitalOcean Droplets (simple production), and DigitalOcean Kubernetes (enterprise). For internal/personal use only — commercial VPN services are prohibited.

## Key Information
- Requires Twingate Home plan or higher (Exit Networks not available on free Starter)
- Three methods: Minikube (free/local), DO Droplets (low cost), DO Kubernetes (medium-high cost)
- Repository: `https://github.com/Twingate-Community/diy-vpn`
- Twingate network name = subdomain from your Twingate URL (e.g., `mycompany` from `mycompany.twingate.com`)

## Prerequisites
- Accounts: Twingate (Home+), DigitalOcean, GitHub
- Twingate Client installed on connecting device
- Twingate API token with **Read, Write, and Provision** permissions
- DigitalOcean API token with **Full Access**
- Docker Desktop (Minikube), Terraform (Droplets/K8s), kubectl + Helm (K8s)
- 4GB+ RAM, 10GB+ disk, WSL2 on Windows

## Step-by-Step

### Method 1: Minikube
```bash
git clone https://github.com/Twingate-Community/diy-vpn.git
cd diy-vpn/minikube
minikube start --cpus=2 --memory=4096 --driver=docker
cp values-example.yaml values.yaml
# Edit values.yaml with credentials
./deploy.sh
kubectl get pods -n twingate
```

### Method 2: DigitalOcean Droplets
```bash
cd diy-vpn/digital_ocean/droplet
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars
terraform init && terraform plan && terraform apply
```

### Method 3: DigitalOcean Kubernetes
```bash
cd diy-vpn/digital_ocean/kubernetes
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars
terraform init && terraform plan && terraform apply
doctl kubernetes cluster kubeconfig save <cluster-name>
```

## Configuration Values

| Variable | Description |
|---|---|
| `tg_api_token` / `apiKey` | Twingate API token |
| `tg_network` / `network` | Twingate network subdomain |
| `do_token` | DigitalOcean API token |
| `remoteNetworkId` | From `https://{network}.twingate.com/exit-networks/{id}` |
| `region` | DO region code (e.g., `tor1`, `nyc1`, `fra1`) |
| `node_size` | Droplet/node size (e.g., `s-1vcpu-1gb`) |
| `auto_scale` | Boolean; enables K8s autoscaling |
| `min_count` / `max_count` | Autoscaling node bounds |

## Gotchas
- API token displayed only once at creation — save immediately
- Free Starter plan does not include Exit Networks
- Minikube needs Docker running before `minikube start`
- Terraform region availability varies by DigitalOcean account
- Connector name must match exactly in Twingate console
- Use `terraform destroy` to avoid charges on test environments

## Troubleshooting
- Connector missing: verify API permissions, exact network name match
- Minikube issues: `minikube delete && minikube start`, increase `--memory=8192`
- K8s issues: `kubectl logs -n twingate deployment/twingate-operator`

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs)
- [Twingate API Reference](https://www.twingate.com/docs)
- [DigitalOcean Terraform Provider](https://registry
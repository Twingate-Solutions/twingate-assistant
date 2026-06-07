# DIY VPN Setup Guide (Twingate + DigitalOcean)

## Summary
Deploys a self-hosted VPN infrastructure using Twingate's zero-trust networking and DigitalOcean's cloud platform. Offers three deployment methods (Minikube, DO Droplets, DO Kubernetes) for different use cases. Internal/personal use only — commercial VPN services are prohibited.

## Key Information
- Three deployment paths: local Minikube (free), DO Droplets (low cost), DO Kubernetes (medium-high cost)
- Requires Twingate Home plan or higher (Exit Networks not available on free Starter plan)
- GitHub repo: `https://github.com/Twingate-Community/diy-vpn`
- Bandwidth subject to Twingate Fair Use Policy

## Prerequisites
- Twingate account (Home plan+), DigitalOcean account, GitHub account
- Twingate Client installed on connecting device
- Twingate API token: Settings → API → Generate (Read, Write, Provision permissions)
- DigitalOcean API token: Full Access scope
- Network name = subdomain of `https://<network>.twingate.com`
- Docker Desktop (Minikube); Terraform (Droplets/K8s); `doctl`, `kubectl`, `helm` (K8s)
- 4GB+ RAM, 10GB+ disk, macOS/Linux/WSL2

## Step-by-Step

### Method 1: Minikube
```bash
git clone https://github.com/Twingate-Community/diy-vpn.git
cd diy-vpn/minikube
minikube start --cpus=2 --memory=4096 --driver=docker
cp values-example.yaml values.yaml
# Edit values.yaml with network name, API key, remoteNetworkId
./deploy.sh
kubectl get pods -n twingate
```

### Method 2: DO Droplets (Terraform)
```bash
cd diy-vpn/digital_ocean/droplet
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars
terraform init && terraform plan && terraform apply
```

### Method 3: DO Kubernetes
```bash
cd diy-vpn/digital_ocean/kubernetes
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform plan && terraform apply
doctl kubernetes cluster kubeconfig save <cluster-name>
kubectl get pods -n twingate
```

## Configuration Values

| Variable | Description |
|---|---|
| `tg_network` / `network` | Twingate subdomain name |
| `tg_api_token` / `apiKey` | Twingate API token |
| `do_token` | DigitalOcean API token |
| `remoteNetworkId` | From Exit Networks URL |
| `region` | DO region code (e.g., `tor1`, `nyc1`, `fra1`) |
| `node_size` | DO droplet/node size (e.g., `s-1vcpu-1gb`) |
| `auto_scale` | Boolean; K8s only |
| `min_count` / `max_count` | K8s autoscaling bounds |

## Gotchas
- API token not shown after creation — copy immediately
- `remoteNetworkId` must match exactly: `https://{network}.twingate.com/exit-networks/{remoteNetworkId}`
- Minikube: increase resources if failing (`--memory=8192 --cpus=4`); requires Docker running
- Terraform state lock can block re-runs if previous apply failed
- Verify Twingate Admin Console: Internet Security → Exit Networks for connector status
- Destroy test environments with `terraform destroy` to avoid costs

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs/connector-issues)
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [DigitalOcean Regions](https://docs.digitalocean.com/platform/regional-availability/)
- [DigitalOcean Terraform Provider](https://registry.terraform.io/providers/digitalocean/
# DIY VPN Setup Guide (Twingate + DigitalOcean)

## Summary
Three-method guide for deploying a self-managed VPN using Twingate zero-trust networking on DigitalOcean infrastructure. Covers local Kubernetes (Minikube), cloud VMs (Droplets), and managed Kubernetes (DOKS). For personal/internal use only — commercial VPN services are prohibited.

## Key Information
- Three deployment methods: Minikube (free/local), DO Droplets (low cost), DO Kubernetes (enterprise)
- Requires Twingate Home plan or higher (Exit Networks not available on free Starter plan)
- Uses Twingate Operator and Connectors deployed via Helm charts
- Repository: `github.com/Twingate-Community/diy-vpn`

## Prerequisites
- Twingate account (Home plan+), DigitalOcean account, GitHub account
- Twingate Client installed on end-user devices
- Twingate API token with **Read, Write, and Provision** permissions
- DigitalOcean API token with **Full Access**
- Your Twingate network name (subdomain from `https://{name}.twingate.com`)

**Per-method software:**
| Method | Tools Required |
|--------|---------------|
| Minikube | Docker Desktop, minikube, kubectl, helm |
| DO Droplets | terraform |
| DO Kubernetes | terraform, doctl, kubectl, helm |

## Step-by-Step

### Method 1: Minikube
```bash
git clone https://github.com/Twingate-Community/diy-vpn.git && cd diy-vpn/minikube
minikube start --cpus=2 --memory=4096 --driver=docker
cp values-example.yaml values.yaml  # edit with credentials
./deploy.sh
kubectl get pods -n twingate
```

### Method 2: DO Droplets
```bash
cd diy-vpn/digital_ocean/droplet
cp terraform.tfvars.example terraform.tfvars  # edit with credentials
terraform init && terraform plan && terraform apply
```

### Method 3: DO Kubernetes
```bash
cd diy-vpn/digital_ocean/kubernetes
cp terraform.tfvars.example terraform.tfvars  # edit with credentials
terraform init && terraform plan && terraform apply
doctl kubernetes cluster kubeconfig save <cluster-name>
kubectl get pods -n twingate
```

## Configuration Values

**values.yaml (Minikube):**
- `twingate-operator.twingateOperator.network` — Twingate network name
- `twingate-operator.twingateOperator.apiKey` — Twingate API token
- `twingate-operator.twingateOperator.remoteNetworkId` — Exit Network ID

**terraform.tfvars (Droplets/Kubernetes):**
- `do_token` — DigitalOcean API token
- `tg_api_token` — Twingate API token
- `tg_network` — Twingate network name
- `droplets`/`clusters` — Region/size map (e.g., `tor1`, `nyc1`, `fra1`, `sgp1`)
- `auto_scale`, `min_count`, `max_count` — Kubernetes autoscaling (K8s method only)

## Gotchas
- API token not shown after creation — copy immediately
- Network name must match exactly (case-sensitive subdomain)
- Minikube needs Docker running; increase resources if pods fail: `--memory=8192 --cpus=4`
- Terraform failures often indicate missing DO token write permissions or locked state
- Verify connector status at Admin Console → Internet Security → Exit Networks

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs/connector-issues)
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [Twingate Plans Comparison](https://www.twingate.com/pricing)
- [DigitalOcean Terraform Provider](https://registry.terraform.io/providers/digitalocean/digitalocean/latest/docs)
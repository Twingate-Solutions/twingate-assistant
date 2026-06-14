# DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Step-by-step guide to deploying a self-managed VPN using Twingate zero-trust networking on DigitalOcean infrastructure. Offers three deployment methods: local Minikube (testing), DigitalOcean Droplets (simple production), and DigitalOcean Kubernetes (enterprise). Internal/personal use only — commercial VPN services are prohibited.

## Key Information
- Three deployment methods with increasing complexity and cost
- Uses Twingate Exit Networks feature (requires Home plan or above — not available on free Starter)
- Infrastructure-as-code via Terraform; container orchestration via Helm/Kubernetes
- Source repo: `github.com/Twingate-Community/diy-vpn`

## Prerequisites
- **Twingate**: Home plan or higher (Exit Networks required)
- **DigitalOcean account**
- **GitHub account**
- Twingate Client installed on connecting device
- Docker Desktop (Minikube method)
- 4GB+ RAM, 10GB+ disk, macOS/Linux/WSL2

## Deployment Methods

| Method | Use Case | Complexity |
|--------|----------|------------|
| Minikube | Local dev/learning | Low |
| DO Droplets | Personal/small team | Medium |
| DO Kubernetes | Enterprise/auto-scale | High |

## Step-by-Step (All Methods)

### API Keys Required
1. **Twingate**: Admin Console → Settings → API → Generate Token (Read, Write, Provision permissions)
2. **DigitalOcean**: Control Panel → API → Generate New Token (Full Access)
3. **Network name**: subdomain from `https://{network}.twingate.com`

### Method 1: Minikube
```bash
git clone https://github.com/Twingate-Community/diy-vpn.git
cd diy-vpn/minikube
minikube start --cpus=2 --memory=4096 --driver=docker
cp values-example.yaml values.yaml
# Edit values.yaml, then:
./deploy.sh
```

### Method 2: DO Droplets
```bash
cd diy-vpn/digital_ocean/droplet
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars, then:
terraform init && terraform plan && terraform apply
```

### Method 3: DO Kubernetes
```bash
cd diy-vpn/digital_ocean/kubernetes
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform plan && terraform apply
doctl kubernetes cluster kubeconfig save <cluster-name>
```

## Configuration Values

**values.yaml (Minikube)**
- `twingate-operator.twingateOperator.network` — Twingate network name
- `twingate-operator.twingateOperator.apiKey` — Twingate API token
- `twingate-operator.twingateOperator.remoteNetworkId` — Exit network ID

**terraform.tfvars (Droplets/Kubernetes)**
- `do_token` — DigitalOcean API token
- `tg_api_token` — Twingate API token
- `tg_network` — Twingate network name
- `droplets`/`clusters` — Region/size/count map
- Kubernetes supports `auto_scale`, `min_count`, `max_count`

## Gotchas
- Exit Networks not available on free Starter plan
- Twingate API token not shown after creation — copy immediately
- Minikube requires Docker Desktop running before `minikube start`
- Terraform state lock can block re-runs if prior apply failed
- Bandwidth subject to Twingate Fair Use Policy
- Commercial VPN services using this setup are explicitly prohibited

## Troubleshooting
- Connector missing in console → check API token permissions and exact network name match
- Terraform fails → verify DO token has write permissions; check region availability
- Minikube issues → increase resources: `minikube start --memory=8192 --cpus=4`

## Related Docs
- [Twingate Exit Networks](https://www.twingate.com/docs/exit-networks)
- [
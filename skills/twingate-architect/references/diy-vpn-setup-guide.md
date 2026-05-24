# DIY VPN Setup Guide (Twingate + DigitalOcean)

## Summary
Build a self-managed VPN using Twingate's zero-trust networking and DigitalOcean cloud. Three deployment methods available: local Minikube, DigitalOcean Droplets (Terraform), and DigitalOcean Kubernetes. Internal/personal use only — commercial VPN offerings are prohibited.

## Prerequisites
- **Twingate**: Home plan or higher (Exit Networks not available on free Starter)
- **DigitalOcean account** + **GitHub account**
- **Twingate Client** installed on connecting devices
- Docker Desktop (Minikube method), 4GB+ RAM, 10GB+ disk

## Deployment Methods

| Method | Use Case | Cost | Complexity |
|--------|----------|------|------------|
| Minikube | Local dev/learning | Free | Low |
| DO Droplets | Personal/small teams | Low | Medium |
| DO Kubernetes | Enterprise/auto-scale | Medium-High | High |

## API Key Setup
**Twingate**: Settings → API → Generate Token → requires **Read, Write, and Provision** permissions

**DigitalOcean**: API → Generate New Token → **Full Access**

**Network name**: subdomain from `https://{network}.twingate.com`

## Step-by-Step (Per Method)

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

**values.yaml (Minikube)**:
- `twingate-operator.twingateOperator.network` — Twingate network name
- `twingate-operator.twingateOperator.apiKey` — Twingate API token
- `twingate-operator.twingateOperator.remoteNetworkId` — Exit network ID

**terraform.tfvars (Droplets/K8s)**:
- `do_token` — DigitalOcean API token
- `tg_api_token` — Twingate API token
- `tg_network` — Twingate network name
- `droplets`/`clusters` — Region/size config blocks

**DO Regions**: `tor1`, `nyc1`, `nyc3`, `sfo3`, `ams3`, `fra1`, `lon1`, `sgp1`, `blr1`, `syd1`

## Gotchas
- Twingate API token is shown **only once** — save immediately
- Exit Networks require **paid plan** (not Starter/free)
- Minikube needs Docker running; reset with `minikube delete && minikube start`
- Terraform state lock can block reapply if previous run failed
- Network name in config must match exactly (case-sensitive)
- Commercial VPN use violates ToS; subject to Fair Use Policy on bandwidth

## Troubleshooting
- Connector missing in console → check API token permissions, verify network name
- `terraform apply` fails → confirm DO token has write scope, check region availability
- K8s issues → `kubectl logs -n twingate deployment/twingate-operator`

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs/connector-issues)
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [DigitalOcean Terraform Provider](https://registry
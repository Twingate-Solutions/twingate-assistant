# DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Step-by-step guide for building a self-hosted VPN using Twingate's zero-trust networking on DigitalOcean infrastructure. Offers three deployment paths: local Minikube (beginner), DigitalOcean Droplets (simple production), and DigitalOcean Kubernetes (enterprise). Internal/personal use only — commercial VPN services are prohibited.

## Key Information
- Three deployment methods: Minikube, DO Droplets (Terraform), DO Kubernetes (Terraform)
- Requires Twingate Home plan or higher (Exit Networks not available on free Starter plan)
- Source repo: `github.com/Twingate-Community/diy-vpn`
- Bandwidth subject to Twingate Fair Use Policy

## Prerequisites
- **Accounts**: Twingate (Home+), DigitalOcean, GitHub
- **Twingate API token**: Settings → API → Generate, with **Read, Write, and Provision** permissions
- **DigitalOcean API token**: Full Access scope
- **Twingate network name**: subdomain from `https://<name>.twingate.com`
- **Software**: Docker Desktop, `minikube`, `kubectl`, `helm`, `terraform`, `doctl` (varies by method)
- **System**: 4GB+ RAM (8GB+ for Kubernetes), 10GB+ disk, macOS/Linux/WSL2

## Configuration Values

### Method 1 — Minikube (`values.yaml`)
| Field | Description |
|---|---|
| `twingate-operator.twingateOperator.network` | Twingate network name |
| `twingate-operator.twingateOperator.apiKey` | Twingate API token |
| `twingate-operator.twingateOperator.remoteNetworkId` | Exit Network ID from console URL |

### Method 2 — Droplets (`terraform.tfvars`)
| Variable | Description |
|---|---|
| `do_token` | DigitalOcean API token |
| `tg_api_token` | Twingate API token |
| `tg_network` | Twingate network name |
| `droplets` | Map of region/size/count/image configs |
| `environment` | Label (e.g., `"production"`) |

### Method 3 — Kubernetes (`terraform.tfvars`)
Same as Method 2 plus `clusters` map with `region`, `node_size`, `node_count`, optional `min_count`/`max_count`/`auto_scale`.

## Step-by-Step (Droplets — most common)
1. Generate Twingate API token (Read/Write/Provision)
2. Generate DigitalOcean API token (Full Access)
3. `git clone https://github.com/Twingate-Community/diy-vpn.git && cd diy-vpn/digital_ocean/droplet`
4. `cp terraform.tfvars.example terraform.tfvars` → edit credentials and regions
5. `terraform init && terraform plan && terraform apply`
6. Verify Remote Networks appear in Twingate Admin Console → Connectors show "Connected"

## Gotchas
- **API token not shown again** after creation — copy immediately
- Twingate network name must match exactly (case-sensitive subdomain)
- Exit Networks require paid plan; Starter plan won't work
- Minikube needs Docker running; increase resources with `--memory=8192 --cpus=4` if pods fail
- Terraform state lock can block re-runs if previous apply failed
- Commercial use of this setup violates Twingate ToS

## Troubleshooting
- **Connector missing**: Check token permissions, verify network name, review operator logs
- **Terraform fails**: Confirm DO token has write access, check region availability
- **Minikube issues**: `minikube delete && minikube start` to reset
- **K8s issues**: `kubectl logs -n twingate deployment/twingate-operator`

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs/connector-issues)
-
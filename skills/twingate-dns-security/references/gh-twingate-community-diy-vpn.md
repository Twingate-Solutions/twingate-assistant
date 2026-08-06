---
source: https://github.com/Twingate-Community/diy-vpn
type: github
fetched: 2026-08-06
source_version: 7c20d32318dc5a832d16b928ad868fb49e519f11
---

<!-- triage: unassigned -->

# Twingate DIY VPN

## Summary
Terraform-based tooling for deploying Twingate Exit Networks as a personal VPN across three platforms: local Minikube, DigitalOcean Droplets, and DigitalOcean Kubernetes. All traffic routes through Twingate's zero-trust controller with no inbound ports exposed on the exit node. Personal/internal use only; commercial VPN services are prohibited.

## Key Information
- Three independent deployment options — pick one, do not combine them
- Minikube: free, local-only, good for testing
- DigitalOcean Droplets: lowest cloud cost, production-ready, minimal orchestration
- DigitalOcean Kubernetes: higher cost, requires K8s expertise, suits enterprise workloads
- Includes a reusable Helm chart (`helm/`) used by both Kubernetes and Minikube paths
- Supports DigitalOcean regions across NA, EU, and APAC

## Prerequisites
- Terraform >= 1.0
- Twingate **Home** or **Enterprise** plan (Exit Networks not available on Starter/free tier)
- Twingate API token and network name
- An Exit Network already created in the Twingate Admin Console
- Platform-specific: Docker + Minikube for local; DigitalOcean account + API token for cloud; `kubectl` + Helm for Kubernetes path

## Usage / Step-by-Step

**Minikube (local):**
```bash
cd minikube
# Edit values.yaml with Twingate credentials
./deploy.sh
```

**DigitalOcean Droplets:**
```bash
cd digital_ocean/droplet
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars
terraform init
terraform apply
```

**DigitalOcean Kubernetes:**
```bash
cd digital_ocean/kubernetes
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars
terraform init
terraform apply
```

## Configuration Values
Stored in `terraform.tfvars` (copy from `.example` files):

| Variable | Description |
|---|---|
| `twingate_api_token` | From Twingate Admin Console → Settings → API |
| `twingate_network` | Tenant name prefix (e.g., `company` from `company.twingate.com`) |
| `twingate_exit_network_id` | ID of the Exit Network created in the Admin Console |
| `do_token` | DigitalOcean API token (cloud deployments only) |
| `region` | DigitalOcean region slug (e.g., `nyc3`, `fra1`, `sgp1`) |

Helm values configured via `values.yaml` / `values.example.yaml` in the `minikube/` and `helm/` directories.

## Gotchas
- Exit Networks require a paid plan; the free Starter plan will not work
- Bandwidth through Twingate infrastructure is subject to their Fair Use Policy
- Do not attempt to run multiple deployment options simultaneously — they are fully independent
- Terraform state conflicts can occur in multi-environment setups; use separate state files per environment
- Connector showing offline usually indicates an invalid API token or network connectivity issue
- DigitalOcean region list may change; verify current availability at DigitalOcean docs before deploying

## Related Docs
- [Twingate Documentation](https://docs.twingate.com/)
- [Twingate Pricing / Plans](https://www.twingate.com/pricing)
- [Twingate Fair Use Policy](https://www.twingate.com/terms/sa)
- [DigitalOcean Regional Availability](https://docs.digitalocean.com/platform/regional-availability/)
- [Twingate Community (Reddit)](https://www.reddit.com/r/twingate/)
- [Issue Tracker](https://github.com/Twingate-Community/diy-vpn/issues)
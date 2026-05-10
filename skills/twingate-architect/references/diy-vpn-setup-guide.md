# DIY VPN Setup Guide with Twingate and DigitalOcean

## Summary
Step-by-step guide to deploying a self-managed VPN using Twingate zero-trust networking on DigitalOcean infrastructure. Offers three deployment methods (Minikube, DO Droplets, DO Kubernetes) with Terraform/Helm/kubectl tooling. Personal/internal use only—commercial VPN service use is prohibited.

## Key Information
- Three deployment methods: Minikube (local/free), DigitalOcean Droplets (low cost), DigitalOcean Kubernetes (enterprise)
- Requires Twingate Home plan or higher (Exit Networks not available on free Starter plan)
- Source repo: `github.com/Twingate-Community/diy-vpn`
- Twingate network name = subdomain of your Twingate URL (e.g., `mycompany` from `mycompany.twingate.com`)

## Prerequisites
- Twingate Home+ account, DigitalOcean account, GitHub account
- Twingate Client installed on end-user devices
- 4GB+ RAM (8GB+ for Kubernetes), 10GB+ disk, Docker Desktop (Minikube)
- Tools by method: Minikube→`minikube kubectl helm`; Droplets→`terraform`; Kubernetes→`terraform doctl kubectl helm`

## API Key Setup
**Twingate:** Admin Console → Settings → API → Generate Token (requires Read, Write, Provision permissions)
**DigitalOcean:** Control Panel → API → Generate New Token (Full Access)

## Configuration Values

### Method 1 – Minikube (`values.yaml`)
```yaml
twingate-operator:
  twingateOperator:
    network: "your-company"
    apiKey: "your_twingate_api_key"
    remoteNetworkId: ""  # from exit-networks URL
    logFormat: "json"
    logVerbosity: "debug"
```

### Method 2 – Droplets (`terraform.tfvars`)
```hcl
do_token     = "dop_v1_..."
tg_api_token = "..."
tg_network   = "your-network-name"
droplets = {
  "toronto-vpn" = { region = "tor1", size = "s-1vcpu-1gb", count = 1, image = "ubuntu-24-04-x64" }
}
environment = "production"
```

### Method 3 – Kubernetes (`terraform.tfvars`)
```hcl
do_token     = "..."
tg_api_token = "..."
tg_network   = "..."
clusters = {
  "nyc-cluster" = { region = "nyc1", node_size = "s-2vcpu-4gb", min_count = 1, max_count = 3, auto_scale = true }
}
```

## Step-by-Step (Minikube)
1. `git clone https://github.com/Twingate-Community/diy-vpn.git && cd diy-vpn/minikube`
2. `minikube start --cpus=2 --memory=4096 --driver=docker`
3. `cp values-example.yaml values.yaml` → edit credentials
4. `./deploy.sh`
5. Verify: `kubectl get pods -n twingate` and check Admin Console → Internet Security → Exit Networks

## Gotchas
- Starter (free) plan does **not** include Exit Networks—upgrade required
- Twingate API token shown only once at creation; store immediately
- Minikube requires Docker Desktop running before `minikube start`
- Remote Network IDs appear in Twingate console as `do_<region>` (e.g., `do_tor1`)
- `terraform destroy` required to avoid ongoing costs for test environments

## Related Docs
- [Twingate Connector Troubleshooting](https://www.twingate.com/docs/connector-issues)
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [DigitalOcean Regions](https://docs.digitalocean.com/
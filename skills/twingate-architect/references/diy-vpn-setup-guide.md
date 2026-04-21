## DIY VPN with Twingate and DigitalOcean

Step-by-step guide to building a self-managed, globally distributed VPN using Twingate Exit Networks and DigitalOcean infrastructure. Provides three deployment methods: Minikube (local testing), Droplets via Terraform (simple production), and Kubernetes via Terraform + Helm (enterprise/autoscaling). Source code hosted at `github.com/Twingate-Community/diy-vpn`.

**Key Information**
- **Requires Exit Networks** -- not available on the free Starter plan; requires Twingate Home or paid plan
- **Internal use only** -- cannot be used to offer a commercial VPN service; subject to Fair Use Policy
- Three methods: Minikube (free, local), Droplets (low cost, production), Kubernetes (medium-high cost, enterprise)
- Twingate API token requires Read, Write, and Provision permissions
- Droplet size for testing: `s-1vcpu-1gb`; Kubernetes nodes: start with `s-1vcpu-2gb`

**Prerequisites**
- Twingate Home or paid plan (Exit Networks required)
- DigitalOcean account with API access
- GitHub account (for example repo)
- Twingate API token (Read + Write + Provision) and DigitalOcean API token (Full Access)
- For Droplets/K8s: Terraform installed; for K8s: also `doctl`, `kubectl`, Helm

**Step-by-Step (Droplets)**
1. Generate Twingate and DigitalOcean API tokens; note Twingate network name from URL subdomain
2. `cd diy-vpn/digital_ocean/droplet`; copy and edit `terraform.tfvars` with tokens, network name, regions
3. `terraform init && terraform plan && terraform apply`
4. Verify Connectors in Admin Console -> Internet Security -> Exit Networks

**Configuration Values**
- `terraform.tfvars`: `do_token`, `tg_api_token`, `tg_network`, `droplets` map (region, size, count, image)
- Available regions: tor1, nyc1, nyc3, sfo1, sfo3, ams3, fra1, lon1, sgp1, blr1, syd1
- Kubernetes autoscaling: `min_count`, `max_count`, `auto_scale = true` per cluster

**Gotchas**
- Exit Networks are not available on the Starter (free) plan -- upgrade required
- Twingate API token must have Provision permission, not just Read/Write
- Use `terraform destroy` for test deployments to avoid ongoing DigitalOcean costs
- Connector not appearing: verify API token permissions and that `tg_network` matches the exact subdomain

**Related Docs**
- /docs/digitalocean-getting-started
- /docs/exit-networks
- /docs/kubernetes-operator
- /docs/terraform-provider

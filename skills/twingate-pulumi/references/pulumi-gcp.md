# Pulumi with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on Google Cloud Platform using Pulumi with TypeScript. Creates a complete stack: Twingate remote network, connector, group, resource, plus GCP VPC, subnet, firewall, and two VMs (webserver + connector).

## Key Information
- Language: TypeScript/JavaScript
- Creates 2 GCP VMs: one nginx webserver, one Twingate connector
- Connector tokens are passed to GCP VM via startup script using `pulumi.interpolate`
- Additional examples available in Twingate's [GitHub repository](https://github.com/Twingate)

## Prerequisites
- GCP account with permissions to create/delete resources
- GCP CLI installed and configured
- Pulumi CLI installed
- Node.js installed
- Twingate API token and network name
- Bash-compatible OS

## Step-by-Step

1. `mkdir twingate_pulumi_gcp_demo && cd twingate_pulumi_gcp_demo`
2. `pulumi new typescript`
3. `gcloud auth application-default login`
4. Set Pulumi config (see below)
5. `npm install @pulumi/gcp @twingate/pulumi-twingate`
6. Write `index.ts` with full resource definitions
7. `pulumi preview` → `pulumi up`
8. Assign Twingate user to the created group
9. Teardown: `pulumi down`

## Configuration Values

```bash
# GCP config
pulumi config set gcp:project your-gcp-project-id
pulumi config set gcp:region europe-west2
pulumi config set gcp:zone europe-west2-c

# Twingate config
pulumi config set twingate:apiToken YOUR_TOKEN --secret
pulumi config set twingate:network democompany
```

**Connector startup script env vars:**
- `TWINGATE_ACCESS_TOKEN` — from `tggcpConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `tggcpConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

**Key resource settings:**
- Subnet CIDR: `172.16.0.0/24`
- Machine type: `e2-micro`
- OS image: `ubuntu-os-cloud/ubuntu-2204-lts`
- Firewall: allows ICMP + TCP port 80, source tag `demo`
- TwingateResource protocols: TCP restricted to port 80, UDP allow all

## Gotchas
- `accessConfigs: [{}]` must be present but empty to request an ephemeral IP on GCP instances
- Use `pulumi.interpolate` (not string interpolation) when embedding Pulumi Output values (like connector tokens) into startup scripts
- After `pulumi up`, you must manually assign your Twingate user to the created group — this is not automated
- Firewall rules use source tags (`demo`); VMs must have matching tags to be governed by the firewall

## Related Docs
- Twingate Pulumi provider general prerequisites guide
- [Twingate Pulumi GitHub examples](https://github.com/Twingate)
- GCP CLI setup and IAM permissions documentation
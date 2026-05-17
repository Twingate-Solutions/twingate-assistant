# Pulumi with GCP and Twingate

## Page Title
How to Use Pulumi with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on GCP using Pulumi with TypeScript. Creates a complete setup including a Twingate Remote Network, Connector, Group, Resource, plus GCP VPC, subnet, firewall, and two VMs (web server + connector).

## Key Information
- Language: TypeScript/JavaScript
- NPM packages: `@pulumi/gcp`, `@twingate/pulumi-twingate`
- Creates two GCP VMs: one web server (`e2-micro`, Ubuntu 22.04), one Twingate Connector
- Connector tokens injected via `metadataStartupScript` using `pulumi.interpolate`
- Additional examples available in Twingate GitHub repository

## Prerequisites
- GCP account with permissions to create/delete resources
- GCP CLI installed and configured
- Pulumi CLI installed
- Node.js installed
- Twingate API token (generated from admin panel)
- Twingate network name
- Bash-compatible OS

## Step-by-Step

1. `mkdir twingate_pulumi_gcp_demo && cd twingate_pulumi_gcp_demo`
2. `pulumi new typescript`
3. `gcloud auth application-default login`
4. Set Pulumi config (see below)
5. `npm install @pulumi/gcp @twingate/pulumi-twingate`
6. Write `index.ts` with Twingate + GCP resources
7. `pulumi preview` to validate
8. `pulumi up` to deploy
9. Assign Twingate user to the created group
10. `pulumi down` to destroy

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
- `TWINGATE_ACCESS_TOKEN` — from `TwingateConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `TwingateConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

**Resource protocol config example:**
- TCP: `RESTRICTED`, ports `["80"]`
- UDP: `ALLOW_ALL`
- ICMP: `allowIcmp: true`

**Subnet CIDR:** `172.16.0.0/24`
**Machine type:** `e2-micro`
**Image:** `ubuntu-os-cloud/ubuntu-2204-lts`

## Gotchas
- Use `pulumi.interpolate` (not string interpolation) when referencing Pulumi Output values in startup scripts (connector tokens are async outputs)
- `accessConfigs: [{}]` must be present but empty to request an ephemeral IP on GCP instances
- After `pulumi up`, manually assign the Twingate user to the created group — this step is not automated
- Firewall uses `sourceTags: ["demo"]` — adapt rules for production use
- `autoCreateSubnetworks: false` required on the VPC

## Related Docs
- Twingate Pulumi provider general prerequisites guide
- GCP IAM permissions for resource creation
- Twingate GitHub repository (additional Pulumi/GCP examples)
- Twingate API token generation (admin panel)
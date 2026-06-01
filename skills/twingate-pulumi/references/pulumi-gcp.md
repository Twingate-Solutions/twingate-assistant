# Pulumi with GCP and Twingate

## Page Title
How to Use Pulumi with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on Google Cloud Platform using Pulumi with TypeScript. Creates a complete demo environment including GCP VPC, firewall, two VMs (webserver + Twingate connector), and corresponding Twingate resources/groups.

## Key Information
- Uses TypeScript/Node.js with `@pulumi/gcp` and `@twingate/pulumi-twingate` packages
- Deploys two GCP `e2-micro` VMs: one webserver, one Twingate connector
- Connector tokens passed via `metadataStartupScript` using `pulumi.interpolate`
- Resource address uses VM's private IP (`networkInterfaces[0].networkIp`)

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
6. Write `index.ts` (see Configuration Values)
7. `pulumi preview` → `pulumi up`
8. Assign Twingate user to the created group manually
9. Teardown: `pulumi down`

## Configuration Values

**Pulumi config commands:**
```bash
pulumi config set gcp:project your-gcp-project-id
pulumi config set gcp:region europe-west2
pulumi config set gcp:zone europe-west2-c
pulumi config set twingate:apiToken YOUR_TOKEN --secret
pulumi config set twingate:network democompany
```

**Connector startup script env vars:**
- `TWINGATE_ACCESS_TOKEN` — from `TwingateConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `TwingateConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

**Key resource settings:**
- VM machine type: `e2-micro`
- VM image: `ubuntu-os-cloud/ubuntu-2204-lts`
- Subnet CIDR: `172.16.0.0/24`
- Firewall: allows ICMP + TCP port 80, source tag `demo`
- TwingateResource protocols: TCP restricted to port 80, UDP allow all, ICMP allowed

## Gotchas
- `accessConfigs: [{}]` must be present but empty to request ephemeral public IP on GCP VMs
- Use `pulumi.interpolate` (not string interpolation) when embedding Pulumi Output values (tokens) into startup scripts
- After `pulumi up`, must **manually assign** Twingate user to the created group — not automated
- Firewall uses source tags (`demo`), not IP ranges — VMs must have the `demo` tag applied
- API token should be set with `--secret` flag to encrypt it in Pulumi state

## Related Docs
- Twingate Pulumi provider: `@twingate/pulumi-twingate`
- Additional examples: [Twingate GitHub repository](https://github.com/Twingate)
- GCP CLI authentication: `gcloud auth application-default login`
- General Pulumi prerequisites guide (referenced but not linked)
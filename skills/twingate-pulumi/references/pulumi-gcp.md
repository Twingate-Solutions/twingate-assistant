# Pulumi with GCP and Twingate

## Page Title
How to Use Pulumi with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on GCP using Pulumi with TypeScript. Creates a complete stack including GCP VPC, subnets, firewall, two VMs (webserver + Twingate connector), and corresponding Twingate resources (remote network, connector, group, resource).

## Key Information
- Uses TypeScript/Node.js with `@pulumi/gcp` and `@twingate/pulumi-twingate` packages
- Deploys two GCP VMs: one nginx webserver, one Twingate connector
- Connector tokens are injected via `metadataStartupScript` using `pulumi.interpolate`
- Twingate resource uses the webserver's private IP as its address
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
4. Set Pulumi config (see Configuration Values below)
5. `npm install @pulumi/gcp @twingate/pulumi-twingate`
6. Write `index.ts` with resource definitions
7. `pulumi preview` to validate
8. `pulumi up` to deploy
9. Assign Twingate user to the created group manually in admin panel
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

**Key resource parameters:**
- VM `machineType`: `e2-micro`
- VM `image`: `ubuntu-os-cloud/ubuntu-2204-lts`
- Subnet CIDR: `172.16.0.0/24`
- Firewall allows: ICMP + TCP port 80, source tag `demo`
- TwingateResource TCP policy: `RESTRICTED` (port 80), UDP policy: `ALLOW_ALL`

## Gotchas
- Use `pulumi.interpolate` (not string interpolation) when embedding Pulumi output values (e.g., connector tokens) into startup scripts
- `accessConfigs: [{}]` must be empty array entry to request ephemeral IP on GCP VMs
- User-to-group assignment is **manual** — not handled by this Pulumi config
- Firewall rules in the example are minimal (port 80 only); adapt for production use
- `--secret` flag required when setting `apiToken` to encrypt it in Pulumi state

## Related Docs
- Twingate Pulumi provider general prerequisites guide
- GCP IAM permissions for resource creation
- [Twingate Pulumi GitHub examples](https://github.com/Twingate)
- Pulumi TypeScript getting started
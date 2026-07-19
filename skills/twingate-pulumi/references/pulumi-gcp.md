# Pulumi with GCP and Twingate

## Page Title
How to Use Pulumi with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on Google Cloud Platform using Pulumi with TypeScript. Creates a complete setup including a Twingate Remote Network, Connector, Group, Resource, and GCP infrastructure (VPC, subnet, firewall, two VMs).

## Key Information
- Uses TypeScript/JavaScript for IaC configuration
- Creates two GCP VMs: one webserver (`e2-micro`) and one Twingate Connector (`e2-micro`)
- Connector VM bootstrapped via startup script pulling tokens from Twingate API
- Uses `pulumi.interpolate` to inject dynamic values (connector tokens) into startup scripts
- Additional examples available at Twingate GitHub repository

## Prerequisites
- GCP account with permissions to create/delete resources
- GCP CLI installed and configured
- Pulumi CLI installed (general Pulumi prerequisites met)
- Node.js installed
- Twingate API token and network name
- Bash-compatible OS

## Step-by-Step

1. `mkdir twingate_pulumi_gcp_demo && cd twingate_pulumi_gcp_demo`
2. `pulumi new typescript`
3. `gcloud auth application-default login`
4. Set Pulumi config (see Configuration Values below)
5. `npm install @pulumi/gcp @twingate/pulumi-twingate`
6. Write `index.ts` with Twingate + GCP resources
7. `pulumi preview` to validate
8. `pulumi up` to deploy
9. Assign Twingate user to the created group in admin panel
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

**Key resource settings:**
- Subnet CIDR: `172.16.0.0/24`
- Firewall: allows ICMP + TCP:80, source tag `demo`
- TwingateResource TCP policy: `RESTRICTED` (port 80), UDP: `ALLOW_ALL`
- VM image: `ubuntu-os-cloud/ubuntu-2204-lts`

## Gotchas
- `accessConfigs: [{}]` must be present but empty to request ephemeral public IP on GCP instances
- Must use `pulumi.interpolate` (not template literals) when embedding Pulumi Output values (connector tokens) in startup scripts
- After `pulumi up`, manually assign users to the created Twingate group — not automated in this config
- Firewall uses source tags (`demo`), not IP ranges — VMs must have matching tag

## Related Docs
- Twingate Pulumi provider: `@twingate/pulumi-twingate` (npm)
- GCP Pulumi provider: `@pulumi/gcp` (npm)
- General Pulumi prerequisites guide (referenced but not linked)
- Twingate GitHub repository for additional examples
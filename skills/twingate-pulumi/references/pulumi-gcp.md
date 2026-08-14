---
source: https://www.twingate.com/docs/pulumi-gcp
type: docs
fetched: 2026-08-14
source_version: ad51fa43498e672c26ec168a34ff7c8e1805c783c8f50f9c41de6fff91455627
---

# Pulumi with GCP and Twingate

## Page Title
How to Use Pulumi with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on GCP using Pulumi with TypeScript. Creates a complete stack including GCP VPC/subnet/firewall, a webserver VM, a Twingate connector VM, and Twingate remote network/group/resource configuration.

## Key Information
- Language: TypeScript/JavaScript (Node.js required)
- NPM packages: `@pulumi/gcp`, `@twingate/pulumi-twingate`
- Connector VM installs via curl script using generated access/refresh tokens
- Resource access restricted to TCP port 80 (RESTRICTED policy); UDP ALLOW_ALL
- GCP VM type: `e2-micro`, image: `ubuntu-2204-lts`
- Subnet CIDR: `172.16.0.0/24`, region: `europe-west2`
- Additional examples in Twingate GitHub repository

## Prerequisites
- GCP account with permissions to create/delete resources
- GCP CLI installed and configured
- Pulumi CLI installed (general Pulumi prerequisites met)
- Node.js installed
- Twingate API token and network name
- Bash-compatible OS

## Step-by-Step

1. `mkdir twingate_pulumi_gcp_demo && cd twingate_pulumi_gcp_demo`
2. `pulumi new typescript` (set project name, description, stack name)
3. `gcloud auth application-default login`
4. Set Pulumi config (see Configuration Values below)
5. `npm install @pulumi/gcp @twingate/pulumi-twingate`
6. Write `index.ts` with Twingate + GCP resources (see full file in docs)
7. `pulumi preview` to validate
8. `pulumi up` to deploy
9. Assign Twingate user to the created group in admin panel
10. Test access via private IP in browser
11. `pulumi down` to destroy

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

**Connector startup env vars** (injected via `pulumi.interpolate`):
- `TWINGATE_ACCESS_TOKEN` — from `TwingateConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `TwingateConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

## Gotchas
- Use `pulumi.interpolate` (not template literals) when embedding Pulumi Output values (like tokens) in startup scripts
- `accessConfigs: [{}]` must be present but empty to request ephemeral IP on GCP VM network interfaces
- After `pulumi up`, must manually assign the Twingate user to the created group — not automated in this config
- Firewall uses `sourceTags: ["demo"]` — only applies to VMs tagged `"demo"`; adapt rules for production use
- API token should always be set with `--secret` flag

## Related Docs
- Twingate Pulumi provider (general prerequisites guide)
- GCP IAM permissions for resource creation
- Twingate API token generation
- Twingate GitHub repository (additional Pulumi/GCP examples)
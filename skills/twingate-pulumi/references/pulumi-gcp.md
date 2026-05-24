# Twingate + Pulumi + GCP Integration

## Page Title
How to Use Pulumi with GCP and Twingate

## Summary
Automates Twingate deployment on GCP using Pulumi with TypeScript. Creates a Remote Network, Connector, group, GCP VPC/subnet/firewall, and two VMs (webserver + connector) wired together via startup scripts.

## Key Information
- Language: TypeScript/Node.js
- NPM packages: `@pulumi/gcp`, `@twingate/pulumi-twingate`
- Two VMs created: `twingate-demo-server` (nginx) and `twingate-demo-connector`
- Connector tokens injected via `pulumi.interpolate` into VM startup script
- Firewall restricts to ICMP + TCP port 80 with source tag `demo`
- Resource uses RESTRICTED TCP on port 80, ALLOW_ALL UDP

## Prerequisites
- GCP account with permissions to create/delete resources
- GCP CLI installed and configured
- Pulumi CLI installed
- Node.js installed
- Twingate API token and network name

## Step-by-Step

1. `mkdir twingate_pulumi_gcp_demo && cd twingate_pulumi_gcp_demo`
2. `pulumi new typescript`
3. `gcloud auth application-default login`
4. Set Pulumi config (see Configuration Values below)
5. `npm install @pulumi/gcp @twingate/pulumi-twingate`
6. Write `index.ts` with Twingate + GCP resources
7. `pulumi preview` to validate
8. `pulumi up` to deploy
9. Assign Twingate user to the created group manually in admin panel
10. `pulumi down` to destroy

## Configuration Values

```bash
# GCP
pulumi config set gcp:project your-gcp-project-id
pulumi config set gcp:region europe-west2
pulumi config set gcp:zone europe-west2-c

# Twingate
pulumi config set twingate:apiToken YOUR_TOKEN --secret
pulumi config set twingate:network democompany
```

**Connector startup script env vars:**
- `TWINGATE_ACCESS_TOKEN` — from `tggcpConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `tggcpConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

## Gotchas
- `pulumi.interpolate` required for connector startup script — values are Pulumi `Output<T>` types, not plain strings
- `accessConfigs: [{}]` must be empty object array to request ephemeral IP on GCP VMs
- Firewall uses `sourceTags: ["demo"]` — VMs must have matching tag `"demo"` to be covered
- User-to-group assignment is **manual** in Twingate admin panel after deploy
- API token must be set with `--secret` flag to encrypt in state

## Related Docs
- Twingate Pulumi provider: GitHub repository (additional examples)
- General Pulumi prerequisites guide
- GCP account permissions reference
- Twingate API token generation (admin panel)
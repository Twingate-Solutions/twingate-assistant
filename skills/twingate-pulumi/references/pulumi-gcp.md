---
source: https://www.twingate.com/docs/pulumi-gcp
type: docs
fetched: 2026-10-04
source_version: 73487219413975dd53e9900ac3549b32f52c81067471ef38f65db8d914b5f958
trust: official
---

# Pulumi with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on Google Cloud Platform using Pulumi with TypeScript. Creates a complete stack: Twingate remote network, connector, group, resource, plus GCP VPC, subnet, firewall, and two VMs (web server + connector).

## Prerequisites
- GCP account with permissions to create/delete compute resources
- GCP CLI installed and configured
- Pulumi CLI installed (see Pulumi prerequisites guide)
- Node.js installed (`node -v` to verify)
- Twingate API token and network name (from admin panel)
- Bash-compatible OS

## Step-by-Step

1. **Create project directory and init Pulumi**
   ```bash
   mkdir twingate_pulumi_gcp_demo && cd twingate_pulumi_gcp_demo
   pulumi new typescript
   ```

2. **Authenticate with GCP**
   ```bash
   gcloud auth application-default login
   ```

3. **Set Pulumi config values**
   ```bash
   pulumi config set gcp:project your-gcp-project-id
   pulumi config set gcp:region europe-west2
   pulumi config set gcp:zone europe-west2-c
   pulumi config set twingate:apiToken YOUR_TOKEN --secret
   pulumi config set twingate:network democompany
   ```

4. **Install Node modules**
   ```bash
   npm install @pulumi/gcp @twingate/pulumi-twingate
   ```

5. **Write `index.ts`** — see Configuration Values below for resource order

6. **Preview and deploy**
   ```bash
   pulumi preview
   pulumi up
   ```

7. **Teardown**
   ```bash
   pulumi down
   ```

## Configuration Values

| Config Key | Description |
|---|---|
| `gcp:project` | GCP project ID |
| `gcp:region` | GCP region (e.g. `europe-west2`) |
| `gcp:zone` | GCP zone (e.g. `europe-west2-c`) |
| `twingate:apiToken` | Twingate API token (set as `--secret`) |
| `twingate:network` | Twingate network name |

**Resource creation order in `index.ts`:**
1. `TwingateRemoteNetwork` → `TwingateConnector` → `TwingateConnectorTokens` → `TwingateGroup`
2. GCP `Network` → `Subnetwork` → `Firewall`
3. Web server `Instance` (runs nginx startup script)
4. Connector `Instance` (startup script pulls from `binaries.twingate.com` using generated tokens)
5. `TwingateResource` pointing to web server's private IP

**Connector startup script** uses `pulumi.interpolate` to inject `accessToken`, `refreshToken`, and network URL at deploy time. Installer downloads from `binaries.twingate.com`.

## Gotchas
- `accessConfigs: [{}]` must be present but empty on `networkInterfaces` to get an ephemeral public IP
- Connector tokens (`accessToken`, `refreshToken`) are runtime-generated outputs — use `pulumi.interpolate` when embedding in startup scripts
- Firewall `sourceTags: ["demo"]` restricts to VMs tagged `"demo"` only; adapt rules for production
- After `pulumi up`, manually assign the Twingate user to the created group to enable access
- Subnet CIDR `172.16.0.0/24` and region `europe-west2` are hardcoded in example — update for your setup

## Related Docs
- [Twingate Pulumi GitHub examples repository](https://github.com/Twingate)
- Twingate Pulumi prerequisites guide (all Pulumi guides)
- GCP IAM permissions for resource creation
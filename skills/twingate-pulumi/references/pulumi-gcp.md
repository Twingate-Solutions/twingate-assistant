# Pulumi with GCP and Twingate

## Page Title
How to Use Pulumi with GCP and Twingate

## Summary
Automates Twingate deployment on GCP using Pulumi (TypeScript). Creates a Remote Network, Connector, Group, and Resource alongside GCP VPC, subnet, firewall, and two VMs (webserver + connector). The Twingate connector VM bootstraps via startup script using generated connector tokens.

## Key Information
- Uses `@pulumi/gcp` and `@twingate/pulumi-twingate` npm packages
- Two GCP VMs: one nginx webserver, one Twingate connector
- Connector tokens are passed to connector VM via `metadataStartupScript` using `pulumi.interpolate`
- Twingate Resource address uses the webserver's private IP (`networkInterfaces[0].networkIp`)
- Additional examples available in Twingate's GitHub repository

## Prerequisites
- GCP account with resource create/delete permissions
- GCP CLI installed and configured
- Pulumi CLI installed
- Node.js installed
- Twingate API token and network name (from admin panel)
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

**Resource settings:**
- Subnet CIDR: `172.16.0.0/24`
- Region: `europe-west2`
- VM machine type: `e2-micro`
- VM image: `ubuntu-os-cloud/ubuntu-2204-lts`
- Firewall: allows ICMP + TCP port 80, source tag `demo`
- Twingate Resource: TCP RESTRICTED port 80, UDP ALLOW_ALL, ICMP allowed

**Connector startup script env vars:**
- `TWINGATE_ACCESS_TOKEN` — from `tggcpConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `tggcpConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

## Gotchas
- Must use `pulumi.interpolate` (not string interpolation) when embedding Pulumi Output values (connector tokens) into startup scripts
- `accessConfigs: [{}]` must be empty object array to request ephemeral IP on GCP VMs
- After `pulumi up`, you must **manually assign the Twingate user** to the created group — not automated
- Firewall uses source tags (`demo`) — VMs must have matching tag to receive traffic

## Related Docs
- Twingate Pulumi provider general prerequisites guide
- [Twingate Pulumi GitHub examples repository](https://github.com/Twingate)
- GCP CLI authentication: `gcloud auth application-default login`
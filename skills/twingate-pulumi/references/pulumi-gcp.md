# Pulumi with GCP and Twingate

## Page Title
How to Use Pulumi with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on GCP using Pulumi with TypeScript. Creates a complete infrastructure including VPC, subnet, firewall, web server VM, Twingate connector VM, remote network, group, and resource.

## Key Information
- Uses TypeScript/Node.js for Pulumi configuration
- Creates two VMs: web server (`e2-micro`, Ubuntu 22.04) and Twingate connector
- Connector installed via startup script using `binaries.twingate.com/connector/setup.sh`
- Uses `pulumi.interpolate` to pass dynamic connector tokens into startup scripts
- Additional examples at Twingate's GitHub repository

## Prerequisites
- GCP account with permissions to create/delete resources
- GCP CLI installed and configured
- Pulumi CLI installed (with general Pulumi prerequisites met)
- Node.js installed
- Twingate API token and network name

## Step-by-Step

1. `mkdir twingate_pulumi_gcp_demo && cd twingate_pulumi_gcp_demo`
2. `pulumi new typescript`
3. `gcloud auth application-default login`
4. Set Pulumi config (see Configuration Values below)
5. `npm install @pulumi/gcp @twingate/pulumi-twingate`
6. Write `index.ts` with resources in order: TwingateRemoteNetwork → TwingateConnector → TwingateConnectorTokens → TwingateGroup → GCP Network → Subnetwork → Firewall → web server VM → connector VM → TwingateResource
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

**Key resource parameters:**
- Subnet CIDR: `172.16.0.0/24`
- Machine type: `e2-micro`
- Image: `ubuntu-os-cloud/ubuntu-2204-lts`
- Firewall: allows ICMP + TCP port 80, source tag `demo`
- TwingateResource TCP policy: `RESTRICTED` (port 80), UDP: `ALLOW_ALL`

**Connector startup script env vars:**
- `TWINGATE_ACCESS_TOKEN`
- `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_URL` (`https://<network>.twingate.com`)

## Gotchas
- `accessConfigs: [{}]` must be empty array entry to request ephemeral IP on network interfaces
- Connector tokens reference dynamic Pulumi outputs — must use `pulumi.interpolate` (not string concatenation) in startup script
- Group assignment for users must be done manually after deployment; not automated in this guide
- Firewall `sourceTags: ["demo"]` restricts traffic — VMs must have `tags: ["demo"]`

## Related Docs
- Twingate Pulumi provider general prerequisites
- GCP account permissions guide
- Twingate API token generation
- Twingate GitHub repository (additional Pulumi/GCP examples)
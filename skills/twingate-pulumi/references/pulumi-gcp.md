# Pulumi with GCP and Twingate

## Summary
Automates Twingate deployment on Google Cloud Platform using Pulumi with TypeScript. Creates a complete setup including GCP VPC, subnets, firewall, web server VM, Twingate connector VM, and Twingate resources/groups. The Pulumi Twingate provider is an open-source community tool.

## Key Information
- Language: TypeScript/JavaScript
- Creates: Remote Network, Connector, Connector Tokens, Group, Resource in Twingate + VPC/Subnet/Firewall/2x VMs in GCP
- Connector installed via startup script using `binaries.twingate.com/connector/setup.sh`
- Uses `pulumi.interpolate` to inject runtime-generated tokens into startup scripts
- More examples available in [Twingate GitHub repository](https://github.com/Twingate)

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
6. Write `index.ts` with resources
7. `pulumi preview` → `pulumi up`
8. Manually assign Twingate user to created group
9. `pulumi down` to destroy

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
- VM type: `e2-micro`
- VM image: `ubuntu-os-cloud/ubuntu-2204-lts`
- Firewall: allows ICMP + TCP port 80, source tag `demo`
- Resource protocols: TCP restricted to port 80, UDP allow all, ICMP allowed

## Gotchas
- `accessConfigs: [{}]` must be empty array entry to request ephemeral IP on network interfaces
- Connector startup script requires `pulumi.interpolate` (not template literals) because `accessToken`/`refreshToken` are Pulumi Output types resolved at deploy time
- User-to-group assignment is **manual** — not automated in this IaC setup
- Firewall uses source tags (`demo`), not IP ranges — VMs must have the `demo` tag to be governed by this rule
- API token should always be set with `--secret` flag

## Related Docs
- Twingate Pulumi provider (general prerequisites)
- GCP IAM permissions for resource creation
- Twingate Admin Panel (for network name and API token generation)
- [Twingate Pulumi GitHub examples](https://github.com/Twingate)
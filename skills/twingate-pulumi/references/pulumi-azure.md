# Pulumi with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Pulumi with TypeScript. Creates a Connector VM and test web server VM in Azure, with corresponding Twingate Remote Network, Connector, Group, and Resource configured for access.

## Key Information
- Uses TypeScript with `@pulumi/azure`, `@pulumi/azure-native`, and `@twingate/pulumi-twingate` packages
- Deploys two VMs: one for Twingate Connector (Ubuntu 22.04), one test web server (Ubuntu 16.04)
- Connector VM uses `userData` with base64-encoded startup script; web server uses `customData`
- VNet CIDR: `10.0.0.0/16`, subnet: `10.0.1.0/24`
- Both VMs use `Standard_B1ms` size

## Prerequisites
- Azure account with permissions to create/delete resources
- Pulumi CLI installed (see general Pulumi prerequisites)
- Azure CLI (`az`) installed and logged in
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step

1. `mkdir twingate_pulumi_azure_demo && cd twingate_pulumi_azure_demo`
2. `pulumi new typescript`
3. Install modules: `npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate`
4. Authenticate: `az login && az account set --subscription=<id>`
5. Set config values (see below)
6. Write `index.ts` with full resource definitions
7. `pulumi preview` then `pulumi up`
8. Assign Twingate user to created Group manually
9. Teardown: `pulumi down`

## Configuration Values

```bash
pulumi config set twingate:network <yournetwork>
pulumi config set twingate:apiToken <yourToken> --secret
pulumi config set twingate_pulumi_azure_demo:username tgadmin
pulumi config set twingate_pulumi_azure_demo:password --secret <password>
pulumi config set azure-native:location uksouth
```

**Connector startup script env vars:**
- `TWINGATE_ACCESS_TOKEN`
- `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_URL` → `https://<network>.twingate.com`

## Gotchas
- **Secrets file**: `Pulumi.demo.yaml` stores encrypted secrets — exclude from source control
- **Azure password policy**: VM password must meet Azure complexity requirements
- **User access not automated**: After `pulumi up`, manually add Twingate user to the created group
- `customData` (web server) vs `userData` (connector) — different fields used for startup scripts
- NSG `sourceAddressPrefix` in example is hardcoded to a specific IP (`88.98.90.108/32`) — change for your environment
- Web server uses Python 2 `SimpleHTTPServer` — only works on Ubuntu 16.04 image

## Related Docs
- Twingate Pulumi provider: [GitHub](https://github.com/Twingate/pulumi-twingate)
- General Pulumi prerequisites (Twingate docs)
- Twingate API key generation guide
- Additional examples: Twingate GitHub repository
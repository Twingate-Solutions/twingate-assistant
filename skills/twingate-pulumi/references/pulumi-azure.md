# Pulumi with Azure and Twingate

## Page Title
How to Use Pulumi with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Pulumi with TypeScript. Creates a Connector VM and a test web server VM in Azure, with corresponding Twingate Remote Network, Connector, Group, and Resource. The Connector VM bootstraps via startup script using Twingate access/refresh tokens.

## Key Information
- Language: TypeScript
- npm packages: `@pulumi/azure-native`, `@pulumi/azure`, `@twingate/pulumi-twingate`
- Two VMs created: Connector VM (Ubuntu 22.04 Jammy) and test web server VM (Ubuntu 16.04 LTS)
- Connector VM size: `Standard_B1ms`
- VNet CIDR: `10.0.0.0/16`, Subnet: `10.0.1.0/24`
- Web server runs Python SimpleHTTPServer on port 80

## Prerequisites
- Azure account with permissions to create/delete resources
- Bash-compatible OS
- Pulumi CLI installed
- Azure CLI (`az`) installed and authenticated
- Twingate API key and tenant name

## Step-by-Step
1. `mkdir twingate_pulumi_azure_demo && cd twingate_pulumi_azure_demo`
2. `pulumi new typescript`
3. Install modules: `npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate`
4. Authenticate Azure: `az login && az account set --subscription=<id>`
5. Set Pulumi config values (see below)
6. Write `index.ts` with full resource definitions
7. `pulumi preview` then `pulumi up`
8. Assign Twingate user to the created Group manually
9. Tear down: `pulumi down`

## Configuration Values

```bash
pulumi config set twingate:network <yournetwork>
pulumi config set twingate:apiToken <yourToken> --secret
pulumi config set twingate_pulumi_azure_demo:username tgadmin
pulumi config set twingate_pulumi_azure_demo:password --secret <password>
pulumi config set azure-native:location uksouth
```

**Connector startup script env vars:**
- `TWINGATE_ACCESS_TOKEN` — from `TwingateConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `TwingateConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

## Gotchas
- Azure password must meet [Azure Password Requirements](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/faq#what-are-the-password-requirements-when-creating-a-vm)
- `Pulumi.demo.yaml` stores encrypted secrets — exclude from source control
- NSG `sourceAddressPrefix` in example is hardcoded (`88.98.90.108/32`) — replace with your IP
- `customData` (web server) vs `userData` (connector) — different fields used for startup scripts
- Web server VM uses deprecated Ubuntu 16.04; connector uses 22.04
- User-to-Group assignment must be done manually after `pulumi up`

## Related Docs
- Twingate Pulumi provider general prerequisites
- Twingate API key generation guide
- Additional examples: [Twingate GitHub repository](https://github.com/Twingate)
# Pulumi with Azure and Twingate

## Summary
Automates Twingate deployment on Microsoft Azure using Pulumi with TypeScript. Creates a Connector VM and test web server VM in Azure, with corresponding Twingate Remote Network, Connector, Group, and Resource. The Connector VM bootstraps via startup script using Twingate access/refresh tokens.

## Key Information
- Uses TypeScript with `@pulumi/azure-native`, `@pulumi/azure`, and `@twingate/pulumi-twingate` packages
- Creates two VMs: Connector VM (Ubuntu 22.04) and test web server VM (Ubuntu 16.04)
- Connector VM size: `Standard_B1ms`; installs via `https://binaries.twingate.com/connector/setup.sh`
- VNet: `10.0.0.0/16`, subnet: `10.0.1.0/24`
- Web server VM runs Python SimpleHTTPServer on port 80 via `customData` (base64-encoded)
- Connector uses `userData` (base64-encoded) for startup script

## Prerequisites
- Azure account with permissions to create/delete resources
- Pulumi CLI installed with general Pulumi prerequisites met
- Azure CLI (`az`) installed and authenticated
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step
1. `mkdir twingate_pulumi_azure_demo && cd twingate_pulumi_azure_demo`
2. `pulumi new typescript`
3. Install modules: `npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate`
4. Authenticate Azure: `az login && az account set --subscription=<id>`
5. Set Pulumi config values (see below)
6. Write `index.ts` with all resources
7. `pulumi preview` then `pulumi up`
8. Teardown: `pulumi down`

## Configuration Values
```bash
pulumi config set twingate:network <yourNetwork>
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
- Web server VM uses deprecated Ubuntu 16.04; Connector VM uses 22.04 — mix may cause issues in production
- NSG `sourceAddressPrefix` (`88.98.90.108/32`) is hardcoded — replace with your IP
- Secrets stored in `Pulumi.<stack>.yaml` — exclude from source control
- Connector tokens passed via `userData`; web server init via `customData` — these are different Azure VM mechanisms
- After `pulumi up`, manually assign the Twingate user to the created group

## Related Docs
- Twingate Pulumi provider: `@twingate/pulumi-twingate`
- Additional examples: Twingate GitHub repository
- Twingate API key generation guide
- General Pulumi prerequisites guide
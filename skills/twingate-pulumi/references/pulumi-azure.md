# Pulumi with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Pulumi with TypeScript. Creates a Connector VM and test web server VM in Azure, with corresponding Twingate Remote Network, Connector, Group, and Resource. The Connector VM auto-installs via startup script using connector tokens.

## Key Information
- Language: TypeScript
- Creates 2 Azure VMs: one for Twingate Connector, one as test web server
- Connector tokens injected via `userData` (base64-encoded startup script)
- Web server VM uses `customData` for init script
- VMs use `Standard_B1ms` size; Connector uses Ubuntu 22.04, web server uses Ubuntu 16.04

## Prerequisites
- Azure account with permissions to create/delete resources
- Pulumi CLI installed with general Pulumi prerequisites met
- Azure CLI (`az`) installed and authenticated
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step

1. `mkdir twingate_pulumi_azure_demo && cd twingate_pulumi_azure_demo`
2. `pulumi new typescript` (stack name: `azure`)
3. Install modules: `npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate`
4. Authenticate Azure: `az login && az account set --subscription=<id>`
5. Set Pulumi config values (see below)
6. Write `index.ts` with full resource definitions
7. `pulumi preview` then `pulumi up`
8. Assign Twingate user to the created group manually
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
- `TWINGATE_ACCESS_TOKEN` — from `TwingateConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `TwingateConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

**Twingate Resource protocols:** TCP ports `22`, `80` restricted; UDP allow-all; ICMP enabled.

## Gotchas
- Azure password must meet [Azure Password Requirements](https://docs.microsoft.com/azure/virtual-machines/windows/faq#what-are-the-password-requirements-when-creating-a-vm)
- Exclude `Pulumi.<stack>.yaml` from source control (contains encrypted secrets)
- Connector VM uses `userData` (not `customData`) for startup script
- Security group `sourceAddressPrefix` is hardcoded to a specific IP (`88.98.90.108/32`) — update for your environment
- After `pulumi up`, manually assign Twingate users to the created group; this is not automated
- Web server VM uses deprecated Ubuntu 16.04 LTS image

## Related Docs
- Twingate Pulumi provider: `@twingate/pulumi-twingate`
- [Additional Pulumi + Azure examples on GitHub](https://github.com/Twingate)
- General Pulumi guides prerequisites (Twingate docs)
- Twingate API key generation instructions
---
source: https://www.twingate.com/docs/pulumi-azure
type: docs
fetched: 2026-08-14
source_version: 98e7161eb32a5b566d0156f3c4a43ea89556a3b2ef7d6a6af93cdc373d202b1b
---

# Pulumi with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Pulumi with TypeScript. Creates a Connector VM and a test web server VM, then configures Twingate resources/groups to control access. The Connector VM auto-installs via a startup script using connector tokens.

## Key Information
- Language: TypeScript
- Creates: RemoteNetwork, Connector, ConnectorTokens, Group, TwingateResource in Twingate + ResourceGroup, VNet, NSG, 2x VMs in Azure
- Connector VM: Ubuntu 22.04 (Jammy), installs via `binaries.twingate.com/connector/setup.sh`
- Test VM: Ubuntu 16.04-LTS, runs Python SimpleHTTPServer on port 80
- VM size: `Standard_B1ms` for both VMs

## Prerequisites
- Azure account with permissions to create/delete resources
- Pulumi CLI installed (see general Pulumi prerequisites)
- `az` CLI installed and authenticated
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step

1. `mkdir twingate_pulumi_azure_demo && cd twingate_pulumi_azure_demo`
2. `pulumi new typescript`
3. Install modules: `npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate`
4. `az login && az account list && az account set --subscription=<id>`
5. Set Pulumi config (see below)
6. Write `index.ts` (full code in docs)
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

**Connector startup env vars:**
- `TWINGATE_ACCESS_TOKEN` — from `TwingateConnectorTokens.accessToken`
- `TWINGATE_REFRESH_TOKEN` — from `TwingateConnectorTokens.refreshToken`
- `TWINGATE_URL` — `https://<network>.twingate.com`

## Gotchas
- Azure password must meet [Azure Password Requirements](https://docs.microsoft.com/azure/virtual-machines/linux/faq#what-are-the-password-requirements-when-creating-a-vm)
- NSG `sourceAddressPrefix` in the example is hardcoded (`88.98.90.108/32`) — replace with your IP
- Connector uses `userData` (base64); test VM uses `customData` (base64) — different fields
- After `pulumi up`, user-to-group assignment in Twingate must be done manually
- Exclude `Pulumi.<stack>.yaml` from source control (contains encrypted secrets)

## Related Docs
- [Twingate Pulumi Provider](https://www.twingate.com/docs/pulumi)
- [Generate API Key](https://www.twingate.com/docs/api-overview)
- [GitHub Examples Repository](https://github.com/Twingate-Labs/pulumi-twingate)
---
source: https://www.twingate.com/docs/pulumi-azure
type: docs
fetched: 2026-10-04
source_version: 3c24bd51b3052238f3bc8d52fe88d1668bbc4eeb4e52d0a38c92f65416b88fae
trust: official
---

# Pulumi with Azure and Twingate

## Summary
Automates Twingate deployment on Microsoft Azure using Pulumi (TypeScript). Creates a Connector VM and a test web server VM, wiring them together with Twingate Remote Network, Group, and Resource objects. Community-maintained open source tooling; support via GitHub Issues.

## Prerequisites
- Azure account with permissions to create/delete resources
- Pulumi CLI installed and configured (see general Pulumi prerequisites)
- Azure CLI (`az`) installed
- Node.js / npm
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step

1. **Scaffold project**: `mkdir twingate_pulumi_azure_demo && cd twingate_pulumi_azure_demo && pulumi new typescript`
2. **Install modules**: `npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate`
3. **Authenticate Azure**: `az login && az account set --subscription=<id>`
4. **Set Pulumi config** (see Configuration Values below)
5. **Write `index.ts`** with resources in order: Twingate objects → Azure Resource Group → Networking → VMs → Twingate Resource
6. **Preview**: `pulumi preview`
7. **Deploy**: `pulumi up`
8. **Assign** Twingate user to the created Group manually
9. **Teardown**: `pulumi down`

## Configuration Values

```bash
pulumi config set twingate:network <yourNetwork>
pulumi config set twingate:apiToken <yourToken> --secret
pulumi config set twingate_pulumi_azure_demo:username tgadmin
pulumi config set twingate_pulumi_azure_demo:password --secret <password>
pulumi config set azure-native:location uksouth
```

## Key Twingate Resources Created

| Resource | Purpose |
|---|---|
| `TwingateRemoteNetwork` | Logical network in Twingate for Azure |
| `TwingateConnector` | Connector bound to remote network |
| `TwingateConnectorTokens` | Access/refresh tokens injected into Connector VM `userData` |
| `TwingateGroup` | Group scoping access to the resource |
| `TwingateResource` | Maps to web server private IP; TCP ports 22, 80 |

## Azure Resources Created

- Resource Group (UK South default)
- Static Public IP (Standard SKU, Zone 1) — for Connector VM only
- VNet `10.0.0.0/16`, subnet `10.0.1.0/24`
- Network Security Group (inbound SSH/HTTP, restrict `sourceAddressPrefix`)
- **Connector VM**: Ubuntu 22.04 LTS, `Standard_B1ms`, runs Twingate installer via `userData`
- **Web Server VM**: Ubuntu 16.04 LTS, `Standard_B1ms`, runs `python -m SimpleHTTPServer 80`

## Connector Installer
The Connector VM installs via script fetched from `binaries.twingate.com/connector/setup.sh`, passing `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, and `TWINGATE_URL` as environment variables via `userData` (base64-encoded).

## Gotchas
- Azure VM passwords must meet [Azure Password Requirements](https://learn.microsoft.com/azure/virtual-machines/windows/faq#what-are-the-password-requirements-when-creating-a-vm)
- `Pulumi.<stack>.yaml` stores encrypted secrets — exclude from source control
- NSG `sourceAddressPrefix` in example is hardcoded to a specific IP; update for your environment
- Web server VM uses Python 2 (`SimpleHTTPServer`); Ubuntu 16.04 is EOL — consider updating image
- User-to-Group assignment must be done manually after `pulumi up`
- `customData` vs `userData`: web server uses `customData`, Connector uses `userData` — both base64-encoded

## Related Docs
- [Twingate Pulumi GitHub repository](https://github.com/Twingate) (additional examples)
- Twingate general Pulumi prerequisites guide
- T
# Pulumi with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Pulumi with TypeScript. Creates a Connector VM and test web server VM, wires them together with Twingate resources/groups, and configures network access. Uses `@twingate/pulumi-twingate` provider alongside `@pulumi/azure-native`.

## Key Information
- Language: TypeScript (Node.js)
- Creates: RemoteNetwork, Connector, ConnectorTokens, Group, Resource in Twingate + Resource Group, VNet, NSG, two VMs in Azure
- Connector VM: Ubuntu 22.04 (jammy), installs via `binaries.twingate.com/connector/setup.sh`
- Web server VM: Ubuntu 16.04-LTS, runs Python SimpleHTTPServer on port 80
- VM size: `Standard_B1ms` for both VMs
- VNet CIDR: `10.0.0.0/16`, subnet: `10.0.1.0/24`

## Prerequisites
- Azure account with resource creation permissions
- Azure CLI (`az`) installed and authenticated
- Pulumi CLI installed
- Node.js/npm
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step
1. `mkdir twingate_pulumi_azure_demo && cd twingate_pulumi_azure_demo`
2. `pulumi new typescript`
3. Install packages: `npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate`
4. `az login && az account set --subscription=<id>`
5. Set Pulumi config values (see below)
6. Write `index.ts` with full configuration
7. `pulumi preview` then `pulumi up`
8. Teardown: `pulumi down`

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

**Connector install:**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo TWINGATE_ACCESS_TOKEN="..." TWINGATE_REFRESH_TOKEN="..." TWINGATE_URL="..." bash
```

## Gotchas
- Azure VM passwords must meet [Azure Password Requirements](https://docs.microsoft.com/azure/virtual-machines/windows/faq#what-are-the-password-requirements-when-creating-a-vm)
- Connector uses `userData` (base64); web server uses `customData` (base64) — different fields
- NSG `sourceAddressPrefix` in example is hardcoded to a specific IP (`88.98.90.108/32`) — update for your environment
- Secrets stored in `Pulumi.<stack>.yaml` — exclude from source control
- Must manually assign the Twingate user to the created Group after deployment
- Both `@pulumi/azure` and `@pulumi/azure-native` are used (not interchangeable)

## Related Docs
- [Pulumi guides prerequisites](https://www.twingate.com/docs/pulumi)
- [Twingate API key generation](https://www.twingate.com/docs/api-overview)
- [GitHub examples repository](https://github.com/Twingate-Labs/twingate-pulumi-examples)
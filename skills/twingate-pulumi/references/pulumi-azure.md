# Pulumi with Azure and Twingate

## Page Title
How to Use Pulumi with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Pulumi with TypeScript. Creates a Connector VM and test web server VM, wires up Twingate Remote Network/Connector/Resource/Group, and configures Azure networking. The Connector VM auto-installs via a startup script using connector tokens.

## Key Information
- Language: TypeScript
- Creates: RemoteNetwork, Connector, ConnectorTokens, Group, TwingateResource + Azure VNet, NSG, two VMs
- Connector VM: Ubuntu 22.04 (Jammy); Web server VM: Ubuntu 16.04 LTS
- VM size: `Standard_B1ms` for both VMs
- VNet CIDR: `10.0.0.0/16`, subnet: `10.0.1.0/24`
- Connector installed via `https://binaries.twingate.com/connector/setup.sh`

## Prerequisites
- Azure account with permissions to create/delete resources
- Pulumi CLI installed with general Pulumi prerequisites met
- `az` CLI installed and authenticated
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step

1. `mkdir twingate_pulumi_azure_demo && cd twingate_pulumi_azure_demo`
2. `pulumi new typescript`
3. Install modules: `npm install @pulumi/azure-native @pulumi/azure @twingate/pulumi-twingate`
4. Authenticate Azure: `az login && az account set --subscription=<id>`
5. Set Pulumi config (see Configuration Values below)
6. Write `index.ts` (see Final Code section in source)
7. `pulumi preview` → `pulumi up`
8. Grant Twingate user access to the created Group
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

**TwingateResource protocol config:**
- TCP: `RESTRICTED`, ports `["22", "80"]`
- UDP: `ALLOW_ALL`
- ICMP: `true`

## Gotchas
- Azure VM password must meet [Azure Password Requirements](https://docs.microsoft.com/azure/virtual-machines/windows/faq#what-are-the-password-requirements-when-creating-a-vm)
- Secrets stored in `Pulumi.<stack>.yaml` — exclude from source control
- NSG `sourceAddressPrefix` in example is hardcoded (`88.98.90.108/32`) — update for your IP
- Web server VM uses Python 2's `SimpleHTTPServer` (Ubuntu 16.04); may need adjustment for newer images
- Connector VM uses `userData` (base64); web server uses `customData` (base64) — different fields
- After `pulumi up`, manually assign Twingate user to the created Group

## Related Docs
- [Pulumi guides prerequisites](https://www.twingate.com/docs/pulumi)
- [Twingate API key generation](https://www.twingate.com/docs/api-overview)
- [Additional Pulumi/Azure examples on GitHub](https://github.com/Twingate)
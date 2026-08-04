# Getting Started with ZimaOS and Twingate

## Summary
Deploys a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to a ZimaOS environment. The Connector bridges the ZimaOS local network to Twingate's remote access infrastructure.

## Prerequisites
- Running ZimaOS instance with web UI accessible locally
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one → choose **ZimaOS** option
3. Scroll to **Step 2** → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy Connector via App Store
1. Open ZimaOS web UI → navigate to **App Store**
2. Search "Twingate" → click Twingate Connector app → **Install**
3. On dashboard, hover over Twingate tile → click **…** → **Settings**
4. Set **Web UI** dropdown to `https`, add `{network_name}.twingate.com/networks/overview`
5. Fill **Environment Variables** with tokens and network name
6. Click **Save** — container starts automatically

### 3. Verify Installation
Admin Console → **Remote Networks** → select network → select Connector → confirm **Controller** and **Relay** statuses show **Connected**

### 4. Expose ZimaOS Dashboard as Resource
1. Admin Console → **Resources** → **+ Resource**
2. Select the remote network, provide a name (e.g., "ZimaOS")
3. Enter dashboard's local IP (format: `192.168.x.x`)
4. Select a group → **Grant Access**
5. Connect Twingate client → navigate to dashboard IP to verify remote access

## Configuration Values

| Field | Value |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | Token from Admin Console Step 2 |
| `TWINGATE_REFRESH_TOKEN` | Token from Admin Console Step 2 |
| `TWINGATE_NETWORK` | Subdomain of Twingate URL (e.g., `example` from `example.twingate.com`) |
| Web UI URL | `https://{network_name}.twingate.com/networks/overview` |

## Gotchas
- **Do not reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Network name = subdomain only (e.g., `example`, not `example.twingate.com`)
- Container does not connect successfully until environment variables are saved post-install
- Dashboard IP must be the same private IP used for local access (`192.168.x.x`)

## Troubleshooting
- Token errors: re-verify Access/Refresh token values are copied exactly
- Connectivity issues: confirm ZimaOS web UI is locally accessible and container is running
- Reference: [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [CasaOS Setup Guide](https://www.twingate.com/docs/casaos-getting-started)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Configuring Resources](https://www.twingate.com/docs/resources)
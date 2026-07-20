# Getting Started with CasaOS and Twingate

## Summary
Deploy a Twingate Connector on CasaOS via the custom app store installation using Docker Compose. This enables secure remote access to your CasaOS dashboard and other private resources on your home network.

## Key Information
- Connector is deployed as a Docker container via CasaOS custom app install
- Docker Compose config is generated from the Twingate Admin Console (includes tokens)
- Each Connector requires its own unique Access/Refresh token pair — never reuse tokens
- After deployment, verify Connector shows **Controller** and **Relay** statuses as `Connected`

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- An existing Remote Network in Twingate Admin Console

## Step-by-Step

### 1. Generate Docker Compose Config
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector (or select undeployed one) → choose **Homelab** → select **CasaOS**
3. Scroll to Step 2 → click **Generate Tokens** → authenticate
4. Copy the full Docker Compose configuration (contains Network name, Access token, Refresh token)

### 2. Deploy via CasaOS Custom Install
1. Open CasaOS web UI → **App Store**
2. Click **Custom Install** (top right)
3. Click **Import** on the Manual App Install page
4. Paste the Docker Compose config → **Submit** → **Ok** → **Install**

### 3. Verify Connector
1. Admin Console → **Remote Networks** → select network → select Connector
2. Confirm **Controller** and **Relay** statuses show `Connected`

### 4. Add CasaOS Dashboard as a Resource
1. Admin Console → **Resources** → **+ Resource**
2. Select the Remote Network
3. Name the resource (e.g., `CasaOS Dashboard`)
4. Add private IP (format: `192.168.x.x`) — same address used for local access
5. Select a group → **Grant Access**

## Configuration Values
| Value | Source |
|-------|--------|
| Access Token | Generated in Admin Console Step 2 |
| Refresh Token | Generated in Admin Console Step 2 |
| Network Name | From Admin Console Remote Network |
| Dashboard IP | Local LAN IP (e.g., `192.168.x.x`) |

## Gotchas
- **Do not reuse token sets** — each Connector must have unique Access/Refresh tokens
- Private IP for the Resource must match the locally-accessible CasaOS dashboard address
- CasaOS web UI must be locally accessible before attempting Twingate setup

## Troubleshooting
- **Token Errors**: Re-verify Access/Refresh tokens are correctly pasted from the config
- **Connectivity**: Confirm CasaOS web interface is reachable locally and the Connector container is running

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [ZimaOS Setup Guide](https://www.twingate.com/docs/zimaos)
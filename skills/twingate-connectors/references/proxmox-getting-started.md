# Getting Started with Proxmox VE and Twingate

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector on Proxmox VE using a community helper script that creates an LXC container. Requires pre-generated Access and Refresh tokens from the Twingate Admin Console before running the script.

## Key Information
- Connector is deployed as an LXC container via the Proxmox VE Helper Scripts community repository
- Each Connector requires its own unique token pair (do not reuse tokens)
- Script runs on the Proxmox VE head node

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Remote Network already created in Twingate Admin Console

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens → copy Access Token and Refresh Token
2. **Run helper script** on Proxmox head node:
   ```bash
   bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
   ```
3. **Enter when prompted**:
   - Network: `<network>.twingate.com`
   - Access Token
   - Refresh Token
4. **Verify**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay show `connected`

## Configuration Values

| Prompt | Value |
|--------|-------|
| Network | `<yournetwork>.twingate.com` |
| Access Token | From Admin Console token generation |
| Refresh Token | From Admin Console token generation |

## Gotchas
- **Never reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- Tokens must be copied immediately after generation (not retrievable later)
- Script must be run on the head node, not a VM or container

## Troubleshooting
- Token errors: re-verify tokens were entered correctly
- Connectivity issues: confirm Proxmox web interface is locally accessible and the Twingate LXC container is running
- See Twingate troubleshooting docs for persistent issues

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs) — configure access to private apps/services
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
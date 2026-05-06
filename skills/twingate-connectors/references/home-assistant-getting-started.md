# Getting Started with Home Assistant and Twingate

## Summary
Installs a Twingate Connector as a Home Assistant app to enable secure remote access to smart home devices. The connector runs as a Docker container within Home Assistant OS, linking to a Twingate Remote Network via Access/Refresh tokens.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Connector is installed via a third-party repository added to the HA App Store
- Each Connector requires its own unique token pair (do not reuse tokens)
- Source repository available on Twingate's Community GitHub page

## Prerequisites
- Running Home Assistant OS instance
- Twingate account with Admin Console access
- Basic Home Assistant configuration familiarity

## Step-by-Step

1. **Add Repository** — Open HA repository manager, add Twingate repository URL, click Add
2. **Check for Updates** — In App Store, click ellipses → "Check for updates" (refresh page if needed)
3. **Install App** — Search "Twingate" in App Store, select entry under "Twingate Connector app repository", click Install
4. **Generate Tokens** — In Admin Console: Remote Networks → select network → add/select Connector → Manual → Generate Tokens → copy Access Token and Refresh Token
5. **Configure App** — In HA Twingate app Configuration tab, enter Network domain, Access Token, Refresh Token
6. **Start App** — Click Start on Info tab; verify Logs tab shows no errors
7. **Verify** — In Admin Console, confirm Connector shows Controller and Relay status as **connected**

## Configuration Values

| Field | Description | Example |
|-------|-------------|---------|
| Network | Twingate Remote Network domain | `network.twingate.com` |
| Access Token | Generated from Admin Console | (unique per connector) |
| Refresh Token | Generated from Admin Console | (unique per connector) |

## Gotchas
- **Do not reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- After adding the repository, a manual "Check for updates" step is required before the app appears
- Page refresh may also be needed for the app to appear in the App Store
- Home Assistant containers (non-OS) are explicitly unsupported

## Troubleshooting
- Token errors: verify tokens are copied correctly with no extra whitespace
- Connectivity issues: confirm local HA web interface is accessible and the app is running
- Check Logs tab within the Twingate app for runtime errors

## Related Docs
- Twingate Troubleshooting Docs
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
- Setting Up Resources (configuring Twingate resources/access policies)
# Getting Started with Home Assistant and Twingate

## Summary
Installs a Twingate Connector as a Home Assistant app to enable secure remote access to smart home devices. The connector runs as a Docker container managed by Home Assistant OS and connects to a Twingate Remote Network using token-based authentication.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Connector app is hosted in a third-party repository on Twingate's Community GitHub page
- Each Connector requires its own unique Access Token + Refresh Token pair (never reuse tokens)
- Connector runs as a background Docker container after app start

## Prerequisites
- Home Assistant OS (running instance)
- Twingate account with Admin Console access
- A configured Remote Network in Twingate Admin Console

## Step-by-Step

1. **Add Repository** — Open Home Assistant App Store repository manager, add the Twingate repository URL, then close the manager
2. **Check for Updates** — Use ellipses menu → "Check for updates" in App Store; refresh page if needed
3. **Install App** — Search "Twingate" in App Store → select entry under "Twingate Connector app repository" → click Install
4. **Generate Tokens** — In Admin Console: Remote Networks → select network → add/select Connector → Manual → Step 2 → Generate Tokens → copy Access Token and Refresh Token
5. **Configure App** — In app Configuration tab, enter Network domain, Access Token, Refresh Token
6. **Start App** — Click Start; verify in Logs tab for errors
7. **Verify** — In Admin Console, confirm Connector shows Controller and Relay status as **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Home Assistant containers are not supported** — OS only
- Must manually trigger "Check for updates" after adding repository; page refresh may also be required
- **Do not reuse token sets** — each Connector instance requires uniquely generated tokens
- Token entry errors are the most common issue; verify exact copy/paste from Admin Console

## Troubleshooting
- Token errors → re-verify tokens are correctly entered
- Connectivity issues → confirm local HA web interface is accessible and app is running
- Check Logs tab in the app for runtime errors
- Refer to Twingate troubleshooting docs for persistent issues

## Related Docs
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
- Setting Up Resources (configuring Twingate resources/access policies)
- Twingate Apps GitHub page (issue reporting)
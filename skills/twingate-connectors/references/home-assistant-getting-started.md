# Home Assistant + Twingate Getting Started

## Summary
Installs a Twingate Connector as a Home Assistant OS app to enable secure remote access to smart home devices. The app runs a Docker container that connects to a Twingate Remote Network using token-based authentication.

## Key Information
- Deploys Twingate Connector via Home Assistant App Store (third-party repository)
- Connector runs as a background Docker container within Home Assistant OS
- Each Connector requires its own unique Access/Refresh token pair
- Source repository available on Twingate Community GitHub

## Prerequisites
- Home Assistant **OS** (not containers — containers do not support apps)
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate Admin Console

## Step-by-Step

1. **Add repository**: Open repository manager in Home Assistant, add Twingate repository URL
2. **Check for updates**: Use ellipses menu → "Check for updates" in App Store; refresh page if needed
3. **Install app**: Search "Twingate" in App Store → install from "Twingate Connector app repository" section
4. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → "Generate Tokens"
5. **Configure app**: Enter Network domain, Access Token, Refresh Token in Configuration tab
6. **Start app**: Click Start on Info tab; verify no errors in Logs tab
7. **Verify**: Admin Console → Remote Networks → Connector → confirm Controller and Relay show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network-name>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Home Assistant OS only** — container installations are not supported
- **Do not reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- After adding the repository, manually trigger "Check for updates" before the app appears in search results
- Page refresh may be required after adding the repository

## Related Docs
- [Troubleshooting docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
- [Apps GitHub page](https://github.com/Twingate) (issue reporting)
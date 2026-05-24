# Home Assistant + Twingate: Getting Started

## Summary
Installs the Twingate Connector as a Home Assistant OS app to enable secure remote access to smart home devices. The connector runs as a Docker container and links to a Twingate Remote Network via Access/Refresh token pairs.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Connector is installed via a third-party app repository added to the HA App Store
- Each Connector requires its own unique token set (do not reuse tokens)
- Source available on Twingate's Community GitHub page

## Prerequisites
- Running Home Assistant OS instance
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Add Repository**: Open HA App Store → add Twingate repository URL via repository manager
2. **Check for Updates**: Use ellipsis menu → "Check for updates"; refresh page if needed
3. **Install App**: Search "Twingate" in App Store → install from "Twingate Connector app repository" section
4. **Generate Tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens → copy Access Token and Refresh Token
5. **Configure App**: App Configuration tab → enter Network domain, Access Token, Refresh Token
6. **Start App**: Info tab → click Start → check Logs tab for errors
7. **Verify**: Admin Console → Remote Networks → Connector → confirm Controller and Relay show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Home Assistant containers not supported** — OS installation required
- After adding repository, must manually trigger "Check for updates" before app appears; may also require page refresh
- Token sets must be unique per Connector — never reuse across multiple deployments
- Connector name in Admin Console must not have been previously deployed

## Related Docs
- [Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
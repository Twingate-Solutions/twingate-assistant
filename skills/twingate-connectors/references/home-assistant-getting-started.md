# Home Assistant + Twingate Getting Started

## Summary
Installs a Twingate Connector as a Home Assistant app to enable secure remote access to smart home devices. The connector runs as a Docker container within Home Assistant OS and connects to a Twingate Remote Network using Access/Refresh token pairs.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Connector is installed via a third-party app repository added to the HA App Store
- Repository source available on Twingate's Community GitHub page
- Each Connector requires its own unique token set (do not reuse tokens)

## Prerequisites
- Home Assistant OS (running instance)
- Twingate account with Admin Console access
- An existing Remote Network in Twingate Admin Console

## Step-by-Step

1. **Add Repository**: Add Twingate repository URL via Home Assistant App Store → Repository Manager
2. **Check for Updates**: Use ellipses menu → "Check for updates"; refresh page if needed
3. **Install App**: Search "Twingate" in App Store → install from "Twingate Connector app repository" section
4. **Generate Tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens → copy Access Token and Refresh Token
5. **Configure App**: In HA Twingate app Configuration tab, enter:
   - Network domain (e.g., `yournetwork.twingate.com`)
   - Access Token
   - Refresh Token
6. **Start App**: Click Start; verify no errors in Logs tab
7. **Verify**: Admin Console → Remote Networks → Connector → confirm Controller and Relay show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Home Assistant containers not supported** — OS version only
- After adding repository, must manually trigger "Check for updates" and possibly refresh the page before app appears
- **Never reuse token sets** across multiple Connectors — each Connector needs unique tokens
- Tokens must be copied immediately after generation (not retrievable later)

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
- Setting Up Resources (configuring Twingate resources for private app access)
- [Community GitHub / Apps GitHub](https://github.com/Twingate-Labs) for issues/feedback
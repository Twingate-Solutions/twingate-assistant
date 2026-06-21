# Home Assistant + Twingate Getting Started

## Summary
Installs a Twingate Connector as a Home Assistant app to enable secure remote access to smart home devices. The connector runs as a Docker container managed by Home Assistant OS and links to a Twingate Remote Network via token-based authentication.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Connector is installed via a third-party app repository added to the HA App Store
- Each Connector requires its own unique Access/Refresh token pair (no reuse)
- Source available on [Twingate Community GitHub](https://github.com)

## Prerequisites
- Home Assistant OS (running instance)
- Twingate account with Admin Console access
- Existing Remote Network in Twingate Admin Console

## Step-by-Step

1. **Add Repository** — Open HA repository manager, add the Twingate repository URL; close dialog
2. **Check for Updates** — In App Store, click ellipsis → "Check for updates" (may need page refresh)
3. **Install App** — Search "Twingate" in App Store → install entry under "Twingate Connector app repository"
4. **Generate Tokens** — In Admin Console: Remote Networks → select network → add/select Connector → Manual → Generate Tokens → copy Access Token + Refresh Token
5. **Configure App** — In HA Twingate app Configuration tab, enter:
   - Network domain
   - Access Token
   - Refresh Token
6. **Start App** — Click Start; check Logs tab for errors
7. **Verify** — In Admin Console, confirm Connector shows `Controller` and `Relay` status as **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Home Assistant containers are unsupported** — OS variant only
- **Do not reuse token sets** — each Connector must have unique tokens
- After adding repository, manually trigger "Check for updates" in App Store; a page refresh may also be required
- Search for app under the "Twingate Connector app repository" section specifically (not generic search results)

## Troubleshooting
- Token errors: re-verify copy/paste accuracy of both tokens
- Connectivity issues: confirm HA web interface is locally accessible and app is running
- Check Logs tab in the Twingate app for runtime errors

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs/proxmox)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
# Getting Started with Home Assistant and Twingate

## Page Title
Getting Started with Home Assistant and Twingate

## Summary
Installs a Twingate Connector as an app on Home Assistant OS to enable secure remote access to smart home devices. The setup involves adding a third-party repository, installing the app, and configuring it with tokens generated from the Twingate Admin Console.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Twingate runs as a Docker container managed by the Home Assistant app framework
- Each Connector requires its own unique Access/Refresh token pair — do not reuse tokens
- Repository source available on Twingate's Community GitHub page

## Prerequisites
- Running Home Assistant OS instance
- Twingate account with Admin Console access
- Basic familiarity with Home Assistant configuration

## Step-by-Step

1. **Add Repository** — Open Home Assistant App Store → Repository Manager → Add Twingate repository URL
2. **Check for Updates** — Use ellipses menu → "Check for updates"; refresh page if needed
3. **Install App** — App Store → Search "Twingate" → Select entry under "Twingate Connector app repository" → Install
4. **Generate Tokens** — Admin Console → Remote Networks → Select network → Add/select Connector → Manual → Step 2 → Generate Tokens → Copy Access Token and Refresh Token
5. **Configure App** — Twingate app → Configuration tab → Enter Network domain, Access Token, Refresh Token
6. **Start App** — Info tab → Click Start → Check Logs tab for errors
7. **Verify** — Admin Console → Remote Networks → Select Connector → Confirm Controller and Relay show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Container installs unsupported** — must be Home Assistant OS, not Docker/container deployments
- After adding the repository, a manual "Check for updates" is required before the app appears; page refresh may also be needed
- Token reuse across Connectors will cause issues — generate a fresh token set per Connector
- Tokens are only shown once at generation time — copy immediately

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs/proxmox)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Apps GitHub Page](https://github.com/twingate) (for issue reporting)
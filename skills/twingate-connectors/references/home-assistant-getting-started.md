# Getting Started with Home Assistant and Twingate

## Page Title
Getting Started with Home Assistant and Twingate

## Summary
Installs a Twingate Connector as a Home Assistant app to enable secure remote access to smart home devices. The connector runs as a Docker container within Home Assistant OS and connects to a Twingate Remote Network using token-based authentication.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Connector runs as a background Docker container
- Source repository available on Twingate Community GitHub page
- Each Connector requires its own unique token set (do not reuse tokens)

## Prerequisites
- Running Home Assistant OS instance
- Twingate account with Admin Console access
- Basic Home Assistant configuration familiarity

## Step-by-Step

1. **Add repository**: Open repository manager in Home Assistant, add Twingate repository URL
2. **Check for updates**: Use ellipses menu → "Check for updates" in App Store; refresh page if needed
3. **Install app**: Search "Twingate" in App Store → install from "Twingate Connector app repository" section
4. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → Step 2 → Generate Tokens → copy both tokens
5. **Configure app**: Configuration tab → enter Network domain, Access Token, Refresh Token
6. **Start app**: Info tab → click Start → verify via Logs tab
7. **Verify**: Admin Console → Remote Networks → select Connector → confirm Controller and Relay show `connected`

## Configuration Values

| Field | Value |
|-------|-------|
| `Network` | `<network>.twingate.com` |
| `Access Token` | Generated from Admin Console |
| `Refresh Token` | Generated from Admin Console |

## Gotchas
- After adding the repository, manually trigger "Check for updates" — new apps don't appear automatically
- Page refresh may also be required after adding repository
- Tokens are one-time use per Connector — never reuse a token set across multiple Connectors
- Home Assistant container installs are explicitly unsupported

## Related Docs
- Twingate troubleshooting docs
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
- Setting Up Resources (configuring Twingate resources post-install)
- Apps GitHub page (bug reports/feedback)
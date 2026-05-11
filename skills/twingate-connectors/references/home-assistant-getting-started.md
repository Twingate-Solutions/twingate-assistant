# Getting Started with Home Assistant and Twingate

## Summary
Installs a Twingate Connector as a Home Assistant app to enable secure remote access to smart home devices. The connector runs as a Docker container managed by Home Assistant OS and links to a Twingate Remote Network via token-based authentication.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Connector runs as a background Docker container
- Repository source available on Twingate Community GitHub page
- Each Connector requires its own unique Access/Refresh token pair

## Prerequisites
- Running Home Assistant OS instance
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Add Repository** — Open App Store repository manager, add Twingate repository URL
2. **Check for Updates** — Use ellipsis menu → "Check for updates"; refresh page if needed
3. **Install App** — Search "Twingate" in App Store, install from "Twingate Connector app repository" section
4. **Generate Tokens** — Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens
5. **Configure App** — Configuration tab, enter Network domain, Access Token, Refresh Token
6. **Start App** — Click Start; verify via Logs tab
7. **Verify** — Admin Console → Remote Networks → Connector → confirm Controller and Relay show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Do not reuse token sets** — each Connector must have unique Access/Refresh tokens
- After adding the repository, manually trigger "Check for updates" in App Store; a page refresh may also be required
- Home Assistant container installs are not supported — OS installs only
- Token errors and connectivity issues are the most common failure points

## Related Docs
- Twingate Troubleshooting Docs
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
- Setting Up Resources (configuring Twingate Resources for private app access)
- Twingate Apps GitHub page (bug reports/feedback)
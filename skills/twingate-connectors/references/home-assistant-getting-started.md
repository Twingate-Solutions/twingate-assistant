---
source: https://www.twingate.com/docs/home-assistant-getting-started
type: docs
fetched: 2026-08-14
source_version: abbfc7012c44a6b063e4c325ab9b3f3b2f3c8c9a500edad5cefbf1241532fe9f
---

# Getting Started with Home Assistant and Twingate

## Summary
Integrates Twingate Connector as a Home Assistant app to enable secure remote access to smart home devices. Installation involves adding a third-party repository, generating connector tokens from the Twingate Admin Console, and configuring the app with those tokens.

## Key Information
- Works **only on Home Assistant OS** — containers are not supported
- The Twingate app runs a Docker container in the background that installs and connects the Connector
- Source repository available on Twingate's Community GitHub page
- Each Connector requires its own unique token set — do not reuse tokens

## Prerequisites
- Home Assistant OS (not container install)
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate Admin Console

## Step-by-Step

1. **Add Repository** — Add Twingate repository via Home Assistant App Store repository manager
2. **Check for Updates** — Use ellipses menu → "Check for updates" in App Store; refresh page if needed
3. **Install App** — Search "Twingate" in App Store, install from "Twingate Connector app repository" section
4. **Generate Tokens** — Admin Console → Remote Networks → select network → add/select Connector → Manual → Step 2 → Generate Tokens
5. **Configure App** — Configuration tab: enter Network domain, Access Token, Refresh Token
6. **Start App** — Click Start; verify in Logs tab
7. **Verify** — Admin Console → Remote Networks → Connector → confirm Controller and Relay show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network-name>.twingate.com` |
| Access Token | Generated from Admin Console (Step 2 of Connector setup) |
| Refresh Token | Generated from Admin Console (Step 2 of Connector setup) |

## Gotchas
- After adding the repository, manually trigger "Check for updates" — new apps don't appear automatically
- Page refresh may also be required after checking for updates
- Token sets must be unique per Connector; reusing tokens will cause issues
- If tokens are entered incorrectly, the Connector will fail to authenticate

## Related Docs
- Twingate troubleshooting docs
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
- Setting Up Resources (configuring Twingate resources for private apps/services)
- Apps GitHub page (bug reports/feedback)
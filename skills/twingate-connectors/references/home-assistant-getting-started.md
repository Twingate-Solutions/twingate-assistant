# Getting Started with Home Assistant and Twingate

## Summary
Installs the Twingate Connector as a Home Assistant app to enable secure remote access to smart home devices. The connector runs as a Docker container managed by Home Assistant OS and links to a Twingate Remote Network via token-based authentication.

## Key Information
- Only works on **Home Assistant OS** — containers are not supported
- Connector runs as a background Docker container
- Repository source available on Twingate Community GitHub page
- Each Connector requires its own unique Access/Refresh token pair

## Prerequisites
- Home Assistant OS (running instance)
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate Admin Console

## Step-by-Step

1. **Add Repository**: Open Home Assistant App Store → repository manager → add Twingate repository URL → close manager
2. **Check for Updates**: Click ellipses (top right) → "Check for updates" → refresh page if needed
3. **Install App**: App Store → search "Twingate" → select entry under "Twingate Connector app repository" → Install
4. **Generate Tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose Manual → Step 2 → Generate Tokens → copy Access Token and Refresh Token
5. **Configure App**: Configuration tab → enter Network domain, Access Token, Refresh Token
6. **Start App**: Info tab → click Start → verify no errors in Logs tab
7. **Verify**: Admin Console → Remote Networks → select Connector → confirm Controller and Relay statuses show **connected**

## Configuration Values

| Field | Format | Example |
|-------|--------|---------|
| Network | Twingate domain | `network.twingate.com` |
| Access Token | Generated in Admin Console | (unique per connector) |
| Refresh Token | Generated in Admin Console | (unique per connector) |

## Gotchas
- **Do not reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- After adding the repository, a manual "Check for updates" is required; page refresh may also be needed before the app appears
- App Store search may not surface the app immediately — look for the "Twingate Connector app repository" section at the bottom

## Troubleshooting
- Token errors: verify tokens are copied correctly with no extra whitespace
- Connectivity issues: confirm Home Assistant web UI is accessible locally and app is running
- Check Logs tab in the Twingate app for error details
- Refer to Twingate troubleshooting docs for persistent issues

## Related Docs
- Twingate Troubleshooting Docs
- Setting Up Resources (configuring private apps/services)
- Proxmox Helper Script Guide
- Unraid Helper Script Guide
- Apps GitHub page (issue reporting)
# Twingate iOS Client

## Summary
Install and configure the Twingate iOS client to connect to private resources. The app authenticates via your organization's identity provider and runs transparently in the background.

## Key Information
- App only intercepts traffic for defined private Resources, not general internet traffic
- Can run in background after initial setup
- Authentication is SSO-based via your organization's identity provider
- Network name format: `<orgname>.twingate.com`

## Prerequisites
- iOS device with App Store access
- Network name (found in welcome email)
- Valid credentials for your organization's identity provider

## Step-by-Step

1. **Install** — Search "Twingate" on App Store or visit `get.twingate.com`
2. **Set Network** — Enter network address (e.g., `autoco.twingate.com`) when prompted, tap **Join Network**
3. **Authenticate** — Tap **Sign in to Connect**; complete login in browser window that opens
4. **Connect** — Browser closes automatically; client shows "online" status
5. **Close app** — App can be closed; connection remains active in background

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Network name | `<org>.twingate.com` | `autoco.twingate.com` |

## Gotchas
- Network name must be entered without `https://` prefix (implied by format)
- If already authenticated with IdP, re-login is usually not required
- App does **not** proxy all traffic — only configured private Resources are intercepted

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Admin: Resource configuration
- Identity Provider integration guides
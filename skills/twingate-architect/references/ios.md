# Twingate iOS Client

## Summary
Install and configure the Twingate iOS client to connect to private resources. The app runs in the background after setup, only intercepting traffic for defined private Resources without affecting regular internet browsing.

## Key Information
- Available on Apple App Store
- Shortcut URL: `get.twingate.com`
- App runs in background after initial setup
- Only intercepts traffic for private Twingate Resources (not general internet traffic)
- Authentication delegated to configured Identity Provider (IdP)

## Prerequisites
- iOS device with App Store access
- Twingate network name (format: `yourcompany.twingate.com`) — found in welcome email
- Valid credentials for your organization's Identity Provider

## Step-by-Step Setup

1. **Install** — Search "Twingate" in App Store or navigate to `get.twingate.com`
2. **Set Network** — Open app, enter network address (e.g., `autoco.twingate.com`), tap **Join Network**
3. **Authenticate** — Tap **Sign in to Connect**; app opens browser for IdP login
4. **Complete Auth** — Enter IdP credentials (skipped if already authenticated); browser closes automatically
5. **Verify** — Client displays "online" status; app can be backgrounded

## Configuration Values

| Field | Format | Example |
|-------|--------|---------|
| Network name | `<tenant>.twingate.com` | `autoco.twingate.com` |

## Gotchas
- Network name must be obtained from welcome email — no in-app discovery
- Authentication opens an external browser window; this is expected behavior
- App must remain running in background to maintain Resource access
- Does **not** proxy all traffic — only configured private Resources are affected

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Identity Provider configuration
- Resource access configuration
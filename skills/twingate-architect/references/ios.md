# Twingate iOS Client

## Summary
Instructions for installing and configuring the Twingate iOS client app. The client authenticates via your organization's identity provider and runs in the background, only intercepting traffic for configured private Resources.

## Key Information
- App available on Apple App Store
- Network name format: `<orgname>.twingate.com`
- Network name found in welcome email
- Client runs persistently in background after setup
- Only intercepts traffic for private Resources, not general internet traffic
- Authentication handled by existing identity provider (SSO)

## Prerequisites
- iOS device
- App Store access
- Organization network name (from welcome email)
- Valid identity provider credentials

## Step-by-Step

1. **Install** — Search "Twingate" in App Store or navigate to `get.twingate.com`
2. **Set Network** — Enter network name (e.g., `autoco.twingate.com`) when prompted on first launch
3. **Join** — Tap "Join Network"
4. **Authenticate** — Tap "Sign in to Connect"; complete IdP login in browser window that opens
5. **Confirm Connected** — Client displays "online" status; browser window closes automatically
6. **Minimize** — App can be closed; connection persists in background

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Network name | `<org>.twingate.com` | `autoco.twingate.com` |

## Gotchas
- If already authenticated with IdP, re-login may not be required
- App must remain running in background to maintain connectivity to Resources
- Normal internet traffic is **not** routed through Twingate — only traffic to defined private Resources

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Admin: configuring Resources
- Identity provider integration
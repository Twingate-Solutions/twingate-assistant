# Twingate iOS Client

## Summary
Instructions for installing and configuring the Twingate iOS client app. The app connects users to private resources via their organization's Twingate network using identity provider authentication.

## Key Information
- App available on Apple App Store (search "Twingate" or visit `get.twingate.com`)
- Network name format: `<orgname>.twingate.com`
- Authentication handled via existing identity provider (SSO)
- App runs in background; only intercepts traffic for configured private Resources, not general internet traffic

## Prerequisites
- iOS device with App Store access
- Organization's Twingate network name (found in welcome email)
- Valid credentials for the organization's identity provider

## Step-by-Step

1. **Install** — Search "Twingate" in App Store or navigate to `get.twingate.com`
2. **Set Network** — Enter network address (e.g., `autoco.twingate.com`) and tap **Join Network**
3. **Authenticate** — Tap **Sign in to Connect**; complete IdP login in the browser window that opens
4. **Connected** — Browser window closes automatically; app shows "online" status
5. **Background operation** — App can be closed; connection persists in background

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Network name | `<org>.twingate.com` | `autoco.twingate.com` |

## Gotchas
- If already authenticated with IdP, login prompt may be skipped automatically
- App must remain connected (not force-quit) to maintain access to private Resources
- Does **not** proxy general internet traffic — only affects configured private Resources

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Admin: Resource configuration
- Identity provider integration guides
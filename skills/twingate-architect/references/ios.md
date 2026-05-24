# Twingate iOS Client

## Summary
Instructions for installing and configuring the Twingate iOS client app. The app connects users to private Resources through their organization's identity provider without affecting regular internet traffic.

## Key Information
- App available on the App Store (also accessible via `get.twingate.com`)
- Network name format: `<orgname>.twingate.com`
- Network name is provided in the welcome email
- App uses a VPN-like mechanism but only intercepts traffic for defined private Resources
- Regular internet browsing is unaffected when Twingate is connected
- App can run in background once connected

## Prerequisites
- iOS device with App Store access
- Organization network name (from welcome email)
- Valid credentials for the organization's identity provider (IdP)

## Step-by-Step

1. **Install** — Search "Twingate" in the App Store or visit `get.twingate.com`
2. **Set Network** — Open app, enter network name (e.g., `autoco.twingate.com`), tap **Join Network**
3. **Authenticate** — Tap **Sign in to Connect**; app opens browser for IdP authentication
4. **Connect** — Complete IdP login; browser closes and client shows "online" status
5. **Use** — Close app; leave it connected in background

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Network name | `<org>.twingate.com` | `autoco.twingate.com` |

## Gotchas
- If already authenticated with the IdP, login step may be skipped automatically
- App must remain running (background) to maintain Resource access
- Only intercepts traffic destined for configured private Resources — not a full VPN tunnel

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Admin: Resource configuration
- Identity provider integration guides
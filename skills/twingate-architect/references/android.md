# Twingate Android Client

## Summary
Install and configure the Twingate Android client to connect to a Twingate network. The app routes only private Resource traffic through Twingate, leaving regular internet traffic unaffected.

## Key Information
- Install via Google Play Store or `get.twingate.com`
- Minimum supported Android version: **Android 10**
- Uses split tunneling by default (only intercepts traffic for private Resources)
- App can remain running in background after setup

## Prerequisites
- Android 10 or higher
- Google Play Store access
- Twingate network name (your organization's subdomain)
- Valid credentials for your organization's Identity Provider (IdP)

## Step-by-Step

1. **Install** — Search "Twingate" on Google Play Store or visit `get.twingate.com`
2. **Set Network** — Open app, enter your Twingate Network name
3. **Authenticate** — Tap "Sign in to connect"; app opens browser for IdP authentication
4. **Connect** — Browser closes automatically; client shows "online" status
5. **Minimize** — Close app UI; connection persists in background

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Network name | Your organization's Twingate subdomain |
| Install URL | `get.twingate.com` |
| Min OS version | Android 10 |

## Gotchas
- If already authenticated with your IdP, the browser step may complete automatically without requiring credential entry
- App must remain running (background) to maintain Resource access; closing/killing the app disconnects the tunnel
- Only private Resource traffic is intercepted — standard internet browsing is unaffected (split tunnel)

## Related Docs
- iOS client setup
- Twingate network administration
- Identity Provider configuration
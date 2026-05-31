# Twingate Android Client

## Summary
Install and configure the Twingate Android client to connect to a Twingate network. The app intercepts only private Resource traffic, leaving regular internet browsing unaffected.

## Key Information
- Install via Google Play Store or `get.twingate.com`
- Minimum supported Android version: **Android 10**
- Authentication handled through identity provider via browser redirect
- App can run in background; only intercepts traffic for configured private Resources

## Prerequisites
- Android 10 or newer
- Google Play Store access
- Twingate Network name (provided by admin)
- Valid identity provider credentials

## Step-by-Step

1. Install the Twingate app from Google Play Store or `get.twingate.com`
2. Open the app and enter your **Twingate Network name**
3. Tap **"Sign in to connect"**
4. Complete authentication in the browser window that opens (uses existing IdP credentials)
5. Browser window closes automatically; client shows **online** status
6. App can be minimized — connection persists in background

## Gotchas
- If already authenticated with your IdP, re-login is typically not required
- App must remain running in background to maintain connection to Resources
- Does **not** route all traffic through Twingate — only traffic to defined private Resources is intercepted

## Related Docs
- iOS client setup
- Desktop client setup
- Twingate Network configuration
- Identity Provider integration
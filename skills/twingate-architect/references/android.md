# Twingate Android Client

## Summary
Installs via Google Play Store and connects to a Twingate network through identity provider authentication. The client runs in the background, only intercepting traffic for defined private Resources.

## Key Information
- Minimum supported Android version: **Android 10**
- Download via Google Play Store or `get.twingate.com`
- Client only intercepts traffic for private Resources, not general internet traffic
- Can remain running in background without impacting regular browsing

## Prerequisites
- Android 10 or higher
- Google Play Store access
- Twingate Network name (provided by admin)
- Valid identity provider credentials

## Step-by-Step

1. **Install** — Search "Twingate" in Google Play Store or visit `get.twingate.com`
2. **Set Network** — Open app, enter your Twingate Network name
3. **Authenticate** — Tap "Sign in to connect"; app opens browser for IdP authentication
4. **Connect** — Browser window closes automatically; client shows "online" status
5. **Background** — Close app; client remains connected in background

## Configuration Values
None (no CLI flags, env vars, or API params for end-user Android setup)

## Gotchas
- If already authenticated with IdP, re-login is typically not required
- App must remain running in background to maintain Resource access (minimize, don't force-quit)
- No support for Android versions below 10

## Related Docs
- iOS client setup
- Twingate Network administration
- Identity provider configuration
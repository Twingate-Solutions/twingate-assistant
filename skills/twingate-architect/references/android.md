# Twingate Android Client

## Summary
Instructions for installing and configuring the Twingate Android client app. The app connects users to their Twingate network via identity provider authentication and only intercepts traffic for configured private Resources.

## Key Information
- Install via Google Play Store or `get.twingate.com`
- Minimum supported Android version: **Android 10**
- App runs in background without affecting regular internet traffic
- Only intercepts network traffic destined for private Twingate Resources

## Prerequisites
- Android 10 or higher
- Google Play Store access
- Twingate Network name (provided by admin)
- Valid identity provider credentials

## Step-by-Step

1. Install Twingate from Google Play Store (search "Twingate") or visit `get.twingate.com`
2. Open the Twingate app
3. Enter your Twingate Network name
4. Tap **"Sign in to connect"**
5. Complete authentication in the browser window that opens (uses existing IdP credentials)
6. Browser window closes automatically; client shows "online" status
7. App can be closed — connection remains active in background

## Gotchas
- If already authenticated with your IdP, re-login is typically not required
- App must remain running in background to maintain Resource access (close the UI, not the app)
- No split-tunneling concerns — regular browsing is unaffected

## Related Docs
- iOS client setup
- Desktop client setup
- Identity Provider configuration
- Resource access configuration
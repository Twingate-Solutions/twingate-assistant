# Twingate Android Client

## Summary
Instructions for installing and configuring the Twingate Android client app. The app connects users to their Twingate network via identity provider authentication and only intercepts traffic for private Resources.

## Key Information
- Install via Google Play Store or `get.twingate.com`
- Minimum supported Android version: **Android 10**
- App runs in background without affecting regular internet browsing
- Only intercepts traffic destined for configured private Resources

## Prerequisites
- Android 10 or higher
- Google Play Store access
- Twingate Network name (provided by admin)
- Valid credentials for your organization's Identity Provider

## Step-by-Step

1. **Install** — Search "Twingate" on Google Play Store or visit `get.twingate.com`
2. **Set Network** — Open app, enter your Twingate Network name
3. **Authenticate** — Tap "Sign in to connect"; app opens browser for IdP authentication
4. **Complete Login** — Enter IdP credentials (skipped if already authenticated)
5. **Confirm Connected** — Browser closes, client shows "online" status
6. **Background Operation** — Close app; it remains connected in background

## Configuration Values
| Field | Value |
|-------|-------|
| Network Name | Your organization's Twingate network name (e.g., `yourcompany`) |

## Gotchas
- If already authenticated with your IdP, the browser step may complete automatically without prompting for credentials
- App must remain running in background to maintain Resource access (Android battery optimization may kill background processes — may need to whitelist Twingate)
- No traffic for non-Resource destinations is intercepted

## Related Docs
- iOS client setup
- Getting started / network configuration
- Identity Provider configuration
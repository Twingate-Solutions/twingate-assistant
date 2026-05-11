# ChromeOS Twingate Client

## Summary
Twingate on ChromeOS uses the Android app via the Google Play Store running in ChromeOS's Android compatibility layer. Installation and authentication follow standard mobile patterns, but device posture checks have significant limitations due to the Android compatibility layer.

## Key Information
- ChromeOS client is an Android app running in ChromeOS's Android compatibility layer
- App available via Google Play Store or `get.twingate.com`
- After connecting, app can be minimized — it only intercepts traffic for defined private Resources, not general internet traffic

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate Network name (your organization's subdomain)
- Valid identity provider credentials

## Step-by-Step Installation

1. Open Google Play Store, search "Twingate" or visit `get.twingate.com`
2. Install the Twingate app
3. Open the app and enter your Twingate Network name
4. Tap **Connect**
5. Complete IdP authentication in the browser window that opens (uses existing credentials if already authenticated)
6. Browser window closes automatically; client shows "online" status
7. App can be minimized — connection persists in background

## Device Posture Check Limitations

The following posture checks are **not supported** on ChromeOS:

| Check | Reason |
|-------|--------|
| Screen lock | ChromeOS does not expose this to Android apps |
| Biometric configuration | ChromeOS does not expose biometric status to Android layer |
| Hard drive encryption | Managed at OS level, inaccessible to Android app |

## Gotchas
- ChromeOS posture checks behave differently than standard Android — do not assume Android posture check policies apply to ChromeOS users
- If your Twingate policies require screen lock, biometric, or encryption posture checks, ChromeOS users will be unable to satisfy those requirements
- Plan access policies accordingly for ChromeOS users in your organization

## Related Docs
- Android client documentation
- Device posture checks configuration
- Identity provider integration
# ChromeOS - Twingate Client

## Summary
Twingate on ChromeOS uses the Android app running in ChromeOS's Android compatibility layer. Installation and authentication follow standard mobile app patterns, but device posture checks have significant limitations due to the Android compatibility layer.

## Key Information
- ChromeOS client is the Android app running via ChromeOS's Android compatibility layer
- App is available via Google Play Store or `get.twingate.com`
- Only intercepts traffic for private Twingate Resources; does not affect regular internet browsing
- Can remain running in background after setup

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate Network name (your organization's subdomain)
- Valid credentials for your organization's Identity Provider

## Step-by-Step Installation

1. Install **Twingate** from Google Play Store or visit `get.twingate.com`
2. Open the app and enter your Twingate Network name
3. Tap **Connect**
4. Authenticate via the browser window that opens (uses your existing IdP credentials)
5. Browser window closes automatically; client shows "online" status
6. Close the app — connection remains active in background

## Device Posture Checks — Unsupported on ChromeOS

| Check | Reason Unsupported |
|---|---|
| Screen lock | ChromeOS does not allow querying this check |
| Biometric configuration | ChromeOS does not expose biometric status to Android apps |
| Hard drive encryption | ChromeOS manages disk encryption at OS level, outside Android layer |

## Gotchas
- **Posture checks unavailable**: If your Twingate policies require screen lock, biometric, or encryption posture checks, ChromeOS users will not satisfy those requirements — plan policies accordingly
- The Android app on ChromeOS ≠ native Android; do not assume feature parity with Android device deployments
- If already authenticated with your IdP, re-authentication is typically skipped automatically

## Related Docs
- Android client documentation
- Device Posture Checks configuration
- Identity Provider setup
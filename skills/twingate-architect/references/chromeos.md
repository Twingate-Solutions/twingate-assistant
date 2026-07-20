# ChromeOS Twingate Client

## Summary
Twingate on ChromeOS uses the Android app via the Google Play Store, running in ChromeOS's Android compatibility layer. Installation and connection follow standard Android procedures, but device posture check support is limited due to the Android compatibility layer architecture.

## Key Information
- ChromeOS client is an Android app running in ChromeOS's Android compatibility layer
- Available via Google Play Store or `get.twingate.com`
- App only intercepts traffic for private Resources; regular internet browsing is unaffected
- Can be minimized/closed after connecting—connection persists

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate Network name
- Valid identity provider credentials

## Step-by-Step Installation

1. Install from Google Play Store (search "Twingate") or visit `get.twingate.com`
2. Open the Twingate app
3. Enter your Twingate Network name
4. Tap **Connect**
5. Authenticate via identity provider in the browser window that opens
6. Browser window closes automatically; client shows "online" status
7. Close the app—connection remains active

## Device Posture Checks — Unsupported on ChromeOS

| Check | Status | Reason |
|---|---|---|
| Screen lock | ❌ Not supported | ChromeOS does not expose this to Android layer |
| Biometric configuration | ❌ Not supported | ChromeOS does not expose biometric status to Android apps |
| Hard drive encryption | ❌ Not supported | ChromeOS manages encryption at OS level, separate from Android layer |

## Gotchas
- **Posture checks silently unsupported**: If your Twingate policies require posture checks (screen lock, biometrics, encryption), ChromeOS clients cannot satisfy them—plan access policies accordingly
- Standard Android posture checks may appear available in configuration but will not function on ChromeOS
- Re-authentication typically not required if already authenticated with your IdP

## Related Docs
- Android client documentation
- Device posture checks configuration
- Identity provider setup
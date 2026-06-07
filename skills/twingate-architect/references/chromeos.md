# ChromeOS Twingate Client

## Summary
Twingate on ChromeOS uses the Android app via the Google Play Store running in ChromeOS's Android compatibility layer. Installation and connection follow standard Android app procedures. Device posture checks have significant limitations due to the Android compatibility layer architecture.

## Key Information
- ChromeOS client is the Android app running in ChromeOS's Android compatibility layer
- Available via Google Play Store or `get.twingate.com`
- App only intercepts traffic for configured private Resources; does not affect regular browsing
- Authentication handled via identity provider in a browser window

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate Network name
- Valid identity provider credentials

## Step-by-Step Installation

1. Install from Google Play Store (search "Twingate") or navigate to `get.twingate.com`
2. Open Twingate app and enter your Twingate Network name
3. Tap **Connect**
4. Complete authentication via identity provider in the browser window that opens
5. Browser window closes automatically; client shows "online" status
6. App can be minimized — connection persists in background

## Device Posture Checks — Unsupported on ChromeOS

| Check | Status | Reason |
|---|---|---|
| Screen lock | ❌ Not supported | ChromeOS does not expose this to Android layer |
| Biometric configuration | ❌ Not supported | ChromeOS does not expose biometric status to Android apps |
| Hard drive encryption | ❌ Not supported | ChromeOS manages encryption at OS level, outside Android layer |

## Gotchas
- **Posture checks unavailable**: All three common device posture checks fail on ChromeOS regardless of device configuration — do not create policies requiring these checks for ChromeOS users
- ChromeOS users may appear non-compliant in posture-enforced policies even if the device is properly configured
- The Android app on ChromeOS behaves differently than on native Android — features available on Android may not work on ChromeOS

## Related Docs
- Android client documentation
- Device posture checks configuration
- Identity provider integration
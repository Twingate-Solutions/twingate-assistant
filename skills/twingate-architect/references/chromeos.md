---
source: https://www.twingate.com/docs/chromeos
type: docs
fetched: 2026-08-14
source_version: c2acab2ee29eb04cbf2595229fb94cab03a2149ef3f0d65deda157112a9e61ff
---

# ChromeOS Twingate Client

## Summary
Twingate on ChromeOS uses the Android app via the Google Play Store running in ChromeOS's Android compatibility layer. Installation and authentication follow standard mobile app patterns, but device posture checks have significant limitations due to the Android compatibility layer.

## Key Information
- ChromeOS client is the Android app running in ChromeOS's Android compatibility layer
- App remains connected in background without affecting regular internet traffic
- Only intercepts traffic for configured private Resources
- Device posture checks are substantially limited on ChromeOS

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate Network name
- Identity Provider credentials

## Step-by-Step Installation

1. Install from Google Play Store — search "Twingate" or visit `get.twingate.com`
2. Open the Twingate app
3. Enter your Twingate Network name
4. Tap **Connect**
5. Complete authentication in the browser window that opens (uses existing IdP credentials)
6. Browser window closes automatically; client shows "online"
7. Close app — connection persists in background

## Device Posture Checks — Unsupported on ChromeOS

| Check | Reason Unsupported |
|---|---|
| Screen lock | ChromeOS does not expose this to Android layer |
| Biometric configuration | ChromeOS does not expose biometric status to Android apps |
| Hard drive encryption | ChromeOS manages disk encryption at OS level, outside Android layer |

## Gotchas
- Posture checks that work on standard Android devices **will not work** on ChromeOS — same app, different behavior
- If posture checks are enforced on Resources, ChromeOS users may be blocked from access even if the device is configured correctly
- Authentication reuse: if already authenticated with IdP, re-login is typically not required

## Related Docs
- Android client documentation
- Device Posture Checks configuration
- Identity Provider setup
# ChromeOS – Twingate Client

## Summary
Twingate on ChromeOS uses the Android app via the Google Play Store running in ChromeOS's Android compatibility layer. Installation and connection follow standard mobile app flow. Device posture checks have significant limitations due to the Android compatibility layer architecture.

## Key Information
- App is an Android app running in ChromeOS's Android compatibility layer (not a native ChromeOS client)
- Install via Google Play Store or `get.twingate.com`
- Authentication delegates to identity provider via browser window
- App can remain connected in background without affecting regular internet traffic
- Only intercepts traffic for configured private Resources

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate Network name (your organization's subdomain)
- Valid identity provider credentials

## Step-by-Step Installation

1. Open Google Play Store, search "Twingate" or visit `get.twingate.com`
2. Install the Twingate app
3. Open app, enter your Twingate Network name
4. Tap **Connect**
5. Complete IdP authentication in the browser window that opens
6. Browser window closes automatically; client shows "online"
7. App can be minimized — connection persists in background

## Device Posture Checks — Unsupported on ChromeOS

| Check | Status | Reason |
|---|---|---|
| Screen lock | ❌ Not supported | ChromeOS does not expose this to Android layer |
| Biometric configuration | ❌ Not supported | Biometric status not exposed to Android apps |
| Hard drive encryption | ❌ Not supported | Managed at OS level, invisible to Android layer |

## Gotchas
- **Posture checks silently unavailable**: If your Twingate policies require screen lock, biometric, or encryption posture checks, ChromeOS users will not satisfy them — plan policies accordingly
- Posture checks that work on standard Android devices may **not** work on ChromeOS even though the same Android app is used
- No native ChromeOS client exists; all functionality runs through Android compatibility layer

## Related Docs
- Android client documentation
- Device posture checks configuration
- Identity provider setup
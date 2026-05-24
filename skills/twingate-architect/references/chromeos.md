# ChromeOS Twingate Client

## Summary
Twingate for ChromeOS is installed via the Google Play Store as an Android app running in ChromeOS's Android compatibility layer. Setup requires entering your network name and authenticating via your identity provider. Device posture checks have significant limitations due to the Android compatibility layer architecture.

## Key Information
- ChromeOS client is an Android app running in ChromeOS's Android compatibility layer
- Once connected, app can be minimized — it only intercepts traffic for private Resources, not general browsing
- Re-authentication is not required if already authenticated with your IdP

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate network name
- Valid identity provider credentials

## Step-by-Step Installation

1. Install from Google Play Store — search "Twingate" or visit `get.twingate.com`
2. Open the Twingate app
3. Enter your Twingate Network name
4. Tap **Connect**
5. Authenticate via your identity provider in the browser window that opens
6. Browser window closes automatically; client shows "online" status

## Device Posture Check Limitations

Three posture checks are **not supported** on ChromeOS:

| Check | Reason |
|-------|--------|
| Screen lock | ChromeOS does not expose this to Android layer |
| Biometric configuration | ChromeOS doesn't expose biometric auth status to Android apps |
| Hard drive encryption | Managed at OS level, not accessible via Android layer |

## Gotchas
- Posture checks that work on standard Android devices **will not work** on ChromeOS, even if configured — do not rely on these for ChromeOS users
- If your Twingate policies require unsupported posture checks, ChromeOS users may be blocked from Resources
- The Android compatibility layer is the root cause of all posture limitations — this is an architectural constraint, not a bug

## Related Docs
- Android client documentation
- Device posture checks configuration
- Identity provider setup
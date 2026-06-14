# ChromeOS Twingate Client

## Summary
Twingate on ChromeOS uses the Android app via the Google Play Store, running in ChromeOS's Android compatibility layer. Installation and connection follow standard Android app procedures, but device posture checks have significant limitations due to the compatibility layer architecture.

## Key Information
- ChromeOS client is the Android app running in the Android compatibility layer
- Available via Google Play Store or `get.twingate.com`
- App only intercepts traffic for private Resources; regular browsing is unaffected
- Can be minimized/closed after connecting — connection persists

## Prerequisites
- ChromeOS device with Google Play Store access (Android compatibility layer enabled)
- Twingate Network name
- Valid identity provider credentials

## Step-by-Step Installation & Connection

1. Install from Google Play Store (search "Twingate") or visit `get.twingate.com`
2. Open the Twingate app
3. Enter your Twingate Network name
4. Tap **Connect**
5. Complete IdP authentication in the browser window that opens
6. Browser window closes automatically; client shows "online" status
7. Close the app — connection remains active

## Configuration Values
- **Network name**: Your organization's Twingate network identifier (entered on first launch)

## Gotchas

**Device Posture Checks — Not Supported on ChromeOS:**

| Check | Reason |
|---|---|
| Screen lock | ChromeOS does not expose this to the Android layer |
| Biometric configuration | ChromeOS does not expose biometric status to Android apps |
| Hard drive encryption | Managed at OS level, inaccessible to Android layer |

- Posture checks that work on standard Android devices will **not** work on ChromeOS, even if configured
- If your Twingate policies enforce unsupported posture checks, ChromeOS users may be blocked from Resources

## Related Docs
- Android client documentation
- Device Posture Checks configuration
- Identity Provider setup
# Twingate ChromeOS Client

## Summary
Twingate on ChromeOS uses the Android app installed via Google Play Store, running in ChromeOS's Android compatibility layer. Device posture checks have significant limitations due to this architecture.

## Key Information
- App source: Google Play Store or `get.twingate.com`
- ChromeOS client is an Android app running in Android compatibility layer — not a native ChromeOS app
- App only intercepts traffic for defined private Resources; regular internet browsing is unaffected
- Can be minimized/closed while staying connected

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate Network name (your organization's subdomain)
- Valid credentials for your organization's Identity Provider (IdP)

## Step-by-Step: Installation & Connection
1. Install "Twingate" from Google Play Store or navigate to `get.twingate.com`
2. Open the Twingate app
3. Enter your Twingate Network name
4. Tap **Connect**
5. Complete IdP authentication in the browser window that opens (skipped if already authenticated)
6. Browser window closes automatically; client shows "online" status
7. App can be closed — connection remains active

## Device Posture Check Limitations

| Posture Check | ChromeOS Support | Reason |
|---|---|---|
| Screen lock | ❌ Not supported | ChromeOS does not expose this to Android layer |
| Biometric configuration | ❌ Not supported | ChromeOS does not expose biometric status to Android apps |
| Hard drive encryption | ❌ Not supported | Managed at OS level, inaccessible to Android layer |

## Gotchas
- **Posture checks silently unsupported**: Even if posture checks are configured for Android, they will not function on ChromeOS — plan access policies accordingly
- Device posture-gated Resources may behave unexpectedly for ChromeOS users if policies rely on these checks
- Standard Android posture checks that *do* work on physical Android devices will **not** work on ChromeOS

## Related Docs
- Android client documentation
- Device Posture Checks configuration
- Identity Provider setup
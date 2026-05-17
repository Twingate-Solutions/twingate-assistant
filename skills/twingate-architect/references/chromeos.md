# ChromeOS Twingate Client

## Summary
Twingate on ChromeOS uses the Android app via the Google Play Store running in ChromeOS's Android compatibility layer. Installation and authentication follow standard mobile patterns, but device posture checks have significant limitations due to the Android compatibility layer architecture.

## Key Information
- ChromeOS client is an Android app running in ChromeOS's Android compatibility layer
- App available via Google Play Store or `get.twingate.com`
- Once connected, app can be minimized — only intercepts traffic for private Resources, not general browsing
- Device posture checks are **not natively supported** on ChromeOS

## Prerequisites
- ChromeOS device with Google Play Store access
- Twingate Network name (your organization's subdomain)
- Valid identity provider credentials

## Step-by-Step Installation

1. Install "Twingate" from Google Play Store or visit `get.twingate.com`
2. Open the Twingate app
3. Enter your Twingate Network name
4. Tap **Connect**
5. Complete IdP authentication in the browser window that opens
6. Browser window closes automatically when authenticated — client shows "online"

## Unsupported Device Posture Checks

| Posture Check | Reason Unsupported |
|---|---|
| Screen lock | ChromeOS does not expose this to Android layer |
| Biometric configuration | ChromeOS does not expose biometric auth status to Android apps |
| Hard drive encryption | Managed at OS level, inaccessible to Android layer |

## Gotchas
- Even if posture checks work on standard Android, they **will not work on ChromeOS** — same app, different behavior due to compatibility layer
- If your Twingate policy requires any of the unsupported posture checks, ChromeOS users will be blocked from accessing affected Resources
- Re-authentication is typically not required if already authenticated with your IdP (SSO session reuse)

## Related Docs
- Android client documentation
- Device posture checks configuration
- Identity provider setup
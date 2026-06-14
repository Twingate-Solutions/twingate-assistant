# Twingate Android Client

## Page Title
Android

## Summary
Install and configure the Twingate Android client to connect to a Twingate network. The client runs in the background, only intercepting traffic for private Resources while leaving regular internet browsing unaffected.

## Key Information
- Minimum supported Android version: **Android 10**
- Download via Google Play Store (search "Twingate") or go to `get.twingate.com`
- Client runs silently in background after setup
- Only intercepts traffic for defined private Resources, not general internet traffic

## Prerequisites
- Android 10 or higher
- Twingate Network name (provided by admin)
- Valid credentials for your organization's Identity Provider (IdP)

## Step-by-Step

1. Install the Twingate app from Google Play Store or via `get.twingate.com`
2. Open the app and enter your **Twingate Network name**
3. Tap **"Sign in to connect"**
4. Complete authentication in the browser window that opens (uses your existing IdP credentials)
5. Browser window closes automatically; client shows **"online"** status
6. Close the app — it remains connected in the background

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Network name format | `<your-org>.twingate.com` (org-specific) |

## Gotchas
- If already authenticated with your IdP, re-login is typically not required
- App must remain running in background to maintain Resource access (close the UI, not the service)
- No manual VPN configuration required — handled automatically by the client

## Related Docs
- [iOS Client](https://www.twingate.com/docs/ios)
- [get.twingate.com](https://get.twingate.com)
- Identity Provider configuration (admin-side setup)
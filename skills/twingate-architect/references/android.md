# Android Client Setup

## Page Title
Twingate Android Client

## Summary
Instructions for installing and configuring the Twingate Android client app. The app runs in the background after initial setup, only intercepting traffic destined for private Twingate Resources.

## Key Information
- Install via Google Play Store or `get.twingate.com`
- Minimum supported Android version: **Android 10**
- App only intercepts traffic for configured private Resources, not general internet traffic
- Can run in background after initial connection

## Prerequisites
- Android 10 or higher
- Google Play Store access
- Twingate Network name (your organization's network identifier)
- Valid credentials for your organization's Identity Provider (IdP)

## Step-by-Step

1. Install the Twingate app from Google Play Store (search "Twingate") or via `get.twingate.com`
2. Open the app and enter your Twingate Network name
3. Tap **"Sign in to connect"**
4. Complete IdP authentication in the browser window that opens (uses existing SSO session if available)
5. Browser window closes automatically; client shows "online" status
6. App can be closed — connection persists in background

## Configuration Values
| Field | Value |
|-------|-------|
| Network Name | Your organization's Twingate network identifier |

## Gotchas
- If already authenticated with your IdP, re-login is typically not required
- App uses Android VPN service to intercept traffic — users may see a VPN indicator in the status bar
- No manual VPN configuration required; all routing is handled automatically

## Related Docs
- [iOS Client](https://www.twingate.com/docs/ios)
- [get.twingate.com](https://get.twingate.com) — universal client download page
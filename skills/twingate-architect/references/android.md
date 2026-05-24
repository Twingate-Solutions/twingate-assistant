# Twingate Android Client

## Summary
Install and configure the Twingate Android client to connect to a Twingate network. The client runs in the background and only intercepts traffic destined for private Resources, leaving regular internet traffic unaffected.

## Key Information
- Download from Google Play Store or via `get.twingate.com`
- Minimum supported Android version: **Android 10**
- Authentication delegates to your configured Identity Provider (IdP) via browser window
- Client runs persistently in background without affecting general internet traffic
- Only intercepts traffic for explicitly defined private Resources

## Prerequisites
- Android 10 or higher
- Google Play Store access
- Twingate Network name (your organization's network identifier)
- Valid credentials for your organization's Identity Provider

## Step-by-Step Setup

1. **Install** the app from Google Play Store (search "Twingate") or navigate to `get.twingate.com`
2. **Open** the Twingate app
3. **Enter** your Twingate Network name
4. **Tap** "Sign in to connect"
5. **Authenticate** via the browser window that opens (uses existing IdP credentials; may skip if already authenticated)
6. **Confirm** the client shows "online" status
7. **Close** the app — it remains connected in the background

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Network name | Your organization's Twingate network identifier |
| Auth method | Identity Provider (configured by admin) |

## Gotchas
- If already authenticated with your IdP, the browser window may close automatically without requiring credential entry
- The VPN permission will be requested on Android — this is required for traffic interception
- No manual configuration of Resources needed on the client; Resources are managed server-side by admins

## Related Docs
- iOS client setup
- Twingate network administration
- Identity Provider configuration
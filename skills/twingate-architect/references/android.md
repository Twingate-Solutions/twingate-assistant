# Twingate Android Client

## Summary
Twingate Android client connects users to their Twingate network via the Google Play Store app. Authentication is handled through the configured Identity Provider (IdP) via browser redirect. Once connected, only private Resource traffic is intercepted.

## Key Information
- Minimum supported Android version: **Android 10**
- App available via Google Play Store or **get.twingate.com**
- Uses VPN-based tunnel; does not affect regular internet traffic
- Authentication handled by existing IdP (SSO) credentials
- App can run in background after initial connection

## Prerequisites
- Android 10 or later
- Twingate network name (provided by admin)
- Valid IdP credentials for your organization
- Google Play Store access

## Step-by-Step

1. **Install** – Search "Twingate" on Google Play Store or visit `get.twingate.com`
2. **Set Network** – Open app, enter your Twingate Network name
3. **Authenticate** – Tap "Sign in to connect"; browser window opens for IdP login
4. **Connect** – Browser closes automatically; client shows "online" status
5. **Background** – Close the app; connection persists, only private Resource traffic is routed through Twingate

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Network name | Your organization's Twingate network identifier (e.g., `yourcompany`) |

## Gotchas
- If already authenticated with IdP, re-login is typically not required (session reuse)
- Regular internet browsing is **not** routed through Twingate — only configured private Resources
- No manual split-tunnel configuration needed; handled automatically

## Related Docs
- iOS client setup
- Twingate network naming conventions
- Identity Provider configuration
- Resource access setup
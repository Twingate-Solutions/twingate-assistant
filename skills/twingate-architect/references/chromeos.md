# ChromeOS Twingate Client

## Page Title
ChromeOS Installation and Setup

## Summary
Instructions for installing and configuring the Twingate client on ChromeOS via Google Play Store. The client runs as an Android app and authenticates through an identity provider to access private Resources.

## Key Information
- Installed via Google Play Store (Android app compatibility)
- Available at `get.twingate.com` as an alternative to direct Play Store search
- Client only intercepts traffic for private Resources; regular internet browsing is unaffected
- App can remain running in background after initial setup

## Prerequisites
- ChromeOS device with Google Play Store access enabled
- Twingate Network name (provided by admin)
- Valid credentials for your organization's identity provider

## Step-by-Step

1. **Install** - Search "Twingate" in Google Play Store or navigate to `get.twingate.com`
2. **Set Network** - Open app, enter Twingate Network name
3. **Authenticate** - Tap "Connect"; app opens browser window for IdP authentication
4. **Login** - Enter IdP credentials (skipped if already authenticated)
5. **Verify** - Browser window closes; client displays "online" status
6. **Minimize** - Close app UI; leave client connected in background

## Configuration Values
- **Network name**: Subdomain of your Twingate tenant (e.g., `yourcompany` for `yourcompany.twingate.com`)

## Gotchas
- Requires Google Play Store to be enabled on the ChromeOS device (may need admin enablement on managed devices)
- Authentication opens an external browser window — ensure browser isn't blocked or restricted
- If already authenticated with IdP (SSO session active), re-authentication prompt may be skipped automatically

## Related Docs
- [get.twingate.com](https://get.twingate.com) — client download portal
- Identity Provider configuration (org-specific)
- Twingate Network setup / admin docs
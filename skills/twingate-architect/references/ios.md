# Twingate iOS Client

## Summary
Instructions for installing and configuring the Twingate iOS client app. The app connects users to private resources via their organization's Twingate network using identity provider authentication.

## Key Information
- App available on the Apple App Store
- Direct install link: `get.twingate.com`
- App runs in background without affecting regular internet traffic
- Only intercepts traffic destined for configured private Resources

## Prerequisites
- iOS device with App Store access
- Organization's Twingate network name (format: `yourcompany.twingate.com`)
- Valid credentials for your organization's identity provider
- Network name available in Twingate welcome email

## Step-by-Step Setup

1. **Install** – Search "Twingate" in App Store or visit `get.twingate.com`
2. **Set Network** – On first launch, enter your network address (e.g., `autoco.twingate.com`), tap **Join Network**
3. **Authenticate** – Tap **Sign in to Connect**; app opens browser for IdP login
4. **Complete Auth** – Enter IdP credentials in browser window (skipped if already authenticated)
5. **Confirm Connected** – Browser closes; client shows "online" status
6. **Background Operation** – App can be closed; remains connected in background

## Configuration Values
| Field | Format | Source |
|-------|--------|--------|
| Network Name | `<orgname>.twingate.com` | Welcome email |

## Gotchas
- Network name must be entered on first launch only; subsequent launches reuse saved network
- If already authenticated with IdP (SSO session active), login step is skipped automatically
- App uses VPN profile on iOS to intercept traffic — iOS may prompt for VPN permission on first connect
- Does **not** route general internet traffic through Twingate (split tunnel by default)

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Admin: Configuring Resources and Access Policies
- Identity Provider integration guides
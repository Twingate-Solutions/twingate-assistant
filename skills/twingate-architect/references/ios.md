# Twingate iOS Client

## Page Title
iOS Client Setup

## Summary
Instructions for installing and configuring the Twingate iOS client. The app connects users to private resources via their organization's identity provider without affecting regular internet traffic.

## Key Information
- App available on the App Store (also accessible via get.twingate.com)
- Network name format: `<orgname>.twingate.com`
- Network name is provided in the welcome email
- App runs in background after initial setup; does not intercept general internet traffic
- Only intercepts traffic destined for configured private Resources

## Prerequisites
- iOS device with App Store access
- Organization network name (from welcome email)
- Valid credentials for the organization's identity provider (IdP)

## Step-by-Step

1. **Install** — Search "Twingate" in the App Store or visit `get.twingate.com`
2. **Set Network** — Open app, enter network name (e.g., `autoco.twingate.com`), tap **Join Network**
3. **Authenticate** — Tap **Sign in to Connect**; browser window opens for IdP login
4. **Connect** — Browser closes automatically; app shows "online" status
5. **Background** — Close the app; it remains connected and only routes private Resource traffic

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Network Name | `<org>.twingate.com` | `autoco.twingate.com` |

## Gotchas
- If already authenticated with the IdP, login prompt may be skipped automatically
- App must remain running (backgrounded) to maintain Resource access
- Regular internet browsing is unaffected — only private Resource traffic is intercepted

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Identity provider configuration
- Resource access configuration
# iOS – Twingate Client Setup

## Page Title
iOS Client Installation and Configuration

## Summary
Instructions for installing and configuring the Twingate client on iOS devices. The client runs in the background after setup, only intercepting traffic destined for private Resources without affecting general internet browsing.

## Key Information
- App available via App Store (search "Twingate") or direct link: `get.twingate.com`
- Network name format: `<your-org>.twingate.com`
- Network name is provided in the welcome email
- Authentication delegated to configured Identity Provider (IdP)
- Client can remain running in background; does not proxy general internet traffic
- Only intercepts traffic for explicitly defined private Resources

## Prerequisites
- iOS device with App Store access
- Twingate network name (from welcome email)
- Valid credentials for the organization's Identity Provider

## Step-by-Step

1. **Install** – Download "Twingate" from the App Store or visit `get.twingate.com`
2. **Set Network** – On first launch, enter network name (e.g., `autoco.twingate.com`) and tap **Join Network**
3. **Authenticate** – Tap **Sign in to Connect**; a browser window opens for IdP authentication
4. **Complete Auth** – Log in with IdP credentials (skipped if already authenticated); browser closes automatically
5. **Confirm Online** – Client displays online status; app can be minimized

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Network Name | `<org>.twingate.com` | `autoco.twingate.com` |

## Gotchas
- Network name must be entered exactly as provided; incorrect names will fail to connect
- If already authenticated with the IdP, the browser step may complete without requiring credentials
- App must remain running (background) to maintain Resource access; fully closing it disconnects the VPN tunnel

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Resource access configuration (Admin Console)
- Identity Provider configuration
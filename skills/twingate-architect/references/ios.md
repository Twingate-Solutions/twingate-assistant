# Twingate iOS Client

## Summary
Instructions for installing and configuring the Twingate iOS client app. The client authenticates via an identity provider and routes only private resource traffic through Twingate, leaving regular internet traffic unaffected.

## Key Information
- Install via App Store (search "Twingate") or navigate to `get.twingate.com`
- Network name format: `<orgname>.twingate.com`
- Network name is provided in the welcome email
- Authentication handled by configured identity provider via browser redirect
- App operates as a split-tunnel VPN — only intercepts traffic to defined private Resources
- App can remain running in background after setup

## Prerequisites
- iOS device with App Store access
- Twingate network name (from welcome email)
- Valid credentials for the organization's identity provider
- Active Twingate account with at least one Resource assigned

## Step-by-Step

1. Install the Twingate app from the App Store or via `get.twingate.com`
2. Open the app; enter your network name (e.g., `autoco.twingate.com`) when prompted
3. Tap **Join Network**
4. Tap **Sign in to Connect**
5. Complete authentication in the browser window using your IdP credentials
6. Browser window closes automatically; client shows **Online** status
7. Close the app — it remains connected in the background

## Configuration Values
| Field | Example | Source |
|-------|---------|--------|
| Network name | `autoco.twingate.com` | Welcome email |

## Gotchas
- If already authenticated with the IdP, the browser step may complete automatically without requiring credential entry
- The app must remain running (background) to maintain connectivity to Resources
- Only traffic to configured Resources is intercepted — normal internet traffic is unaffected (split tunnel)

## Related Docs
- [Android Client Setup](https://www.twingate.com/docs/android)
- [macOS Client Setup](https://www.twingate.com/docs/macos)
- [Windows Client Setup](https://www.twingate.com/docs/windows)
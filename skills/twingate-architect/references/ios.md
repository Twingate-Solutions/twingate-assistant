---
source: https://www.twingate.com/docs/ios
type: docs
fetched: 2026-08-14
source_version: 510355d44a6588b7d07a728d040ee87ed799bba3442796cbadb5eb014686b3c4
---

# Twingate iOS Client

## Page Title
iOS Client Setup

## Summary
Install and configure the Twingate iOS client from the App Store. The client authenticates via your organization's identity provider and runs in the background, only intercepting traffic destined for private Resources.

## Key Information
- App available on Apple App Store (also accessible via `get.twingate.com`)
- Network name format: `<orgname>.twingate.com`
- Authentication handled by your existing identity provider (SSO)
- Client runs passively in background; does not affect regular internet traffic
- Only intercepts traffic for configured private Resources

## Prerequisites
- iOS device with App Store access
- Organization's Twingate network name (found in welcome email)
- Valid identity provider credentials for your organization

## Step-by-Step

1. **Install** — Search "Twingate" in the App Store or visit `get.twingate.com`
2. **Set Network** — Open app, enter network name (e.g., `autoco.twingate.com`), tap **Join Network**
3. **Authenticate** — Tap **Sign in to Connect**; complete IdP login in the browser window that opens
4. **Confirm Online** — Browser window closes automatically; client displays "online" status
5. **Minimize** — App can be closed; connection remains active in background

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Network Name | `<org>.twingate.com` | `autoco.twingate.com` |

## Gotchas
- If already authenticated with your IdP, the browser step may complete without requiring credential entry
- App must remain connected (not force-quit) to maintain access to private Resources
- No manual VPN configuration required; handled entirely through the app

## Related Docs
- [Android Client](https://www.twingate.com/docs/android)
- [macOS Client](https://www.twingate.com/docs/macos)
- [Windows Client](https://www.twingate.com/docs/windows)
# Twingate iOS Client

## Summary
Install and configure the Twingate iOS client to connect to private resources. The app runs in the background after setup and only intercepts traffic destined for configured private resources.

## Key Information
- App available on the App Store or via `get.twingate.com`
- Network name format: `<company>.twingate.com`
- Authentication handled by your organization's identity provider (IdP)
- App can run in background without affecting regular internet traffic
- Only intercepts traffic for configured private Resources, not all traffic

## Prerequisites
- iOS device with App Store access
- Twingate network name (found in welcome email)
- Valid credentials for your organization's identity provider

## Step-by-Step Setup

1. **Install** — Search "Twingate" in App Store or visit `get.twingate.com`
2. **Set Network** — Enter network name (e.g., `autoco.twingate.com`) when prompted
3. **Join Network** — Tap "Join Network"
4. **Authenticate** — Tap "Sign in to Connect"; complete IdP login in browser window that opens
5. **Connected** — Browser closes automatically; client shows "online" status
6. **Background** — Close app; it remains connected

## Configuration Values
| Field | Format | Source |
|-------|--------|--------|
| Network name | `<orgname>.twingate.com` | Welcome email |

## Gotchas
- If already authenticated with IdP, re-login is typically not required
- App does **not** route all traffic — only private Resource traffic is intercepted
- Network name must be entered exactly as provided (subdomain only or full URL accepted)

## Related Docs
- Android client setup
- Desktop client setup (macOS, Windows, Linux)
- Twingate Admin Console (for Resource configuration)
# Twingate Android Client

## Summary
Guide for installing and configuring the Twingate Android client app. The app runs in the background, intercepting only private Resource traffic without affecting regular internet browsing.

## Key Information
- Minimum supported Android version: **Android 10**
- Install via Google Play Store or **get.twingate.com**
- App only intercepts traffic for private Resources, not general internet traffic
- Can remain running in background after setup

## Prerequisites
- Android 10 or newer
- Google Play Store access
- Twingate Network name (provided by admin)
- Valid credentials for your organization's Identity Provider

## Step-by-Step

1. **Install** — Search "Twingate" on Google Play Store or visit `get.twingate.com`
2. **Set Network** — Open app, enter your Twingate Network name
3. **Authenticate** — Tap "Sign in to connect"; app opens browser for IdP authentication
4. **Connect** — Browser closes automatically; client shows "online" status
5. **Background** — Close app; it remains connected and active

## Configuration Values
- **Network name**: Provided by your Twingate admin (entered on first launch)

## Gotchas
- If already authenticated with your IdP, re-login is typically not required
- App must stay running in background to maintain Resource access — ensure Android battery optimization doesn't kill the process
- No mention of split tunneling configuration in this doc; traffic routing is automatic

## Related Docs
- iOS client setup
- Desktop client setup
- Identity Provider configuration
- Resource access management
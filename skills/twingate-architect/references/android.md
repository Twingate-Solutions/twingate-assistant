---
source: https://www.twingate.com/docs/android
type: docs
fetched: 2026-08-14
source_version: 9948a5df2b9bc67e6563e13a48033fd0aaf12901dac4dbe17579cb4860f318eb
---

# Twingate Android Client

## Page Title
Android Client Installation and Setup

## Summary
Installs the Twingate Android client from Google Play Store to connect mobile devices to a Twingate network. Authentication uses the organization's existing identity provider via browser-based OAuth flow.

## Key Information
- Minimum supported Android version: **Android 10**
- Download via Google Play Store or `get.twingate.com`
- Client only intercepts traffic for private Resources; regular internet browsing is unaffected
- App can run in background once connected

## Prerequisites
- Android 10 or newer
- Twingate Network name (organization's subdomain)
- Valid credentials for the organization's identity provider

## Step-by-Step

1. Install the Twingate app from Google Play Store (search "Twingate") or visit `get.twingate.com`
2. Open the app and enter your Twingate Network name
3. Tap **"Sign in to connect"**
4. Complete authentication in the browser window that opens (uses existing IdP credentials)
5. Browser window closes automatically; client shows "online" status
6. App can be minimized — connection persists in background

## Configuration Values
| Field | Value |
|-------|-------|
| Network name | Your organization's Twingate subdomain |
| Download URL | `get.twingate.com` |

## Gotchas
- If already authenticated with the IdP, re-login is typically not required
- App must remain running (background) to maintain resource access
- No configuration for split tunneling — it is automatic; only Twingate Resources route through the VPN

## Related Docs
- iOS client setup
- Identity provider configuration
- Resource access configuration
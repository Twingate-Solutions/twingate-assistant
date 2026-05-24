# Using Twingate Client

## Summary
Covers how to connect the Twingate Client to a network, access resources, manage multiple accounts, and handle resource authentication/authorization. Includes tips on split tunneling and reconnection behavior.

## Key Information
- First-time setup requires entering your network URL (e.g., `autoco` from `autoco.twingate.com`) and logging in via SSO/social login
- Resources are accessed normally (browser, SSH, RDP, etc.) once connected — no workflow changes required
- Split tunneling is automatic: non-Resource traffic bypasses Twingate entirely; no performance impact from leaving Client running
- Client auto-reconnects on network changes; may open browser for re-authentication

## Multiple Accounts
Supported on:
- macOS ≥ 2025.227, Windows ≥ 2025.232, iOS ≥ 2025.227

- Add accounts via **Add Another Account**; remove via **Log Out** under More submenu
- Only **one account active at a time** — accounts have no visibility into each other
- Must switch accounts to access Resources from a different account

## Resource Authentication
- Resources with stricter Security Policy than user's baseline show a **lock icon**
- Two ways to authenticate:
  1. Visit the Resource — Twingate triggers a notification; click to complete auth in browser
  2. Manually: find Resource in Client → open menu → select **Authenticate**
- Authorization expires per Security Policy; re-authentication required after expiry

## Proactive Reauthentication
- **Renew Session**: Resource menu → **Renew Session** (manual proactive renewal)
- **Proactive notifications** (early access, requires enablement by Twingate team):
  - Supported on macOS/Windows/Linux/iOS/Android ≥ 2025.72
  - Notifies before authorization expires; click notification to renew without finding Resource manually

## Prerequisites
- Twingate Client installed
- Network URL from your Twingate admin
- Valid SSO/social login credentials

## Gotchas
- Security Policy applied to a Resource is **not visible** in the Client
- Quitting the Client may require full reauthentication on restart — leave it running instead
- Proactive reauthentication notifications require contacting Twingate to enable
- Multiple account support requires specific minimum Client versions; older versions do not support this

## Related Docs
- Twingate Client Installation
- Security Policy configuration
- MFA setup
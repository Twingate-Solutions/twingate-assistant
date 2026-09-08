---
source: https://help.twingate.com/articles/4209242719-macos-client-enabling-notifications-for-additional-authentication-prompts
type: help
fetched: 2026-09-06
source_version: dfd240085fd108a1588a61368fb418ad742f8a667610bc869902627769e58bba
---

# macOS Client: Enabling Notifications for Additional Authentication Prompts

## Summary
Twingate macOS Client uses system notifications to prompt users for additional authentication (2FA) as required by Security Policies. Notifications must be explicitly enabled in macOS System Preferences to receive these prompts.

## Key Information
- Notifications are required for Security Policy 2FA/additional authentication prompts
- Focus modes (e.g., Do Not Disturb) will block authentication prompts even if notifications are enabled
- Alert style must be set to **Alerts** (not Banners) to ensure prompts are actionable

## Prerequisites
- Twingate macOS Client installed and signed in
- macOS user account with access to System Preferences

## Step-by-Step

1. Click the **Apple icon** (top left of screen)
2. Select **System Preferences** from the dropdown
3. Click **Notifications & Focus**
4. Scroll down and click **Twingate**
5. Enable the **Allow Notifications** toggle
6. Set alert style to **Alerts**
7. Configure any additional optional alert settings as desired

## Configuration Values
| Setting | Required Value |
|---|---|
| Allow Notifications | Enabled (toggle on) |
| Alert Style | Alerts |

## Gotchas
- **Do Not Disturb / Focus modes** will suppress Twingate notifications and block 2FA prompts — users must disable Focus or add Twingate as an exception
- Setting alert style to "Banners" instead of "Alerts" may result in prompts dismissing before user interaction
- Steps reference **System Preferences** (macOS Ventura and earlier); macOS Ventura+ uses **System Settings** — navigation path may differ slightly

## Related Docs
- Twingate Security Policies (2FA configuration)
- macOS Client documentation
---
source: https://help.twingate.com/articles/4209242719-macos-client-enabling-notifications-for-additional-authentication-prompts
type: help
fetched: 2026-10-04
source_version: d795ef6253a4c0ca24fa026de74396a3abf404dfd80c50e8b84add7449ac69bf
trust: official
---

# macOS Client: Enabling Notifications for Additional Authentication Prompts

## Summary
The Twingate macOS Client requires system notifications to prompt users for additional authentication (2FA) as defined by Security Policies. Without notifications enabled, users will not receive MFA prompts and may be unable to access protected resources.

## Key Information
- Notifications are required for Security Policy-triggered 2FA prompts
- Alert style must be set to **Alerts** (not Banners) to ensure prompts are actionable
- Focus modes (e.g., Do Not Disturb) will suppress Twingate notifications even if enabled

## Prerequisites
- Twingate macOS Client installed and signed in
- macOS user account with permission to modify notification settings

## Step-by-Step

1. Click the **Apple icon** (top-left of screen)
2. Select **System Preferences** from the dropdown
3. Click **Notifications & Focus**
4. Scroll down and click **Twingate** in the app list
5. Enable the **Allow Notifications** toggle
6. Set alert style to **Alerts**
7. Configure any additional optional alert settings as desired

## Configuration Values
| Setting | Required Value |
|---|---|
| Allow Notifications | Enabled (toggle on) |
| Alert Style | Alerts |

## Gotchas
- **Do Not Disturb / Focus modes** will block Twingate notifications regardless of notification settings — users must account for active Focus profiles
- Using **Banners** instead of **Alerts** may cause prompts to disappear before the user can respond; **Alerts** persist until dismissed
- Steps reference **System Preferences** (macOS Ventura and earlier); on macOS Ventura+ the app is renamed **System Settings** and navigation may differ slightly

## Related Docs
- Twingate Security Policies (2FA configuration)
- Twingate macOS Client setup
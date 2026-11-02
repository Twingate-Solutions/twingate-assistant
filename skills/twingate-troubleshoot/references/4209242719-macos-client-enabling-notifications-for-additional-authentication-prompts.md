---
source: https://help.twingate.com/articles/4209242719-macos-client-enabling-notifications-for-additional-authentication-prompts
type: help
fetched: 2026-11-01
source_version: 5fb13efb4845da87ce33ba9c4d57167c1c5d6e9271b82d4ed9db996feccdb666
trust: official
---

# macOS Client: Enabling Notifications for Additional Authentication Prompts

## Summary
The Twingate macOS Client uses system notifications to prompt users for additional authentication (2FA) required by Security Policies. Notifications must be explicitly enabled in macOS System Preferences, and the alert style must be set to **Alerts** (not Banners) to ensure prompts appear correctly.

## Key Information
- Affects: 2FA/MFA prompts triggered by Twingate Security Policies
- Alert style must be **Alerts** (not Banners) — Banners auto-dismiss and may cause missed prompts
- macOS Focus modes (e.g., Do Not Disturb) can suppress prompts even if notifications are enabled

## Prerequisites
- Twingate macOS Client installed and signed in
- macOS user must be logged in as the desktop user (not via remote/admin session)

## Step-by-Step

1. Click the **Apple icon** (top-left of screen)
2. Select **System Preferences** from the dropdown
3. Click **Notifications & Focus**
4. Scroll down and select **Twingate** in the app list
5. Enable the **Allow Notifications** toggle
6. Set alert style to **Alerts**
7. Configure any optional notification settings as desired

## Gotchas
- **Do Not Disturb / Focus modes** will suppress Twingate notifications — users must ensure Focus settings allow Twingate notifications or disable Focus when authentication prompts are expected
- Using **Banners** instead of **Alerts** as the alert style may cause prompts to disappear before the user can respond, blocking resource access
- This must be configured per macOS user account; system-wide MDM configuration may be required in managed environments

## Related Docs
- Twingate Security Policies (2FA configuration)
- Twingate macOS Client documentation
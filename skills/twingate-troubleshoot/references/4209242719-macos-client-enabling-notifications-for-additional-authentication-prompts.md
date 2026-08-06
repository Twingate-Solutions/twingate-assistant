---
source: https://help.twingate.com/articles/4209242719-macos-client-enabling-notifications-for-additional-authentication-prompts
type: help
fetched: 2026-08-06
source_version: f82a221592744beaa6b4c927827ec69a46fdc8bc4456decff94b5e5332869f0e
---

# macOS Client: Enabling Notifications for Additional Authentication Prompts

## Summary
macOS notification permissions must be explicitly enabled for the Twingate client to deliver additional authentication (2FA) prompts defined by Security Policies. Without proper notification settings, users will not receive MFA challenges when accessing protected resources.

## Key Information
- Notifications are required for Security Policy-triggered additional authentication (2FA/MFA)
- Alert style must be set to **Alerts** (not Banners) to ensure prompts are actionable
- Focus modes (e.g., Do Not Disturb) will block authentication prompts even if notifications are enabled

## Prerequisites
- Twingate macOS client installed and user signed in
- macOS desktop user account access (not admin required)

## Step-by-Step

1. Click the **Apple icon** (top-left of screen)
2. Select **System Preferences** from the dropdown
3. Click **Notifications & Focus**
4. Scroll down and click **Twingate** in the app list
5. Enable the **Allow Notifications** toggle
6. Set alert style to **Alerts**
7. Configure any optional alert settings as desired

## Configuration Values
| Setting | Required Value |
|---|---|
| Allow Notifications | Enabled (toggle on) |
| Alert Style | Alerts |
| Focus/Do Not Disturb | Must be disabled or Twingate must be exempted |

## Gotchas
- **Do Not Disturb / Focus modes** silently block authentication prompts — users may think they're connected but can't access resources requiring step-up auth
- Using **Banners** instead of **Alerts** may cause prompts to auto-dismiss before the user can respond
- This must be configured per macOS user account; does not apply system-wide automatically

## Related Docs
- Twingate Security Policies (2FA configuration)
- macOS Client general setup
- MDM/managed device notification policy configuration (for enterprise deployments)
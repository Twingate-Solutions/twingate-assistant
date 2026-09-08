---
source: https://help.twingate.com/articles/3391673762-reset-totp-two-factor-authentication-2fa
type: help
fetched: 2026-09-06
source_version: f8a64040bcc809cd4d9da769f79d0bafb0e87353da0b47c3d249b0b208b35d4b
---

# Reset TOTP/Two-Factor Authentication (2FA)

## Summary
Twingate Admins can reset a user's TOTP/2FA configuration when the user loses access to their authenticator app. After reset, the user must reconfigure 2FA before accessing protected resources.

## Key Information
- Reset is per-user, initiated by an Admin in the Admin Console
- After reset, user is prompted to reconfigure 2FA on next access to a 2FA-protected resource
- Reset does not disable 2FA enforcement — the user must set it up again

## Prerequisites
- **Role required:** Twingate Administrator
- Access to the Twingate Admin Console (`https://<network>.twingate.com`)

## Step-by-Step

1. Open the Twingate Admin Console at `https://<network>.twingate.com`
2. Navigate to **Team > Users**
3. Find the target user and click their username
4. On the user account page, hover over the 2FA option on the left-hand side to reveal the **Reset** icon
5. Click the Reset icon — a confirmation prompt will appear
6. Click **Reset** to confirm
7. Notify the user they must reconfigure 2FA

## Gotchas
- The Reset icon only appears on **hover** — it is not visible by default
- User must be explicitly informed to reconfigure; Twingate does not automatically notify them
- User will only be prompted to reconfigure 2FA when they next attempt to access a **2FA-protected resource** (not on general login)

## Related Docs
- Two Factor Authentication (configuration guide) — linked in Twingate help docs
- Twingate Admin Console: `https://<network>.twingate.com`
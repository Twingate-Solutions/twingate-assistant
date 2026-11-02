---
source: https://help.twingate.com/articles/3391673762-reset-totp-two-factor-authentication-2fa
type: help
fetched: 2026-11-01
source_version: 496f7f0ad9565ffceeba5d496c619703ce4b14bbee5f049a8ee5cebbd7f55140
trust: official
---

# Reset TOTP/Two-Factor Authentication (2FA)

## Page Title
Reset TOTP/Two-Factor Authentication (2FA)

## Summary
Twingate Admins can reset a user's TOTP/2FA configuration when the user loses access to their authenticator app. After reset, the user must reconfigure 2FA the next time they access a 2FA-protected resource.

## Key Information
- Reset is per-user, initiated from the Admin Console
- Reset does not disable 2FA — the user will be prompted to reconfigure it on next access to a protected resource
- Only applies to TOTP-based 2FA used with Twingate resources

## Prerequisites
- **Role required:** Twingate Administrator
- Access to the Twingate Admin Console (`https://<network-name>.twingate.com`)

## Step-by-Step

1. Open the Admin Console at `https://<network-name>.twingate.com`
2. Navigate to **Team → Users**
3. Locate the target user and click their username
4. On the user detail page, hover over the 2FA field on the left side — a **Reset** icon appears on hover
5. Click the Reset icon; confirm the action in the prompt by clicking **Reset**
6. Notify the user they must reconfigure 2FA — they will be prompted automatically on next access to a 2FA-protected resource

## Configuration Values
- None (UI-only operation; no CLI flags or API parameters documented)

## Gotchas
- The **Reset icon only appears on hover** — easy to miss in the UI
- User is not automatically notified; admin must manually inform them
- After reset, the user cannot access 2FA-protected resources until they complete reconfiguration

## Related Docs
- Twingate Two-Factor Authentication setup documentation (linked in Admin Console help under "Two Factor Authentication")
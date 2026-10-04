---
source: https://help.twingate.com/articles/3391673762-reset-totp-two-factor-authentication-2fa
type: help
fetched: 2026-10-04
source_version: 25920de04ff728a6acaae9ef6a69787850fe5397d01c339af44af8b0ea18b9be
trust: official
---

# Reset TOTP/Two-Factor Authentication (2FA)

## Page Title
Reset TOTP/Two-Factor Authentication (2FA)

## Summary
Twingate Admins can reset a user's TOTP/2FA configuration when the user has lost access to their authenticator app. After reset, the user must reconfigure 2FA before accessing protected resources again.

## Key Information
- Reset is performed per-user from the Admin Console
- After reset, the user's existing 2FA config is cleared
- User is prompted to reconfigure 2FA on next attempt to access a 2FA-protected resource
- No action required from the user until they try to access a protected resource

## Prerequisites
- **Role:** Twingate Administrator
- Access to the Twingate Admin Console (`https://<network-name>.twingate.com`)

## Step-by-Step

1. Open the Twingate Admin Console at `https://<network-name>.twingate.com`
2. Navigate to **Team → Users**
3. Locate the affected user and click their username
4. On the user detail page, hover over the 2FA field on the left side — a **Reset** icon will appear on hover
5. Click the Reset icon
6. Confirm the reset in the prompt by clicking **Reset**
7. Notify the user they must reconfigure 2FA; they will be prompted automatically on next access to a 2FA-protected resource

## Configuration Values
None — this is a UI-only operation with no API parameters, CLI flags, or environment variables documented on this page.

## Gotchas
- The Reset icon is **only visible on hover** — easy to miss if you don't know to hover over the 2FA field
- Admin must manually inform the user after reset; there is no mention of an automatic notification email
- User cannot reconfigure 2FA proactively; the setup prompt only appears when accessing a 2FA-protected resource

## Related Docs
- Two Factor Authentication (Twingate documentation — search "Two Factor Authentication" in Twingate Help Center)
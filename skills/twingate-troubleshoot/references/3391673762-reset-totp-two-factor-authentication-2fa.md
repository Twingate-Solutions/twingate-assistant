---
source: https://help.twingate.com/articles/3391673762-reset-totp-two-factor-authentication-2fa
type: help
fetched: 2026-11-08
source_version: eb2b7155977b0283ec6651193eaa93c93d14983121ff8aa589dcbfdbe80a3bde
trust: official
---

# Reset TOTP/Two-Factor Authentication (2FA)

## Page Title
Reset TOTP/Two-Factor Authentication (2FA)

## Summary
Twingate Admins can reset a user's TOTP-based 2FA when the user loses access to their authenticator app. After reset, the user must reconfigure 2FA the next time they attempt to access a 2FA-protected resource.

## Key Information
- Reset is per-user and initiated from the Admin Console
- After reset, the user is not locked out permanently — they re-enroll on next 2FA-protected resource access
- Only applies to TOTP-based 2FA configured within Twingate

## Prerequisites
- **Role:** Twingate Administrator
- Access to the Twingate Admin Console (`https://<network>.twingate.com`)

## Step-by-Step

1. Open the Admin Console at `https://<network>.twingate.com`
2. Navigate to **Team → Users**
3. Locate and click the target user's username
4. On the user detail page, hover over the 2FA option on the left-hand side — a **Reset** icon appears on hover
5. Click the Reset icon; confirm the action in the prompt by clicking **Reset**
6. Notify the user they must reconfigure 2FA; they will be prompted to do so on next access to a 2FA-protected resource

## Configuration Values
- None (UI-only operation; no API parameters, CLI flags, or env vars documented)

## Gotchas
- The **Reset icon only appears on hover** — it is not visible by default; easy to miss in the UI
- After reset, the user **will not be re-prompted until they attempt to access a 2FA-protected resource** — notify them proactively
- This resets TOTP enrollment only; it does not disable 2FA requirements on the resources themselves

## Related Docs
- Twingate Two-Factor Authentication setup documentation (linked as "Two Factor Authentication" in the Admin Console help)
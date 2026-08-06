---
source: https://help.twingate.com/articles/3391673762-reset-totp-two-factor-authentication-2fa
type: help
fetched: 2026-08-06
source_version: dfa1dc7f852a91898edfcd2613edb13e00315c8116535f82a4d49adc2a1836fa
---

# Reset TOTP/Two-Factor Authentication (2FA)

## Summary
Twingate Admins can reset a user's TOTP/2FA configuration when the user loses access to their authenticator app. After reset, the user must reconfigure 2FA before accessing protected resources.

## Key Information
- Reset is required when a user loses access to their authenticator app and cannot generate 2FA codes
- After reset, the user will be prompted to reconfigure 2FA on next access to a 2FA-protected resource
- Action is irreversible (requires user to fully reconfigure)

## Prerequisites
- **Role required:** Twingate Administrator
- Access to the Twingate Admin Console (`https://<network_name>.twingate.com`)

## Step-by-Step

1. Open the Twingate Admin Console at `https://<network_name>.twingate.com`
2. Navigate to **Team** > **Users**
3. Locate the affected user and click their username
4. Hover over the 2FA option on the left-hand side — a **Reset** icon appears on hover
5. Click the Reset icon and confirm the action in the prompt
6. Notify the user they must reconfigure 2FA

## Gotchas
- The Reset icon only appears on **hover** — not visible by default in the UI
- After reset, the user cannot access 2FA-protected resources until they complete reconfiguration
- Admin must manually notify the user; no automatic notification is mentioned

## Related Docs
- [Two Factor Authentication](https://help.twingate.com) — setup/configuration guide for end users post-reset
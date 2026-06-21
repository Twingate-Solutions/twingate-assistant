# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdP instances can be connected simultaneously.

## Key Information
- **Supported IdPs**: Google Workspace (all plans), Entra ID, Okta, OneLogin, JumpCloud, Keycloak (Business/Enterprise)
- **Social logins**: Google, Microsoft, GitHub, LinkedIn — users added manually by admin
- **Multiple IdPs**: Supported simultaneously (e.g., Okta + Entra ID, or two Okta instances)
- **User source tracking**: View Teams page → filter by Source to identify which IdP a user came from
- **IdP renaming**: Supported for easier management of multiple instances
- **Offboarding**: Managed in the IdP; changes must sync to Twingate

## Prerequisites
- Business or Enterprise plan for non-Google Workspace IdPs
- Admin access to Twingate Admin Console
- At least one admin user must remain after any IdP removal

## Configuration Steps

### Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select options on configured IdP → Disconnect
3. If removal would eliminate all admins, provide an email for a new admin (must use social login: Google, Microsoft, GitHub, or LinkedIn)
4. Re-authenticate via Admin Console with the provided email
5. Configure new IdP from Identity Provider page

### Connecting First IdP (with social login active)
1. Begin IdP setup — prompt will appear to keep or remove social login users
2. **Recommended**: Remove social login users for cleaner transition

### Multiple IdPs
1. Navigate to **Settings → Identity Provider**
2. Add additional IdP configurations as needed
3. Optionally rename each IdP for tracking purposes
4. Verify at least one admin remains when removing any IdP

## Gotchas
- **Disconnecting an IdP removes ALL associated users and synced groups** — no partial retention
- If last admin would be removed during IdP disconnect, a fallback admin email is required before proceeding
- When setting up a first IdP alongside existing social login users, not removing social login users may cause transition issues
- Offboarding requires both IdP-side removal AND sync to Twingate — IdP change alone is insufficient

## Related Docs
- [Entra ID Setup](https://www.twingate.com/docs/entra-id)
- [Google Workspace Setup](https://www.twingate.com/docs/google-workspace)
- [Okta Setup](https://www.twingate.com/docs/okta)
- [OneLogin Setup](https://www.twingate.com/docs/onelogin)
- [JumpCloud Setup](https://www.twingate.com/docs/jumpcloud)
- [Keycloak Setup](https://www.twingate.com/docs/keycloak)
- Offboarding Users
- Twingate Universal 2FA setup
# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdPs and multiple instances of the same IdP can be configured simultaneously.

## Key Information
- **Supported IdPs**: Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Google Workspace**: Available on all plans
- **All other IdPs**: Business and Enterprise plans only
- **Social logins**: Google, Microsoft, GitHub, LinkedIn — manually added by admin, useful for contractors
- **Multiple IdPs**: Supported concurrently (e.g., Okta + Entra ID + social login, or two Okta instances)
- **User source visibility**: View via Teams page → filter by Source
- **IdP renaming**: Supported for easier management of multiple providers

## Prerequisites
- Business or Enterprise plan (for non-Google IdPs)
- Admin access to Twingate Admin Console
- At least one admin user must remain after any IdP removal

## Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select the IdP options menu → Disconnect
3. If removal would eliminate all admins, provide an email for a new admin (must use social login: Google, Microsoft, GitHub, or LinkedIn)
4. Re-authenticate via Admin Console using the provided email
5. Configure new IdP from the Identity Provider page

**Warning**: Disconnecting an IdP removes **all associated users and synced groups**.

## First-Time IdP Setup (with existing social login users)
- When adding first IdP with social login active, you'll be prompted to keep or remove social login users
- **Recommended**: Remove social login users for cleaner transition

## Offboarding Users
- Manage user removal within the IdP
- Ensure changes sync to Twingate
- See dedicated Offboarding Users documentation for full process

## Gotchas
- Disconnecting an IdP **deletes all synced users and groups** — not just unlinks them
- Must have at least one remaining admin before removing an IdP
- If all admins would be removed, the replacement admin email must support social login authentication
- Social login users are manually managed and not directory-synced

## 2FA Recommendation
Twingate recommends using **native Twingate Universal 2FA** regardless of IdP:
- Applies 2FA at the network resource level
- No application-side configuration required
- Configured separately from IdP settings

## Related Docs
- Entra ID setup
- Google Workspace setup
- Okta setup
- OneLogin setup
- JumpCloud setup
- Keycloak setup
- Offboarding Users
- Twingate Universal 2FA setup
# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdPs and multiple instances of the same IdP can be configured simultaneously.

## Key Information
- **Supported IdPs**: Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Google Workspace**: Available on all plans; others require Business/Enterprise
- **Multiple IdPs**: Supported — can run Okta + Entra ID + social login concurrently, or two separate Okta instances
- **Social logins**: Google, Microsoft, GitHub, LinkedIn — users added manually by admin
- **User source tracking**: View Teams page, filter by "Source" to identify which IdP each user came from
- **IdP renaming**: Supported for easier management of multiple instances

## Prerequisites
- Business or Enterprise plan for non-Google IdPs
- Admin access to Twingate Admin Console
- At least one admin user must remain after any IdP removal

## Changing / Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select options on the configured IdP and choose disconnect
3. If removal would eliminate all admins, provide an email for a new admin (must use social login: Google, Microsoft, GitHub, or LinkedIn)
4. Re-authenticate via the provided email
5. Configure new IdP from the Identity Provider page

**Warning**: Disconnecting an IdP removes **all associated users and synced groups**.

## First IdP Setup (with Social Login enabled)
- When adding first IdP alongside existing social login users, you'll be prompted to keep or remove social login users
- **Recommendation**: Remove social login users for cleaner transition

## Offboarding Users
- Manage user removal within the IdP itself
- Ensure changes sync to Twingate after IdP-side removal
- See separate Offboarding Users documentation for full process

## Gotchas
- Disconnecting an IdP is destructive — all synced users and groups are deleted immediately
- Must maintain at least one admin account when removing an IdP; if none would remain, a social-login-capable email is required as fallback
- Social login users are manually managed (no auto-sync); useful for contractors without managed accounts

## Security Recommendation
- Use **Twingate Universal 2FA** regardless of IdP — applies 2FA at the network resource level without per-application configuration

## Related Docs
- Entra ID setup
- Google Workspace setup
- Okta setup
- OneLogin setup
- JumpCloud setup
- Keycloak setup
- Offboarding Users
- Twingate Native 2FA setup
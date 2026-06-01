# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdP instances can be connected simultaneously.

## Key Information
- **Supported IdPs**: Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Google Workspace**: Available on all plans; all others require Business/Enterprise
- **Social logins**: Google, Microsoft, GitHub, LinkedIn — manually added by admin, useful for contractors
- **Multiple IdPs**: Supported simultaneously (e.g., Okta + Entra ID, or two Okta instances)
- **User source tracking**: View Teams page → filter by "Source" to identify which IdP a user comes from
- **IdP renaming**: Supported for easier management of multiple instances

## Prerequisites
- Business or Enterprise plan for non-Google Workspace IdPs
- Admin access to Twingate Admin Console
- At least one admin must remain after any IdP removal

## Configuration Steps

### Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select options on the configured IdP → Disconnect
3. If removal would eliminate all admins, provide an email for a new admin (must use social login: Google, Microsoft, GitHub, or LinkedIn)
4. Re-authenticate via the provided email
5. Configure new IdP from the Identity Provider page

### Adding First IdP (with existing social login users)
1. Begin IdP setup — prompted to keep or remove social login users
2. **Recommended**: Remove social login users for cleaner transition

### Multiple IdP Setup
1. Navigate to **Settings → Identity Provider**
2. Add additional providers alongside existing ones
3. Optionally rename each IdP for tracking purposes

## Gotchas
- **Disconnecting an IdP removes all associated users and synced groups immediately**
- If the last admin would be removed during IdP disconnect, a new admin email is required — that user must authenticate via social login
- Social login users must be manually managed; they don't sync automatically
- Offboarding requires managing users in the IdP first, then ensuring sync propagates to Twingate

## Configuration Values
| Setting | Location |
|---|---|
| IdP configuration | Settings → Identity Provider |
| User source filter | Teams page → Source filter |
| 2FA configuration | Separate native 2FA settings |

## Related Docs
- Entra ID setup
- Google Workspace setup
- Okta setup
- OneLogin setup
- JumpCloud setup
- Keycloak setup
- Offboarding Users
- Twingate Universal 2FA (native 2FA — recommended regardless of IdP)
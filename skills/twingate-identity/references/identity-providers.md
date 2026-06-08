# Identity Providers

## Summary
Twingate supports multiple identity providers for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdPs and multiple instances of the same IdP can be configured simultaneously.

## Key Information
- **Supported IdPs**: Google Workspace (all plans), Entra ID, Okta, OneLogin, JumpCloud, Keycloak (Business/Enterprise)
- **Social logins**: Google, Microsoft, GitHub, LinkedIn — manually added by admins, useful for contractors
- **Multiple IdPs**: Supported simultaneously (e.g., Okta + Entra ID + social login, or two Okta instances)
- **User source tracking**: View Teams page → filter by Source to identify which IdP a user came from
- **IdP renaming**: Supported for easier management when running multiple instances
- **Offboarding**: Managed through the IdP; changes must sync to Twingate

## Prerequisites
- Business or Enterprise plan for non-Google Workspace IdPs
- At least one admin must remain on account when disconnecting an IdP

## Configuration Steps

### Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select options on the configured IdP → Disconnect
3. If disconnecting would remove all admins, provide an email for a new admin (must use social login: Google, Microsoft, GitHub, or LinkedIn)
4. Re-authenticate via Admin Console with the provided email
5. Configure new IdP from the Identity Provider page

### Adding First IdP (when social login exists)
1. Begin IdP setup — prompted to keep or remove social login users
2. **Recommended**: Remove social login users for cleaner transition

### Multiple IdPs
1. Navigate to **Settings → Identity Provider**
2. Add additional IdP configurations as needed
3. Optionally rename each IdP for tracking purposes
4. Verify at least one admin remains before removing any IdP

## Gotchas
- **Disconnecting an IdP removes ALL users and synced groups** associated with it — irreversible action
- When first connecting an IdP alongside existing social login users, failing to remove social logins may complicate user management
- Admin lockout prevention: system requires fallback admin email if last admin would be removed

## Configuration Values
| Setting | Location |
|---|---|
| IdP management | Settings → Identity Provider |
| User source filter | Teams page → Source filter |
| 2FA configuration | Separate native Twingate 2FA settings |

## Related Docs
- Entra ID setup
- Google Workspace setup
- Okta setup
- OneLogin setup
- JumpCloud setup
- Keycloak setup
- Offboarding Users
- Twingate Universal 2FA
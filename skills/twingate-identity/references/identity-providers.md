# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdP instances can be connected simultaneously.

## Key Information
- **Supported IdPs**: Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Google Workspace**: Available on all plans; others require Business/Enterprise
- **Multiple IdPs**: Supported — can run multiple providers simultaneously, including multiple instances of the same IdP (e.g., two Okta instances)
- **Social logins**: Google, Microsoft, GitHub, LinkedIn — users can be manually added by admin outside IdP sync
- **User source tracking**: View Teams page → filter by "Source" to identify which IdP a user came from
- **Renaming IdPs**: Supported for easier management when running multiple instances

## Prerequisites
- Business or Enterprise plan for non-Google Workspace IdPs
- Admin access to Twingate Admin Console
- At least one admin user must remain after any IdP removal

## Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select options on the configured IdP → Disconnect
3. If removal would eliminate all admins, provide an email for a new admin (must use social login: Google, Microsoft, GitHub, or LinkedIn)
4. Re-authenticate via Admin Console using the provided email
5. Configure new IdP from Identity Provider page

**Warning**: Disconnecting an IdP removes **all associated users and synced groups**.

## Adding First IdP with Social Login Active
- You will be prompted to keep or remove existing social login users
- **Recommendation**: Remove social login users for a cleaner transition

## Offboarding Users
- Manage user removal within the IdP
- Ensure changes sync to Twingate
- See separate Offboarding Users documentation for full process

## Gotchas
- Disconnecting an IdP **deletes all synced users and groups** — not just unlinking
- Admin lockout prevention: Twingate requires a fallback admin email (social login capable) before removing the last admin IdP
- Social login users are manually managed — not auto-synced; useful for contractors/external parties
- When migrating IdPs, social login users should be removed to avoid conflicts

## Configuration Values
| Setting | Location |
|---|---|
| IdP configuration | Settings → Identity Provider |
| User source filter | Teams page → Source filter |
| Native 2FA | Separate setup required (recommended regardless of IdP) |

## Related Docs
- Entra ID setup
- Google Workspace setup
- Okta setup
- OneLogin setup
- JumpCloud setup
- Keycloak setup
- Offboarding Users
- Twingate Universal 2FA setup
# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdP instances can be configured simultaneously.

## Key Information
- **Supported IdPs**: Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Google Workspace**: Available on all plans; others require Business/Enterprise
- **Multiple IdPs**: Supported — can run multiple providers simultaneously, including multiple instances of the same IdP (e.g., two Okta instances)
- **Social logins**: Google, Microsoft, GitHub, LinkedIn — manually added by admin, useful for contractors
- **User source tracking**: View Teams page → filter by "Source" to identify which IdP a user came from
- **IdP renaming**: Supported for easier multi-IdP management

## Prerequisites
- Business or Enterprise plan for non-Google IdPs
- Admin access to Twingate Admin Console
- Access to Settings → Identity Provider page

## Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select options on the configured IdP → Disconnect
3. **Warning**: Disconnecting removes all associated users and synced groups
4. If disconnection would remove all admins, provide an email for a new admin who can log in via social login (Google, Microsoft, GitHub, or LinkedIn)
5. Re-authenticate via that email, then configure new IdP

## Connecting First IdP (with social login already enabled)
- Prompted to keep or remove existing social login users
- **Recommendation**: Remove social login users for smoother transition

## Offboarding Users
- Manage user offboarding within the IdP itself
- Ensure changes sync to Twingate
- See dedicated Offboarding Users documentation for details

## Gotchas
- Disconnecting an IdP **permanently removes all synced users and groups** from that provider
- Cannot disconnect last IdP/admin without designating a social-login-capable replacement admin
- When adding first IdP alongside existing social login users, those users must be explicitly kept or removed
- Multiple instances of same IdP are supported but require careful naming to track user sources

## Configuration Notes
- **Universal 2FA**: Twingate recommends using native 2FA regardless of IdP — applies to any network resource without per-application configuration

## Related Docs
- Entra ID setup
- Google Workspace setup
- Okta setup
- OneLogin setup
- JumpCloud setup
- Keycloak setup
- Offboarding Users
- Twingate Universal 2FA setup
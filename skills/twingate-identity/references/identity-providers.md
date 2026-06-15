# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdPs and multiple instances of the same IdP can be configured simultaneously.

## Key Information
- **Supported IdPs**: Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Google Workspace** is the only IdP available on all plans; others require Business/Enterprise
- Users can be auto-synced from IdP directories or manually added (social logins: Google, LinkedIn, etc.)
- Multiple IdPs can run concurrently (e.g., Okta + Entra ID + social login, or two Okta instances)
- IdPs can be renamed for easier management
- User source is visible on the Teams page via the **Source** filter

## Prerequisites
- Business or Enterprise plan for non-Google Workspace IdPs
- Admin access to Twingate Admin Console
- At least one admin must remain after any IdP removal

## Configuration Steps

### Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select options on the configured IdP → Disconnect
3. If removal would eliminate all admins, provide an email for a new admin (must use social login: Google, Microsoft, GitHub, or LinkedIn)
4. Re-authenticate via Admin Console using the provided email
5. Set up new IdP from the Identity Provider page

### Adding First IdP (with social login already enabled)
1. Begin IdP setup in **Settings → Identity Provider**
2. When prompted, choose to **remove** social login users (recommended for cleaner transition)
3. Complete IdP-specific configuration

### Multiple IdPs
1. Configure additional IdPs via **Settings → Identity Provider**
2. Optionally rename each IdP for tracking purposes
3. Ensure at least one admin-privileged user remains when removing any IdP

## Gotchas
- **Disconnecting an IdP removes all associated users and synced groups immediately**
- If removing an IdP would leave no admins, a new admin email is required before disconnection can complete
- The replacement admin must authenticate via a supported social login (Google, Microsoft, GitHub, LinkedIn)
- Offboarding users requires managing them in the IdP first, then ensuring sync propagates to Twingate

## Recommendations
- Enable **Twingate Universal 2FA** (native functionality) regardless of IdP — allows per-resource 2FA enforcement without application-level configuration
- Remove social login users when transitioning to a dedicated IdP for cleaner user management

## Related Docs
- [Entra ID Setup](#)
- [Google Workspace Setup](#)
- [Okta Setup](#)
- [OneLogin Setup](#)
- [JumpCloud Setup](#)
- [Keycloak Setup](#)
- [Offboarding Users](#)
- [Twingate Universal 2FA](#)
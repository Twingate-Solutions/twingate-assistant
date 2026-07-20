# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdPs and multiple instances of the same IdP can be configured simultaneously.

## Key Information
- **Supported IdPs**: Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Google Workspace**: Available on all plans; others require Business/Enterprise
- **Social logins**: Google, Microsoft, GitHub, LinkedIn — manually added by admin, useful for contractors
- **Multiple IdPs**: Supported simultaneously (e.g., Okta + Entra ID + social login, or two Okta instances)
- **User source tracking**: View Teams page and filter by "Source" to identify which IdP a user came from
- **IdPs can be renamed** for easier management

## Prerequisites
- Business or Enterprise plan for non-Google Workspace IdPs
- Admin access to Twingate Admin Console
- At least one admin user must remain after any IdP removal

## Step-by-Step: Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select the configured IdP's options menu → Disconnect
3. If disconnecting would remove all admins, provide an email address for a new admin (must use social login: Google, Microsoft, GitHub, or LinkedIn)
4. Re-authenticate into Admin Console with the provided email
5. Navigate back to Identity Provider page to configure a new IdP

## Step-by-Step: First IdP Setup with Existing Social Login Users
1. Begin IdP setup from **Settings → Identity Provider**
2. When prompted, choose to **remove** social login users (recommended for smoother transition)
3. Complete IdP-specific configuration

## Gotchas
- **Disconnecting an IdP removes all associated users and synced groups** — this is irreversible
- If removal would eliminate all admins, you must pre-designate a social-login-capable admin email before disconnecting
- When adding first IdP alongside social login users, removing social login users is recommended to avoid conflicts
- Offboarding requires managing users in the IdP and ensuring sync propagates to Twingate — changes are not instant

## Configuration Values
- No specific env vars or API params documented on this page
- IdP-specific configuration values are in individual IdP setup docs

## Related Docs
- [Entra ID setup](#)
- [Google Workspace setup](#)
- [Okta setup](#)
- [OneLogin setup](#)
- [JumpCloud setup](#)
- [Keycloak setup](#)
- Offboarding Users page
- Twingate Universal 2FA setup
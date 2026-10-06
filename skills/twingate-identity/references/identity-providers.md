---
source: https://www.twingate.com/docs/identity-providers
type: docs
fetched: 2026-10-04
source_version: c594517f13ab67cb309b5279f68d549d89f06e2a63ce7fe18fedd6ce48207e91
trust: official
---

# Identity Providers

## Page Title
Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdP instances can run simultaneously to support migration, contractors, or subsidiaries.

## Key Information
- **Supported IdPs:** Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Social logins:** Google, Microsoft, GitHub, LinkedIn (manually added by admin; useful for contractors without managed accounts)
- **Multiple IdPs:** Supported — can mix different providers or run multiple instances of the same provider (e.g., two Okta instances)
- **User source visibility:** Teams page → filter by "Source" to identify which IdP each user originates from
- **IdP renaming:** Supported for easier management of multi-IdP setups
- **Offboarding:** Managed within the IdP; changes must sync to Twingate

## Prerequisites
- Business or Enterprise plan for non-Google IdPs
- Admin access to Twingate Admin Console
- At least one admin user must remain after any IdP removal

## Configuration Steps

### Connect an IdP
1. Navigate to **Settings → Identity Provider** in Admin Console
2. Select desired IdP and follow provider-specific setup guide
3. If social login users exist, choose to keep or remove them (removal recommended for clean transition)

### Disconnect/Change an IdP
1. Go to **Settings → Identity Provider**
2. Open options for the configured IdP → Disconnect
3. If disconnection would remove all admins, provide an email for a new admin (must use a supported social login)
4. Re-authenticate via the provided email
5. Configure new IdP from the Identity Provider page

### Add Multiple IdPs
1. Navigate to **Settings → Identity Provider**
2. Add additional providers alongside existing ones
3. Optionally rename each IdP for tracking purposes

## Gotchas
- **Disconnecting an IdP removes all associated users and synced groups** — no partial removal
- If no admins would remain after IdP removal, a social-login-capable admin email is required before proceeding
- Social login users must be manually added; they are not directory-synced
- When first connecting an IdP alongside existing social login users, removing social login users is recommended for a smoother transition

## Configuration Values
- No environment variables or API params documented on this page
- Provider-specific config values are in individual IdP setup pages

## Related Docs
- [Entra ID Setup](#)
- [Google Workspace Setup](#)
- [Okta Setup](#)
- [OneLogin Setup](#)
- [JumpCloud Setup](#)
- [Keycloak Setup](#)
- [Offboarding Users](https://www.twingate.com/docs/offboarding-users)
- [Twingate Universal 2FA](https://www.twingate.com/docs/two-factor-authentication)
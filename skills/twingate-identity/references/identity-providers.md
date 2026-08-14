---
source: https://www.twingate.com/docs/identity-providers
type: docs
fetched: 2026-08-14
source_version: 3ab0a265393d5cd3e9007e012445f47ed066dbbc4e55640f4420b1c5f4f7a58a
---

# Identity Providers

## Summary
Twingate supports multiple identity providers (IdPs) for user authentication and directory sync. Google Workspace is available on all plans; Entra ID, Okta, OneLogin, JumpCloud, and Keycloak require Business or Enterprise plans. Multiple IdP instances can be configured simultaneously.

## Key Information
- **Supported IdPs**: Entra ID (Azure AD), Google Workspace, Okta, OneLogin, JumpCloud, Keycloak
- **Google Workspace** is the only IdP available on all plans; others require Business/Enterprise
- Users can be auto-synced from IdP directories or manually added via social logins (Google, LinkedIn)
- Multiple IdP instances supported simultaneously (e.g., two Okta instances + Entra ID)
- IdPs can be renamed for easier management
- View user source via Teams page → filter by **Source**

## Prerequisites
- Business or Enterprise plan for non-Google IdPs
- Admin access to Twingate Admin Console
- Admin access to the target IdP

## Changing/Disconnecting an IdP
1. Navigate to **Settings → Identity Provider**
2. Select options on configured IdP → Disconnect
3. **Warning**: Disconnecting removes ALL synced users and groups
4. If disconnect would remove all admins, provide an email for a new admin who can log in via social login (Google, Microsoft, GitHub, or LinkedIn)
5. Re-authenticate via Admin Console using the provided email
6. Configure new IdP from Identity Provider page

## Adding First IdP (When Social Login Exists)
- Twingate prompts to keep or remove existing social login users
- **Recommendation**: Remove social login users for smoother transition

## Multiple Identity Providers
- Use cases: tool migration, contractors, subsidiaries
- No limit specified on number of IdP connections
- Requirement when removing an IdP: at least one admin must remain on the account
- Can rename individual IdP configurations for tracking

## Offboarding Users
- Enterprise IdP: manage offboarding within the IdP; changes sync to Twingate
- See separate Offboarding Users documentation for details

## Gotchas
- Disconnecting an IdP **immediately removes all associated users and groups** — no soft delete
- If last admin would be removed, a fallback admin email is required before disconnection can proceed
- Social login users (contractors, etc.) are managed manually by admins, not synced
- When first connecting an IdP alongside social login, prompt to remove social users appears — skipping this may cause conflicts

## Security Recommendation
- Use **Twingate Universal 2FA** (native) regardless of IdP — applies 2FA to any network resource without per-application configuration

## Related Docs
- Entra ID setup
- Google Workspace setup
- Okta setup
- OneLogin setup
- JumpCloud setup
- Keycloak setup
- Offboarding Users
- Twingate Native 2FA setup
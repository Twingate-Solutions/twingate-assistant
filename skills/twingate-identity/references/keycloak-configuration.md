# Keycloak Configuration

## Summary
Twingate integrates with Keycloak to delegate user authentication via OIDC. Only users associated with the Twingate app in Keycloak can access Twingate resources. Configuration requires direct contact with Twingate support.

## Key Information
- Authentication delegation uses OIDC protocol
- User access is scoped to users associated with the Twingate app in Keycloak
- No self-serve configuration available — must contact Twingate to set up

## Prerequisites
- Business or Enterprise Twingate plan (not available on lower tiers)
- Existing Keycloak instance

## Step-by-Step
No public self-serve steps documented. Contact Twingate directly to initiate configuration.

## Configuration Values
None publicly documented.

## Gotchas
- **Plan restriction**: Business and Enterprise only — will not work on free/starter plans
- **No self-serve setup**: Unlike some other IdP integrations, Keycloak requires contacting Twingate support to configure
- Only authentication is delegated (OIDC); no mention of SCIM/directory sync support

## Related Docs
- Twingate pricing page (for plan comparison)
- Other IdP integration docs (Okta, Azure AD, Google Workspace) for self-serve alternatives
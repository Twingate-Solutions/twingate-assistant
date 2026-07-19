# Keycloak Configuration

## Page Title
Keycloak Configuration (Twingate Identity Provider Integration)

## Summary
Twingate integrates with Keycloak to delegate user authentication via OIDC. Only users associated with the Twingate app in Keycloak can authenticate and access private resources. This feature is restricted to Business and Enterprise plans.

## Key Information
- Authentication delegation uses **OIDC** (OpenID Connect)
- Keycloak acts as the identity provider (IdP) for Twingate
- Only Keycloak users assigned to the Twingate application can access Twingate resources
- No self-service configuration steps are documented — setup requires contacting Twingate support

## Prerequisites
- **Twingate Business or Enterprise plan** (not available on lower tiers)
- An existing Keycloak instance
- Contact with Twingate support to initiate configuration

## Step-by-Step
No public step-by-step configuration documented. To configure:
1. Contact Twingate directly via the "Contact Us" link on the docs page

## Configuration Values
None publicly documented.

## Gotchas
- **Plan restriction**: Keycloak integration is explicitly limited to Business and Enterprise plans — attempting to configure on lower plans will not work
- Configuration is **not self-service** — requires Twingate involvement, unlike some other IdP integrations
- Only user **authentication** is delegated (OIDC); no mention of SCIM/provisioning support

## Related Docs
- Twingate pricing page (for plan comparison)
- Other IdP integration docs (e.g., Okta, Azure AD, Google) for self-service alternatives
- Twingate OIDC/SSO general documentation
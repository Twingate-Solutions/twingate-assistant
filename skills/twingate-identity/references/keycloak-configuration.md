# Keycloak Configuration

## Page Title
Keycloak Configuration (Twingate + Keycloak OIDC Integration)

## Summary
Twingate integrates with Keycloak to delegate user authentication via OIDC. Only users associated with the Twingate app in Keycloak can authenticate and access private resources. Configuration requires direct contact with Twingate support.

## Key Information
- Authentication protocol: **OIDC** (OpenID Connect)
- Twingate delegates **user authentication only** to Keycloak (not authorization/provisioning)
- Users must be explicitly associated with the Twingate app in Keycloak to gain access

## Prerequisites
- **Business or Enterprise plan** required (not available on lower tiers)
- Active Keycloak instance
- Contact Twingate support to initiate configuration

## Step-by-Step
No self-serve configuration steps documented. To configure:
1. Contact Twingate via the "Contact Us" link on the docs page
2. Work with Twingate team to complete integration setup

## Configuration Values
- No self-documented env vars, CLI flags, or API parameters in this page
- Integration type: OIDC

## Gotchas
- **Plan restriction**: Keycloak integration is gated behind Business and Enterprise plans — attempting to configure on lower plans will not work
- **No self-serve setup**: Unlike some other IdP integrations, Keycloak requires contacting Twingate support; no independent configuration steps are published
- Only authentication is delegated — verify separately how user provisioning/deprovisioning is handled (not addressed in this doc)

## Related Docs
- [Twingate Pricing](https://www.twingate.com/pricing) — to verify plan eligibility
- Other IdP integration docs (Okta, Azure AD, Google Workspace) for comparison reference
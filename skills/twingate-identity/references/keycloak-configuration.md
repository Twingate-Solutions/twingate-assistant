---
source: https://www.twingate.com/docs/keycloak-configuration
type: docs
fetched: 2026-08-14
source_version: 36774aea3e3865ac679c237ec6aa96f6eca8d1e946b5c877600a2d163349a6bc
---

# Keycloak Configuration

## Page Title
Keycloak Configuration (Twingate Identity Provider Integration)

## Summary
Twingate integrates with Keycloak to delegate user authentication via OIDC. Only users associated with the Twingate app in Keycloak can authenticate and access private resources. Configuration requires direct contact with Twingate support.

## Key Information
- Integration uses **OIDC** (OpenID Connect) for user authentication
- User access is scoped: only users associated with the Twingate app in Keycloak are permitted
- No self-serve setup — configuration requires contacting Twingate directly

## Prerequisites
- **Business or Enterprise** Twingate plan (not available on lower tiers)
- An existing Keycloak instance
- Contact with Twingate support to initiate setup

## Step-by-Step
1. Confirm you are on a Business or Enterprise Twingate plan
2. Contact Twingate support via the "Contact Us" link to initiate Keycloak configuration
3. Work with Twingate to complete the integration (steps are not publicly documented)

## Configuration Values
- **Protocol**: OIDC
- No specific env vars, CLI flags, or API parameters documented on this page

## Gotchas
- No self-service configuration is available — this page does not contain setup steps; you must go through Twingate support
- Only users **explicitly associated with the Twingate app** in Keycloak will gain access; other Keycloak users are excluded
- Plan gating: attempting to configure on Starter/Teams plans will not be supported

## Related Docs
- Twingate Pricing Page (for plan comparison)
- Other IdP integrations (Okta, Azure AD, Google Workspace) for alternative identity provider options
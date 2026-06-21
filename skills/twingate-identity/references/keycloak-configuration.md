# Keycloak Configuration

## Page Title
Keycloak Configuration

## Summary
Twingate integrates with Keycloak to delegate user authentication via OIDC. Only users associated with the Twingate app in Keycloak can authenticate and access private resources. Configuration requires direct engagement with Twingate support.

## Key Information
- Integration uses OIDC for user authentication delegation
- Only users assigned to the Twingate app in Keycloak can access Twingate resources
- Twingate handles: user authentication via OIDC (no mention of SCIM/provisioning)

## Prerequisites
- Business or Enterprise plan required (not available on lower tiers)

## Step-by-Step
No self-service configuration steps are documented. Contact Twingate directly to configure Keycloak integration.

## Configuration Values
None published in documentation.

## Gotchas
- No self-serve setup — must contact Twingate to initiate configuration
- Integration scope is limited to OIDC authentication only; automated user provisioning (SCIM) is not mentioned as supported for Keycloak

## Related Docs
- Twingate pricing page (for plan eligibility)
- Other IdP configuration docs (e.g., Okta, Azure AD) for comparison
# Keycloak Configuration

## Page Title
Keycloak Configuration (Twingate + Keycloak OIDC Integration)

## Summary
Twingate integrates with Keycloak to delegate user authentication via OIDC. Only users associated with the Twingate app in Keycloak can authenticate and access private resources. This feature is restricted to Business and Enterprise plans.

## Key Information
- Authentication protocol: **OIDC** (OpenID Connect)
- Twingate delegates **user authentication only** to Keycloak
- User access scoped to those associated with the Twingate app in Keycloak
- Integration is **not self-serve** — requires contacting Twingate support

## Prerequisites
- Twingate **Business or Enterprise** plan (not available on lower tiers)
- Existing Keycloak instance
- Contact with Twingate support to initiate configuration

## Step-by-Step
1. Confirm you are on a Business or Enterprise plan
2. Contact Twingate via the "Contact Us" link to request Keycloak integration setup
3. Configuration is completed with Twingate support assistance

## Configuration Values
- None documented publicly — configuration details provided through Twingate support engagement

## Gotchas
- **No self-service setup**: Unlike some other IdP integrations, Keycloak requires direct engagement with Twingate support
- Users **not** associated with the Twingate app in Keycloak will be blocked from accessing any resources
- Only authentication is delegated; authorization/resource access control remains in Twingate

## Related Docs
- [Twingate Pricing](https://www.twingate.com/pricing) — to verify plan eligibility
- Other IdP integration docs (e.g., Okta, Azure AD) for comparison reference
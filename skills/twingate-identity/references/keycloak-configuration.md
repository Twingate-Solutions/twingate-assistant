# Keycloak Configuration

## Page Title
Keycloak Configuration (Twingate + Keycloak OIDC Integration)

## Summary
Twingate integrates with Keycloak to delegate user authentication via OIDC. Only users associated with the Twingate app in Keycloak can access Twingate and private resources. Configuration requires direct contact with Twingate support.

## Key Information
- Authentication delegation uses **OIDC protocol**
- Only Keycloak users **associated with the Twingate app** gain access — unassociated users cannot authenticate
- Twingate handles user authentication only (not provisioning/SCIM details mentioned on this page)

## Prerequisites
- **Business or Enterprise plan** required — not available on lower tiers
- Access to a Keycloak instance
- Twingate account with admin access

## Step-by-Step
No self-serve configuration steps are documented. Setup requires contacting Twingate directly.

## Configuration Values
None documented publicly on this page.

## Gotchas
- **No self-service setup** — must contact Twingate to initiate Keycloak integration
- Plan gating is strict: Business or Enterprise only; verify plan before attempting setup
- Scope is limited to **authentication only** (OIDC); any additional identity provider features (e.g., group sync, SCIM) are not addressed on this page

## Related Docs
- [Twingate Pricing Page](https://www.twingate.com/pricing) — to verify plan eligibility
- Contact Twingate support to begin configuration
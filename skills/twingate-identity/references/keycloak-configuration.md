# Keycloak Configuration

## Summary
Twingate integrates with Keycloak to delegate user authentication via OIDC. Only users associated with the Twingate app in Keycloak can access Twingate and private resources. Configuration requires contacting Twingate support directly.

## Key Information
- Integration type: OIDC-based user authentication delegation
- Access control: Only Keycloak users associated with the Twingate app can use Twingate
- Twingate does **not** handle user authentication when Keycloak is configured — Keycloak does
- No self-serve configuration available; must contact Twingate

## Prerequisites
- **Business or Enterprise plan required** (not available on lower tiers)
- Existing Keycloak instance

## Step-by-Step
No public self-serve steps documented. Contact Twingate to initiate configuration.

## Configuration Values
None documented publicly.

## Gotchas
- This feature is **Business & Enterprise only** — attempting to configure on lower plans will not work
- No documented self-serve setup path; configuration is handled through Twingate support
- Documentation is minimal — implementation details are not publicly available

## Related Docs
- [Twingate Pricing](https://www.twingate.com/pricing)
- Contact Twingate support to proceed: https://www.twingate.com/contact
# Okta Configuration

## Page Title
Okta Configuration (Twingate + Okta Integration)

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via OpenID Connect (OIDC) and SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Configuration requires setup in both Okta Admin console and Twingate Admin console.

## Key Information
- **Plan requirement**: Business and Enterprise plans only
- **Authentication method**: SP-Initiated SSO via OIDC
- **User/group sync**: SCIM protocol
- **Delegated functions**: User authentication (OIDC) + User/group synchronization (SCIM)
- Two-phase setup: configure in Okta first, then complete in Twingate Admin console

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- **Okta Lifecycle Management module** required for direct SCIM sync (otherwise manual workflow applies)

## Step-by-Step
1. Create and configure the Twingate application in the Okta Admin console
2. Configure SCIM synchronization in Okta (separate step)
3. Complete and validate integration in the Twingate Admin console
4. Set up Authentication Policy using credentials from the Okta Twingate application

## Configuration Values
- **SSO Protocol**: OpenID Connect (OIDC)
- **SSO Type**: Service Provider (SP) Initiated only
- **Sync Protocol**: SCIM

## Gotchas
- **No Lifecycle Management module**: Users will NOT appear in Twingate Admin panel until they first log into the Twingate Client and authenticate via Okta — manual group assignment required afterward
- SCIM configuration is a **separate step** from OIDC setup; both must be completed independently
- Authentication policies for the Twingate client app are controlled through the Okta Twingate application, not Twingate directly

## Related Docs
- [Twingate Okta Application setup](#) (linked inline — Okta-side config)
- [SCIM synchronization configuration](#) (linked inline — sync setup)
- Twingate pricing page (plan eligibility)
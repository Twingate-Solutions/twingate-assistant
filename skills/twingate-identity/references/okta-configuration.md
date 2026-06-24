# Okta Configuration

## Page Title
Okta Configuration (Twingate + Okta Integration)

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via OIDC and SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Setup requires two phases: configuring the app in Okta, then completing validation in the Twingate Admin console.

## Key Information
- **Authentication**: SP-Initiated SSO via OpenID Connect (OIDC)
- **User/Group Sync**: SCIM protocol
- **Plan Requirement**: Business and Enterprise plans only
- Users must be explicitly assigned to the Okta Twingate application to use Twingate
- Okta handles sign-in policies for the Twingate client application

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- **Okta Lifecycle Management Module** required for direct SCIM user/group syncing
  - Without it: SCIM sync unavailable; users only appear in Twingate Admin panel after first login via Okta; groups must be managed manually

## Step-by-Step
1. Create and configure the Twingate application in the **Okta Admin console**
2. Configure SCIM synchronization separately in Okta
3. Complete and validate the integration in the **Twingate Admin console**
4. Set up an Authentication Policy using credentials from the Okta Twingate application

## Configuration Values
- **Protocol**: OpenID Connect (OIDC) for authentication
- **Sync Protocol**: SCIM for user/group synchronization
- **SSO Type**: Service Provider Initiated (SP-Initiated)

## Gotchas
- **No Lifecycle Management Module**: Users are invisible in Twingate Admin until they complete their first Okta login via the Twingate client; group assignment must be done manually afterward
- SCIM sync must be configured as a **separate step** from OIDC setup — it is not automatic
- Authentication policy configuration is done at the Okta application level, not Twingate

## Related Docs
- [Twingate Okta Application setup](#) (Okta-side configuration)
- [SCIM synchronization configuration](#) (User & group sync)
- [Twingate Pricing](https://www.twingate.com/pricing) (plan eligibility)
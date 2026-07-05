# Okta Configuration

## Page Title
Okta Configuration (Twingate + Okta Integration)

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via OpenID Connect (OIDC) and SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Setup requires configuration in both the Okta Admin console and Twingate Admin console.

## Key Information
- **Authentication**: SP-Initiated SSO via OIDC
- **User/Group Sync**: SCIM protocol
- **Plan requirement**: Business and Enterprise plans only
- **Two-phase setup**: Configure in Okta first, then validate in Twingate Admin console
- Users assigned to the Okta Twingate application gain access; unassigned users are blocked

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- **Okta Lifecycle Management module** required for direct SCIM user/group sync
  - Without it: users only appear in Twingate Admin panel after first login via Twingate Client; manual group assignment required

## Step-by-Step
1. Create and configure the Twingate application in the Okta Admin console
2. Configure SCIM synchronization separately in Okta
3. Complete and validate the integration in the Twingate Admin console
4. Set up an Authentication Policy in Twingate using credentials from the Okta Twingate application

## Configuration Values
- **Protocol**: OpenID Connect (OIDC) for authentication
- **Sync Protocol**: SCIM for user/group synchronization
- Authentication Policy credentials sourced from the Okta Twingate application

## Gotchas
- **No Lifecycle Management module**: Users are invisible in Twingate Admin panel until they complete their first login through the Twingate Client against Okta — manual group assignment needed afterward
- SCIM sync must be configured as a **separate step** from OIDC setup; it is not automatic
- Only SP-Initiated SSO is supported (IdP-Initiated not supported)

## Related Docs
- [Configure the Twingate Okta Application](#) — Okta-side app setup
- [Configure SCIM synchronization](#) — User/group sync setup
- Twingate Pricing Page — plan eligibility
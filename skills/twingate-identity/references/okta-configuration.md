# Okta Configuration

## Page Title
Okta Configuration (Twingate + Okta Integration)

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via OpenID Connect (OIDC) and SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Setup requires configuration in both Okta Admin console and Twingate Admin console.

## Key Information
- **Authentication**: SP-Initiated SSO via OIDC
- **User/Group Sync**: SCIM protocol
- **Plan requirement**: Business and Enterprise plans only
- **Two-phase setup**: Configure in Okta first, then validate in Twingate Admin console
- **Okta Lifecycle Management module** is required for direct SCIM user/group syncing

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- Okta Lifecycle Management module (required for SCIM sync; without it, manual workarounds apply)

## Step-by-Step
1. Create and configure the Twingate application in the **Okta Admin console**
2. Configure SCIM synchronization separately in Okta
3. Complete and validate integration in the **Twingate Admin console** (set up Authentication Policy using credentials from the Okta Twingate app)

## Configuration Values
- **Protocol**: OpenID Connect (OIDC)
- **Sync Protocol**: SCIM
- **SSO Type**: SP-Initiated (SP-Initiated SSO only; IdP-Initiated not supported)

## Gotchas
- **Without Lifecycle Management module**: Users are NOT visible in Twingate Admin panel until they manually log in via the Twingate Client and authenticate through Okta. Groups must be assigned manually afterward.
- SCIM sync must be configured as a **separate step** from OIDC setup — it is not automatic.
- Authentication policies for Twingate client access are controlled via the Okta Twingate application settings in Okta.

## Related Docs
- [Twingate Okta Application setup](#) (Okta-side configuration)
- [SCIM synchronization configuration](#) (separate SCIM setup guide)
- [Twingate Pricing Page](https://www.twingate.com/pricing)
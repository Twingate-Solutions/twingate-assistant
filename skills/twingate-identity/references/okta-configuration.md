# Okta Configuration

## Page Title
Okta Configuration (Twingate)

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via OpenID Connect (OIDC) and SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Setup requires two phases: configuring the app in Okta, then completing integration in Twingate Admin console.

## Key Information
- **Plan requirement**: Business and Enterprise plans only
- **Authentication**: SP-Initiated SSO via OIDC
- **User/Group sync**: SCIM protocol
- Only assigned Okta users can authenticate and access private resources
- Okta Authentication Policy must be configured using credentials from the Okta Twingate app

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- **Okta Lifecycle Management module** required for direct SCIM user/group syncing
  - Without it: users only appear in Twingate Admin panel after first login via Twingate Client; groups must be managed manually

## Step-by-Step
1. Create and configure the Twingate application in the **Okta Admin console**
2. Configure SCIM synchronization separately in Okta
3. Complete and validate integration in the **Twingate Admin console**

## Configuration Values
| Component | Protocol | Notes |
|-----------|----------|-------|
| Authentication | OIDC (OpenID Connect) | SP-Initiated SSO |
| User/Group Sync | SCIM | Requires Lifecycle Management module for automatic sync |

## Gotchas
- **No Lifecycle Management module**: Users are invisible in Twingate Admin panel until they complete their first login through the Twingate Client against Okta. Manual group assignment required afterward.
- SCIM sync must be configured as a **separate step** after the OIDC app setup — it is not automatic.
- Authentication policies in Okta apply to Twingate Client users via the Okta Twingate application — verify these policies match your security requirements.

## Related Docs
- [Twingate Okta Application setup](#) (linked inline — Okta side config)
- [SCIM synchronization configuration](#) (linked inline — user/group sync)
- [Twingate Pricing Page](https://www.twingate.com/pricing)
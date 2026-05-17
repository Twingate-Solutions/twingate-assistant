# Okta Configuration – Twingate

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via OpenID Connect (OIDC) and SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Configuration requires two phases: setup in Okta Admin console, then validation in Twingate Admin console.

## Key Information
- **Authentication**: SP-Initiated SSO via OIDC
- **User/Group sync**: SCIM protocol
- **Plan requirement**: Business and Enterprise only
- Users not assigned to the Okta Twingate app cannot use Twingate
- SCIM sync requires the **Okta Lifecycle Management module**
- Without Lifecycle Management: users only appear in Twingate Admin panel after first login via Twingate Client; manual group assignment required

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- Okta Lifecycle Management module (required for automatic SCIM user/group sync)

## Step-by-Step

1. **Create Twingate app in Okta Admin console**
   - Add the Twingate application from the Okta integration catalog
   - Configure the app (OIDC credentials, sign-in policies)

2. **Configure SCIM synchronization in Okta** (requires Lifecycle Management module)
   - Set up SCIM provisioning within the Okta Twingate app

3. **Complete integration in Twingate Admin console**
   - Enter OIDC credentials from the Okta Twingate app
   - Set up an Authentication Policy using those credentials
   - Validate the connection

## Configuration Values
| Component | Protocol | Notes |
|-----------|----------|-------|
| Authentication | OIDC | SP-Initiated only |
| User/Group sync | SCIM | Requires Lifecycle Management module |
| Policy type | Authentication Policy | Configured in Twingate Admin console |

## Gotchas
- **No Lifecycle Management module**: Users are invisible in Twingate Admin until they complete their first login through the Twingate Client; groups must be managed manually
- Only **SP-Initiated SSO** is supported (IdP-Initiated not supported)
- Okta sign-in policies applied to the Twingate app govern all Twingate client authentication behavior
- User assignment to the Okta app is a hard gate—unassigned users get no access

## Related Docs
- [Twingate Okta Application setup](https://www.twingate.com/docs/okta-configuration)
- [SCIM synchronization configuration](https://www.twingate.com/docs/okta-configuration)
- [Twingate pricing page](https://www.twingate.com/pricing)
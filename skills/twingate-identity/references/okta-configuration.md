# Okta Configuration

## Page Title
Okta Configuration (Twingate Integration)

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via OpenID Connect (OIDC) and SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Setup requires two phases: configuring the Twingate app in Okta, then completing integration in the Twingate Admin console.

## Key Information
- **Authentication**: SP-Initiated SSO via OpenID Connect (OIDC)
- **User/Group sync**: SCIM protocol
- **Plan requirement**: Business and Enterprise plans only
- **Two-step setup**: Okta Admin console → Twingate Admin console
- Users must be assigned to the Okta Twingate application to use Twingate

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- **Okta Lifecycle Management module** required for direct SCIM user/group sync

## Step-by-Step

1. **Create Twingate app in Okta Admin console**
   - Configure the Twingate Okta Application (see linked sub-guide)

2. **Configure SCIM synchronization** (separate step)
   - Configure SCIM synchronization in Okta (see linked sub-guide)

3. **Complete integration in Twingate Admin console**
   - Set up Authentication Policy using credentials from the Okta Twingate application

## Configuration Values
- **Protocol**: OpenID Connect (OIDC) for authentication
- **Sync protocol**: SCIM for user/group synchronization
- Authentication Policy credentials sourced from the Okta Twingate application

## Gotchas
- **Without Lifecycle Management module**: SCIM sync is unavailable. Users only appear in Twingate Admin panel after they log into the Twingate Client and authenticate against Okta. Group assignment must be done manually.
- SCIM configuration is a **separate step** from OIDC setup — easy to miss.
- Only SP-Initiated (not IdP-Initiated) SSO is supported.
- Okta sign-in policies for Twingate client are controlled via the Okta Twingate application, not Twingate directly.

## Related Docs
- Twingate Okta Application setup (sub-guide)
- SCIM synchronization configuration (sub-guide)
- [Twingate Pricing](https://www.twingate.com/pricing)
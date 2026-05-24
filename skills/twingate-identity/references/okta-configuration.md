# Okta Configuration

## Page Title
Okta Configuration (Twingate + Okta Integration)

## Summary
Twingate integrates with Okta to delegate user authentication via OIDC and synchronize users/groups via SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Requires Business or Enterprise plan.

## Key Information
- **Authentication**: SP-Initiated SSO via OpenID Connect (OIDC)
- **Sync Protocol**: SCIM for user and group synchronization
- **Plan Requirement**: Business and Enterprise only
- **Two-step setup**: Configure in Okta Admin console first, then complete in Twingate Admin console
- **Okta Lifecycle Management Module** required for direct SCIM sync; without it, users only appear in Twingate Admin panel after first login

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- Okta Lifecycle Management Module (for SCIM user/group sync)

## Step-by-Step
1. Create and configure the Twingate application in the **Okta Admin console**
2. Configure SCIM synchronization separately in Okta
3. Complete and validate integration in the **Twingate Admin console**
4. Set up an Authentication Policy using credentials from the Okta Twingate application

## Configuration Values
- **SSO Type**: SP-Initiated (Service Provider Initiated)
- **Protocol**: OpenID Connect (OIDC)
- **Sync Protocol**: SCIM

## Gotchas
- **Without Lifecycle Management Module**: Users are invisible in Twingate Admin panel until they log into the Twingate Client and authenticate against Okta — manual group assignment required afterward
- SCIM sync must be configured as a **separate step** after OIDC setup; it is not automatic
- Authentication policies for Twingate client users are controlled through the Okta Twingate application

## Related Docs
- Twingate Okta Application setup guide (linked inline)
- SCIM synchronization configuration guide (linked inline)
- Twingate pricing page (plan eligibility)
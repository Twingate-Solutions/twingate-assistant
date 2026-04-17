## Okta Configuration

**URL:** https://www.twingate.com/docs/okta-configuration

**Summary:** Twingate integrates with Okta for SSO via OIDC and user/group sync via SCIM. Only users assigned to the Okta Twingate application can authenticate and access private resources. Setup requires two phases: configuring the app in Okta, then completing validation in the Twingate Admin console.

**Key Information:**
- Supports SP-Initiated SSO via OpenID Connect (OIDC)
- Supports SCIM for user and group synchronization
- Only assigned Okta users can access Twingate resources
- Authentication policies for the Twingate client are configured via the Okta Twingate application

**Prerequisites:**
- Business or Enterprise plan (not available on lower tiers)
- Okta Lifecycle Management module required for direct SCIM sync
- Without Lifecycle Management: users must manually log in via Twingate Client first before appearing in the Admin panel; groups must be assigned manually

**Step-by-Step:**
1. Create and configure the Twingate application in the Okta Admin console
2. Configure SCIM synchronization separately in Okta
3. Complete and validate the integration in the Twingate Admin console

**Gotchas:**
- Without the Okta Lifecycle Management module, SCIM push does not work automatically — users are only provisioned to Twingate after their first login, and group membership requires manual assignment
- OIDC and SCIM are configured as separate steps; completing OIDC alone does not enable user/group sync
- Okta sign-in policies (MFA, device trust, etc.) apply through the Okta Twingate application — misconfigured policies can block all Twingate access

**Related Docs:**
- Twingate Okta Application setup (linked from this page)
- SCIM synchronization configuration (linked from this page)
- Pricing page (plan eligibility)
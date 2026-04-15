<!-- initial seed — to be refreshed by pipeline -->

## Page Title
Identity Provider (IdP) Setup

## Summary
Twingate integrates with enterprise identity providers via OIDC or SAML to enable SSO, enforce MFA, and automatically sync users and groups. SCIM provisioning keeps Twingate group memberships in sync with the IdP in real time, so access policies stay accurate without manual administration.

## Key Information
- **Supported IdPs**: Okta, Microsoft Entra ID (Azure AD), Google Workspace, OneLogin, JumpCloud, and any generic OIDC or SAML 2.0-compliant provider
- **SSO protocols**: OIDC (recommended — simpler token flow, refresh token support) and SAML 2.0 (legacy or enterprise mandate); both are supported for all major IdPs
- **SCIM provisioning**: enables automatic user creation/deactivation and group sync from the IdP; Twingate acts as the SCIM service provider; requires a SCIM token generated in the Admin Console
- **Group sync**: IdP groups map directly to Twingate Groups; access policy assignments (which resources a group can reach) stay current as IdP group memberships change
- **JIT (Just-in-Time) provisioning**: users are created in Twingate on first login if SCIM is not configured; less preferred than SCIM because deprovisioning is not automated
- **Device trust signals**: Entra ID (Intune) and Okta Device Trust feed device compliance state into Twingate access policies — non-compliant devices can be blocked at the resource level
- **MFA enforcement**: MFA can be required at the IdP (recommended), or Twingate can enforce a re-authentication challenge at the session level via policy

## Prerequisites
- Twingate account with admin access
- An active IdP with admin rights to create an application/OIDC client or SAML service provider
- (For SCIM) SCIM endpoint URL and bearer token from Twingate Admin Console → Settings → Authentication
- (For device trust) Intune or Okta Device Trust configured and integrated with the IdP

## Step-by-Step
1. Admin Console → Settings → Authentication → Add Identity Provider → select provider type
2. Choose protocol: OIDC (enter client ID, client secret, issuer URL) or SAML (upload IdP metadata XML or enter manually)
3. In the IdP, create a new application: enter Twingate's ACS URL and entity ID (SAML) or redirect URI (OIDC) from the Admin Console
4. Map IdP groups to Twingate: enable group sync in the IdP application settings and ensure group claims are included in the token or SAML assertion
5. (Optional — SCIM) Enable SCIM in the IdP application; paste Twingate's SCIM endpoint URL and bearer token; configure attribute mappings (email, displayName, groups)
6. Test login: click "Test Connection" in the Admin Console; verify token/assertion is valid and groups are received
7. Assign users or groups to the IdP application in the IdP to control who can authenticate to Twingate

## Configuration Values
- SCIM endpoint format: `https://<tenant>.twingate.com/api/v1/scim`
- OIDC redirect URI: `https://<tenant>.twingate.com/auth/oidc/callback`
- SAML ACS URL: `https://<tenant>.twingate.com/auth/saml/callback`
- SAML entity ID: `https://<tenant>.twingate.com`
- SCIM token: generated once in Admin Console; treat as a secret

## Gotchas
- SCIM and JIT provisioning are mutually exclusive per IdP integration — enable SCIM for any production deployment to ensure deprovisioning works
- Group claims must be explicitly enabled in most IdPs (Okta requires group filter configuration; Entra ID requires adding a "Groups" claim to the token); missing groups claims means Twingate cannot map group memberships
- When using SAML, clock skew greater than 5 minutes between the IdP and Twingate will cause assertion validation failures — ensure NTP is configured on the IdP
- Device trust requires a separate integration in the IdP before it can be referenced in Twingate policies; Twingate does not manage device enrollment itself
- Removing an IdP integration that is the only authentication method will lock all users out — always have a local admin account or backup IdP before making changes
- JIT-provisioned users are not automatically removed when offboarded from the IdP; SCIM deprovisioning is the only automated path for user removal

## Related Docs
- `/docs/idp-okta` — Okta OIDC and SCIM configuration walkthrough
- `/docs/idp-azure-ad` — Entra ID (Azure AD) OIDC, SAML, and SCIM setup
- `/docs/idp-google` — Google Workspace OIDC configuration
- `/docs/idp-onelogin` — OneLogin SAML and SCIM setup
- `/docs/idp-jumpcloud` — JumpCloud OIDC configuration
- `/docs/device-trust` — device trust policy enforcement
- `/docs/groups` — Twingate Groups and access policy assignment
- `/docs/scim` — SCIM provisioning reference

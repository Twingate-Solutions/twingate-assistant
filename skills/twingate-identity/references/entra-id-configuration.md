## Entra ID (Azure AD) Configuration

How to integrate Microsoft Entra ID (formerly Azure AD) with Twingate -- enables OIDC user authentication + SCIM user/group sync.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### Two-Step Setup

**Step 1: Twingate Side -- Sign in with Entra ID**

- Twingate Admin Console -> **Settings -> Identity Provider -> Entra ID**
- Get the Tenant ID:
  - Azure portal (https://portal.azure.com) -> **Entra ID** (left sidebar) -> **Tenant information** -> copy **Tenant ID**
- Paste Tenant ID into Twingate -> **Sign in with Entra ID**
- Verify sign-in succeeds before proceeding

**Step 2: Microsoft -> Add the Twingate Gallery App + Enable SCIM**

- Follow Microsoft's official Twingate gallery app docs (linked from this page)
- Steps covered there:
  - Add Twingate from the Entra ID Gallery to your tenant
  - Configure user/group sync via SCIM
  - Determine which users/groups should sync to Twingate

### Critical Setting: Assignment Required = Yes

- **Default in Entra ID**: `Assignment Required = No`
- **Effect**: any user in your Entra ID tenant can sign in to Twingate, even if not assigned to the Twingate enterprise app
- These accidental sign-ins create Twingate users that are **not managed by Entra ID** (manual cleanup required)
- **Recommendation**: change to `Assignment Required = Yes` -- restricts Twingate access to users explicitly assigned to the Twingate app

### Email Address Requirement (for Help Center Access)

- The Twingate Help Center requires email addresses for sign-in
- Entra ID accounts can be configured **without an email** -- those accounts cannot access support
- To enable Help Center access: set the **Email property** on the Entra ID account; SCIM will sync the email to Twingate

### Decision Notes

- Always set Assignment Required = Yes -- otherwise unmanaged users accumulate in Twingate
- Use Entra ID **Conditional Access** for SaaS App Gating (per /docs/saas-app-gating-with-entra-id, /docs/entra-id-app-gating-office-365)
- For multi-tenant Microsoft environments: Twingate is single-tenant per Entra ID -- one Twingate tenant maps to one Entra ID tenant

### Gotchas

- Email is required for support access; verify all your end users have email properties set in Entra ID
- The Twingate Gallery app is a **Microsoft-published app** -- its config follows Microsoft's enterprise application patterns; use Microsoft's official guide as the source of truth
- SCIM sync interval is determined by Entra ID, not Twingate -- delays of minutes are normal

### Related Docs

- /docs/identity-providers -- IdP overview
- /docs/scim-provisioning-api -- SCIM mechanics
- /docs/saas-app-gating-with-entra-id, /docs/entra-id-app-gating-office-365 -- App gating patterns
- /docs/groups -- Synced Groups behavior

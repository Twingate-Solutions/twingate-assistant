# Entra ID (Azure AD) Configuration

## Summary
Integrates Entra ID with Twingate for OpenID Connect authentication and SCIM-based user/group sync. Requires two steps: configuring the identity provider in Twingate Admin Console, then setting up the Twingate gallery app in Microsoft Entra ID. Business and Enterprise plans only.

## Key Information
- Enables both OIDC user authentication and user/group sync via SCIM
- Uses the official Twingate app in the Microsoft Entra ID Gallery
- `Assignment Required` defaults to `No` in Entra ID — must be changed to `Yes`
- Accounts without email addresses cannot access Twingate's Help Center support

## Prerequisites
- Twingate Business or Enterprise plan
- Azure portal access with permissions to configure Entra ID enterprise applications
- Entra ID Tenant ID

## Step-by-Step

### Step 1: Configure Twingate Admin Console
1. Go to **Settings > Identity Provider > Entra ID** in Twingate Admin Console
2. Retrieve Tenant ID: Azure Portal → Entra ID → **Tenant information** box → copy **Tenant ID**
3. Paste Tenant ID into Twingate and click **Sign in with Entra ID**

### Step 2: Configure Entra ID Gallery App
1. Follow [Microsoft's official Twingate Entra ID Gallery app instructions](https://www.twingate.com/docs/entra-id-configuration)
2. Add Twingate app from Entra ID Gallery
3. Configure which users/groups sync to Twingate
4. Set **Assignment Required** to **Yes**

## Configuration Values

| Setting | Location | Recommended Value |
|---|---|---|
| Assignment Required | Entra ID Enterprise App properties | `Yes` |
| Email property | Per-user Entra ID account | Required for Help Center access |

## Gotchas
- **`Assignment Required = No` (default):** Any Entra ID domain user can log into Twingate even without explicit assignment, creating unmanaged Twingate users. Change to `Yes` immediately.
- **Accounts without email addresses:** Users without an Entra ID email cannot access Twingate's support Help Center. Fix by setting the `Email` property on the Entra ID account — it will sync to Twingate automatically.
- Twingate Admin Console sign-in must be completed *before* configuring the gallery app.

## Related Docs
- [Microsoft Entra ID Gallery App Instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/) (external)
- Twingate pricing page (for plan eligibility)
- SCIM provisioning documentation
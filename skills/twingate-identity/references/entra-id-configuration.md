# Entra ID (Azure AD) Configuration – Twingate

## Summary
Configures Entra ID (formerly Azure AD) as Twingate's identity provider, enabling OpenID Connect authentication and SCIM-based user/group sync. Requires two distinct steps: signing into Entra ID via Twingate Admin Console, then configuring the Twingate gallery app in Microsoft Entra ID.

## Key Information
- Available on **Business and Enterprise plans only**
- Enables both **OIDC authentication** and **SCIM user/group sync**
- Uses the official **Twingate Entra ID Gallery app** from Microsoft

## Prerequisites
- Business or Enterprise Twingate plan
- Access to Azure portal (`portal.azure.com`)
- Admin access to both Twingate Admin Console and Microsoft Entra ID tenant

## Step-by-Step

### Step 1: Connect Entra ID in Twingate
1. Go to Twingate Admin Console → **Settings → Identity Provider → Entra ID**
2. In Azure portal, navigate to **Entra ID → Tenant information**, copy **Tenant ID**
3. Paste Tenant ID into Twingate, click **"Sign in with Entra ID"**
4. Verify sign-in succeeds before proceeding

### Step 2: Configure Gallery App in Microsoft Entra ID
1. Follow [Microsoft's Twingate Entra ID Gallery app instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial) covering:
   - Adding Twingate Gallery app to Entra ID instance
   - Selecting users/groups to sync via SCIM
   - Configuring **Assignment Required** setting

## Configuration Values

| Setting | Location | Recommended Value |
|---|---|---|
| Tenant ID | Azure portal → Entra ID → Tenant information | (your tenant's GUID) |
| Assignment Required | Entra ID → Enterprise App → Properties | **Yes** (change from default `No`) |

## Gotchas

- **`Assignment Required` defaults to `No`** – Any user in the Entra ID domain can log into Twingate even without app assignment, creating unmanaged users. **Set to `Yes` immediately.**
- **Accounts without email addresses** – Entra ID permits accounts without email; these users cannot access Twingate's Help Center support portal. Fix by setting the `Email` property on the Entra ID account, which syncs to Twingate.
- Step 1 (Admin Console sign-in) must be completed **before** configuring the gallery app.

## Related Docs
- [Microsoft Twingate Gallery App Setup](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)
- [Twingate Pricing](https://www.twingate.com/pricing)
- Twingate Help Center (requires email-enabled account)
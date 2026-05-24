# Entra ID (Azure AD) Configuration

## Page Title
Entra ID (formerly Azure AD) Configuration

## Summary
Integrates Twingate with Microsoft Entra ID for OpenID Connect authentication and SCIM-based user/group sync. Requires two steps: enabling the integration in Twingate Admin Console, then configuring the official Twingate gallery app in Microsoft Entra ID.

## Key Information
- Enables both OIDC user authentication and SCIM user/group sync
- Business and Enterprise plans only
- Uses the official Twingate app from the Microsoft Entra ID Gallery
- SCIM sync is configured via the gallery app after initial sign-in

## Prerequisites
- Business or Enterprise Twingate plan
- Access to Azure Portal (`portal.azure.com`)
- Admin access to both Twingate Admin Console and Microsoft Entra ID tenant

## Step-by-Step

### Step 1: Configure in Twingate
1. Go to **Settings > Identity Provider > Entra ID** in Twingate Admin Console
2. Open Azure Portal → navigate to **Entra ID** in left menu
3. Copy **Tenant ID** from the Tenant Information box
4. Paste Tenant ID into Twingate and click **"Sign in with Entra ID"**

### Step 2: Configure Entra ID Gallery App
1. Follow [Microsoft's official Twingate Entra ID Gallery app instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)
2. Add Twingate gallery app to your Entra ID instance
3. Configure which users/groups sync to Twingate
4. **Set "Assignment Required" to Yes** (see Gotchas)

## Configuration Values
| Setting | Location | Recommended Value |
|---|---|---|
| Tenant ID | Azure Portal → Entra ID → Tenant Information | (your tenant ID) |
| Assignment Required | Entra ID Enterprise App settings | `Yes` |

## Gotchas
- **Assignment Required defaults to `No`**: Any user in the Entra ID domain can log into Twingate even without explicit assignment, creating unmanaged Twingate users. **Change to `Yes` immediately.**
- **Accounts without email addresses**: Entra ID permits email-less accounts, but these users cannot access Twingate's Help Center (support portal). Fix by setting the `Email` property on the Entra ID account — it will sync to Twingate automatically.
- Must complete the Twingate Admin Console sign-in step **before** configuring the gallery app.

## Related Docs
- [Microsoft Entra ID Gallery App - Twingate setup instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)
- [Twingate Pricing](https://www.twingate.com/pricing)
- Azure Portal: `https://portal.azure.com`
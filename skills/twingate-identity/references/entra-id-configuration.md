# Entra ID (Azure AD) Configuration

## Summary
Integrates Entra ID with Twingate for OpenID Connect authentication and SCIM-based user/group sync. Requires two steps: configuring the identity provider in Twingate Admin Console, then setting up the official Twingate gallery app in Microsoft Entra ID.

## Key Information
- Enables both OIDC user authentication and user/group sync via SCIM
- Business and Enterprise plans only
- Two-phase setup: Twingate Admin Console first, then Entra ID Gallery app second
- Microsoft hosts detailed gallery app setup instructions externally

## Prerequisites
- Business or Enterprise Twingate plan
- Azure portal access with sufficient permissions
- Entra ID Tenant ID (found at Azure Portal → Entra ID → Tenant information)

## Step-by-Step

### Phase 1: Twingate Admin Console
1. Navigate to **Settings > Identity Provider > Entra ID**
2. Retrieve Tenant ID from [portal.azure.com](https://portal.azure.com) → Entra ID → Tenant information box
3. Paste Tenant ID into Twingate and click **"Sign in with Entra ID"**

### Phase 2: Entra ID Gallery App
1. Follow [Microsoft's official Twingate Entra ID Gallery app instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial) covering:
   - Adding Twingate gallery app to Entra ID instance
   - Configuring which users/groups sync to Twingate
   - Enabling SCIM provisioning

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| Tenant ID | Azure Portal → Entra ID → Tenant information | Required for initial setup |
| Assignment Required | Entra ID Enterprise App properties | Default: `No` — change to `Yes` |

## Gotchas
- **Assignment Required defaults to `No`**: Any user in the Entra ID domain can log into Twingate even without app assignment. These users are created outside SCIM management. **Set to `Yes` to restrict access to assigned users only.**
- **Accounts without email addresses**: Entra ID permits email-less accounts, but Twingate's Help Center (support) requires an email. Users without email cannot access support. Fix: set the `Email` property on the Entra ID account — it will sync to Twingate automatically.
- Phase 1 (Admin Console sign-in) must be completed before Phase 2 (gallery app setup).

## Related Docs
- [Microsoft Entra ID Gallery App Instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial) (external)
- Twingate Pricing Page (for plan eligibility)
- Twingate SCIM documentation
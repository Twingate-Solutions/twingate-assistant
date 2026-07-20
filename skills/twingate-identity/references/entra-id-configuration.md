# Entra ID (Azure AD) Configuration

## Page Title
Entra ID (formerly Azure AD) Configuration

## Summary
Configures Entra ID integration with Twingate for OpenID Connect authentication and SCIM-based user/group sync. Requires two distinct phases: initial Twingate-side configuration, then Microsoft Entra ID Gallery app setup. Available on Business and Enterprise plans only.

## Key Information
- Enables both OIDC user authentication and SCIM user/group sync
- Two-phase setup: Twingate Admin Console config → Microsoft Entra ID Gallery app config
- Official Twingate app available in Microsoft Entra ID Gallery
- SCIM sync only applies to users explicitly assigned to the enterprise application

## Prerequisites
- Business or Enterprise Twingate plan
- Azure portal access with sufficient permissions to configure Entra ID
- Azure Tenant ID (retrieved from Azure portal → Entra ID → Tenant information)

## Step-by-Step

### Phase 1: Twingate Console
1. Navigate to **Settings > Identity Provider > Entra ID** in Twingate Admin Console
2. Retrieve Tenant ID from [portal.azure.com](https://portal.azure.com) → Entra ID → Tenant information
3. Paste Tenant ID into Twingate and click **Sign in with Entra ID**
4. Verify successful sign-in before proceeding

### Phase 2: Microsoft Entra ID Gallery App
1. Add Twingate from the Entra ID Gallery to your Entra ID instance
2. Determine which users/groups should sync to Twingate
3. Enable SCIM provisioning
4. Set **Assignment Required** to **Yes** (see Gotchas)

Full Microsoft-hosted instructions: [Twingate Entra ID Gallery app instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)

## Configuration Values
| Setting | Location | Recommended Value |
|---|---|---|
| Tenant ID | Azure portal → Entra ID → Tenant information | Your Azure Tenant ID |
| Assignment Required | Entra ID enterprise app properties | `Yes` |

## Gotchas
- **Assignment Required defaults to `No`** — users in the Entra ID domain can log into Twingate without being assigned to the app, creating unmanaged Twingate accounts. **Change to `Yes` immediately.**
- **Accounts without email addresses** cannot access Twingate's Help Center (support portal). Fix by setting the `Email` property on the Entra ID account; it will sync to Twingate.
- Phase 1 (Twingate sign-in) must be completed before configuring the Gallery app in Phase 2.

## Related Docs
- [Microsoft Entra ID Gallery - Twingate provisioning tutorial](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)
- Twingate pricing page (for plan eligibility)
- Twingate Help Center (for support access requirements)
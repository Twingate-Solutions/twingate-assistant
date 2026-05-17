# Entra ID (Azure AD) Configuration

## Page Title
Entra ID (formerly Azure AD) Configuration

## Summary
Integrates Twingate with Microsoft Entra ID for OpenID Connect authentication and SCIM-based user/group sync. Requires two distinct steps: configuring the identity provider in Twingate Admin Console, then setting up the official Twingate gallery app in Microsoft Entra ID.

## Key Information
- Enables both OIDC user authentication and SCIM user/group sync
- Business and Enterprise plans only
- Two-phase setup: Twingate Admin Console first, then Entra ID Gallery app second
- SCIM sync details handled via Microsoft's official Twingate Entra ID Gallery app documentation

## Prerequisites
- Business or Enterprise Twingate plan
- Azure portal access with sufficient permissions to add enterprise applications
- Entra ID Tenant ID

## Step-by-Step

### Phase 1: Twingate Admin Console
1. Navigate to **Settings > Identity Provider > Entra ID**
2. Retrieve Tenant ID from `https://portal.azure.com` → Entra ID → Tenant information box
3. Paste Tenant ID into Twingate and click **"Sign in with Entra ID"**

### Phase 2: Entra ID Gallery App
1. Follow [Microsoft's Twingate Entra ID Gallery app instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial) to:
   - Add Twingate gallery app to Entra ID instance
   - Configure SCIM provisioning
   - Determine user/group sync scope

## Configuration Values
| Setting | Location | Recommended Value |
|---|---|---|
| Tenant ID | Azure Portal → Entra ID → Tenant information | Copy and paste into Twingate |
| Assignment Required | Entra ID Enterprise App Properties | **Yes** (change from default `No`) |

## Gotchas
- **Assignment Required defaults to `No`**: Any user in the Entra ID domain can log into Twingate, creating unmanaged users outside SCIM control. **Must be changed to `Yes`.**
- **Accounts without email addresses**: Entra ID permits email-less accounts, but Twingate's Help Center requires an email. Set the `Email` property on affected accounts to enable sync and support access.
- Phase 1 (Twingate sign-in) must be completed before Phase 2 (Gallery app setup).

## Related Docs
- [Microsoft Twingate Entra ID Gallery App Instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)
- Twingate Pricing Page (for plan eligibility)
- Twingate Help Center (support access requirements)
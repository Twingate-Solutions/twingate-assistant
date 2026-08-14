---
source: https://www.twingate.com/docs/entra-id-configuration
type: docs
fetched: 2026-08-14
source_version: 0abd69eaa339059052ab16f995e24d7cc957f9211d65b7023e2220d04e28464a
---

# Entra ID (Azure AD) Configuration

## Page Title
Entra ID (formerly Azure AD) Configuration

## Summary
Configures Entra ID integration with Twingate for OpenID Connect authentication and SCIM-based user/group sync. Requires two steps: enabling the integration in Twingate Admin Console, then configuring the Twingate gallery app in Microsoft Entra ID. Available on Business and Enterprise plans only.

## Key Information
- Enables both OIDC user authentication and user/group sync via SCIM
- Uses the official Twingate app in the Microsoft Entra ID Gallery
- SCIM handles ongoing user and group provisioning/deprovisioning

## Prerequisites
- Twingate Business or Enterprise plan
- Azure portal access with admin privileges
- Entra ID Tenant ID (found at portal.azure.com → Entra ID → Tenant information)

## Step-by-Step

### Step 1: Twingate Admin Console
1. Go to **Settings > Identity Provider > Entra ID**
2. Retrieve Tenant ID from `portal.azure.com` → Entra ID → Tenant information box
3. Paste Tenant ID into Twingate
4. Click **Sign in with Entra ID** and verify login succeeds

### Step 2: Microsoft Entra ID Gallery App
1. Follow [Microsoft's official Twingate Entra ID Gallery app instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)
2. Add Twingate app to your Entra ID instance
3. Configure which users/groups sync to Twingate
4. Enable SCIM provisioning

## Configuration Values
| Setting | Location | Recommended Value |
|---|---|---|
| Tenant ID | Twingate Admin Console | Your Azure Tenant ID |
| Assignment Required | Entra ID Enterprise App settings | **Yes** (change from default `No`) |

## Gotchas

- **Assignment Required defaults to `No`**: Any Entra ID domain user can log into Twingate even without explicit assignment, creating unmanaged Twingate users. **Set to `Yes` immediately** to restrict access to assigned users only.
- **Accounts without email addresses**: Entra ID permits accounts without email. These accounts cannot access Twingate's Help Center (support portal). Fix by setting the `Email` property on the Entra ID account — it will sync to Twingate automatically.
- Step 1 (Twingate console sign-in) must be completed **before** configuring the gallery app in Entra ID.

## Related Docs
- [Microsoft Entra ID Gallery - Twingate provisioning tutorial](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)
- [Twingate Pricing](https://www.twingate.com/pricing)
- Azure portal: https://portal.azure.com
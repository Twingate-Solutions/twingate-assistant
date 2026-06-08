# Entra ID (Azure AD) Configuration

## Page Title
Entra ID (formerly Azure AD) Configuration

## Summary
Integrates Twingate with Microsoft Entra ID for OpenID Connect authentication and SCIM-based user/group sync. Requires two phases: configuring the identity provider in Twingate Admin Console, then setting up the official Twingate gallery app in Microsoft Entra ID.

## Key Information
- Enables both OIDC user authentication and SCIM user/group sync
- Business and Enterprise plans only
- Two-phase setup: Twingate Admin Console → Microsoft Entra ID Gallery app
- SCIM provisioning handled via official Twingate gallery app in Microsoft Entra ID

## Prerequisites
- Business or Enterprise Twingate plan
- Access to Azure Portal (`https://portal.azure.com`)
- Admin access to both Twingate Admin Console and Microsoft Entra ID tenant

## Step-by-Step

### Phase 1: Twingate Configuration
1. Navigate to **Settings > Identity Provider > Entra ID** in Twingate Admin Console
2. Open Azure Portal → navigate to Entra ID → copy **Tenant ID** from Tenant information box
3. Paste Tenant ID into Twingate and click **"Sign in with Entra ID"**

### Phase 2: Entra ID Gallery App
1. Follow [Microsoft's Twingate Entra ID Gallery app instructions](https://learn.microsoft.com/en-us/entra/identity/saas-apps/twingate-provisioning-tutorial) to:
   - Add the Twingate Entra ID Gallery app to your Entra ID instance
   - Configure which users/groups sync to Twingate
   - Enable SCIM provisioning

## Configuration Values
| Setting | Location | Recommended Value |
|---|---|---|
| Tenant ID | Azure Portal > Entra ID > Tenant information | (your tenant ID) |
| Assignment Required | Entra ID Enterprise App properties | **Yes** (change from default `No`) |

## Gotchas
- **Assignment Required defaults to `No`** — any user in the Entra ID domain can log into Twingate even without explicit app assignment, creating unmanaged users. **Must manually set to `Yes`.**
- **Accounts without email addresses** — Entra ID permits accounts with no email; these users cannot access Twingate's Help Center support portal. Fix by setting the `Email` property on the Entra ID account; it will sync to Twingate automatically.
- Phase 1 (signing into Entra ID in Twingate) must be completed before proceeding to gallery app setup.

## Related Docs
- [Microsoft's Twingate Entra ID Gallery App Instructions](https://learn.microsoft.com/en-us/entra/identity/saas-apps/twingate-provisioning-tutorial)
- Twingate Pricing Page (for plan eligibility)
- Twingate Help Center (support access requires email on account)
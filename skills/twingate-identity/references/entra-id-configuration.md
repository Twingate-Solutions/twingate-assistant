# Entra ID (Azure AD) Configuration – Twingate

## Summary
Integrates Entra ID with Twingate for OpenID Connect authentication and SCIM-based user/group sync. Requires two phases: configuring the identity provider in Twingate Admin Console, then setting up the official Twingate gallery app in Microsoft Entra ID.

**Plan requirement:** Business & Enterprise only.

## Key Information
- Enables both OIDC user authentication and SCIM user/group sync
- Uses the official Twingate app from the Microsoft Entra ID Gallery
- SCIM sync is configured from the Microsoft side after Twingate-side setup

## Prerequisites
- Twingate Business or Enterprise plan
- Azure portal access with permissions to manage Entra ID enterprise applications
- Entra ID Tenant ID

## Step-by-Step

### Phase 1: Twingate Admin Console
1. Go to **Settings > Identity Provider > Entra ID**
2. Retrieve Tenant ID: Azure Portal → Entra ID → **Tenant information** box
3. Paste Tenant ID into Twingate and click **"Sign in with Entra ID"**
4. Verify sign-in succeeds before proceeding

### Phase 2: Entra ID Gallery App
1. Follow [Microsoft's official Twingate Entra ID Gallery app instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/) for:
   - Adding the Twingate gallery app to your Entra ID instance
   - Configuring which users/groups sync to Twingate
   - Enabling SCIM provisioning

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| `Tenant ID` | Azure Portal → Entra ID → Tenant information | Required for Twingate-side setup |
| `Assignment Required` | Entra ID enterprise app properties | Default: `No` — **change to `Yes`** |

## Gotchas
- **`Assignment Required` defaults to `No`**: Any Entra ID domain user can log into Twingate even without app assignment, creating unmanaged Twingate users. Set to **`Yes`** to restrict access to assigned users only.
- **Accounts without email addresses**: Entra ID permits email-less accounts, but Twingate's Help Center requires an email for support access. Fix by setting the `Email` property on the Entra ID account — it will sync to Twingate automatically.
- Phase 2 (gallery app) cannot be started until Phase 1 (Twingate sign-in) is fully completed.

## Related Docs
- [Microsoft Entra ID Gallery – Twingate App Instructions](https://www.twingate.com/docs/entra-id-configuration)
- [Twingate Pricing](https://www.twingate.com/pricing)
- Microsoft Azure Portal: https://portal.azure.com
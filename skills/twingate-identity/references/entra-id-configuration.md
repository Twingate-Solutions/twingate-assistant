---
source: https://www.twingate.com/docs/entra-id-configuration
type: docs
fetched: 2026-09-13
source_version: 32bd12d1243c57ea720d23fda8585a78d946f55c54b17096e782be16968f0509
---

# Entra ID Configuration – Twingate

## Summary
Configures Entra ID (formerly Azure AD) as both an OpenID Connect identity provider and SCIM user/group sync source for Twingate. Requires two distinct setup phases: Twingate-side tenant configuration, then Microsoft Gallery app setup. Available on Business and Enterprise plans only.

## Key Information
- Enables OIDC authentication + SCIM-based user/group sync
- Twingate does **not** poll Entra ID; Entra pushes changes via SCIM
- "Last synced" timestamp reflects last received change, not last cycle run
- Entra ID provisioning logs are authoritative for sync status verification

## Prerequisites
- Business or Enterprise Twingate plan
- Azure tenant ID (found in Azure Portal → Entra ID → Tenant information)
- Admin access to both Twingate Admin Console and Azure Portal

## Step-by-Step

### Phase 1: Twingate Console
1. Go to **Settings → Identity Provider → Entra ID**
2. Retrieve Tenant ID from [portal.azure.com](https://portal.azure.com) → Entra ID → Tenant information
3. Paste Tenant ID into Twingate
4. Click **"Sign in with Entra ID"** and verify login

### Phase 2: Microsoft Entra Gallery App
1. Add [Twingate Entra ID Gallery app](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial) to Entra ID instance
2. Configure which users/groups to sync
3. Enable SCIM provisioning

## Critical Configuration: Assignment Required
| Setting | Default | Recommended |
|---------|---------|-------------|
| Assignment Required | No | **Yes** |

- Default (`No`): Any Entra ID domain user can log into Twingate, creating unmanaged accounts outside SCIM control
- Set to **Yes** to restrict access to explicitly assigned users only

## Gotchas
- **Sync timestamp is misleading**: "Last synced" shows last *change received*, not last cycle. A healthy sync with no changes will show an old timestamp
- **Check Entra provisioning logs** (not Twingate UI) to confirm provisioning is actively running
- **On-demand provisioning** available to force push pending changes without waiting for next cycle
- **Accounts without email addresses**: Users without email in Entra ID cannot access Twingate's Help Center (support portal). Fix by setting the `Email` property in Entra ID — it will sync to Twingate automatically
- SCIM runs incremental cycles continuously; only changed objects are pushed each cycle

## Related Docs
- [Microsoft Twingate Gallery App Instructions](https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/twingate-provisioning-tutorial)
- [Entra ID Provisioning Logs](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-provisioning-logs)
- [On-demand Provisioning](https://learn.microsoft.com/en-us/azure/active-directory/app-provisioning/provision-on-demand)
- Twingate Pricing Page (for plan eligibility)
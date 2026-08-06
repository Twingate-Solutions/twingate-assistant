---
source: https://help.twingate.com/articles/4707021810-entra-id-all-users-are-able-to-log-into-twingate-even-though-they-are-not-assigned
type: help
fetched: 2026-08-06
source_version: 268f5642cb2ed8d63d96da989fcab91b43376dbc71f32acd64029e733b404035
---

# [Entra ID] All Users Able to Log Into Twingate Despite Not Being Assigned

## Summary
When Entra ID's "Assignment required" is set to "No," any user in the tenant can authenticate to Twingate regardless of group sync or provisioning status. This creates orphaned users in Twingate that cannot be easily removed.

## Key Information
- **Root cause**: Entra ID "Assignment required" setting defaults or is set to "No" on the Twingate Enterprise Application
- **Effect**: Users bypass group-based provisioning and log in without being synced
- **Result**: Users become stuck in Twingate with no automatic removal path

## Prerequisites
- Admin access to Entra ID (Microsoft Entra admin center)
- Twingate Enterprise Application configured in Entra ID
- Provisioning (SCIM sync) configured in Entra ID

## Resolution Steps

1. Navigate to the Twingate Enterprise Application in Entra ID
2. Set **"Assignment required"** to **"Yes"**
3. Go to the Provisioning settings
4. Under **Scope**, select **"Sync only assigned users and groups"**
5. Run a Provisioning task to remove unassigned users

## Removing Manually-Added Stuck Users
If users were added to Twingate outside of provisioning (manual method):
1. **Assign** the stuck user to the Twingate Enterprise Application in Entra ID
2. **Remove** that user from the Twingate Enterprise Application
3. This triggers a SCIM deprovision event, removing them from Twingate

## Configuration Values
| Setting | Location | Correct Value |
|---|---|---|
| Assignment required | Entra ID > Enterprise App > Properties | **Yes** |
| Provisioning Scope | Entra ID > Enterprise App > Provisioning | **Sync only assigned users and groups** |

## Gotchas
- Setting "Assignment required" to "No" allows **all tenant users** to authenticate, even without provisioning configured
- Simply changing the setting alone is insufficient—a provisioning sync must be run afterward to purge existing unauthorized users
- Stuck users cannot be removed by deleting them directly in Twingate; they must be cycled through Entra ID assignment/removal to trigger the SCIM delete event

## Related Docs
- Twingate Entra ID (Azure AD) Integration setup
- SCIM Provisioning configuration for Entra ID
---
source: https://help.twingate.com/articles/4707021810-entra-id-all-users-are-able-to-log-into-twingate-even-though-they-are-not-assigned
type: help
fetched: 2026-09-06
source_version: c295c7715d91440f14194a2fc678ea6b7cded689452407daa99d14ec030c5e18
---

# [Entra ID] All Users Able to Log Into Twingate Despite Not Being Assigned

## Summary
When Entra ID's "Assignment required" option is set to "No," any user in the tenant can authenticate to Twingate regardless of group sync or provisioning status. This creates orphaned users in Twingate that cannot be removed through normal means.

## Key Information
- **Root cause**: Entra ID "Assignment required" setting defaults to or is set to "No" on the Twingate Enterprise Application
- **Effect**: Users bypass group-based provisioning controls and appear in Twingate without a sync record
- **Side effect**: These users become "stuck" — no automated mechanism removes them since they weren't provisioned via sync

## Prerequisites
- Admin access to Entra ID (Microsoft Entra admin center)
- Twingate Enterprise Application configured in Entra ID
- Provisioning (SCIM sync) configured in Entra ID for Twingate

## Resolution Steps

### Fix the Assignment Setting
1. Navigate to the Twingate Enterprise Application in Entra ID
2. Go to **Properties**
3. Set **"Assignment required"** to **"Yes"**
4. Save changes

### Remove Unauthorized Users via Provisioning
1. Go to **Provisioning** settings for the Twingate Enterprise Application
2. Under **Scope**, select **"Sync only assigned users and groups"**
3. Run a provisioning task to deprovision users not assigned to the application

### Remove Manually Added/Stuck Users
If users were added to Twingate outside of provisioning sync:
1. Explicitly **assign** the stuck user to the Twingate Enterprise Application in Entra ID
2. Then **remove** that user from the application
3. This triggers a provisioning removal event, which removes the user from Twingate

## Configuration Values
| Setting | Location | Correct Value |
|---|---|---|
| Assignment required | Entra ID → Enterprise App → Properties | **Yes** |
| Provisioning Scope | Entra ID → Enterprise App → Provisioning | **Sync only assigned users and groups** |

## Gotchas
- Setting "Assignment required" to "No" allows **all tenant users** to authenticate, even without any provisioning setup
- Users who entered Twingate via this bypass cannot be removed by simply adjusting provisioning scope — they must be explicitly assigned then unassigned to trigger removal
- Changing scope alone without running a provisioning cycle will not remove existing unauthorized users

## Related Docs
- Twingate Entra ID (Azure AD) integration setup
- Entra ID SCIM Provisioning configuration
- Twingate user management / deprovisioning
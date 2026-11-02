---
source: https://help.twingate.com/articles/4707021810-entra-id-all-users-are-able-to-log-into-twingate-even-though-they-are-not-assigned
type: help
fetched: 2026-11-01
source_version: 083c283f00689a38da45ea4ea41281338b99145663e95864b08fd51c4bf8f4d0
trust: official
---

# [Entra ID] All Users Able to Log Into Twingate Despite Not Being Assigned

## Summary
When Entra ID's "Assignment required" option is set to "No," any user in the tenant can authenticate to Twingate regardless of group sync or provisioning status. This creates orphaned users in Twingate that cannot be easily removed.

## Key Information
- Setting "Assignment required" to "No" bypasses group-based access controls entirely
- Affected users become "stuck" in Twingate with no automatic removal path
- This issue occurs independently of whether SCIM provisioning has been configured

## Cause
Entra ID enterprise application setting `Assignment required = No` allows all tenant users to authenticate to Twingate, ignoring group sync membership.

## Resolution Steps

1. In Entra ID, navigate to the Twingate enterprise application
2. Set **Assignment required** → **Yes**
3. Run a Provisioning task
4. Under **Scope**, select **"Sync only assigned users/groups"**
5. Execute the provisioning cycle to remove unassigned users

## Removing Manually-Added Stuck Users
If users were added outside of provisioning and are stuck in Twingate:
1. Manually assign the stuck user to the Twingate enterprise application in Entra ID
2. Then remove them from the application
3. This triggers the deprovisioning event and removes them from Twingate

## Configuration Values

| Setting | Location | Correct Value |
|---|---|---|
| Assignment required | Entra ID → Enterprise Apps → Twingate → Properties | **Yes** |
| Provisioning Scope | Entra ID → Enterprise Apps → Twingate → Provisioning | **Sync only assigned users and groups** |

## Gotchas
- Simply enabling "Assignment required" does not retroactively remove already-authenticated users — a provisioning sync must be triggered
- Users added without provisioning cannot be removed by just deleting them from Twingate; the remove-then-add workaround via Entra ID is required
- This misconfiguration can occur even before provisioning/SCIM is set up at all

## Related Docs
- Twingate Entra ID integration setup
- Entra ID SCIM provisioning configuration
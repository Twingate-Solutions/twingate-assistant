---
source: https://help.twingate.com/articles/4707021810-entra-id-all-users-are-able-to-log-into-twingate-even-though-they-are-not-assigned
type: help
fetched: 2026-10-04
source_version: 5095291310591e0ea69d40ca3fa758675993a0623a151fff589955b60cc2ed94
trust: official
---

# [Entra ID] All Users Able to Log Into Twingate Despite Not Being Assigned

## Summary
When Entra ID's "Assignment required" option is set to "No," any user in the tenant can authenticate to Twingate regardless of group sync status. This creates orphaned users in Twingate that cannot be cleanly removed without additional steps.

## Key Information
- The root cause is the **"Assignment required"** toggle in the Entra ID Enterprise Application settings
- Default or misconfigured value of `No` allows unrestricted tenant-wide login
- Affected users become "stuck" in Twingate — no automatic removal mechanism triggers for them
- Provisioning (SCIM sync) must also be scoped correctly to enforce user removal

## Prerequisites
- Admin access to Entra ID (Microsoft Entra / Azure AD)
- Twingate Enterprise Application configured in Entra ID
- Provisioning (SCIM) set up or being set up in Entra ID

## Step-by-Step Resolution

1. **Navigate** to the Twingate Enterprise Application in Entra ID
2. **Set** "Assignment required" → `Yes` under Properties
3. **Go to** Provisioning settings for the Twingate app
4. **Set Scope** to `Sync only assigned users and groups`
5. **Run** a Provisioning cycle to deprovision users not in assigned groups

### Removing Manually-Added Stuck Users
If users were already added to Twingate outside of provisioning:
1. **Assign** the stuck user to the Twingate Enterprise Application in Entra ID
2. **Remove** that user from the application
3. This triggers the SCIM removal event, deleting the user from Twingate

## Configuration Values

| Setting | Location | Correct Value |
|---|---|---|
| Assignment required | Entra ID → Enterprise Apps → Twingate → Properties | `Yes` |
| Provisioning Scope | Entra ID → Enterprise Apps → Twingate → Provisioning | `Sync only assigned users and groups` |

## Gotchas
- Simply setting "Assignment required" to `Yes` is **not sufficient alone** — a provisioning sync must run with correct scope to clean up existing unauthorized users
- Users added outside of SCIM provisioning require the manual assign-then-remove workaround to trigger deletion
- If provisioning was never configured, unauthorized logins can occur even before any sync runs

## Related Docs
- [Twingate Entra ID Integration](https://help.twingate.com)
- Microsoft Entra ID: Enterprise Application Assignment Settings
- Microsoft Entra ID: Configure SCIM Provisioning Scope
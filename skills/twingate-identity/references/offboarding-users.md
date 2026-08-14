---
source: https://www.twingate.com/docs/offboarding-users
type: docs
fetched: 2026-08-14
source_version: 7d9d31482b92c43f09edfd15e5b6527e8d5f2ff5aa47306da26f3969e1707e04
---

# Offboarding Users

## Summary
Covers two offboarding scenarios: social login users (managed directly in Twingate Admin Console) and enterprise IdP users (managed in IdP with Twingate sync). Immediate access revocation requires blocking devices in the Admin Console regardless of scenario.

## Key Information
- **Disabled users**: Cannot log in, account data retained, still count toward billable users
- **Deleted users**: Account permanently removed, no longer count toward billable users
- **IdP sync**: Changes propagate automatically but with potential delay — device blocking provides immediate revocation
- **Device blocking**: Prevents resource access immediately; device remains blocked until manually unblocked

## Prerequisites
- Admin Console access with administrative credentials
- For IdP scenario: admin access to enterprise IdP (Okta, Entra ID, etc.)

## Step-by-Step

### Scenario 1: Social Logins (Microsoft, Google, LinkedIn, GitHub)
1. Log in to Twingate Admin Console
2. Navigate to **Teams** page
3. Locate the target user
4. Select **Disable** or **Delete**
5. Confirm the action

### Scenario 2: Enterprise IdP (Okta, Entra ID, etc.)
1. Log in to enterprise IdP
2. **Full offboard**: Disable or delete user account in IdP
   **Access removal only**: Remove user from groups synced to Twingate
3. Changes auto-sync to Twingate (delay possible)
4. For immediate revocation: log in to Admin Console → **Devices** → block user's device(s)

## Gotchas
- Disabled accounts still count as billable users — delete if billing reduction is needed
- IdP sync delay means a window of potential access remains after IdP-side changes; always block devices for immediate effect
- Device block must be manually reversed to restore access
- Removing a user from synced groups (not deleting them) only removes Twingate access, not the broader IdP account

## Related Docs
- Device management (Admin Console Devices section)
- IdP integration guides (Okta, Entra ID)
- Teams/user management in Admin Console
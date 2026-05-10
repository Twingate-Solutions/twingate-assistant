# Offboarding Users – Twingate

## Summary
Covers two offboarding scenarios: social login users (managed directly in Twingate Admin Console) and enterprise IdP users (managed via IdP with Twingate sync). Immediate device blocking in the Admin Console is recommended to bypass sync delays.

## Key Information
- **Disabled users**: Cannot log in, account data retained, still count toward billable users
- **Deleted users**: Account permanently removed, no longer billable
- **IdP sync**: Changes propagate automatically but may have delays depending on IdP configuration
- **Device blocking**: Immediately revokes access regardless of IdP sync status; device cannot access any Resources until unblocked

## Prerequisites
- Admin Console access with administrative credentials
- For IdP scenario: admin access to enterprise IdP (Okta, Entra ID, etc.)

## Step-by-Step

### Scenario 1: Social Logins (Microsoft, Google, LinkedIn, GitHub)
1. Log in to Twingate Admin Console
2. Navigate to **Teams** page
3. Locate the target user
4. Select **Disable** (retains data, remains billable) or **Delete** (permanent removal, not billable)
5. Confirm the action

### Scenario 2: Enterprise IdP (Okta, Entra ID, etc.)
1. Log in to your IdP
2. **Full offboard**: Disable or delete the user's IdP account
   **Access removal only**: Remove user from groups synced to Twingate
3. Wait for sync propagation to Twingate
4. **Recommended – immediate revocation**: Log in to Twingate Admin Console → navigate to **Devices** → block the user's device(s)

## Configuration Values
- No specific env vars or API parameters documented on this page
- Sync delay varies by IdP and its settings

## Gotchas
- Disabled users **still count as billable**; delete if seat reduction is needed
- IdP sync is **not immediate** — always block devices in Admin Console for time-sensitive offboarding
- Removing a user from a synced group (not deleting the IdP account) is sufficient if only Twingate access needs to be revoked
- Blocked devices remain blocked until manually unblocked — verify before re-onboarding

## Related Docs
- Twingate Admin Console – Teams page
- Twingate Admin Console – Devices page
- IdP integration guides (Okta, Entra ID)
- Billable user management
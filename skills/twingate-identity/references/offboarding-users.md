# How to Offboard Users from Twingate

## Summary
Covers two offboarding scenarios: social login users (managed directly in Twingate Admin Console) and enterprise IdP users (managed in IdP with Twingate sync). Blocking devices in the Admin Console provides immediate access revocation regardless of IdP sync delays.

## Key Information
- Disabled users cannot log in but account data is retained and they **still count toward billable users**
- Deleted users are permanently removed and **no longer count toward billable users**
- IdP sync changes may have delays; device blocking provides immediate revocation
- Blocked devices cannot access any Resources until explicitly unblocked

## Prerequisites
- Admin access to Twingate Admin Console
- For IdP scenario: admin access to enterprise IdP (Okta, Entra ID, etc.)

## Step-by-Step

### Scenario 1: Social Logins (Microsoft, Google, LinkedIn, GitHub)
1. Log in to Twingate Admin Console
2. Navigate to **Teams** page
3. Locate the target user
4. Select **Disable** (retains data, keeps billable seat) or **Delete** (permanent removal, frees billable seat)
5. Confirm the action

### Scenario 2: Enterprise IdP (Okta, Entra ID, etc.)
1. Log in to your IdP
2. **Full offboard**: Disable or delete user account in IdP → changes auto-sync to Twingate
   **Access-only removal**: Remove user from groups synced to Twingate
3. For immediate revocation (don't wait for sync):
   - Log in to Twingate Admin Console
   - Navigate to **Devices** section
   - Block the user's device(s)

## Gotchas
- **Sync delay risk**: IdP changes are not instant in Twingate; always block devices manually for immediate access revocation
- **Billing**: Disabled users still consume billable seats — delete if seat reclamation is needed
- **Device blocking is additive**: Even after IdP sync completes, blocked devices remain blocked until manually unblocked
- **Group-based access**: If using IdP groups, removing from all synced groups removes Twingate access without deleting the IdP account

## Configuration Values
| Action | Location | Effect |
|--------|----------|--------|
| Disable user | Admin Console → Teams | Blocks login, retains data, billable |
| Delete user | Admin Console → Teams | Permanent removal, not billable |
| Block device | Admin Console → Devices | Immediate Resource access revocation |

## Related Docs
- Identity Provider integration guides (Okta, Entra ID)
- Device management in Twingate
- User synchronization / SCIM provisioning
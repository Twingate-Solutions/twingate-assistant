# How to Offboard Users

## Summary
Covers best practices for removing user access from Twingate across two scenarios: social login users and enterprise IdP-integrated users. Proper offboarding ensures immediate access revocation and prevents unauthorized resource access.

## Key Information
- Two distinct offboarding paths depending on authentication method
- Disabled users retain account data and **continue counting toward billable users**
- Deleted users are permanently removed and no longer billed
- IdP sync may have delays — device blocking provides immediate revocation
- Blocked devices cannot access any Resources until explicitly unblocked

## Prerequisites
- Admin Console access with administrative credentials
- For IdP scenario: admin access to enterprise IdP (Okta, Entra ID, etc.)

---

## Step-by-Step

### Scenario 1: Social Logins (Google, Microsoft, LinkedIn, GitHub)
1. Log in to Twingate Admin Console
2. Navigate to **Teams** page
3. Locate the target user
4. Select **Disable** (retains account, blocks login) or **Delete** (permanent removal)
5. Confirm the action

### Scenario 2: Enterprise IdP (Okta, Entra ID, etc.)
1. Log in to your IdP
2. Choose one:
   - **Full offboard**: Disable or delete user account in IdP → syncs to Twingate automatically
   - **Twingate-only removal**: Remove user from groups synced to Twingate
3. **For immediate revocation** (don't wait for sync):
   - Log in to Twingate Admin Console
   - Navigate to **Devices** section
   - Block the user's device(s)

---

## Configuration Values
| Action | Effect | Billable |
|--------|--------|----------|
| Disable user | Blocks login, retains data | Yes |
| Delete user | Permanent removal | No |
| Block device | Immediate access revocation | N/A |

---

## Gotchas
- **Billing**: Disabled users still count as billable — delete to stop billing
- **IdP sync delay**: Disabling in IdP does not immediately revoke access in Twingate; always block devices manually for time-sensitive offboarding
- **Scope difference**: Removing from synced groups only removes Twingate access; full IdP disable/delete removes all org access
- Device blocking is reversible; deletion is not

## Related Docs
- User management / Teams page
- Device management
- IdP integration (Okta, Entra ID)
- Billing and user counts
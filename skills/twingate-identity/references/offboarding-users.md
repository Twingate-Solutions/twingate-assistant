# Offboarding Users | Twingate

## Summary
Covers two offboarding scenarios: social login users (managed directly in Twingate Admin Console) and enterprise IdP users (managed in IdP with Twingate sync). Immediate access revocation for IdP users requires blocking devices directly in the Admin Console to bypass sync delays.

## Key Information
- **Disabled users**: Cannot log in, account data retained, **still count toward billable users**
- **Deleted users**: Account permanently removed, no longer count toward billable users
- **IdP sync**: Changes may have delays depending on IdP configuration
- **Device blocking**: Immediately revokes all Resource access regardless of IdP sync status

## Prerequisites
- Admin Console access with administrative credentials
- For IdP scenario: access to enterprise IdP admin panel

---

## Scenario 1: Social Login Offboarding (Microsoft, Google, LinkedIn, GitHub)

1. Log in to Twingate Admin Console
2. Navigate to **Teams** page
3. Locate the target user
4. Select **Disable** or **Delete**
5. Confirm the action

---

## Scenario 2: Enterprise IdP Offboarding (Okta, Entra ID, etc.)

**Full offboard:**
1. Log in to enterprise IdP
2. Disable or delete user account in IdP
3. Changes sync automatically to Twingate

**Remove Twingate access only:**
1. Remove user from any groups synced to Twingate

**Ensure immediate revocation (both cases):**
1. Log in to Twingate Admin Console
2. Navigate to **Devices** section
3. Block the user's device(s)

---

## Gotchas
- Disabled ≠ Deleted — disabled users still consume billable seats
- IdP sync is **not immediate**; always block devices in Admin Console for instant revocation
- Blocked devices cannot access any Resources until manually unblocked
- Removing a user from synced groups only removes Twingate access, not full IdP account

## Related Docs
- User Management / Teams
- Device Management
- IdP Integration (Okta, Entra ID)
- Billing / User Seats
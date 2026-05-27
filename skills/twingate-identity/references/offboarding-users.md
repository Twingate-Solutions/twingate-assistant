# Offboarding Users – Twingate

## Summary
Covers two offboarding scenarios: social login users (managed directly in Twingate Admin Console) and enterprise IdP users (managed in IdP with Twingate sync). For immediate access revocation in IdP scenarios, blocking devices in the Admin Console is recommended to bypass sync delays.

## Key Information
- Two distinct workflows depending on identity source (social login vs. enterprise IdP)
- Disabled users retain account data and **count toward billable users**
- Deleted users are permanently removed and **do not count toward billable users**
- IdP sync may have delays; device blocking provides immediate revocation
- Blocked devices cannot access any Resources until manually unblocked

## Prerequisites
- Admin Console access with administrative credentials
- For IdP scenario: admin access to the enterprise identity provider (Okta, Entra ID, etc.)

## Step-by-Step

### Scenario 1: Social Logins (Microsoft, Google, LinkedIn, GitHub)
1. Log in to Twingate Admin Console
2. Navigate to **Teams** page
3. Locate the target user
4. Select **Disable** (retains data, still billable) or **Delete** (permanent removal, not billable)
5. Confirm the action

### Scenario 2: Enterprise IdP (Okta, Entra ID, etc.)
**Full offboard:**
1. Log in to enterprise IdP
2. Disable or delete the user account in the IdP
3. Changes sync automatically to Twingate

**Remove Twingate access only:**
1. Log in to enterprise IdP
2. Remove user from any groups synced to Twingate
3. Changes sync automatically to Twingate

**For immediate revocation (both cases):**
1. Log in to Twingate Admin Console
2. Navigate to **Devices** section
3. Block the user's device(s)

## Configuration Values
None (UI-based workflow only)

## Gotchas
- **Sync delay**: IdP changes are not instant in Twingate; always block devices in the console if immediate revocation is required
- **Billing**: Disabled users still consume a billable seat; delete if the account is no longer needed
- **Device blocking is independent**: Blocking a device in the console works immediately regardless of IdP sync status
- Deleted user data is **permanently removed**; no recovery path documented

## Related Docs
- Twingate Teams/Users management
- Device management in Admin Console
- IdP integration guides (Okta, Entra ID)
- Group sync configuration
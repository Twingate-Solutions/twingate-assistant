# Offboarding Users - Twingate

## Summary
Covers two offboarding scenarios: social login users (managed directly in Twingate Admin Console) and enterprise IdP users (managed in IdP with Twingate sync). Immediate access revocation for IdP users requires blocking devices directly in Twingate Admin Console due to sync delays.

## Key Information
- Disabled users **cannot log in** but account data is retained and they **still count toward billable users**
- Deleted users have account data **permanently removed** and **do not count toward billable users**
- IdP sync changes may have delays depending on IdP configuration
- Blocking a device in Twingate immediately revokes all Resource access regardless of IdP sync status

## Prerequisites
- Admin access to Twingate Admin Console
- For IdP scenario: Admin access to enterprise IdP (Okta, Entra ID, etc.)

## Step-by-Step

### Scenario 1: Social Logins (Microsoft, Google, LinkedIn, GitHub)
1. Log in to Twingate Admin Console
2. Navigate to **Teams** page
3. Locate the target user
4. Select **Disable** (retains account, blocks login) or **Delete** (permanently removes account)
5. Confirm the action

### Scenario 2: Enterprise IdP (Okta, Entra ID, etc.)
1. Log in to your IdP
2. **Full offboarding**: Disable or delete user account in IdP → syncs to Twingate automatically
3. **Twingate-only removal**: Remove user from groups synced to Twingate → syncs automatically
4. **For immediate revocation**: Log in to Twingate Admin Console → navigate to **Devices** → block the user's device(s)

## Configuration Values
- N/A — actions performed via UI only

## Gotchas
- **Billing**: Disabled users still count as billable; delete if you want to remove from billing
- **Sync delay**: IdP changes are not instant — always block the device in Twingate for immediate revocation
- **Device blocking is independent**: A blocked device cannot access any Resources until explicitly unblocked, even if the user account is later re-enabled in the IdP
- Deleting a user is **permanent** — no recovery of account data

## Related Docs
- Twingate Teams/Users management
- Device management in Admin Console
- IdP integration guides (Okta, Entra ID)
- SCIM provisioning/sync configuration
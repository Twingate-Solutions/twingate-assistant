---
source: https://www.twingate.com/docs/offboarding-users
type: docs
fetched: 2026-10-04
source_version: b3f4fb7b018631c5cebe7416849de79bc1280aa02448c0a88a47b505377eb2d2
trust: official
---

# How to Offboard Users

## Summary
Covers two offboarding scenarios: social login users (managed directly in Twingate Admin Console) and enterprise IdP users (managed in IdP with Twingate sync). For immediate access revocation with IdP users, blocking devices in the Admin Console is recommended to bypass sync delays.

## Key Information
- **Disabled users**: Cannot log in, account info retained, still count toward billable users
- **Deleted users**: Account permanently removed, no longer count toward billable users
- **IdP sync**: Changes made in IdP propagate to Twingate automatically but with possible delay
- **Device blocking**: Immediate revocation regardless of IdP sync status; device cannot access any Resources until unblocked

## Prerequisites
- Admin Console access with administrative credentials
- For IdP scenario: admin access to the enterprise identity provider (Okta, Entra ID, etc.)

## Step-by-Step

### Scenario 1: Social Logins (Microsoft, Google, LinkedIn, GitHub)
1. Log in to Twingate Admin Console
2. Navigate to **Teams** page
3. Locate the target user
4. Select **Disable** (retains data, keeps billing) or **Delete** (permanent removal, stops billing)
5. Confirm the action

### Scenario 2: Enterprise IdP (Okta, Entra ID, etc.)
**Full offboarding:**
1. Log in to the enterprise IdP
2. Disable or delete the user's account in the IdP
3. Changes sync automatically to Twingate (delay may occur)

**Access-only removal (keep IdP account):**
1. Remove user from any groups synced to Twingate in the IdP

**For immediate revocation (recommended in both cases):**
1. Log in to Twingate Admin Console
2. Navigate to **Devices** section
3. Block the user's device(s)

## Configuration Values
- No CLI flags or API parameters documented on this page
- Sync delay varies by IdP and its configuration settings

## Gotchas
- **Billing**: Disabled users still count as billable; delete to stop billing
- **IdP sync delay**: Do not rely solely on IdP changes for immediate access revocation — block devices in Admin Console as a failsafe
- **Group-based sync**: If using group sync, removing a user from synced groups (rather than deleting the IdP account) is sufficient to revoke Twingate access
- Blocked devices remain blocked until manually unblocked — verify intent before blocking

## Related Docs
- Twingate Teams/Users management
- Device management in Admin Console
- IdP integration setup (Okta, Entra ID)
- Group synchronization configuration
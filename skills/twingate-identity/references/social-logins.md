---
source: https://www.twingate.com/docs/social-logins
type: docs
fetched: 2026-08-14
source_version: 8f9bb6d387f017daa4b134ae39686ce5997628f01a30cf7efc2f3f970db2075c
---

# Social Logins

## Summary
Twingate supports social identity providers as an alternative when no third-party IdP is available. Users authenticate via social accounts where the email must match their Twingate account email. Admins manage users through the Admin Console Team page.

## Key Information
- **Supported providers:** Google, Microsoft, LinkedIn, GitHub
- Email address from social provider **must match** the email registered in Twingate
- Users must accept invite email before first sign-in
- Disabled users **are still billed**

## Prerequisites
- Admin access to Twingate Admin Console
- User's email address for invitation

## Step-by-Step

### Inviting Users
1. Navigate to Admin Console → Team page → Users tab
2. Click **Add User**
3. Enter user's email address
4. Click **Send Invite Email**
5. User accepts invite via email, then downloads Client and logs in

### Managing Users
1. Navigate to Admin Console → Team page
2. Click the **three dots** (⋮) on the user's record
3. Select action:
   - **Edit** – Update display name
   - **Manage Role** – Change user role
   - **Disable** – Temporarily block login (user remains billable)
   - **Remove** – Permanently delete user

## Gotchas
- Social account email **must exactly match** the Twingate-registered email — mismatches prevent login
- Disabled users still count toward billing
- Users cannot log in until they accept the invite email

## Related Docs
- Admins guide (Role management)
- Offboarding Users
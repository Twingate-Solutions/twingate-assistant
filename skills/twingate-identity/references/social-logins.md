# Social Logins

## Summary
Twingate supports social identity providers as an alternative when no third-party IdP is available. Users authenticate via social accounts where the email must match the Twingate account email. Admins manage users through the Team page in the Admin Console.

## Key Information
- Four supported social providers: **Google, Microsoft, LinkedIn, GitHub**
- Email address from social provider must exactly match the user's Twingate account email
- Users must accept invite email before first sign-in
- Disabled users are still billed

## Prerequisites
- Admin access to Twingate Admin Console
- User's email address for invitation

## Step-by-Step: Inviting Users
1. Navigate to **Admin Console → Team → Users tab**
2. Click **"Add User"**
3. Enter the user's email address
4. Click **"Send Invite Email"**
5. User must accept invite via email before first login

## Step-by-Step: Managing Users
1. Navigate to **Admin Console → Team → Users tab**
2. Click the **three-dot menu** on the user's record
3. Select action:
   - **Edit** – update display name
   - **Manage Role** – change user role
   - **Disable** – temporarily block login (user remains billable)
   - **Remove** – permanently delete user

## Configuration Values
None (UI-only configuration, no env vars or API params documented on this page)

## Gotchas
- Disabled users **continue to incur billing charges** — use Remove to stop billing
- Social account email must **exactly match** the Twingate account email; mismatches will prevent login
- Invitees cannot log in until they **accept the invite email**

## Related Docs
- Admins Guide (Role management)
- Offboarding Users
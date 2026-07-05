# Social Logins

## Summary
Twingate supports social identity providers as an alternative to third-party IdPs. Users authenticate via social accounts where the email must match their Twingate account email. Admins manage all user lifecycle operations through the Admin Console Team page.

## Key Information
- **Supported providers:** Google, Microsoft, LinkedIn, GitHub
- Email address on social account **must match** the email address registered in Twingate
- No third-party IdP configuration required
- Disabled users **still count toward billing**

## Prerequisites
- Admin access to Twingate Admin Console
- User's email address for invitation

## Step-by-Step: Inviting Users
1. Navigate to Admin Console → Team → Users tab
2. Click **Add User**
3. Enter the user's email address
4. Click **Send Invite Email**
5. User must accept the invite via email before first sign-in

## Step-by-Step: Managing Users
1. Navigate to Admin Console → Team page
2. Click the **three-dot menu** on the right side of a user record
3. Select action:
   - **Edit** — update display name
   - **Manage Role** — change user role
   - **Disable** — temporarily block login (user remains billable)
   - **Remove** — permanently delete user

## Configuration Values
None (UI-only configuration, no env vars or API params documented on this page)

## Gotchas
- Disabled users are still billed — use **Remove** to stop billing for a user
- Users must accept the invite email before they can log in for the first time
- Social account email must exactly match the Twingate-registered email; mismatches will block login

## Related Docs
- [Admins Guide](https://www.twingate.com/docs/) — role management details
- [Offboarding Users](https://www.twingate.com/docs/) — full offboarding process for social users
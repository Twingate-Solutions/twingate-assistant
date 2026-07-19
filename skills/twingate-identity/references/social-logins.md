# Social Logins

## Summary
Twingate supports social identity providers as an alternative when no third-party IdP is available. Users authenticate via social accounts where the email must match their Twingate account email. Admins manage users through the Team page in the Admin Console.

## Key Information
- Four supported social login providers: **Google, Microsoft, LinkedIn, GitHub**
- Email address from social provider must match the email address in Twingate
- Users must accept invite email before first sign-in
- Disabled users still count toward billing

## Prerequisites
- Admin access to Twingate Admin Console
- User's email address to send invite

## Step-by-Step: Inviting Users
1. Navigate to **Team page → Users tab** in Admin Console
2. Click **"Add User"**
3. Enter the user's email address
4. Click **"Send Invite Email"**
5. User accepts invite via email, then downloads Client and logs in

## User Management Options
Access via three-dot menu on user record:

| Option | Action |
|--------|--------|
| Edit | Update display name |
| Manage Role | Change user role |
| Disable | Temporarily block login (user retained) |
| Remove | Permanently delete user |

## Gotchas
- **Disabled users are still billed** — removal is required to stop billing
- Users cannot sign in for the first time until invite email is accepted
- Social account email must exactly match the Twingate account email; mismatches will block login

## Related Docs
- Admins guide (role management)
- Offboarding Users page
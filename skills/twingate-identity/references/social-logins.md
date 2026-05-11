# Social Logins

## Summary
Twingate supports social identity providers as an alternative when no third-party IdP is available. Users authenticate via social accounts where the email must match the email registered in Twingate. Admins manage users through the Team page in the Admin Console.

## Key Information
- Four supported social providers: **Google, Microsoft, LinkedIn, GitHub**
- Email address from social account must exactly match the user's email in Twingate
- No external IdP required for this authentication method
- Users must accept invite email before first sign-in

## Prerequisites
- Admin access to Twingate Admin Console
- User's email address to send invite

## Step-by-Step: Inviting Users
1. Navigate to **Admin Console → Team → Users tab**
2. Click **"Add User"**
3. Enter user's email address
4. Click **"Send Invite Email"**
5. User accepts invite via email, then downloads Client and logs in

## User Management Options
Access via three-dot menu on any user record:

| Option | Action |
|--------|--------|
| Edit | Update display name |
| Manage Role | Change user role |
| Disable | Temporarily block login (user retained) |
| Remove | Permanently delete user |

## Configuration Values
- No environment variables or API parameters specific to social logins
- Role assignment options documented in the Admins guide

## Gotchas
- **Disabled users are still billed** — disabling does not remove them from billing
- Social account email must **exactly match** the Twingate-registered email; mismatches will prevent login
- Invitees cannot sign in until they accept the invite email

## Related Docs
- Admins Guide (Role management)
- Offboarding Users page
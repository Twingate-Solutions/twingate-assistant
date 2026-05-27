# Social Logins

## Summary
Twingate supports social identity providers as an alternative when no third-party IdP is available. Users authenticate via social accounts where the email must match their Twingate account email. Admins manage users through the Team page in the Admin Console.

## Key Information
- Four supported social login providers: **Google, Microsoft, LinkedIn, GitHub**
- User's social account email must exactly match the email address registered in Twingate
- New users must accept invite via email before first sign-in
- User management handled via Admin Console → Team page → Users tab

## Prerequisites
- Admin access to Twingate Admin Console
- User's email address for invitation

## Step-by-Step: Inviting Users
1. Navigate to Admin Console → Team page → Users tab
2. Click **Add User**
3. Enter the user's email address
4. Click **Send Invite Email**
5. User receives email with Client download link and must accept invite before first login

## User Management Options
Access via three-dot menu on any user record:

| Option | Action |
|--------|--------|
| Edit | Update display name |
| Manage Role | Change user role |
| Disable | Temporarily block login (user retained) |
| Remove | Permanently delete user |

## Configuration Values
- No env vars or API params specific to social logins
- Role assignment available during management (see Admins guide for role definitions)

## Gotchas
- **Disabled users are still billed** — disabling does not remove the user from billing
- Email address matching is required — social account email must match Twingate account email exactly
- Invitees must accept the email invite before they can sign in for the first time
- Social logins are intended for environments **without** a third-party IdP; if you have an IdP, use that instead

## Related Docs
- Admins Guide (Role management)
- Offboarding Users
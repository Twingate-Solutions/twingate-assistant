# Social Logins

## Summary
Twingate supports social identity providers as an alternative when no third-party IdP is available. Users authenticate via social accounts where the email must match their Twingate account email. Admins manage users through the Team page in the Admin Console.

## Key Information
- **Supported providers**: Google, Microsoft, LinkedIn, GitHub
- Email address on social account **must match** the email address registered in Twingate
- Invitees must accept the invite email before first sign-in
- Disabled users **are still billed**

## Prerequisites
- Admin access to Twingate Admin Console
- No third-party IdP required (social login is the fallback option)

## Step-by-Step: Inviting Users
1. Navigate to Admin Console → Team page → Users tab
2. Click **Add User**
3. Enter the user's email address
4. Click **Send Invite Email**
5. User receives email with Client download link and must accept invite before logging in

## User Management Options
Access via the three-dot menu on a user's record:

| Option | Action |
|--------|--------|
| Edit | Update display name |
| Manage Role | Change user role |
| Disable | Temporarily block login (user remains, still billed) |
| Remove | Permanently delete user |

## Configuration Values
- No environment variables or API parameters specific to social login configuration
- Role management referenced in Admins guide (separate doc)

## Gotchas
- **Billing**: Disabled users count toward billing — use **Remove** to stop billing for a user
- **Email matching**: Social account email must exactly match the Twingate-registered email; mismatches prevent login
- Users cannot log in until they accept the invite email (pending state)

## Related Docs
- Admins guide (Role management)
- Offboarding Users page
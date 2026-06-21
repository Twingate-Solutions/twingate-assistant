# Twingate Admins

## Summary
Twingate supports four admin roles with varying levels of Admin Console access. Admin roles are assigned per-user via the Admin Console and count toward license usage like standard users.

## Key Information
- Network creator is the only admin by default
- All admin users consume a license seat
- Four distinct roles with different permission scopes
- Role badge displayed in UI for non-Admin roles (DevOps, Support, Access Reviewer)
- Blocked actions show an error message inline

## Role Permissions Matrix

| Role | Write Access | Read Access |
|------|-------------|-------------|
| **Admin** | Entire Admin Console | Entire Admin Console |
| **DevOps** | Network tab only (Resources, Connectors, Remote Networks, Groups on Resources, Access Requests) | All tabs except Secure DNS and Client Configuration (Internet Security) |
| **Support** | None | Entire Admin Console |
| **Access Reviewer** | Access Requests page only | Access Requests page only |

## Prerequisites
- Must have Admin role to assign roles to other users
- Users must exist in the system before role assignment

## Step-by-Step: Assigning an Admin Role
1. Navigate to **Users** tab in Admin Console
2. Click the target user's name
3. Select **Manage**
4. Select **Manage Role**
5. Choose the desired role

## Accessing the Admin Console
- URL: `https://<your-subdomain>.twingate.com`
- Authentication: configured email + identity provider or supported social identity

## Gotchas
- DevOps admins **cannot** access Secure DNS or Client Configuration sections under Internet Security
- Access Reviewer role has very limited scope — read access restricted to Access Requests page only (not full console)
- Attempting unauthorized edits shows an error but does not log out or escalate — simply blocked inline
- No guest/read-only role with full console read that doesn't consume a license; Support role fills that function but still uses a seat

## Related Docs
- Users tab management
- Access Requests
- Internet Security (Secure DNS, Client Configuration)
- Remote Networks, Connectors, Resources configuration
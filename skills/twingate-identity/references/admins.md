# Twingate Admins

## Summary
Twingate supports four admin roles with varying levels of access to the Admin Console. The network creator is the default admin; additional admins must be manually assigned. Role assignment is done per-user through the Admin Console UI.

## Key Information

- Four admin roles available: **Admin**, **DevOps**, **Support**, **Access Reviewer**
- Network creator is the only admin by default
- All non-Admin roles have full read access to the Admin Console
- Role badge displayed in UI for DevOps, Support, and Access Reviewer users
- Unauthorized edit attempts show an error message and are blocked

## Role Permissions Matrix

| Role | Write Access | Read Access |
|------|-------------|-------------|
| Admin | Entire Admin Console | Entire Admin Console |
| DevOps | Network tab only (Resources, Connectors, Remote Networks, Groups on Resources, Request Access) | Entire Admin Console |
| Support | None | Entire Admin Console |
| Access Reviewer | Request Access page only | Entire Admin Console |

## Prerequisites

- Must have Admin role to assign roles to other users
- Users must exist in the Twingate network before role assignment

## Step-by-Step: Assigning an Admin Role

1. Log in to Admin Console at `https://your-subdomain.twingate.com`
2. Navigate to **Users** tab
3. Click the target user's name
4. Click **Manage**
5. Select **Manage Role**
6. Choose the desired role

## Configuration Values

- Admin Console URL: `https://your-subdomain.twingate.com`
- Authentication: configured email + identity provider or supported social identities

## Gotchas

- Only **Admin** role has write access outside the Network tab — DevOps cannot modify user settings, billing, or security policies
- **Access Reviewer** write access is limited solely to the Request Access page
- Role restrictions are enforced server-side; blocked actions display an error message
- No CLI or API method mentioned for role assignment — UI only

## Related Docs

- Users tab documentation
- Request Access management
- Identity provider configuration
- Remote Networks and Connectors setup
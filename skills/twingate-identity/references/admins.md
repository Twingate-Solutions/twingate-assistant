# Twingate Admins

## Summary
Twingate supports four admin roles with varying levels of read/write access to the Admin Console. The network creator is the only admin by default; additional admins must be manually designated. Role assignment is done per-user through the Admin Console.

## Key Information
- Four admin roles available: **Admin**, **DevOps**, **Support**, **Access Reviewer**
- All roles have full **read** access to the entire Admin Console
- Write access varies by role (see table below)
- Non-Admin roles display a badge next to the Twingate logo indicating their role

## Role Permissions Table

| Role | Write Access | Read Access |
|------|-------------|-------------|
| Admin | Entire Admin Console | Entire Admin Console |
| DevOps | Network tab only (Resources, Connectors, Remote Networks, Groups on Resources, Request Access) | Entire Admin Console |
| Support | None | Entire Admin Console |
| Access Reviewer | Request Access page only | Entire Admin Console |

## Prerequisites
- Must have Admin role to assign roles to other users
- Users must exist in the Twingate network before roles can be assigned

## Step-by-Step: Assigning an Admin Role
1. Log in to Admin Console at `https://your-subdomain.twingate.com`
2. Navigate to the **Users** tab
3. Click on the target user's name
4. Click **Manage**
5. Select **Manage Role**
6. Select the desired role

## Accessing the Admin Console
- URL: `https://your-subdomain.twingate.com`
- Authentication: configured email + identity provider or supported social identity

## Gotchas
- Only the network creator has Admin access by default — additional admins must be explicitly assigned
- DevOps, Support, and Access Reviewer admins attempting unauthorized edits will receive an error message and be blocked
- Hover over the role badge in the console to see detailed access level information

## Related Docs
- Users tab management
- Request Access configuration
- Remote Networks, Connectors, Resources setup (relevant to DevOps role scope)
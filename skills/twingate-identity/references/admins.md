# Twingate Admins

## Summary
Twingate supports four admin roles with varying levels of Admin Console access. The network creator is the default admin; additional admins must be manually designated. Role assignment is managed through the Admin Console user detail view.

## Key Information

- Four admin roles available: **Admin**, **DevOps**, **Support**, **Access Reviewer**
- All non-Admin roles have full **read** access to the entire Admin Console
- Write access is restricted by role

## Role Permissions Matrix

| Role | Write Access | Read Access |
|------|-------------|-------------|
| Admin | Entire Admin Console | Entire Admin Console |
| DevOps | Network tab only (Resources, Connectors, Remote Networks, Groups on Resources, Request Access) | Entire Admin Console |
| Support | None | Entire Admin Console |
| Access Reviewer | Request Access page only | Entire Admin Console |

## Prerequisites

- Must have Admin role to assign roles to other users
- Users must already exist in the Twingate network

## Assigning Admin Roles (Step-by-Step)

1. Navigate to **Users** tab in Admin Console
2. Click the target user's name
3. Select **Manage**
4. Select **Manage Role**
5. Choose the desired role

## Accessing the Admin Console

- URL: `https://your-subdomain.twingate.com`
- Authentication: configured email + identity provider or supported social identities

## Gotchas

- Only the **network creator** is an admin by default — additional admins must be explicitly assigned
- DevOps, Support, and Access Reviewer roles display a **role badge** next to the Twingate logo in the console
- Attempting to edit settings outside a role's write permissions results in a **blocked action + error message** (no silent failures)
- DevOps write access is limited to the **Network tab only** — cannot modify user or team settings

## Related Docs

- Users tab management
- Request Access configuration
- Identity provider setup
- Groups and Resources management
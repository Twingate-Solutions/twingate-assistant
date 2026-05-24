# Twingate Admins

## Summary
Twingate supports four admin roles with varying levels of Admin Console access. The network creator is the only admin by default; additional admins must be manually assigned. Each role has defined write and read permissions scoped to specific console areas.

## Key Information

- **Four admin roles**: Admin, DevOps, Support, Access Reviewer
- All non-Admin roles have **full read access** to the entire Admin Console
- Write access is progressively restricted by role
- Role badge displays next to Twingate logo for non-Admin roles; hover for access details
- Attempting unauthorized edits shows a blocking error message

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

## Assigning a Role (Step-by-Step)

1. Navigate to the **Users** tab in the Admin Console
2. Click the target user's name
3. Click **Manage**
4. Select **Manage Role**
5. Choose the desired role

## Accessing the Admin Console

- URL: `https://your-subdomain.twingate.com`
- Authentication: configured email + identity provider or supported social identities for the network

## Gotchas

- Only **one admin** exists by default (network creator); additional admins require manual assignment
- DevOps admins can only write to the Network tab — all other tabs are read-only
- Support admins have **zero write capabilities** — read-only across entire console
- Blocked actions display an error message but do not explain what role is required

## Related Docs

- Users tab management
- Request Access configuration
- Remote Networks / Connectors setup
- Identity provider configuration
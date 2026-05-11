# Twingate Admins

## Summary
Twingate supports four admin roles with varying levels of console access. The network creator is the sole admin by default; additional admins must be manually assigned. Role assignments are managed through the Admin Console user detail view.

## Key Information

- **Four admin roles**: Admin, DevOps, Support, Access Reviewer
- Network creator is the only admin by default
- Non-Admin roles display a badge next to the Twingate logo in the console
- Unauthorized edit attempts show an error message and are blocked

## Role Permissions Matrix

| Role | Write Access | Read Access |
|------|-------------|-------------|
| **Admin** | Entire Admin Console | Entire Admin Console |
| **DevOps** | Network tab only (Resources, Connectors, Remote Networks, Groups on Resources, Request Access) | Entire Admin Console |
| **Support** | None | Entire Admin Console |
| **Access Reviewer** | Request Access page only | Entire Admin Console |

## Assigning Roles (Step-by-Step)

1. Log in to the Admin Console at `https://your-subdomain.twingate.com`
2. Navigate to the **Users** tab
3. Click the target user's name
4. Select **Manage**
5. Select **Manage Role**
6. Choose the desired role

## Accessing the Admin Console

- URL: `https://your-subdomain.twingate.com`
- Authentication: configured email + identity provider or supported social identities

## Gotchas

- Only the **Admin** role has full write access; all others have restricted or no write permissions
- DevOps admins can only write to the Network tab — they cannot modify user, billing, or security settings
- Support admins have **zero** write capabilities despite full read access
- Role badge hover reveals access level details for non-Admin roles

## Related Docs

- Users tab management
- Request Access configuration
- Remote Networks and Connectors setup
- Groups and Resources management
# Twingate Admins

## Summary
Twingate supports four admin roles with different permission levels in the Admin Console. The network creator is the sole admin by default; additional admins must be explicitly assigned. Each role has distinct read/write capabilities scoped to specific console sections.

## Key Information

- **Four admin roles**: Admin, DevOps, Support, Access Reviewer
- Network creator is the only admin by default
- Role badge appears next to Twingate logo for non-Admin roles (DevOps, Support, Access Reviewer)
- Unauthorized edit attempts are blocked with an error message

## Role Permissions Matrix

| Role | Write Access | Read Access |
|------|-------------|-------------|
| **Admin** | Entire Admin Console | Entire Admin Console |
| **DevOps** | Network tab only (Resources, Connectors, Remote Networks, Groups on Resources, Access Requests) | All tabs except Secure DNS and Client Configuration in Internet Security |
| **Support** | None | Entire Admin Console |
| **Access Reviewer** | Access Requests page only | Access Requests page only |

## Assigning Roles

1. Navigate to **Users** tab in Admin Console
2. Click on the target user's name
3. Select **Manage**
4. Select **Manage Role**
5. Choose the desired role

## Accessing the Admin Console

- URL: `https://your-subdomain.twingate.com`
- Authentication: configured email + identity provider or supported social identities

## Gotchas

- Only existing admins can assign/change admin roles — plan for at least two admins to avoid lockout scenarios
- DevOps admins cannot access **Secure DNS** or **Client Configuration** sections under Internet Security (read or write)
- Access Reviewer role is highly restricted — read access limited to Access Requests page only, unlike Support which can read the full console

## Related Docs
- Users tab management
- Access Requests
- Remote Networks / Connectors / Resources configuration
- Internet Security (Secure DNS, Client Configuration)
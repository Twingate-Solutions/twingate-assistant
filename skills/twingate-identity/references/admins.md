# Twingate Admins

## Summary
Twingate supports five admin roles with different access levels to the Admin Console. The network creator is the default admin; additional admins must be manually designated. All admin users consume a license seat.

## Key Information

- **5 admin roles**: Admin, DevOps, Support, Access Reviewer, Billing
- All admin users count toward license limits
- Role badge displayed next to Twingate logo for non-Admin roles
- Billing role only available on self-serve billing tenants (not invoice-billed, MSP portal, or MSP subtenants)

## Role Permissions Matrix

| Role | Write | Read |
|------|-------|------|
| **Admin** | Entire Admin Console | Entire Admin Console |
| **DevOps** | Network tab (Resources, Connectors, Remote Networks, Groups on Resources, Access Requests) | All tabs except Secure DNS and Client Configuration |
| **Support** | None | Entire Admin Console |
| **Access Reviewer** | Access Requests page only | Access Requests page only |
| **Billing** | Billing Settings (plan changes, payment) | Billing page only |

## Assigning Roles (Step-by-Step)

1. Navigate to **Users** tab in Admin Console
2. Click on the target user's name
3. Select **Manage**
4. Select **Manage Role**
5. Choose the desired role

## Accessing Admin Console

- **URL**: `https://your-subdomain.twingate.com`
- Authentication via configured email + identity provider or supported social identities

## Gotchas

- Only the **network creator** is admin by default — additional admins must be explicitly assigned
- DevOps, Support, and Access Reviewer admins are **blocked with an error** if they attempt unauthorized edits
- Billing role is **unavailable** for invoice-billed accounts, MSP portal tenants, and MSP subtenants
- Support role has **zero write access** — read-only across entire console

## Related Docs

- Access Requests
- Remote Networks
- Resources & Connectors
- Internet Security / Secure DNS
- Client Configuration
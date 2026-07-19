# Twingate Admins

## Summary
Twingate supports five admin roles with varying levels of Admin Console access. The network creator is the default admin; additional admins are assigned via the Admin Console. All admin users consume a license seat.

## Key Information

- **5 admin roles**: Admin, DevOps, Support, Access Reviewer, Billing
- All admin users count against your license quota
- Role badge displayed in console for non-Admin roles (DevOps, Support, Access Reviewer, Billing)
- Blocked actions show an error message when role lacks permission

## Role Permissions Matrix

| Role | Write | Read |
|------|-------|------|
| **Admin** | Entire Admin Console | Entire Admin Console |
| **DevOps** | Network tab only (Resources, Connectors, Remote Networks, Groups on Resources, Access Requests) | All tabs except Secure DNS and Client Configuration (Internet Security) |
| **Support** | None | Entire Admin Console |
| **Access Reviewer** | Access Requests page only | Access Requests page only |
| **Billing** | Billing Settings (plan changes, payment) | Billing page only |

## Prerequisites

- Existing Twingate network with Admin access
- Target user must already exist in the Users tab

## Step-by-Step: Assigning a Role

1. Navigate to the **Users** tab in the Admin Console
2. Click the target user's name
3. Select **Manage Role**
4. Choose the desired role

## Accessing the Admin Console

- URL: `https://your-subdomain.twingate.com`
- Authentication: configured email + identity provider or supported social identity

## Gotchas

- **Billing role availability**: Only on self-serve billing tenants. Not available for invoice-billed tenants, MSP portal tenants, or MSP subtenants.
- Attempting a restricted action displays an error but does not notify admins — blocked silently with UI message only.
- First network creator is the sole admin by default; no other admins exist until explicitly assigned.

## Related Docs

- Access Requests
- Internet Security (Secure DNS, Client Configuration)
- Users tab administration
- Billing/plan management
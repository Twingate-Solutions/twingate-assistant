---
source: https://www.twingate.com/docs/admins
type: docs
fetched: 2026-08-14
source_version: f43ba9b591508305201dad7d04ca3b9145c07993c90a24185e3a8850444ea18c
---

# Twingate Admin Roles

## Summary
Twingate supports six admin roles with varying levels of Admin Console access. The network creator is the sole admin by default; additional admins are assigned via the Admin Console. All admin users consume a license seat.

## Key Information

- **Six roles**: Admin, DevOps, Helpdesk, Support, Access Reviewer, Billing
- Admin Console URL: `https://your-subdomain.twingate.com`
- Role badge displayed in console for non-Admin roles; hover for access details
- Blocked actions show an error message inline

## Role Permissions Matrix

| Role | Write | Read |
|------|-------|------|
| **Admin** | Full console | Full console |
| **DevOps** | Resources, Connectors, Remote Networks, Group-to-Resource, Access Requests | All except Secure DNS, Client Configuration |
| **Helpdesk** | Reset MFA, verify/unverify devices & serial numbers, add/delete serial numbers | All except Secure DNS, Client Configuration, Billing |
| **Support** | None | Full console |
| **Access Reviewer** | Access Requests page only | Access Requests page only |
| **Billing** | Settings > Billing (plan changes, payment) | Billing page only |

## Prerequisites

- Must have Admin role to assign roles to other users
- Billing role requires self-serve Billing page (not available for invoice-billed tenants, MSP portal tenants, or MSP subtenants)

## Assigning Roles (Step-by-Step)

1. Navigate to the **Users** tab in the Admin Console
2. Click the target user's name
3. Select **Manage Role**
4. Choose the desired role

## Gotchas

- **Billing role unavailable** for invoice-billed accounts, MSP portals, and MSP subtenants
- Admin users **count against license quota** — plan accordingly
- DevOps and Helpdesk roles **cannot access** Internet Security > Secure DNS or Client Configuration
- Helpdesk role **cannot access** Settings > Billing
- Unauthorized edit attempts are blocked silently with an error message (no partial saves)

## Related Docs

- Access Requests management
- Internet Security / Secure DNS configuration
- Settings > Billing
- MSP portal administration
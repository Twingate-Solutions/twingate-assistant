---
source: https://www.twingate.com/docs/admins
type: docs
fetched: 2026-10-11
source_version: 703713f93caab5869f9763c39e90b9d620fdcc873dd31cc871fdccaa48e1aeaf
trust: official
---

# Twingate Admin Roles

## Summary
Twingate supports multiple admin roles with different read/write permissions in the Admin Console. The network creator is the only admin by default; additional admins must be manually assigned. All admin users count toward your license.

## Key Information

- **Default admin**: Only the network creator has admin rights initially
- **License impact**: Admin users consume licenses like regular users
- **Upcoming change**: Week of October 19, 2026 — "Support" role renamed to "Viewer"; Support and DevOps roles lose access to some pages

## Role Permissions Matrix

| Role | Write | Read Restrictions |
|------|-------|-------------------|
| **Admin** | Full console | None |
| **Support** | None | Full console |
| **DevOps** | Network tab (Resources, Connectors, Remote Networks, Groups on Resources, Access Requests) | No Internet Security > Secure DNS/Client Config |
| **Internet Security** | Internet Security tab only | No Settings > Billing |
| **Helpdesk** | Reset user MFA, verify/unverify devices & serial numbers, add/delete serial numbers | No Internet Security > Secure DNS/Client Config, no Settings > Billing |
| **Access Reviewer** | Access Requests page only | Access Requests page only |
| **Billing** | Settings > Billing (plan changes, payment) | Billing page only |

**Billing role caveat**: Only available on self-serve billing tenants. Not available for invoice-billed tenants, MSP portal tenants, or MSP subtenants.

## Assigning Admin Roles

1. Navigate to the **Users** tab in the Admin Console
2. Click the target user's name
3. Select **Manage Role**
4. Choose the desired role

## Accessing the Admin Console

- URL: `https://<your-subdomain>.twingate.com`
- Login uses configured email + your identity provider or supported social identity

## Gotchas

- Limited-role admins see a role badge next to the Twingate logo in the console
- Attempting a blocked action shows an explicit error message (no silent failure)
- DevOps and Support roles will lose access to additional pages after October 19, 2026 — audit role assignments before that date

## Related Docs

- Access Requests management
- Internet Security configuration
- Settings > Billing
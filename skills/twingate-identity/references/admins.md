---
source: https://www.twingate.com/docs/admins
type: docs
fetched: 2026-10-25
source_version: 82e1800bd019baf5702658bcd9d9e77a5c2e620ef0540f67894ab832e0fc463e
trust: official
---

# Twingate Admin Roles

## Summary
Twingate supports multiple admin roles with varying read/write permissions in the Admin Console. The network creator is the sole admin by default; additional admins must be manually designated. All admin users consume a license seat.

## Key Information
- Network creator = only default admin
- All admin users count toward license
- Limited-role admins see a role badge next to the Twingate logo
- Blocked actions display an error message in the Console
- **Billing role** only available on self-serve billing tenants (not invoice-billed, MSP portal, or MSP subtenants)

## Admin Role Permissions Matrix

| Role | Write | Read Restrictions |
|------|-------|-------------------|
| **Admin** | Entire console | None |
| **Viewer** (formerly Support) | None | No Secure DNS, Client Config, Billing |
| **DevOps** | Network tab only | No Secure DNS, Client Config, Billing |
| **Internet Security** | Internet Security tab only | No Billing |
| **Helpdesk** | Reset MFA, verify/unverify devices & serial numbers, add/delete serial numbers | No Secure DNS, Client Config, Billing |
| **Access Reviewer** | Access Requests page only | Access Requests page only |
| **Billing** | Settings > Billing only | Settings > Billing only |

## Assigning Roles
1. Navigate to the **Users** tab in Admin Console
2. Click the target user's name
3. Select **Manage Role**
4. Choose the desired role

## Accessing Admin Console
- URL: `https://<your-subdomain>.twingate.com`
- Auth: configured email + identity provider or supported social identity for the network

## Gotchas
- Viewer role was previously called "Support" — same permissions
- Helpdesk cannot access Secure DNS, Client Configuration, or Billing pages
- Billing role is unavailable on invoice-billed accounts and all MSP-related tenants
- Attempting unauthorized edits shows a blocking error (no silent failure)

## Related Docs
- Users tab management
- Internet Security configuration
- Settings > Billing
- Identity provider setup
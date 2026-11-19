---
source: https://www.twingate.com/docs/admins
type: docs
fetched: 2026-11-19
source_version: b47f7bfc2dfe3b0cb9e4eee2a09ed16f94a3b0fb889ee4cc10e2f4d183dfe760
trust: official
---

# Page Title
Admins (Twingate Docs)

## Summary
The user who creates a Twingate network is the only admin by default. Additional admins can be designated in the Admin Console, and each counts toward the license like any other user. Twingate offers several admin roles with different read/write permissions in the Admin Console.

## Key Information

Admin roles and permissions:

| Role | Write | Read |
|---|---|---|
| Admin | Entire Admin Console | Entire Admin Console |
| Viewer | None | All pages except Internet Security > Secure DNS, Internet Security > Client Configuration, Settings > Billing |
| DevOps | Network tab only | Same exclusions as Viewer |
| Internet Security | Internet Security tab only | All pages except Settings > Billing |
| Helpdesk | Reset user MFA; verify/unverify devices; verify/unverify serial numbers; add/delete serial numbers | Same exclusions as Viewer |
| Access Reviewer | Access Requests page only | Access Requests page only |
| Billing | Settings > Billing page only | Settings > Billing page only |

- Admins with a limited role see a role badge next to the Twingate logo in the Admin Console. Hovering over it shows the permissions.
- If a limited-role admin tries to edit a setting their role doesn't permit, the Admin Console blocks the change and shows an error.

## Prerequisites
- Existing Twingate network with an Admin-role user to assign roles.
- The target user must exist in the Users tab.

## Step-by-Step: Assigning a Role
1. Open the Admin Console and go to the **Users** tab.
2. Click the user's name.
3. Select **Manage Role**.
4. Choose the desired role.

## Accessing the Admin Console
- Log in at `https://your-subdomain.twingate.com`.
- Authenticate with the configured email address via the identity provider or supported social identities for your network.

## Configuration Values
- None (no env vars, CLI flags, or API parameters on this page). Role assignment is done through the Admin Console UI.

## Gotchas
- Admin users consume licenses.
- The **Billing** role is only available on tenants with a self-serve Billing page. It is not available for invoice-billed tenants, MSP portal tenants, or MSP subtenants.
- Only Admin has full write access. Viewer, DevOps, and Helpdesk cannot see Secure DNS or Client Configuration pages.
- Only the Internet Security role can read Secure DNS and Client Configuration besides Admin.
- Helpdesk write access is limited to MFA resets and device/serial number verification and management.

## Related Docs
- Admin Console, Users tab, and Settings > Billing documentation
- Identity provider and social login setup
- Device and serial number verification (Helpdesk tasks)
- Access Requests (Access Reviewer role)
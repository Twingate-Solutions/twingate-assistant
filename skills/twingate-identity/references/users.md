---
source: https://www.twingate.com/docs/users
type: docs
fetched: 2026-10-25
source_version: 1428ced0a8279380e598391727ce59d4c9f7ca45e318372a689426508aed8fa3
trust: official
---

# Twingate Users

## Summary
Twingate manages users via social logins or a synchronized IdP (SCIM). New users default to the "Everyone" group with no Resource access unless explicitly granted. Billing applies to all synchronized users and service accounts.

## Key Information
- **Default auth**: Social logins (Google, Microsoft, GitHub, LinkedIn) managed via Admin Console
- **IdP sync**: When a third-party IdP is connected, users are auto-synced via SCIM; cannot be manually modified in Admin Console
- **Default access**: All new users land in "Everyone" group only — no Resources accessible unless assigned
- **Access visibility**: User detail page shows accessible Resources as list or Access Graph (filterable by Group, Remote Network, Resource)
- **Billing**: All synchronized users + service accounts are billable

## Admin Roles

| Role | Permissions |
|------|-------------|
| **Admin** | Full read/write across entire Admin Console |
| **Viewer** | Read-only (excludes Secure DNS, Client Config, Billing) |
| **DevOps** | Read/write on Network tab; read-only elsewhere (excludes Secure DNS, Client Config, Billing) |
| **Internet Security** | Read/write on Internet Security tab; read-only elsewhere (excludes Billing) |
| **Helpdesk** | Reset MFA, verify/unverify devices, manage serial numbers; read-only elsewhere (excludes Secure DNS, Client Config, Billing) |
| **Access Reviewer** | Access Requests page only |
| **Billing** | Billing page only (plan and payment management) |

## Gotchas
- New users have **zero Resource access** by default — must explicitly add Resources to "Everyone" group or assign users to Groups with Resources
- With IdP/SCIM configured, user creation/deactivation **must** be managed in the IdP, not Twingate Admin Console
- Viewer, DevOps, Helpdesk, and Access Reviewer roles cannot access Secure DNS or Client Configuration pages

## Prerequisites
- Admin Console access with Admin role to manage users
- IdP configured if using SCIM sync (optional)

## Related Docs
- [Social Logins](https://www.twingate.com/docs/social-logins)
- [Identity Providers](https://www.twingate.com/docs/identity-providers)
- [Groups](https://www.twingate.com/docs/groups)
- [Offboarding Users](https://www.twingate.com/docs/offboarding-users)
- [Admins](https://www.twingate.com/docs/admins)
- [Billing](https://www.twingate.com/docs/billing)
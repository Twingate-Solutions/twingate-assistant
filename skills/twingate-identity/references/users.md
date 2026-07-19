# Twingate Users

## Summary
Twingate users can be managed via social logins or synced automatically from a third-party IdP via SCIM. New users only have access to the "Everyone" group by default and must be explicitly granted access to Resources. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth methods: Google, Microsoft, GitHub, LinkedIn (social logins)
- IdP-connected accounts: users sync automatically via SCIM; cannot be modified in Admin Console
- New users start with **only** "Everyone" group membership — no Resource access unless explicitly assigned
- View user Resource access via user detail page (list view or Access Graph)
- Access Graph shows groups, Resources, paths, and policies; filterable by Group, Remote Network, or Resource
- Billing applies to all synchronized users + service accounts

## Admin Roles

| Role | Access Level |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab; read-only elsewhere |
| Support | Read-only across entire Admin Console |
| Access Reviewer | Access Requests page only |
| Billing | Billing page only (plan and payment management) |

## Prerequisites
- Admin Console access to invite/manage users
- IdP configured (optional) for SCIM sync
- Resources must be added to groups for users to gain access

## Gotchas
- **No automatic Resource access**: New users have zero Resource access until added to a Group with Resources or Resources are added to the Everyone group
- **IdP sync is one-way**: With an IdP connected, user changes must be made in the IdP — the Admin Console becomes read-only for user management
- **Billing impact**: All synchronized users count toward billing, not just active ones
- Deactivation/deletion must go through IdP if SCIM is configured

## Related Docs
- [Social Logins](#) — managing social login providers
- [Identity Providers](#) — configuring IdP/SCIM sync
- [Groups](#) — assigning users to groups and Resources
- [Admins](#) — detailed admin role management
- [Offboarding Users](#) — disabling/deleting users
- [Billing](#) — understanding user billing
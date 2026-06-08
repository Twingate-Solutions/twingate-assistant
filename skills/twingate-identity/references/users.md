# Twingate Users

## Summary
Twingate users can be managed via social logins or synced automatically from a third-party IdP via SCIM. New users default to the "Everyone" group with no Resource access until explicitly assigned. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth: Google, Microsoft, GitHub, LinkedIn social logins
- IdP-connected accounts: users auto-synced via SCIM; cannot be modified in Admin Console
- All new users start in "Everyone" group only — **no Resource access by default**
- Resource access requires: adding Resources to Everyone group, OR assigning users to specific Groups
- User access visibility: detail page shows list view or Access Graph (filterable by Group, Remote Network, Resource)
- Billing applies to all synchronized users + service accounts

## Admin Roles

| Role | Permissions |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab only; read-only elsewhere |
| Support | Read-only across entire Admin Console |

## Prerequisites
- Social logins: no additional setup required
- IdP sync: requires configured Identity Provider with SCIM enabled

## User Lifecycle
1. **Add user** — via Teams page (social login) or auto-sync from IdP
2. **Assign access** — add to Groups that have Resources, or add Resources to Everyone group
3. **Verify access** — check user detail page (list or Access Graph view)
4. **Offboard** — disable or delete user when access no longer needed

## Gotchas
- Users with **no Group assignments beyond Everyone** cannot access any Resources — this is a common misconfiguration
- IdP-managed users **cannot be edited** in the Admin Console; all changes must come from IdP via SCIM and apply immediately
- Deactivated users in IdP are deactivated in Twingate immediately via SCIM
- All synced users count toward billing — including inactive/pending users

## Related Docs
- [Social Logins](#) — managing social login providers
- [Identity Providers](#) — IdP configuration and SCIM setup
- [Groups](#) — assigning Resources to groups
- [Admins](#) — detailed admin role permissions and assignment
- [Offboarding Users](#) — disable/delete user procedures
- [Billing](#) — user billing details
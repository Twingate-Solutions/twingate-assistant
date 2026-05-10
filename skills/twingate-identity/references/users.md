# Twingate Users

## Summary
Twingate users can be managed via social logins or synced automatically from a third-party IdP via SCIM. New users only get access to the "Everyone" group by default and have no Resource access until explicitly assigned. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth: Google, Microsoft, GitHub, LinkedIn social logins
- IdP integration: Users auto-synced via SCIM; cannot be modified in Admin Console manually
- New users added to "Everyone" group only — **no Resource access by default**
- User access viewable via detail page (list view or Access Graph)
- Access Graph shows groups, Resources, paths, and policies with filtering by Group, Remote Network, or Resource
- Billed for all synchronized users + service accounts

## Admin Roles

| Role | Permissions |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab; read-only elsewhere |
| Support | Read-only across entire Admin Console |

## User Lifecycle
1. **Add user** — Invite via Teams page (social login) or auto-sync via IdP/SCIM
2. **Assign access** — Add Resources to Everyone group OR assign user to specific Group(s)
3. **Offboard** — Disable or delete user when access no longer needed

## Gotchas
- Users with no group assignments beyond "Everyone" (and no Resources on Everyone group) have **zero Resource access** — easy to miss during onboarding
- With IdP configured, user creation/deactivation must happen in the IdP; Admin Console changes are blocked
- SCIM changes from IdP apply to Twingate **immediately**
- All synchronized users count toward billing, including inactive/pending users

## Related Docs
- [Social Logins](#) — Managing social login providers
- [Identity Providers](#) — IdP configuration and SCIM setup
- [Groups](#) — Assigning users to groups and Resources
- [Admins](#) — Detailed admin role permissions and assignment
- [Offboarding Users](#) — Disabling and deleting users
- [Billing](#) — User billing details
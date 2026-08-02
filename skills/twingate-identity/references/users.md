# Twingate Users

## Summary
Twingate manages users either through social logins (Google, Microsoft, GitHub, LinkedIn) or a third-party IdP via SCIM sync. New users default to the "Everyone" group with no Resource access unless explicitly configured. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth methods: Google, Microsoft, GitHub, LinkedIn social logins
- IdP-connected accounts: users sync automatically via SCIM; cannot be modified in Admin Console
- All new users start in "Everyone" group only — **no Resource access by default**
- User access viewable via detail page (list view or Access Graph)
- Access Graph shows groups, Resources, paths, and policies; filterable by Group, Remote Network, or Resource
- Billing applies to all synchronized users + service accounts

## User Access Model
- Users need explicit Resource assignment: either add Resources to "Everyone" group OR assign users to specific Groups with Resources
- Access Graph provides visual mapping of access paths and applied policies

## Admin Roles

| Role | Permissions |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab; read-only elsewhere |
| Support | Read-only across entire Admin Console |
| Access Reviewer | Access Requests page only |
| Billing | Billing page only (plan & payment management) |

## User Lifecycle
- **Invite**: Via Teams page in Admin Console (social login mode)
- **Sync**: Automatic via IdP/SCIM (IdP mode)
- **Offboard**: Disable or delete user when access no longer needed

## Gotchas
- IdP-synced users **cannot** be modified in the Admin Console — all changes must be made in the IdP
- New users have **zero Resource access** until Groups/Resources are configured — "Everyone" group has no Resources by default
- All synchronized users count toward billing, regardless of active usage
- SCIM changes (creation, deactivation) update Twingate immediately

## Related Docs
- [Social Logins](https://www.twingate.com/docs/social-logins)
- [Identity Providers](https://www.twingate.com/docs/identity-providers)
- [Groups](https://www.twingate.com/docs/groups)
- [Admins](https://www.twingate.com/docs/admins)
- [Offboarding Users](https://www.twingate.com/docs/offboarding-users)
- [Billing](https://www.twingate.com/docs/billing)
# Twingate Users

## Summary
Twingate users are managed either via social logins (Google, Microsoft, GitHub, LinkedIn) or automatically synchronized from a third-party IdP via SCIM. New users only have access to the "Everyone" group by default and cannot access Resources until explicitly assigned. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth: social logins (Google, Microsoft, GitHub, LinkedIn)
- IdP-connected accounts: users auto-synced via SCIM; cannot be modified in Admin Console
- New users default to "Everyone" group only — no Resource access unless explicitly granted
- Billing covers all synchronized users + service accounts
- User access viewable via detail page (list view or Access Graph)
- Access Graph shows groups, Resources, paths, and policies with filtering by Group, Remote Network, or Resource

## Admin Roles

| Role | Permissions |
|------|-------------|
| **Admin** | Full read/write across entire Admin Console |
| **DevOps** | Read/write on Network tab; read-only elsewhere |
| **Support** | Read-only across entire Admin Console |

## Prerequisites
- Admin Console access
- For IdP sync: configured Identity Provider with SCIM enabled

## User Management

### Social Login (Default)
- Invite users via **Teams page** in Admin Console
- Deactivate users directly in Admin Console

### IdP-Connected
- Users created/deactivated via IdP only
- Changes propagate to Twingate immediately via SCIM
- No user modification available in Admin Console

## Gotchas
- New users have **zero Resource access** by default — must add Resources to Everyone group or assign users to specific Groups
- With IdP integration, user management is locked in Admin Console; all changes must be made at the IdP level
- All synchronized users count toward billing, not just active/licensed ones
- Deleting vs. disabling users are separate actions — see Offboarding Users docs

## Related Docs
- [Social Logins](#) — managing social login configuration
- [Identity Providers](#) — configuring third-party IdP + SCIM
- [Groups](#) — assigning Resources to groups
- [Admins](#) — detailed admin role descriptions and assignment
- [Offboarding Users](#) — disabling/deleting users
- [Billing](#) — user billing details
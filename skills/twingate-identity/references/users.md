# Twingate Users

## Summary
Twingate user management supports either social logins (Google, Microsoft, GitHub, LinkedIn) or a third-party IdP via SCIM sync. New users are added to the "Everyone" group by default with no Resource access until explicitly configured. Billing applies to all synchronized users and service accounts.

## Key Information
- **Default auth**: Social logins managed via Admin Console Teams page
- **IdP integration**: Users sync automatically via SCIM; cannot be modified in Admin Console when IdP is connected
- **Default access**: New users only belong to "Everyone" group — no Resource access unless Resources are assigned to Everyone group or user is added to a Group with Resources
- **Access visibility**: User detail page shows accessible Resources as list or Access Graph (filterable by Groups, Remote Networks, Resources)
- **Billing**: All synchronized users + service accounts are billed
- **Offboarding**: Users can be disabled or deleted when access is no longer needed

## Admin Roles

| Role | Permissions |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab; read-only elsewhere |
| Support | Read-only across entire Admin Console |

## Prerequisites
- Admin Console access to invite/manage users
- IdP configured (optional) for SCIM-based user sync

## Configuration Notes
- **Social login path**: Invite via Admin Console → Teams page
- **IdP path**: Configure IdP → users sync automatically via SCIM → changes (create/deactivate) propagate immediately
- No manual user modification possible in Admin Console when IdP is connected

## Gotchas
- Users added via IdP SCIM **cannot** be modified in the Admin Console — all changes must happen in the IdP
- New users have **zero Resource access** by default; must explicitly assign Groups or add Resources to the Everyone group
- Forgetting to assign Resources to groups is a common reason users report "no access" after onboarding
- All synchronized users count toward billing, including inactive/pending users

## Related Docs
- [Social Logins](#) — managing social login configuration
- [Identity Providers](#) — IdP setup and SCIM configuration
- [Groups](#) — assigning Resources to groups
- [Admins](#) — detailed admin role permissions and assignment
- [Offboarding Users](#) — disabling and deleting users
- [Billing](#) — billing details for users and service accounts
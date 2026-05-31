# Twingate Users

## Summary
Twingate manages users either via social logins (Google, Microsoft, GitHub, LinkedIn) or a third-party IdP with SCIM sync. New users default to the "Everyone" group with no Resource access until explicitly assigned. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth: social logins managed via Admin Console Teams page
- IdP integration: users sync automatically via SCIM; cannot be modified in Admin Console
- New users only have access to the "Everyone" group by default
- Users have **no Resource access** unless Resources are added to Everyone group or users are assigned to a Group with Resources
- User access can be viewed via detail page (list view or Access Graph)
- Access Graph shows groups, Resources, paths, and policies; filterable by Group, Remote Network, or Resource
- Billing covers all synchronized users and service accounts

## Admin Roles

| Role | Permissions |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab only; read-only elsewhere |
| Support | Read-only across entire Admin Console |

## Prerequisites
- Social logins OR configured IdP (not both simultaneously)
- SCIM configured if using IdP sync

## Configuration Notes
- **Social login users**: Invite/deactivate via Admin Console → Teams
- **IdP users**: All lifecycle changes (create/deactivate) must be made in the IdP; changes propagate to Twingate immediately via SCIM

## Gotchas
- Users added via IdP **cannot** be modified in the Admin Console — changes must be made at the IdP level
- New users have zero Resource access by default; the Everyone group grants no access unless Resources are explicitly assigned to it
- Deleting/disabling users is handled separately via the Offboarding Users process

## Related Docs
- [Social Logins](#) — managing social login providers
- [Identity Providers](#) — configuring IdP and SCIM
- [Groups](#) — assigning users to groups with Resource access
- [Admins](#) — detailed admin role descriptions and assignment
- [Offboarding Users](#) — disabling/deleting users
- [Billing](#) — user billing details
# Twingate Users

## Summary
Twingate user management supports social logins (Google, Microsoft, GitHub, LinkedIn) or IdP synchronization via SCIM. New users only receive access to the "Everyone" group by default and have no Resource access until explicitly assigned. Users can be managed through the Admin Console or automatically via IdP.

## Key Information
- Default auth: social logins (Google, Microsoft, GitHub, LinkedIn)
- IdP integration syncs users automatically via SCIM; Admin Console cannot modify synced users
- New users default to "Everyone" group only — no Resource access without explicit assignment
- User Resource access viewable via detail page (list view or Access Graph)
- Access Graph shows groups, Resources, paths, and policies; filterable by Group, Remote Network, or Resource
- Billing applies to all synchronized users and service accounts

## Admin Roles

| Role | Permissions |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab; read-only elsewhere |
| Support | Read-only across entire Admin Console |

## User Lifecycle
1. **Invite** users via Teams page in Admin Console (social login mode)
2. **Assign** users to Groups with Resource access (Everyone group has none by default)
3. **Offboard** by disabling or deleting users when access no longer needed

## Gotchas
- Users added to Twingate have **zero Resource access** until Resources are added to the Everyone group or users are assigned to a Group with Resources
- With IdP/SCIM configured, user creation/deactivation **must** be managed in the IdP — Admin Console changes are not possible
- All synchronized users and service accounts count toward billing regardless of Resource access

## Related Docs
- [Social Logins](https://www.twingate.com/docs/social-logins)
- [Identity Providers](https://www.twingate.com/docs/identity-providers)
- [Groups](https://www.twingate.com/docs/groups)
- [Admins](https://www.twingate.com/docs/admins)
- [Offboarding Users](https://www.twingate.com/docs/offboarding-users)
- [Billing](https://www.twingate.com/docs/billing)
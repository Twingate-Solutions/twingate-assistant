# Twingate Users

## Summary
Twingate manages users either through built-in social logins (Google, Microsoft, GitHub, LinkedIn) or via a third-party IdP with SCIM sync. All new users default to the "Everyone" group with no Resource access until explicitly assigned. Billing applies to all synchronized users and service accounts.

## Key Information
- **Default auth**: Social logins managed via Admin Console Teams page
- **IdP sync**: When IdP is configured, users sync automatically via SCIM; cannot be manually modified in Admin Console
- **Default access**: New users only get "Everyone" group membership — no Resources accessible unless explicitly added
- **Access visibility**: User detail page shows accessible Resources in list view or Access Graph (filterable by Groups, Remote Networks, Resources)
- **Billing**: Applies to all synchronized users + service accounts
- **Offboarding**: Users can be disabled or deleted when access is no longer needed

## Admin Roles

| Role | Permissions |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab; read-only elsewhere |
| Support | Read-only across entire Admin Console |
| Access Reviewer | Access Requests page only |
| Billing | Billing page only (plan & payment management) |

## Prerequisites
- Admin Console access to invite/manage users
- IdP + SCIM configured if using automated user sync (optional)

## Gotchas
- Users with IdP/SCIM sync **cannot** be modified in the Admin Console — all changes must originate from the IdP
- New users have **zero Resource access** by default; requires explicit Group/Resource assignment
- Forgetting to assign users beyond "Everyone" group is a common misconfiguration causing access issues
- All synced users count toward billing regardless of active use

## Related Docs
- [Social Logins](/docs/social-logins)
- [Identity Providers](/docs/identity-providers)
- [Groups](/docs/groups)
- [Offboarding Users](/docs/offboarding-users)
- [Admins](/docs/admins)
- [Billing](/docs/billing)
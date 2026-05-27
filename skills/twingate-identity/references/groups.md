# Twingate Groups

## Summary
Groups are the authorization mechanism in Twingate, linking Users to Resources. A user gains resource access by being a Group member and passing the Resource's Security Policy. Groups can be managed manually, via API, or synced from an IdP.

## Key Information
- Groups define **who** (Users) can access **what** (Resources)
- Users can belong to multiple Groups
- Resource access within a Group can have:
  - **Expiration time** — fully revokes Group access at a set time
  - **Usage-based auto-lock** — temporarily locks access until admin unlocks
- Access requires: (1) Group membership with the Resource AND (2) passing the Resource's Security Policy

## Group Types

| Type | Description | User Management |
|------|-------------|-----------------|
| **Everyone** | Built-in; includes all users automatically | Automatic |
| **Custom** | Manually created via Admin Console or API | Manual |
| **Synced** | Synchronized from configured IdP | Controlled in IdP |

## Built-in Groups
- **Everyone** group auto-includes all users
- Use for company-wide resources (e.g., metrics dashboards, domain controllers)

## Custom Groups
- Created and managed in Twingate Admin Console
- Not modified by automated processes
- Manageable via [Admin API](https://www.twingate.com/docs/api)

## Synced Groups
- Auto-synced from configured IdP
- Resources and Access Policies can be set on synced groups
- User membership managed in IdP, reflected in Twingate

### IdP Sync Scoping Behavior
- **Entra ID, Okta, OneLogin** — support SCIM-based scoping of which users/groups sync
- **Google Workspace** — no native granular sync config; use Twingate's [Selective Sync](https://www.twingate.com/docs/selective-sync) to limit users, groups, and OUs

## Prerequisites
- Configured IdP (for Synced Groups)
- Admin Console access (for Custom Groups)
- Admin API credentials (for API-managed Custom Groups)

## Gotchas
- Synced group user membership **cannot** be modified in Twingate — changes must be made in the IdP
- Google Workspace requires Selective Sync configuration for granular control; it does not support native SCIM scoping
- Expiration vs. auto-lock behave differently: expiration = permanent revocation; auto-lock = temporary, re-unlockable by admin
- Custom groups will **not** be modified by automated/sync processes once created

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Resources](https://www.twingate.com/docs/resources)
- [Security Policies / 2FA](https://www.twingate.com/docs/security-policies)
- [Admin API](https://www.twingate.com/docs/api)
- [IdP Configuration](https://www.twingate.com/docs/idp)
- [Selective Sync (Google Workspace)](https://www.twingate.com/docs/selective-sync)
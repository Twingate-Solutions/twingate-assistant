# Twingate Groups

## Summary
Groups are the authorization mechanism in Twingate, linking Users to Resources. A user must belong to a Group that includes a Resource and pass the Resource's Security Policy to gain access. Groups can be managed manually, via API, or synced from an IdP.

## Key Information
- Groups define which users can access which resources
- Users can belong to multiple groups
- Per-resource access can include **expiration time** (full revocation) or **usage-based auto-lock** (temporary lock requiring admin unlock)
- Access requires: group membership + successful Security Policy authentication (may include IdP re-auth or 2FA)

## Group Types

| Type | Description | Management |
|------|-------------|------------|
| **Everyone** | Built-in; all users auto-included | Automatic |
| **Custom** | Manually created | Admin Console or Admin API |
| **Synced** | Synced from IdP | IdP controls user membership |

## Built-in Groups
- `Everyone` group includes all users automatically
- Use for company-wide resources (metrics dashboards, domain controllers, shared infrastructure)

## Synced Groups (IdP-specific behavior)
- **Entra ID, Okta, OneLogin**: Support SCIM scoping to limit which users/groups sync
- **Google Workspace**: No native granular sync control; use Twingate's **Selective Sync** feature to limit users, groups, and OUs

## Gotchas
- Synced groups: Resources and Access Policies can be assigned, but **user membership cannot be managed in Twingate** — only through the IdP
- Custom groups will **not** be modified by automated processes (safe from IdP sync overrides)
- Expiration and auto-lock behave differently: expiration permanently revokes access; auto-lock is temporary and reversible by an admin

## Prerequisites
- IdP configured for Synced groups
- Admin console access for Custom group management
- Admin API access for programmatic group management

## Related Docs
- Users
- Resources
- Security Policies / 2FA
- Admin API
- IdP Configuration (Entra ID, Okta, OneLogin, Google Workspace)
- Selective Sync (Google Workspace)
- SCIM configuration
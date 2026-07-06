# Twingate Groups

## Summary
Groups control user authorization to Resources in Twingate. A group links a set of users to a set of Resources, with optional access expiration or usage-based auto-lock controls. Users must belong to a group containing a Resource AND pass the Resource's Security Policy to gain access.

## Key Information
- Groups connect **users → Resources** (authorization layer, not authentication)
- Users can belong to multiple groups
- Per-resource access controls within a group:
  - **Expiration time**: fully revokes group access after set time
  - **Usage-based auto-lock**: temporarily locks access until admin unlocks
- Three group types: Everyone (built-in), Custom, Synced

## Group Types

| Type | Management | User Control |
|------|-----------|--------------|
| Everyone | Automatic | All users included automatically |
| Custom | Admin Console or API | Manual |
| Synced | IdP via SCIM | IdP-controlled |

## Built-in Groups
- **Everyone**: Includes all users automatically; suitable for company-wide resources, domain controllers, shared infrastructure

## Custom Groups
- Created/managed in Admin Console or via [Admin API](https://www.twingate.com/docs/api)
- Not modified by automated processes

## Synced Groups (IdP)
- Synced from configured IdP
- Resources and Access policies can be set in Twingate
- User membership controlled from IdP

### IdP-Specific Behavior
- **Entra ID, Okta, OneLogin**: Support SCIM scoping to limit which users/groups sync
- **Google Workspace**: No native granular sync control; use Twingate's **Selective Sync** feature to limit users, groups, and OUs

## Access Requirements (both must be met)
1. User is member of a group that includes the Resource
2. User successfully authenticates against the Resource's configured Security Policy (may require IdP re-auth, 2FA, etc.)

## Gotchas
- Synced group user membership cannot be edited in Twingate—changes must be made in the IdP
- Expiration removes access entirely; auto-lock only suspends it (reversible by admin)
- Google Workspace requires Selective Sync configuration since SCIM scoping isn't natively supported

## Related Docs
- Security Policies & 2FA
- Admin API (for programmatic group management)
- IdP Configuration / SCIM setup
- Selective Sync (Google Workspace)
- Resource configuration
- Users management
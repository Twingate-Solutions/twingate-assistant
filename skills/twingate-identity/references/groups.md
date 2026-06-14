# Twingate Groups

## Summary
Groups control user authorization to Resources in Twingate. Each group links a set of users to a set of Resources, with optional access expiration or usage-based auto-lock controls. Users must belong to a group containing a Resource and pass the Resource's Security Policy to gain access.

## Key Information
- Groups have two components: **members** (users) and **Resources** (what they can access)
- Users can belong to multiple groups
- Per-Resource access controls within a group:
  - **Expiration time**: fully revokes group access after set time
  - **Usage-based auto-lock**: temporarily locks access until admin unlocks
- Access requires both group membership AND successful Security Policy authentication (may include IdP re-auth, 2FA)

## Group Types

### Built-in: `Everyone`
- Automatically includes **all users**
- Suitable for company-wide resources (dashboards, domain controllers, shared infrastructure)
- Cannot be deleted or manually scoped

### Custom Groups
- Manually created/managed in Admin console
- Not modified by automated processes
- Manageable via [Admin API](https://www.twingate.com/docs/api)

### Synced Groups
- Auto-synchronized from configured IdP
- Resources and Access policies can be set, but **user membership is IdP-controlled**
- IdP-specific scoping behavior:
  - **Entra ID, Okta, OneLogin**: Support SCIM-based scoping of synced users/groups
  - **Google Workspace**: No native granular sync config; use Twingate's **Selective Sync** feature

## Prerequisites
- Twingate Admin console access
- IdP configured (for synced groups)
- SCIM configured (for Entra ID, Okta, OneLogin scoping)

## Gotchas
- Removing a user from an IdP group propagates to Twingate for synced groups — manage membership at IdP level, not in Twingate console
- `Everyone` group grants access to **all** users — be cautious assigning sensitive Resources here
- Expiration revokes access entirely; auto-lock is temporary and reversible by admin
- Google Workspace requires Selective Sync configuration for group scoping (not SCIM-native)

## Configuration Values
| Parameter | Notes |
|---|---|
| Expiration time | Per Resource within a group; fully revokes on expiry |
| Usage-based auto-lock | Per Resource within a group; locked until admin unlocks |
| Security Policy | Per Resource; can require IdP re-auth or 2FA |

## Related Docs
- Users
- Resources
- Security Policies / 2FA
- Admin API
- IdP Configuration
- Selective Sync (Google Workspace)
- SCIM (Entra ID, Okta, OneLogin)
---
source: https://www.twingate.com/docs/groups
type: docs
fetched: 2026-08-14
source_version: 45743d21e03e68ed83c797fbfe6f00e9229d556e60ff4ba1322e0b475dc615f2
---

# Twingate Groups

## Summary
Groups are the authorization mechanism in Twingate, linking Users to Resources. A user gains resource access by being a member of a Group that includes the Resource and passing the Resource's Security Policy. Groups come in three types: built-in, custom, and synced.

## Key Information
- Groups define **who** (Users) can access **what** (Resources)
- Users can belong to multiple Groups
- Resource access within a Group can have:
  - **Expiration time**: fully revokes Group access after set period
  - **Usage-based auto-lock**: temporarily locks access until admin unlocks
- Access requires both: Group membership + successful Security Policy authentication (may include IdP re-auth or 2FA)

## Group Types

### Built-in: `Everyone`
- Automatically includes **all users**
- Cannot be modified for membership
- Typical use cases: company-wide dashboards, domain controllers, shared infrastructure

### Custom Groups
- Manually created/managed in Admin console
- Not modified by automated processes
- Manageable via [Admin API](https://www.twingate.com/docs/api)

### Synced Groups
- Auto-synchronized from configured IdP
- User membership controlled from IdP side
- Resources and Access policies can still be set in Twingate
- IdP-specific sync behavior:
  - **Entra ID, Okta, OneLogin**: support SCIM-based scoping of synced users/groups
  - **Google Workspace**: no native granular sync config; use Twingate's **Selective Sync** feature to limit which users, groups, and OUs sync

## Prerequisites
- Configured Identity Provider (for Synced Groups)
- Admin console access (for Custom Groups)
- Admin API credentials (for API-managed Custom Groups)

## Configuration Values
| Parameter | Notes |
|---|---|
| Expiration time | Per Resource, per Group; fully revokes access on expiry |
| Usage-based auto-lock | Per Resource, per Group; requires manual admin unlock |
| Security Policy | Per Resource; can enforce IdP re-auth, 2FA |

## Gotchas
- Synced group **user membership** cannot be modified in Twingate—changes must be made in the IdP
- Google Workspace requires Selective Sync configuration since it lacks native SCIM scoping
- Auto-lock from usage-based policy requires **manual admin intervention** to restore access (not automatic)
- `Everyone` group assignments affect **all users**—use carefully for sensitive resources

## Related Docs
- Security Policies / 2FA configuration
- Admin API (Custom Group management)
- IdP Configuration (Entra ID, Okta, OneLogin, Google Workspace)
- Selective Sync (Google Workspace)
- SCIM provisioning
- Resource expiration and auto-lock settings
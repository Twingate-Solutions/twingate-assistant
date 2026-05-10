# Twingate Groups

## Summary
Groups are the primary authorization mechanism in Twingate, linking users to Resources. Groups can be built-in, manually created, or synced from an IdP. A user must belong to a Group containing a Resource and pass the Resource's Security Policy to gain access.

## Key Information
- Groups connect **Users** → **Resources** for access authorization
- Resource access within a group can have:
  - **Expiration time**: fully revokes group access at set time
  - **Usage-based auto-lock**: temporarily locks access until admin unlocks
- Two conditions required for resource access:
  1. User is a member of a Group that includes the Resource
  2. User passes the Resource's configured Security Policy (may require IdP re-auth or 2FA)

## Group Types

### Built-in: `Everyone`
- Automatically includes **all users**
- Cannot be manually managed
- Use for company-wide resources (metrics dashboards, domain controllers, shared infrastructure)

### Custom Groups
- Manually created/managed in Admin Console
- Not modified by automated processes
- Can also be managed via **Twingate Admin API**

### Synced Groups
- Auto-synchronized from configured IdP
- Resources and Access policies can be set on synced groups
- **User management is IdP-controlled** (not manageable in Twingate)
- IdP-specific scoping behavior:
  - **Entra ID, Okta, OneLogin**: support SCIM-based scoping of which users/groups sync
  - **Google Workspace**: no native granular sync config; use Twingate's **Selective Sync** feature

## Configuration Values
| Setting | Description |
|---|---|
| Expiration time | Timestamp after which group's resource access is fully revoked |
| Usage-based auto-lock | Locks access based on usage; requires manual admin unlock |

## Gotchas
- Synced group memberships **cannot be edited in Twingate** — changes must be made in the IdP
- Google Workspace requires Twingate-specific **Selective Sync** configuration since it lacks native SCIM scoping
- `Everyone` group changes affect **all users** — assign resources carefully
- Auto-locked groups require **manual admin intervention** to restore access (not automatic)

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Resources](https://www.twingate.com/docs/resources)
- [Security Policies / 2FA](https://www.twingate.com/docs/security-policies)
- [Admin API](https://www.twingate.com/docs/api)
- [IdP Configuration](https://www.twingate.com/docs/idp)
- [Selective Sync (Google Workspace)](https://www.twingate.com/docs/selective-sync)
- Entra ID / Okta / OneLogin SCIM docs
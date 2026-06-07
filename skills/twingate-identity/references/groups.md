# Twingate Groups

## Summary
Groups are the authorization mechanism in Twingate that connect users to Resources. A user gains access to a Resource by being a member of a Group that includes that Resource and successfully authenticating against the Resource's Security Policy.

## Key Information
- Groups have two core components: **members** (users) and **Resources** (what they can access)
- Users can belong to multiple Groups
- Resource access within a Group can be time-limited via **expiration time** (full revocation) or **usage-based auto-lock** (temporary lock requiring admin unlock)
- Three Group types: **Everyone** (built-in), **Custom**, and **Synced**

## Access Requirements
For a user to access a Resource, they must:
1. Be a member of a Group that includes the Resource
2. Successfully authenticate against the Resource's configured Security Policy (may require IdP re-auth or 2FA)

## Group Types

### Everyone (Built-in)
- Automatically includes **all users** — no management required
- Best for: company-wide resources, domain controllers, shared infrastructure

### Custom Groups
- Manually created/managed in Admin console
- Not modified by automated processes
- Can also be managed via the **Twingate Admin API**

### Synced Groups
- Auto-synchronized from a configured IdP
- Resources and Access policies can be set on Synced groups
- User membership is managed in IdP, not Twingate

## IdP Sync Behavior
| IdP | Scoping Method |
|-----|---------------|
| Entra ID | SCIM (native scoping) |
| Okta | SCIM (native scoping) |
| OneLogin | SCIM (native scoping) |
| Google Workspace | Twingate Selective Sync (no native granular config) |

## Gotchas
- Synced group user membership **cannot** be modified in Twingate — changes must be made in the IdP
- Google Workspace requires Twingate's **Selective Sync** feature to limit which users/groups/OUs sync (not configurable natively)
- Expiration time fully revokes access; usage-based auto-lock only temporarily locks and requires admin action to restore

## Related Docs
- Users
- Resources
- Security Policies / 2FA
- Admin API
- IdP Configuration (Entra ID, Okta, OneLogin, Google Workspace)
- Selective Sync (Google Workspace)
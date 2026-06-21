# Twingate Groups

## Summary
Groups are the authorization mechanism in Twingate that link Users to Resources. A user gains access to a Resource by being a member of a Group that includes that Resource and passing the Resource's Security Policy.

## Key Information
- Groups have two core components: a **member set** (Users) and a **resource set** (Resources)
- Resource access within a group can be time-limited via **expiration time** (revokes access) or **usage-based auto-lock** (temporarily locks until admin unlocks)
- Three group types: **Everyone** (built-in), **Custom** (manually managed), **Synced** (IdP-synchronized)
- The **Everyone** group automatically includes all users — resources added here are accessible company-wide
- Users can belong to multiple Groups

## Access Requirements
For a user to access a Resource, they must:
1. Be a member of a Group that includes the Resource
2. Successfully authenticate against the Resource's configured **Security Policy** (may require IdP re-auth or 2FA)

## Group Types

### Built-in: Everyone
- Auto-includes all users; cannot be scoped
- Use for company-wide resources (metrics dashboards, domain controllers, shared infrastructure)

### Custom Groups
- Created/managed manually in Twingate Admin Console
- Not modified by automated processes
- Can also be managed via **Admin API**

### Synced Groups
- Synchronized automatically from configured IdP
- Resources and Access Policies can be set on synced groups
- User membership is managed in the IdP, not Twingate
- **Entra ID, Okta, OneLogin**: Support SCIM scoping to limit which users/groups sync
- **Google Workspace**: No native granular sync control; use Twingate's **Selective Sync** feature

## Configuration Values
| Setting | Description |
|---|---|
| Expiration Time | Date/time when Group's access to a Resource is fully revoked |
| Usage-based Auto-lock | Locks Group access after inactivity; requires admin to unlock |
| Security Policy | Per-Resource policy applied to all Group members |

## Gotchas
- Expiration time **revokes** access permanently; usage-based auto-lock only **temporarily locks** (admin must unlock)
- Google Workspace lacks native SCIM scoping — requires Selective Sync configuration to limit sync scope
- Synced group user membership **cannot** be managed in Twingate; changes must be made in the IdP

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Resources](https://www.twingate.com/docs/resources)
- [Security Policies / 2FA](https://www.twingate.com/docs/security-policies)
- [Admin API](https://www.twingate.com/docs/admin-api)
- [IdP Configuration](https://www.twingate.com/docs/idp)
- [Selective Sync (Google Workspace)](https://www.twingate.com/docs/selective-sync)
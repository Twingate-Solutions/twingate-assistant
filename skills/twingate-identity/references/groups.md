# Twingate Groups

## Summary
Groups control user authorization to Resources in Twingate. A user gains access to a Resource by being a Group member that includes that Resource and successfully authenticating against the Resource's Security Policy.

## Key Information
- Groups link **Users** → **Resources** with optional access controls
- Access per Resource can include **expiration time** (full revocation) or **usage-based auto-lock** (temporary lock requiring admin unlock)
- Three group types: Built-in, Custom, and Synced

### Built-in Groups
- **Everyone**: Auto-includes all users; suitable for company-wide resources, domain controllers, shared infrastructure

### Custom Groups
- Manually created/managed in Admin console
- Not modified by automated processes
- Manageable via [Admin API](https://www.twingate.com/docs/api)

### Synced Groups
- Auto-synchronized from configured IdP
- Resources and Access policies can be set; user membership controlled from IdP
- **Entra ID, Okta, OneLogin**: Support SCIM scoping for users/groups
- **Google Workspace**: No native granular sync; use Twingate's Selective Sync feature

## Prerequisites
- Configured Identity Provider (for Synced groups)
- Admin console access (for Custom groups)
- Security Policy configured on Resources (for access control)

## Authorization Requirements
User must satisfy **both**:
1. Membership in a Group that includes the target Resource
2. Successful authentication against the Resource's Security Policy (may require IdP re-auth or 2FA)

## Configuration Values
| Setting | Options | Notes |
|---|---|---|
| Resource access expiration | Time-based | Fully revokes Group's access at expiry |
| Usage-based auto-lock | Usage threshold | Locks access; admin must unlock |

## Gotchas
- Removing a user from a Synced group must be done at the IdP level — Twingate reflects IdP state, it does not control it
- Google Workspace requires **Selective Sync** configuration since it lacks native SCIM scoping
- Auto-lock only temporarily suspends access; expiration permanently revokes it until reconfigured
- Users in multiple Groups inherit access from all Groups they belong to

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Resources](https://www.twingate.com/docs/resources)
- [Security Policies / 2FA](https://www.twingate.com/docs/security-policies)
- [Admin API](https://www.twingate.com/docs/api)
- [IdP Configuration](https://www.twingate.com/docs/idp)
- [Selective Sync (Google Workspace)](https://www.twingate.com/docs/selective-sync)
- [Entra ID SCIM](https://www.twingate.com/docs/azure-ad)
- [Okta SCIM](https://www.twingate.com/docs/okta)
- [OneLogin SCIM](https://www.twingate.com/docs/onelogin)
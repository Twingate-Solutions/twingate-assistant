# Twingate Groups

## Summary
Groups are the authorization mechanism in Twingate that connect Users to Resources. A user gains resource access by being a member of a Group that includes that Resource and passing the Resource's Security Policy. Groups come in three types: built-in, custom, and synced.

## Key Information
- Groups define **who** (Users) can access **what** (Resources)
- Users can belong to multiple Groups
- Access per Resource can be time-limited via **expiration time** (full revocation) or **usage-based auto-lock** (temporary lock requiring admin unlock)
- Two access conditions must both be met: group membership + Security Policy authentication

## Built-in Groups
- **Everyone** group: automatically includes all users; cannot be manually modified
- Use for company-wide resources (dashboards, domain controllers, shared infrastructure)

## Custom Groups
- Manually created/managed in the Admin console
- Not modified by automated processes
- Manageable via the **Twingate Admin API**

## Synced Groups
- Auto-synchronized from a configured IdP
- Resources and Access Policies can be set, but **user management is IdP-controlled**
- IdP-specific scoping behavior:
  - **Entra ID, Okta, OneLogin**: support SCIM-based scoping of synced users/groups
  - **Google Workspace**: no native granular sync config; use **Selective Sync** feature

## Prerequisites
- Configured IdP (for Synced Groups)
- Admin console access (for Custom Groups)
- Admin API credentials (for API-managed Custom Groups)

## Access Authorization Requirements
1. User must be a member of a Group containing the target Resource
2. User must authenticate successfully against the Resource's Security Policy (may require IdP re-auth or 2FA)

## Gotchas
- Expiration time **fully revokes** group access; auto-lock only **temporarily locks** it (admin must unlock)
- Google Workspace requires Selective Sync configuration — it does not support granular sync natively
- Synced group membership cannot be modified in Twingate — changes must be made in the IdP
- The Everyone group applies to **all** users automatically; assign Resources to it carefully

## Related Docs
- Users
- Resources
- Security Policy / 2FA
- Admin API
- IdP Configuration (Entra ID, Okta, OneLogin, Google Workspace)
- Selective Sync (Google Workspace)
- SCIM
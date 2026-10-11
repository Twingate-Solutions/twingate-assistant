---
source: https://www.twingate.com/docs/users
type: docs
fetched: 2026-10-11
source_version: dea2b6fef41482211b85824c21e37ee57e40e9158756136581bafa39bf0dc338
trust: official
---

# Twingate Users

## Summary
Twingate manages users either via social logins (default) or a third-party IdP with SCIM sync. All new users start with access only to the "Everyone" group and have no Resource access until explicitly granted. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth: Google, Microsoft, GitHub, LinkedIn social logins
- IdP-connected accounts: users synced automatically via SCIM; cannot be modified in Admin Console
- New users default to "Everyone" group only — **no Resource access without explicit assignment**
- User access viewable via detail page: list view or Access Graph (filterable by Groups, Remote Networks, Resources)
- Access Graph shows group/resource mappings, paths, and applied policies
- Billing covers all synchronized users + service accounts

## Prerequisites
- Admin Console access
- IdP configured (optional) — required for SCIM sync

## Admin Roles

| Role | Permissions |
|------|-------------|
| **Admin** | Full read/write across entire Admin Console |
| **Support** | Read-only across entire Admin Console |
| **DevOps** | Read/write on Network tab; read-only elsewhere |
| **Internet Security** | Read/write on Internet Security tab; read-only elsewhere (except Billing — no access) |
| **Helpdesk** | Reset MFA, verify/unverify devices, manage serial numbers; read-only elsewhere |
| **Access Reviewer** | Access Requests page only |
| **Billing** | Billing page only (plan and payment management) |

## User Lifecycle
1. **Invite** users via Teams page in Admin Console (social login) OR sync via IdP/SCIM
2. **Assign** users to Groups with Resources — default "Everyone" group has no Resources attached
3. **Offboard** by disabling or deleting the user when access no longer needed

## Gotchas
- Users added via IdP **cannot** be created, modified, or deactivated in the Admin Console — all changes must originate from the IdP
- New users have **zero Resource access** by default; "Everyone" group must have Resources assigned, or users must be added to a Group that does
- Internet Security admin role does **not** have read access to Billing (unlike other roles which are read-only elsewhere)

## Related Docs
- [Social Logins](https://www.twingate.com/docs/social-logins)
- [Identity Providers](https://www.twingate.com/docs/identity-providers)
- [Groups](https://www.twingate.com/docs/groups)
- [Admins](https://www.twingate.com/docs/admins)
- [Offboarding Users](https://www.twingate.com/docs/offboarding-users)
- [Billing](https://www.twingate.com/docs/billing)
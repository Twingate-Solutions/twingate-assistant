---
source: https://www.twingate.com/docs/users
type: docs
fetched: 2026-08-14
source_version: b497f0a294bf2cb7aa2969fcec89ee8b94bffcb836cdaa40b6587b3daa9e2258
---

# Twingate Users

## Summary
Twingate manages users either through social logins (Google, Microsoft, GitHub, LinkedIn) or a third-party IdP via SCIM sync. New users default to the "Everyone" group with no Resource access unless explicitly assigned. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth: social logins managed via Admin Console Teams page
- IdP-connected accounts: users sync automatically via SCIM; cannot be modified in Admin Console
- New users only get access to "Everyone" group by default — **no Resources accessible** unless Resources are added to Everyone group or user is added to a specific Group
- User Resource access viewable via user detail page (list view or Access Graph)
- Access Graph shows group mappings, Resources, paths, and policies; filterable by Group, Remote Network, or Resource
- Billing applies to all synchronized users + service accounts

## Admin Roles

| Role | Access Level |
|------|-------------|
| Admin | Full read/write across entire Admin Console |
| DevOps | Read/write on Network tab; read-only elsewhere |
| Helpdesk | Reset MFA, manage device verification/serial numbers; read-only elsewhere |
| Support | Read-only across entire Admin Console |
| Access Reviewer | Access Requests page only |
| Billing | Billing page only (plan and payment management) |

## Prerequisites
- Admin Console access required to invite/deactivate users (social login mode)
- IdP + SCIM configured for automatic user sync (IdP mode)

## Gotchas
- Users added via IdP **cannot** be modified in the Admin Console — all changes must go through the IdP
- SCIM changes (create/deactivate) reflect in Twingate immediately
- New users have **zero Resource access** by default — "Everyone" group membership alone grants nothing unless Resources are explicitly assigned to that group
- All synchronized users count toward billing, even if they have no Resource access

## Related Docs
- [Social Logins](#) — managing social login providers
- [Identity Providers](#) — configuring IdP and SCIM
- [Groups](#) — assigning users to groups with Resource access
- [Offboarding Users](#) — disabling or deleting users
- [Admins](#) — detailed admin role descriptions and assignment
- [Billing](#) — billing details for users and service accounts
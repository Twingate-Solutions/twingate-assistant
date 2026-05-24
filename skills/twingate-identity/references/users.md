# Twingate Users

## Summary
Twingate manages users either through social logins (Google, Microsoft, GitHub, LinkedIn) or a synchronized IdP via SCIM. New users default to the "Everyone" group with no Resource access unless explicitly configured. Billing applies to all synchronized users and service accounts.

## Key Information
- Default auth: social logins (Google, Microsoft, GitHub, LinkedIn) managed in Admin Console
- IdP integration: users sync automatically via SCIM; cannot be modified in Admin Console directly
- New users: added to "Everyone" group only — **no Resource access by default**
- Resource access requires: adding Resources to Everyone group OR assigning users to specific Groups
- User access visibility: detail page shows list view or Access Graph (filterable by Groups, Remote Networks, Resources)
- Billing: all synchronized users + service accounts

## Admin Roles

| Role | Write Access | Read Access |
|------|-------------|-------------|
| Admin | Full (entire console) | Full |
| DevOps | Network tab only | Full |
| Support | None | Full |

## User Lifecycle
- **Add**: Invite via Teams page (social login) or auto-sync via IdP/SCIM
- **Access**: Assign to Groups that have Resources attached
- **Offboard**: Disable or delete via Admin Console (or via IdP for SCIM-managed users)

## Gotchas
- Users with only "Everyone" group membership have **zero Resource access** unless Resources are explicitly added to Everyone
- IdP-synced users: all create/deactivate operations must happen in the IdP, not Twingate console
- SCIM changes reflect in Twingate immediately
- All synchronized users count toward billing, even if they have no Resource access

## Related Docs
- [Social Logins](#) — managing social login providers
- [Identity Providers](#) — IdP configuration and SCIM setup
- [Groups](#) — assigning Resources to groups
- [Admins](#) — detailed admin role permissions and assignment
- [Offboarding Users](#) — disabling/deleting users
- [Billing](#) — billing details for users and service accounts
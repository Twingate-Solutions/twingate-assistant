---
source: https://www.twingate.com/docs/google-workspace-configuration
type: docs
fetched: 2026-08-14
source_version: 47b1dfc345eeee6115d2d0c4067697ec43f832091e036af3ea4d69170d360110
---

# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to synchronize user accounts and delegate authentication via OAuth using the Google Workspace Directory API. Admins authorize the connection from the Identity Provider section in the Twingate Admin Console. Group and OU sync are optional but require read permissions regardless.

## Key Information
- Twingate requires **Groups: Read** permission even if Group Sync is disabled
- User authentication is delegated to Google; email must match configured domain(s)
- Only **active** Google Workspace users can sign in; inactive users sync but are blocked
- Real-time sync applies to **users only** (via webhook); groups/OUs are polled
- Synced data: first/last name, email, avatar, group membership (if enabled)

## Prerequisites
- Google Workspace admin with one of: Super Admin, Groups Admin, User Management Admin, Help Desk Admin, or custom role with **Users: Read** + **Groups: Read** (Admin API permissions)
- Third-party API access must not be restricted in Google Workspace (`Security > API Controls`)

## Step-by-Step
1. Enable Google Workspace integration in Twingate (`Settings > Identity Provider`)
2. Sign in to your Google Workspace domain to authorize OAuth
3. Configure the Twingate application in Google Workspace Admin Console
4. Enable user/group sync as needed via the ⋯ action menu

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| Identity Provider | `Settings > Identity Provider` | Initial connection setup |
| Add Domain | `Settings > Identity Provider > + Add Domain` | Multi-domain support |
| Group/OU Sync | ⋯ action menu | Disabled by default |
| Selective Sync | ⋯ action menu → Manage Selection | Limits which groups/OUs sync |
| Manual Sync | ⋯ action menu → Manually Sync Now | Schedules immediate sync (may take minutes) |

## Sync Polling Intervals
| Plan | Groups/OUs Sync Frequency |
|---|---|
| Starter | Every 24 hours |
| Teams / Business / Enterprise | Every 2 hours |

## Gotchas
- **Selective Sync deselection = deletion**: Removing a group from Selective Sync deletes it even if it has Resource access
- **Don't lock yourself out**: Ensure your own admin account is included in a Selective Sync group
- **API restriction errors**: If authorization fails, check `Security > API Controls > Manage Google Services` — set Google Workspace Admin to Unrestricted, or explicitly trust Twingate in `Manage Third-Party App Access`
- **Domain restriction applies to admins**: Admin accounts must also match the configured domain
- **Disabling Group Sync behavior differs** based on whether Selective Sync is on:
  - Selective Sync OFF: groups with Resource access → converted to Twingate Groups; others deleted
  - Selective Sync ON: all synced groups deleted regardless of Resource access

## Related Docs
- [Google Workspace Identity Provider Setup (Step 1)](https://www.twingate.com/docs/)
- [Google Workspace Admin Console Configuration (Step 2)](https://www.twingate.com/docs/)
- Google Workspace Administrator Roles (Google Help Center)
- Google Workspace multiple domains documentation
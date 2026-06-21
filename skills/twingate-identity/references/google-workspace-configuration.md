# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to sync user accounts, delegate authentication via OAuth, and optionally sync groups/OUs via the Google Workspace Directory API. Configuration is initiated from the Identity Provider section in the Twingate Admin Console. User changes sync in real-time via webhooks; groups/OUs sync on a polling schedule.

## Key Information
- Twingate requires **read permission for Google Workspace groups** even if Group Sync is disabled
- User email must match configured Google Workspace domain(s) to authenticate
- Domain restriction applies to Admin Console users as well
- Multiple domains supported via **Settings > Identity Provider > + Add Domain**
- Group/OU Sync is **disabled by default**

## Prerequisites
- Google Workspace admin role (one of): Super Admin, Groups Admin, User Management Admin, Help Desk Admin, or custom role with **Users: Read** + **Groups: Read** under Admin API
- If API access restricted: set Google Workspace Admin to Unrestricted, OR whitelist Twingate as Trusted in Security > API Controls > Manage Third-Party App Access

## Step-by-Step
1. Enable Google Workspace integration in Twingate Admin Console (Settings > Identity Provider)
2. Sign in to your Google Workspace domain to authorize OAuth access
3. Configure Twingate application in Google Workspace Admin Console
4. Enable user/group sync as needed via the ⋯ action menu

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| Group/OU Sync | ⋯ action menu in Identity Provider | Disabled by default |
| Selective Sync | ⋯ action menu → "Manage Selection" | Requires Group or OU sync enabled first |
| Additional domains | Settings > Identity Provider > + Add Domain | Must be pre-configured in Google Workspace |
| Manual sync | ⋯ action menu → "Manually Sync Now" | May take several minutes to complete |

## Sync Polling Periods
- **Starter plan**: Groups/OUs every 24 hours
- **Teams/Business/Enterprise**: Groups/OUs every 2 hours
- **Users**: Real-time via webhooks

## Gotchas
- **Disabling Group Sync behavior differs by Selective Sync state:**
  - Selective Sync OFF: Groups with Resource access → converted to Twingate Groups; others deleted
  - Selective Sync ON: All synced groups deleted regardless of Resource access
- Selective Sync syncs selected groups, their children, and member users only—non-selected users are not synced
- **Include your own account in Selective Sync**—being excluded locks you out; requires another admin to fix
- Authorization errors often indicate restricted third-party API access in Google Workspace Security settings
- Inactive Google Workspace users are synced but marked inactive and cannot sign in

## Data Synced
- User first/last name, email, avatar
- Group membership (only if Group Sync enabled)

## Related Docs
- [Twingate Identity Provider Settings](https://www.twingate.com/docs/)
- [Google Workspace Administrator Roles](https://support.google.com/a/answer/2406043)
- [Google Workspace Multiple Domains](https://support.google.com/a/answer/182081)
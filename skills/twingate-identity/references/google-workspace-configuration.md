# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to sync user accounts, delegate authentication to Google, and optionally sync groups/OUs via the Directory API using OAuth. Configuration is initiated from the Admin Console under Settings > Identity Provider.

## Key Information
- Twingate requires **read permission for Google Workspace groups** even if Group Sync is disabled
- User authentication is email-domain-based; non-matching domains cannot authenticate (including admin users)
- Multiple Google Workspace domains supported via Settings > Identity Provider > "+ Add Domain"
- Only **active** Google Workspace users can sign in; inactive users sync but are blocked
- Real-time sync applies to **users only** (webhook); groups/OUs use polling

## Prerequisites
- Google Workspace admin account with one of:
  - Super Admin
  - Groups Admin
  - User Management Admin
  - Help Desk Admin
  - Custom role with **Users: Read** + **Groups: Read** under Admin API
- `Google Workspace Admin` must not be restricted in Security > API Controls

## Step-by-Step
1. Enable Google Workspace integration in Twingate Admin Console (Settings > Identity Provider)
2. Sign in to Google Workspace domain to authorize OAuth access
3. Configure Twingate app in Google Workspace Admin Console
4. Enable user and/or group sync via ⋯ action menu
5. (Optional) Enable Selective Sync via ⋯ action menu, then click "Manage Selection"

## Configuration Values

| Setting | Location | Notes |
|---|---|---|
| Group Sync | ⋯ action menu | Disabled by default |
| OU Sync | ⋯ action menu | Disabled by default |
| Selective Sync | "Manage Selection" button | Requires Group or OU sync enabled first |
| Manual Sync | ⋯ action menu > "Manually Sync Now" | May take several minutes to complete |

## Sync Polling Intervals
- **Starter plan**: Groups/OUs every 24 hours
- **Teams/Business/Enterprise**: Groups/OUs every 2 hours
- **Users**: Real-time via webhook

## Gotchas
- **Disabling Group/OU Sync behavior differs** based on Selective Sync state:
  - Selective Sync OFF: groups with Resource access → converted to Twingate Groups; others deleted
  - Selective Sync ON: **all** groups deleted, including those with Resource access
- Deselecting groups in Selective Sync **deletes them even if they have Resource access**
- **Always include your own account** in Selective Sync selection or risk locking yourself out
- API authorization failures likely mean `Google Workspace Admin` is set to **Restricted** — fix via unrestricting it or granting Twingate "Trusted" access in Third-Party App Access settings
- Only domains already configured in Google Workspace can be added as additional domains

## Data Synced
User first/last name, email, avatar; group membership (if Group Sync enabled)

## Related Docs
- Google Workspace multiple domains documentation
- Google Workspace administrator roles (Google Help Center)
- Twingate Selective Sync
- Twingate Group membership / Resources access
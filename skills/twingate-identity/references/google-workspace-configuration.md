# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to synchronize user accounts and delegate authentication via OAuth using the Google Workspace Directory API. Configuration is initiated from the Identity Provider section of the Twingate Admin Console. Group and OU sync are optional and disabled by default.

## Key Information
- Twingate requires **read permission for Google Workspace groups** even if Group Sync is disabled
- User authentication is delegated to Google; email must match configured domain(s)
- Only **active** Google Workspace users can sign in; inactive users sync but are blocked
- Real-time sync applies to **users only** (via webhook); groups/OUs use polling
- Data synced: first/last name, email, avatar, group membership (if enabled)

## Prerequisites
- Google Workspace admin account with one of:
  - Super Admin
  - Groups Admin
  - User Management Admin
  - Help Desk Admin
  - Custom role with **Users: Read** + **Groups: Read** under Admin API permissions
- Third-party API access must be unrestricted (or Twingate explicitly trusted)

## Step-by-Step
1. Go to **Settings > Identity Provider** in Twingate Admin Console
2. Enable Google Workspace integration and sign in to Google domain
3. Configure Twingate app in Google Workspace Admin Console
4. Enable user/group sync via the ⋯ action menu
5. (Optional) Enable Selective Sync via **Manage Selection** button

## Configuration Values

| Setting | Location | Notes |
|---|---|---|
| Add domain | Settings > Identity Provider > + Add Domain | Domain must pre-exist in Google Workspace |
| Group/OU Sync | ⋯ action menu | Disabled by default |
| Selective Sync | ⋯ action menu > Manage Selection | Limits which groups/OUs/users sync |
| Manual sync | ⋯ action menu > Manually Sync Now | Takes several minutes to complete |

## Sync Polling Periods
- **Starter plan**: Groups/OUs every 24 hours
- **Teams/Business/Enterprise**: Groups/OUs every 2 hours
- **Users**: Real-time via webhook

## Gotchas
- **API access errors**: Check `Security > API Controls > Manage Google Services`—if `Google Workspace Admin` is `Restricted`, either unrestrict it or mark Twingate as **Trusted** in Third-Party App Access
- **Selective Sync deletion**: Deselecting groups deletes them from Twingate even if they have Resource access
- **Disabling Group Sync**: If Selective Sync is OFF, groups with Resource access convert to Twingate Groups; if Selective Sync is ON, all synced groups/OUs are deleted
- **Admin lockout risk**: Always include your own account in Selective Sync selections
- **Domain restriction applies to admins**: Admin console users must also match configured domains

## Related Docs
- Google Workspace administrator roles (Google Help Center)
- Google Workspace multiple domains configuration
- Twingate Group Sync documentation
- Twingate Selective Sync
- Twingate Help Center
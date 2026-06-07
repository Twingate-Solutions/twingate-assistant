# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to sync user accounts, delegate authentication, and optionally sync groups/OUs via the Google Workspace Directory API using OAuth. Configuration is initiated from the Identity Provider section in the Twingate Admin Console.

## Key Information
- User changes sync in real-time via webhooks; groups/OUs use polling
- Group/OU sync polling: every 24h (Starter), every 2h (Teams/Business/Enterprise)
- "Manually Sync Now" schedules immediate sync but may take several minutes
- Twingate requires read permission for Google Workspace groups even if Group Sync is disabled
- Only active Google Workspace users can sign in; inactive users are synced but blocked
- Multiple domains supported via Settings > Identity Provider > "+ Add Domain"

## Prerequisites
- Google Workspace admin role (one of): Super Admin, Groups Admin, User Management Admin, Help Desk Admin, or custom role with **Users: Read** and **Groups: Read** under Admin API
- If API access restricted: either set Google Workspace Admin to "Unrestricted" OR mark Twingate as "Trusted" in Security > API Controls > Manage Third-Party App Access

## Step-by-Step
1. Enable Google Workspace integration in Twingate Admin Console (Settings > Identity Provider)
2. Sign in to your Google Workspace domain to authorize OAuth access
3. Configure the Twingate application in Google Workspace Admin Console
4. Enable user and/or group sync as needed
5. (Optional) Enable Selective Sync via the ⋯ action menu, then click "Manage Selection"

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| Group Sync | ⋯ action menu in Identity Provider | Disabled by default |
| OU Sync | ⋯ action menu in Identity Provider | Disabled by default |
| Selective Sync | "Manage Selection" button | Requires Group or OU sync enabled first |
| Additional domains | Settings > Identity Provider > "+ Add Domain" | Must be pre-configured in Google Workspace |

## Gotchas
- **Disabling Group/OU Sync behavior differs by Selective Sync state:**
  - Selective Sync OFF: groups/OUs with Resource access convert to Twingate Groups; others deleted
  - Selective Sync ON: ALL groups/OUs deleted, even those with Resource access
- **Selective Sync includes children**: syncs selected groups, their children, and all users in those groups
- **Admin lockout risk**: When configuring Selective Sync, ensure your own account is in a selected group
- **Domain restriction applies to admin users** as well as regular users
- **API authorization failures** often indicate restricted third-party app access in Google Workspace Security settings
- Twingate only reads: first/last name, email, avatars, group membership

## Related Docs
- Google Workspace Administrator Roles (Google Help Center)
- Google Workspace multiple domains documentation
- Twingate Group Sync documentation
- Twingate Selective Sync
- Twingate Help Center
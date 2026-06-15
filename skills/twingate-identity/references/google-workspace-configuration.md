# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to sync user accounts, delegate authentication, and optionally sync groups/OUs via the Google Workspace Directory API using OAuth. Admins configure the integration from Settings > Identity Provider in the Twingate Admin Console.

## Key Information
- User changes sync in real-time via webhooks; groups/OUs use polling
- Group/OU sync polling: every 24h (Starter), every 2h (Teams/Business/Enterprise)
- Group read permissions are required even if Group Sync is disabled
- Only active Google Workspace users can sign in; inactive users sync but are blocked
- Multiple Google Workspace domains are supported via Settings > Identity Provider > "+ Add Domain"

## Prerequisites
- Google Workspace admin role: Super Admin, Groups Admin, User Management Admin, Help Desk Admin, or custom role with **Users: Read** + **Groups: Read** under Admin API
- Third-party API access must not be restricted (Google Workspace Admin service must be Unrestricted, or Twingate explicitly trusted)

## Step-by-Step
1. Enable Google Workspace integration in Twingate Admin Console (Settings > Identity Provider)
2. Sign in to your Google Workspace domain to authorize OAuth access
3. Configure the Twingate application in Google Workspace Admin Console
4. Enable user/group sync as needed via the ⋯ action menu

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| Group Sync | ⋯ action menu on IdP settings | Disabled by default |
| OU Sync | ⋯ action menu on IdP settings | Disabled by default |
| Selective Sync | "Manage Selection" button | Requires Group or OU sync enabled first |
| Additional domains | Settings > Identity Provider > "+ Add Domain" | Domain must exist in Google Workspace first |

## Gotchas
- **API access control**: If authorization fails, check Security > API Controls > Manage Google Services — `Google Workspace Admin` may be set to `Restricted`. Fix by setting it to Unrestricted or explicitly trusting Twingate in Manage Third-Party App Access
- **Selective Sync self-lockout**: If you omit your own account from Selective Sync, you lose access — ensure your account is in at least one synced group
- **Disabling Group/OU Sync behavior**:
  - Selective Sync OFF: Groups with Resource access convert to Twingate Groups; others deleted
  - Selective Sync ON: All synced groups/OUs deleted regardless of Resource access
- **Deselecting groups in Selective Sync** deletes them even if they have Resource access
- "Manually Sync Now" schedules immediate sync but may still take several minutes

## Data Synced
Only: user first/last name, email addresses, avatars, group membership (if enabled)

## Related Docs
- [Twingate Group Sync](#)
- [Selective Sync](#)
- [Google Workspace administrator roles](https://support.google.com/a/answer/1219251)
- [Google Workspace multiple domains documentation](https://support.google.com/a/answer/182081)
# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to synchronize user accounts and delegate authentication via OAuth using the Google Workspace Directory API. Group and OU sync are optional and disabled by default. Configuration is initiated from the Twingate Admin Console under Settings > Identity Provider.

## Key Information
- Twingate requires **read permission for Google Workspace groups** even without Group Sync enabled
- User authentication is email-domain-based; users not matching configured domain(s) cannot authenticate
- Only **active** Google Workspace users can sign in; inactive users sync but are marked inactive
- Multiple domains supported via Settings > Identity Provider > "+ Add Domain"
- Synced data: first/last name, email, avatar, group membership (if enabled)

## Prerequisites
- Google Workspace admin with one of: Super Admin, Groups Admin, User Management Admin, Help Desk Admin, or custom role with **Users: Read** + **Groups: Read** under Admin API
- Third-party API access must not be restricted (or Twingate explicitly trusted)

## Step-by-Step
1. Enable Google Workspace integration in Twingate Admin Console (Settings > Identity Provider)
2. Sign in to Google Workspace domain to authorize OAuth access
3. Configure Twingate application in Google Workspace Admin Console
4. Enable user/group/OU sync as needed via the ⋯ action menu
5. Optionally configure Selective Sync via "Manage Selection" button

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| Group Sync | ⋯ action menu | Disabled by default |
| OU Sync | ⋯ action menu | Disabled by default |
| Selective Sync | "Manage Selection" button | Requires Group or OU sync enabled first |
| Additional domains | Settings > Identity Provider > "+ Add Domain" | Domain must exist in Google Workspace |

## Sync Behavior & Timing
- **User changes**: Real-time via webhook
- **Groups/OUs**: Polled periodically
  - Starter plan: every 24 hours
  - Teams/Business/Enterprise: every 2 hours
- "Manually Sync Now" schedules immediate start but may take several minutes

## Gotchas
- **Selective Sync**: Deselecting groups deletes them even if they have active Resource access
- **Disabling Group/OU Sync**: If Selective Sync is OFF, groups with Resource access convert to Twingate Groups; others are deleted. If Selective Sync is ON, ALL groups are deleted
- **Lock-out risk**: When configuring Selective Sync, ensure your own admin account is included in a selected group
- **API restriction errors**: Check Security > API Controls > Manage Google Services — `Google Workspace Admin` must not be `Restricted`, or explicitly trust Twingate under Manage Third-Party App Access
- Admin domain restriction applies to Twingate Admin Console admins as well as regular users

## Related Docs
- Twingate Group Sync documentation
- Twingate Selective Sync documentation
- Google Workspace administrator roles (Google Help Center)
- Google Workspace documentation for multi-domain setup
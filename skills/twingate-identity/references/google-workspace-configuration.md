# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to synchronize user accounts and delegate authentication via OAuth using the Google Workspace Directory API. User changes sync in real-time via webhooks; group and OU sync is polling-based with frequency depending on plan tier.

## Key Information
- Twingate requires **read permission for Google Workspace groups** even if Group Sync is disabled
- User email must match configured Google Workspace domain(s) for authentication
- Multiple domains supported via **Settings > Identity Provider > + Add Domain**
- Only data synced: first/last name, email, avatar, group membership (if enabled)

## Prerequisites
- Google Workspace admin with one of: Super Admin, Groups Admin, User Management Admin, Help Desk Admin, or custom role with **Users: Read** + **Groups: Read** under Admin API
- Google Workspace Admin API access must be **Unrestricted** (or Twingate explicitly trusted)

## Step-by-Step
1. Enable Google Workspace integration in Twingate Admin Console (Settings > Identity Provider)
2. Sign in to Google Workspace domain to authorize OAuth
3. Configure Twingate application in Google Workspace Admin Console
4. Enable user/group sync via ⋯ action menu in Identity Provider settings

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| Group Sync | ⋯ action menu | Disabled by default |
| OU Sync | ⋯ action menu | Disabled by default |
| Selective Sync | "Manage Selection" button | Requires Group or OU sync enabled first |
| Manual Sync | ⋯ action menu > "Manually Sync Now" | May take several minutes to complete |

## Sync Behavior
| Plan | Group/OU Poll Interval |
|---|---|
| Starter | Every 24 hours |
| Teams/Business/Enterprise | Every 2 hours |

- **User changes**: Real-time via webhook
- **Groups/OUs**: Polling only (no real-time API support)

## Gotchas
- **Selective Sync**: Deselecting groups deletes them from Twingate even if they have Resource access; always include your own account
- **Disabling Group/OU Sync**: If Selective Sync is OFF, groups with Resource access are converted to Twingate Groups; groups without access are deleted. If Selective Sync is ON, **all** synced groups/OUs are deleted
- **API access errors**: Check Google Workspace Admin Console at Security > API Controls > Manage Google Services — `Google Workspace Admin` must not be `Restricted`
- **Fix API restriction**: Either set Google Workspace Admin to Unrestricted, or go to Security > API Controls > Manage Third-Party App Access > find Twingate > set to "Trusted: Can access all Google services"
- Inactive Google Workspace users are synced but marked inactive in Twingate
- Domain restriction applies to Twingate Admin Console admins as well

## Related Docs
- Google Workspace multiple domains documentation (Google Help Center)
- Google Workspace administrator roles (Google Help Center)
- Twingate Group Sync configuration
- Twingate Selective Sync
- Twingate Help Center
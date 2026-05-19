# Google Workspace Configuration

## Summary
Twingate integrates with Google Workspace to synchronize user accounts and delegate authentication via OAuth and the Google Workspace Directory API. Configuration is initiated from the Twingate Admin Console under Settings > Identity Provider. Group and OU sync are optional and disabled by default.

## Key Information
- Twingate requires **read permission for Google Workspace groups** even if Group Sync is disabled
- User authentication is delegated to Google; email must match configured domain(s)
- Only **active** Google Workspace users can sign in; inactive users sync but are blocked
- Real-time sync applies only to **users** (via webhook); groups/OUs use polling
- Domain restriction applies to both end users and Twingate admin console users

## Prerequisites
- Google Workspace admin account with one of:
  - Super Admin
  - Groups Admin
  - User Management Admin
  - Help Desk Admin
  - Custom role with **Users: Read** + **Groups: Read** under Admin API
- Third-party API access must not be restricted (check Security > API Controls > Manage Google Services)

## Step-by-Step
1. In Twingate Admin Console: Settings > Identity Provider — enable Google Workspace integration and sign in to Google domain
2. Configure Twingate application in Google Workspace Admin Console
3. Enable user/group sync via the ⋯ action menu in Identity Provider settings
4. (Optional) Enable Selective Sync: enable group/OU sync, then click "Manage Selection"

## Configuration Values

| Setting | Location |
|---|---|
| Add additional domains | Settings > Identity Provider > "+ Add Domain" |
| Enable/disable Group or OU Sync | Identity Provider ⋯ action menu |
| Manual sync trigger | Identity Provider ⋯ action menu > "Manually Sync Now" |
| Selective Sync management | "Manage Selection" button in Selective Sync panel |

## Sync Polling Intervals
| Plan | Groups/OUs Sync Frequency |
|---|---|
| Starter | Every 24 hours |
| Teams / Business / Enterprise | Every 2 hours |

## Gotchas
- **API access blocked**: If authorization fails, check Security > API Controls > Manage Google Services — set Google Workspace Admin to "Unrestricted" OR whitelist Twingate as "Trusted" in Manage Third-Party App Access
- **Disabling Group/OU Sync with Selective Sync enabled**: ALL synced groups/OUs are deleted, even those with Resource access
- **Disabling Group/OU Sync with Selective Sync disabled**: Groups/OUs with Resource access are converted to Twingate Groups; others are deleted
- **Selective Sync**: Always include your own admin account in at least one synced group to avoid locking yourself out
- Manual sync may still take several minutes to complete after triggering
- Only domains already configured in Google Workspace can be added to Twingate

## Data Synced
- User first/last names, email addresses, avatars
- Group membership (only if Group Sync enabled)

## Related Docs
- Twingate Group Membership documentation
- Twingate Selective Sync
- Google Workspace administrator roles (Google Help Center)
- Google Workspace domain configuration (Google documentation)
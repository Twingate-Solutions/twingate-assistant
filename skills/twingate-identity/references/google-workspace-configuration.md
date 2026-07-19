# Google Workspace Configuration

## Page Title
Google Workspace Configuration for Twingate

## Summary
Twingate integrates with Google Workspace to sync user accounts, delegate authentication via OAuth, and optionally sync groups/OUs using the Google Workspace Directory API. Configuration is initiated from Settings > Identity Provider in the Twingate Admin Console. User changes sync in real-time via webhooks; group/OU sync is polling-based.

## Key Information
- Twingate **requires read permission for Google Workspace groups** even if Group Sync is disabled
- User email must match configured Google Workspace domain(s) to authenticate — applies to admin users too
- Multiple domains supported via Settings > Identity Provider > "+ Add Domain"
- Only active GW users can sign in; inactive users sync but are blocked
- Group/OU sync is **disabled by default**

## Prerequisites
- Google Workspace admin account with one of: Super Admin, Groups Admin, User Management Admin, Help Desk Admin, or custom role with **Users: Read** + **Groups: Read** under Admin API
- Google Workspace Admin API access must be unrestricted (or Twingate explicitly trusted)

## Step-by-Step
1. In Twingate Admin Console: Settings > Identity Provider — enable Google Workspace integration and sign in to GW domain
2. Configure Twingate app in Google Workspace Admin Console
3. Enable user and group sync as needed via the ⋯ action menu

## Configuration Values

| Setting | Location | Notes |
|---|---|---|
| Group Sync | ⋯ action menu in Identity Provider | Disabled by default |
| OU Sync | ⋯ action menu in Identity Provider | Disabled by default |
| Selective Sync | "Manage Selection" button | Requires Group or OU sync enabled first |
| Additional domains | Settings > Identity Provider > "+ Add Domain" | Must be pre-configured in GW |

## Sync Polling Periods
| Plan | Groups/OUs Sync Interval |
|---|---|
| Starter | Every 24 hours |
| Teams/Business/Enterprise | Every 2 hours |
| User changes | Real-time (webhook) |
| Manual sync | Immediate schedule, may take several minutes |

## Gotchas
- **API access errors**: Check Security > API Controls > Manage Google Services — `Google Workspace Admin` may be set to `Restricted`. Fix by setting to Unrestricted OR explicitly trusting Twingate in Manage Third-Party App Access
- **Selective Sync deletion risk**: Deselecting groups deletes them from Twingate even if they have active Resource access
- **Disabling Group Sync**: If Selective Sync is OFF, groups with Resource access convert to Twingate Groups; without Resource access they're deleted. If Selective Sync is ON, ALL groups are deleted
- **Self-lockout risk**: When configuring Selective Sync, ensure your own account is in a synced group — recover via another admin or Help Center
- Only domains already configured in Google Workspace can be added to Twingate

## Data Synced
- User first/last name, email, avatar
- Group membership (if Group Sync enabled)

## Related Docs
- Twingate Group membership docs
- Twingate Selective Sync
- Google Workspace administrator roles (Google Help Center)
- Google Workspace multiple domains documentation
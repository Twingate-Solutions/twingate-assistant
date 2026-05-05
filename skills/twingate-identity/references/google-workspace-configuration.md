## Google Workspace Configuration

How to integrate Google Workspace with Twingate -- enables OAuth user authentication, real-time user sync via webhook, and optional group/OU sync.

**No plan restriction** (unlike Okta/Entra ID/JumpCloud which are Business+).

### Two-Step Setup

**Step 1: Twingate Side -- Sign In with Google Workspace**

- Admin Console -> **Settings -> Identity Provider** -> Google Workspace section
- Authorize Twingate via OAuth -- requires admin permissions in Google Workspace

**Step 2: Configure Twingate App in Google Workspace + Enable Sync**

- Authorize user/group sync from the Google Workspace admin console

### Required Admin Permissions

To authorize the Google Workspace integration, the user must have **one of**:
- Super Admin
- Groups Admin
- User Management Admin
- Help Desk Admin
- A custom admin role with `Users: Read` + `Groups: Read` permissions under the Admin API

### Important: Group Read Permission Always Required

Twingate requires **read access to Google Workspace groups even if Group Sync is disabled** -- this is a baseline requirement. Group Sync itself is opt-in (disabled by default).

### Sync Behavior

| What | Sync Frequency |
|---|---|
| **User changes** | Real-time (webhook updates) |
| **Groups + OUs (Starter plan)** | Every 24 hours |
| **Groups + OUs (Teams/Business/Enterprise)** | Every 2 hours |

**Manually Sync Now**: triggers an immediate sync from the action menu (still takes a few minutes to complete).

### Selective Sync (Google Workspace Only)

Google's API doesn't support native sync scoping -- so Twingate provides **Selective Sync** to limit which users/groups/OUs are synced.

**Enabling Selective Sync:**
- Action menu -> **Manage Selection** in the Selective Sync panel
- Pick groups/OUs to sync
- **All children of selected groups + all users in synced groups** are synced
- Unselected groups/OUs (and users not in any synced group) are NOT synced

**Critical**: Sync your own admin account or you'll lose access. If you accidentally exclude yourself, another admin must re-add you (or contact Twingate Support).

### Disabling Group/OU Sync (after enabling)

Behavior depends on Selective Sync state:
- **Selective Sync OFF**: Groups with Resource access become Twingate Groups; Groups without are deleted
- **Selective Sync ON**: All synced Groups/OUs are deleted (even those with Resource access)

### User Authentication

- Twingate delegates auth to Google
- User's email must match a configured Google Workspace domain
- Multiple domains supported -- add more via **Settings > Identity Provider > + Add Domain** (only domains already in Google Workspace can be added)
- Users with non-matching email domains cannot authenticate

### Restricted Third-Party App Access

If authorizing Twingate fails: your Google Workspace likely has restricted app access. Two options:

1. Set `Google Workspace Admin` to **Unrestricted** (Security > API Controls > Manage Google Services)
2. Find Twingate in **Manage Third-Party App Access**, set to **Trusted: Can access all Google services**

### Data Privacy

Twingate syncs **only what's needed**:
- First/last name
- Email address
- Avatar
- Group membership (if Group Sync enabled)

### Gotchas

- Google Workspace user inactivity does **not** delete the user from Twingate -- inactive users sync as "inactive" (cannot sign in) but remain billable
- Real-time user webhook updates work; group/OU updates do not -- plan for sync delays (up to 2 hours on paid plans)
- Selective Sync deletion is destructive -- deselected groups are **deleted**, not unsynced; verify selection before saving
- Multi-domain accounts: each domain must be configured separately in Google Workspace; users on unconfigured domains cannot authenticate

### Related Docs

- /docs/identity-providers -- IdP overview
- /docs/groups -- Synced Groups + Selective Sync
- /docs/saas-app-gating-with-google-workspace -- Context-Aware Access for SaaS gating
- /docs/users -- User management

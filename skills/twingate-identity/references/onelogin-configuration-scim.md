## OneLogin SCIM User & Group Sync

How to set up SCIM provisioning between OneLogin and Twingate -- enables automatic user create/update/deactivate + group sync.

**Plan Requirements:**
- **Twingate Business or Enterprise**
- **OneLogin Unlimited Plan** (SCIM is gated by OneLogin's plan tier)

**Prerequisite:**
- The OneLogin Twingate application must already be installed (see /docs/onelogin-configuration)

### Supported SCIM Operations

- Create users in Twingate from OneLogin
- Update user attributes
- Deactivate users (when deactivated in OneLogin or removed from Twingate app)
- Provision groups + group membership

### User Sync Configuration

**Step 1: Get the SCIM Endpoint + Token from Twingate**
- Twingate Admin Console -> Identity Provider -> SCIM details

**Step 2: Paste into OneLogin**
- OneLogin Twingate app -> **Configuration** tab
- **SCIM Base URL**: paste the endpoint
- **SCIM Bearer Token**: paste the token
- Click **Enable**

**Step 3: Verify Username Mapping**
- **Parameters** tab -> verify **SCIM Username** mapping
- Default: maps `Username` to `SCIM Username`
- If OneLogin doesn't use the `Username` field as primary identifier (some configs use Email instead): change the mapping to **Email**
- This is the field Twingate uses to uniquely identify synced users

**Step 4: Enable Provisioning**
- **Provisioning** tab -> tick **Enable provisioning**
- Set **"When users are deleted in OneLogin..."** to **Delete** (otherwise deletions don't propagate)
- **Save**

**Optional but Recommended**: uncheck **"Require admin approval"** for create/delete/update -- otherwise every change requires manual approval in OneLogin's Users tab before syncing.

**Step 5: Reapply Mappings**
- **Users** tab -> **Apply to all** dropdown (top-right) -> **Reapply Mappings**
- If admin approval is unchecked: users sync immediately
- If approval is required: each user shows "Pending" until manually approved

### Group Sync Configuration

OneLogin's recommended approach: map **OneLogin Roles** to **SCIM Groups** (Roles are OneLogin's native group-based assignment mechanism).

**Step 1: Enable Groups in Parameters**
- **Parameters** tab -> **Optional Parameters** section
- Click **Groups** -> tick **"Include in User Provisioning"**
- **Save**
- Groups status should now be **Enabled**

**Step 2: Add a Rule to Map Roles to SCIM Groups**
- **Rules** tab -> **Add Rule**
- Name: e.g., "Synced groups"
- **Actions** section:
  - Action: **Set Groups in Twingate**
  - **For each**: `role`
  - **with value that matches**: `.*` (all roles), or a specific role name, or a regex pattern
- **Save**

**Step 3: Reapply Mappings**
- Users tab -> **Apply to all** -> **Reapply Mappings**

### Decision Notes

- Use Roles -> SCIM Groups -- it's idiomatic OneLogin and produces clean Twingate Groups
- Set OneLogin "When users are deleted -> Delete" -- otherwise deactivation doesn't propagate, leaving stale users in Twingate
- Uncheck admin approval to avoid manual sync friction (after testing)
- Map all roles via `.*` for simplicity; tighten later if needed

### Gotchas

- Default Username mapping must match OneLogin's actual user identifier -- check before enabling
- The "SCIM Base URL cannot be blank" error on initial app save is a known OneLogin UI bug -- use the placeholder workaround in /docs/onelogin-configuration before reaching this guide
- Pending approvals queue up if you forget to uncheck "Require admin approval" -- check OneLogin Users tab if syncs are stuck
- Removing a Role from a user in OneLogin removes the corresponding Twingate Group on next sync -- verify expected behavior

### Related Docs

- /docs/onelogin-configuration -- Required prerequisite (app install)
- /docs/scim-provisioning-api -- Underlying SCIM API
- /docs/groups -- Synced Group behavior
- /docs/identity-providers -- IdP overview

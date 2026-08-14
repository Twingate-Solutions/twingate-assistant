---
source: https://www.twingate.com/docs/onelogin-configuration-scim
type: docs
fetched: 2026-08-14
source_version: 935b4010633769baffa7bddf35500a5e5d71057d7a8f6ed22aa0e88cfdb758de
---

# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM-based provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, updates, deactivation, and group membership sync.

## Key Information
- Supported operations: create users, update attributes, deactivate users, provision groups/membership
- Requires Twingate **Business or Enterprise** plan
- SCIM sync is unidirectional: OneLogin → Twingate

## Prerequisites
- OneLogin Twingate application configured (separate setup step)
- Twingate Business or Enterprise plan
- SCIM Endpoint and SCIM Token from Twingate Admin Console

## User Sync Configuration

1. Copy **SCIM Endpoint** and **SCIM Token** from Twingate Admin Console
2. In OneLogin Twingate app → **Configuration** tab: paste into **SCIM Base URL** and **SCIM Bearer Token** fields → click **Enable**
3. In **Parameters** tab: verify **SCIM Username** mapping
   - Default: maps `Username` → `SCIM Username`
   - If not using Username field: change mapping to `Email`
4. In **Provisioning** tab:
   - Check **Enable provisioning**
   - Set "When users are deleted in OneLogin…" → **Delete**
   - Click **Save**
5. In **Users** tab: click **Apply to all** → **Reapply Mappings**

## Group Sync Configuration

1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. **Rules** tab → **Add Rule**:
   - Actions: **Set Groups in Twingate**
   - For each: `role`
   - With value matching: `.*` (all roles) or specific pattern
   - Save
3. **Users** tab → **Apply to all** → **Reapply Mappings**

## Configuration Values

| Field | Source | Destination |
|-------|--------|-------------|
| SCIM Base URL | Twingate Admin Console (SCIM Endpoint) | OneLogin Configuration tab |
| SCIM Bearer Token | Twingate Admin Console (SCIM Token) | OneLogin Configuration tab |

## Gotchas
- **Admin approval**: By default enabled — requires manual approval per user before sync. Uncheck "Require admin approval" for create/delete/update to enable automatic sync.
- **Deletion behavior**: Must explicitly set deletion action to **Delete** (not default); otherwise deactivated users won't be removed from Twingate.
- **SCIM Username field**: Must match the field actually used for usernames in your OneLogin config — use `Email` if `Username` is not populated.
- **Group sync**: Uses OneLogin Roles as the recommended mapping mechanism; any attribute can technically be used but Roles is default.
- Users show as **Pending** state until manually approved if admin approval is enabled.

## Related Docs
- OneLogin Twingate application setup (prerequisite)
- Twingate SCIM overview
- OneLogin provisioning documentation
# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, updates, deactivation, and group membership sync.

## Key Information
- Supported operations: create users, update attributes, deactivate users, provision groups/membership
- Requires **Business or Enterprise** Twingate plan
- Must complete OneLogin Twingate app setup before configuring SCIM

## Prerequisites
- OneLogin Twingate application configured in OneLogin app catalog
- Twingate Business or Enterprise plan
- SCIM Endpoint and SCIM Token from Twingate Admin Console

## Step-by-Step

### User Sync
1. Copy **SCIM Endpoint** and **SCIM Token** from Twingate Admin Console
2. In OneLogin Twingate app → **Configuration** tab: paste into **SCIM Base URL** and **SCIM Bearer Token** fields → click **Enable**
3. In **Parameters** tab: verify **SCIM Username** mapping
   - Default: maps `Username` → `SCIM Username`
   - If not using Username field: change mapping to `Email`
4. In **Provisioning** tab:
   - Check **Enable provisioning**
   - Set "When users are deleted in OneLogin…" to **Delete**
   - Optionally uncheck "Require admin approval" for create/delete/update
   - Click **Save**
5. In **Users** tab: click **Apply to all** → **Reapply Mappings**

### Group Sync
1. In **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. In **Rules** tab → **Add Rule**:
   - Actions: **Set Groups in Twingate**
   - For each: `role`
   - With value matching: `.*` (all roles) or specific pattern
   - Save
3. In **Users** tab: **Apply to all** → **Reapply Mappings**

## Configuration Values
| Field | Source | Destination |
|-------|--------|-------------|
| SCIM Base URL | Twingate Admin Console (SCIM Endpoint) | OneLogin Configuration tab |
| SCIM Bearer Token | Twingate Admin Console (SCIM Token) | OneLogin Configuration tab |

## Gotchas
- **Admin approval**: If enabled, all sync changes remain in "Pending" state until manually approved per user — uncheck for automatic sync
- **Username vs Email**: Default SCIM Username mapping uses `Username` field; switch to `Email` if your OneLogin setup doesn't populate Username
- **Deletion behavior**: Must explicitly set deleted users option to `Delete` (not the default)
- Group sync requires both the Parameters configuration AND a Rules mapping — neither alone is sufficient
- Must run **Reapply Mappings** after any configuration change to sync existing users

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate Admin Console (SCIM credentials location)
# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, updates, deactivation, and group membership sync.

## Key Information
- Supported operations: create users, update attributes, deactivate users, provision groups/membership
- SCIM username field is used as the unique identifier for synced users
- Groups are synced via OneLogin Roles mapped to SCIM Groups using Rules

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Twingate application already configured (catalog app)
- SCIM Endpoint and SCIM Token from Twingate Admin Console

## User Sync Configuration

1. Copy **SCIM Endpoint** and **SCIM Token** from Twingate Admin Console
2. In OneLogin Twingate app → **Configuration** tab: paste into **SCIM Base URL** and **SCIM Bearer Token** → click **Enable**
3. In **Parameters** tab: verify **SCIM Username** mapping
   - Default: maps `Username` → `SCIM Username`
   - If not using Username field: change mapping to `Email`
4. In **Provisioning** tab:
   - Check **Enable provisioning**
   - Set "When users are deleted in OneLogin" → **Delete**
   - Optionally uncheck **Require admin approval** for all 3 actions
   - Click **Save**
5. In **Users** tab: **Apply to all** → **Reapply Mappings**

## Group Sync Configuration

1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. **Rules** tab → **Add Rule**:
   - Actions: `Set Groups in Twingate`
   - For each: `role`
   - With value matching: `.*` (all roles) or specific pattern
   - Save
3. **Users** tab → **Apply to all** → **Reapply Mappings**

## Configuration Values

| Field | Source |
|-------|--------|
| SCIM Base URL | Twingate Admin Console → SCIM Endpoint |
| SCIM Bearer Token | Twingate Admin Console → SCIM Token |
| SCIM Username mapping | `Username` (default) or `Email` |
| Role regex pattern | `.*` for all roles |

## Gotchas
- **Admin approval**: If left enabled, all synced users show "Pending" status until manually approved in the Users tab
- **Deletion behavior**: Must explicitly set deleted user action to "Delete" — default may not remove users from Twingate
- **SCIM Username**: Must match the field actually used in your OneLogin config; wrong mapping causes user identification failures
- **Group sync**: Requires both the Parameters change AND a Rules mapping — neither alone is sufficient
- **Reapply Mappings**: Must be run after both user and group configuration changes to trigger immediate sync

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate Admin Console (SCIM token generation)
# OneLogin SCIM User & Group Sync Configuration

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, attribute updates, deactivation, and group membership sync.

## Key Information
- Supported plans: Business and Enterprise only
- Prerequisite: OneLogin Twingate application must be configured before SCIM setup
- SCIM identifies users uniquely via **SCIM Username** field (maps to Username or Email)

## Supported SCIM Features
- Create users
- Update user attributes
- Deactivate users (when deactivated in OneLogin or removed from app)
- Provision groups and group membership

## User Sync Configuration

### Steps
1. Copy **SCIM Endpoint** and **SCIM Token** from Twingate Admin Console
2. In OneLogin Twingate app → **Configuration** tab: paste into **SCIM Base URL** and **SCIM Bearer Token** → click **Enable**
3. In **Parameters** tab: verify **SCIM Username** mapping
   - Default: `Username` → `SCIM Username`
   - If not using Username field: change mapping to `Email`
4. In **Provisioning** tab:
   - Check **Enable provisioning**
   - Set "When users are deleted in OneLogin…" → **Delete**
   - Click **Save**
5. In **Users** tab → **Apply to all** dropdown → **Reapply Mappings**

## Group Sync Configuration

### Steps
1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. **Rules** tab → **Add Rule**:
   - Actions: **Set Groups in Twingate**
   - For each: `role`
   - Value matches: `.*` (all roles) or specific regex pattern
   - Save
3. **Users** tab → **Apply to all** → **Reapply Mappings**

## Configuration Values
| Field | Source | Destination |
|-------|--------|-------------|
| SCIM Endpoint | Twingate Admin Console | OneLogin SCIM Base URL |
| SCIM Token | Twingate Admin Console | OneLogin SCIM Bearer Token |

## Gotchas
- **Admin approval**: If "Require admin approval" is enabled, all changes stay **Pending** until manually approved per user — uncheck for all 3 actions (create, delete, update) to enable automatic sync
- **Deletion behavior**: Must explicitly set deleted users action to **Delete** (not default)
- **SCIM Username mapping**: If users are identified by email in OneLogin (not Username), must change mapping to `Email` or sync will fail/mismatch
- Group sync requires both the Parameters config AND a Rules mapping — neither alone is sufficient
- Must **Reapply Mappings** after both user and group config changes to trigger initial sync

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate Admin Console (SCIM endpoint/token source)
# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, attribute updates, deactivation, and group membership sync.

## Key Information
- Supported operations: create users, update attributes, deactivate users, provision groups/membership
- Requires Twingate **Business or Enterprise** plan
- SCIM Username field is used as the unique identifier for synced users

## Prerequisites
- OneLogin Twingate application configured in OneLogin app catalog
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
   - Set "When users are deleted in OneLogin" → **Delete**
   - Optionally uncheck "Require admin approval" for create/delete/update
   - Click **Save**
5. In **Users** tab → **Apply to all** dropdown → **Reapply Mappings**

### Group Sync
1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. **Rules** tab → **Add Rule**:
   - Actions: `Set Groups in Twingate`
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
- **Admin approval enabled**: Users/groups remain in "Pending" state until manually approved in the Users tab — sync does not happen automatically
- **Deletion behavior**: Must explicitly set deleted users action to `Delete`; default may not remove users from Twingate
- **SCIM Username mapping**: If your org uses Email as primary identifier (not Username), the default mapping will fail to correctly identify users
- **Group sync**: Recommended to use OneLogin Roles (not arbitrary attributes) as the source for SCIM Groups
- **Reapply Mappings**: Must be run after both initial setup and after adding group sync rules to trigger sync

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate Admin Console — SCIM configuration section
# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, attribute updates, deactivation, and group membership sync.

## Key Information
- Supported operations: create users, update attributes, deactivate users, provision groups/membership
- Requires Twingate **Business or Enterprise** plan
- SCIM Username field uniquely identifies synchronized users

## Prerequisites
- OneLogin Twingate application configured (catalog app)
- Twingate Business or Enterprise plan
- SCIM Endpoint and SCIM Token from Twingate Admin Console

## Step-by-Step

### User Sync
1. Copy **SCIM Endpoint** and **SCIM Token** from Twingate Admin Console
2. In OneLogin Twingate app → **Configuration** tab: paste into **SCIM Base URL** and **SCIM Bearer Token** → click **Enable**
3. In **Parameters** tab: verify **SCIM Username** mapping
   - Default: maps `Username` → `SCIM Username`
   - If not using Username field: change mapping to `Email`
4. In **Provisioning** tab:
   - Check **Enable provisioning**
   - Set "When users are deleted in OneLogin…" → **Delete**
   - Click **Save**
5. In **Users** tab: **Apply to all** → **Reapply Mappings**

### Group Sync
1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. **Rules** tab → **Add Rule**:
   - Actions: **Set Groups in Twingate**
   - For each: `role`
   - With value matching: `.*` (all roles) or specific regex pattern
   - **Save**
3. **Users** tab → **Apply to all** → **Reapply Mappings**

## Configuration Values
| Field | Source | Destination |
|-------|--------|-------------|
| SCIM Base URL | Twingate Admin Console (SCIM Endpoint) | OneLogin Configuration tab |
| SCIM Bearer Token | Twingate Admin Console (SCIM Token) | OneLogin Configuration tab |

## Gotchas
- **Admin approval**: If "Require admin approval" is enabled, all syncs remain **Pending** until manually approved in the Users tab — uncheck for all 3 actions (create, delete, update) to auto-sync
- **Deletion behavior**: Must explicitly set deleted users action to **Delete**; default may differ
- **Username vs Email**: If OneLogin users don't use the Username field, SCIM sync will fail to match users — switch mapping to Email
- **Group sync via Roles**: OneLogin supports mapping any attribute to SCIM Group, but Roles is the recommended mechanism

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate Admin Console SCIM configuration
# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, updates, deactivation, and group membership sync.

## Key Information
- Supported plans: **Business and Enterprise** only
- Prerequisite: OneLogin Twingate application must be configured before SCIM setup
- Supported operations: create users, update attributes, deactivate users, provision groups/membership

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Twingate application already configured (from OneLogin app catalog)
- SCIM Endpoint and SCIM Token from Twingate Admin Console

## User Sync Configuration

1. Copy **SCIM Endpoint** and **SCIM Token** from Twingate Admin Console
2. In OneLogin Twingate app → **Configuration** tab: paste into **SCIM Base URL** and **SCIM Bearer Token** fields → click **Enable**
3. In **Parameters** tab: verify **SCIM Username** mapping
   - Default: maps `Username` → `SCIM Username`
   - If not using Username field, change mapping to `Email` instead
4. In **Provisioning** tab:
   - Check **Enable provisioning**
   - Set "When users are deleted in OneLogin…" to **Delete**
   - Click **Save**
5. In **Users** tab → **Apply to all** dropdown → **Reapply Mappings**

## Group Sync Configuration

1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. **Rules** tab → **Add Rule**:
   - Actions: **Set Groups in Twingate**
   - For each: `role`
   - With value that matches: `.*` (all roles) or specific regex pattern
   - Save
3. **Users** tab → **Apply to all** → **Reapply Mappings**

## Configuration Values

| Field | Source | Destination |
|-------|--------|-------------|
| SCIM Base URL | Twingate Admin Console (SCIM Endpoint) | OneLogin Configuration tab |
| SCIM Bearer Token | Twingate Admin Console (SCIM Token) | OneLogin Configuration tab |

## Gotchas

- **Admin approval**: By default, admin approval may be required for create/delete/update actions — uncheck "Require admin approval" for all 3 to enable automatic sync; otherwise changes stay "Pending"
- **Username vs Email**: If users don't use the Username field in OneLogin, SCIM Username mapping must be changed to Email or users won't be uniquely identified correctly
- **Deletion behavior**: Must explicitly set deleted users action to **Delete** (not the default)
- **Group sync uses Roles**: SCIM can map any attribute to groups, but OneLogin's Role attribute is the recommended approach

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate Admin Console (SCIM Endpoint/Token location)
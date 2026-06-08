# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, attribute updates, deactivation, and group membership sync.

## Key Information
- Supported operations: create users, update attributes, deactivate users, provision groups/membership
- Required plan: Business or Enterprise
- Prerequisite: OneLogin Twingate application must be configured before SCIM setup

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Twingate application set up from OneLogin's app catalog
- SCIM Endpoint and SCIM Token from Twingate Admin Console

## User Sync Configuration

1. Copy **SCIM Endpoint** and **SCIM Token** from Twingate Admin Console
2. In OneLogin Twingate app → **Configuration** tab: paste into **SCIM Base URL** and **SCIM Bearer Token** fields → click **Enable**
3. In **Parameters** tab: verify **SCIM Username** mapping
   - Default: maps "Username" → "SCIM Username"
   - If not using Username field: change mapping to "Email"
4. In **Provisioning** tab:
   - Check **Enable provisioning**
   - Set "When users are deleted in OneLogin…" → **Delete**
   - Recommended: uncheck "Require admin approval" for create/delete/update
   - Click **Save**
5. In **Users** tab: click **Apply to all** → **Reapply Mappings**

## Group Sync Configuration

1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. **Rules** tab → **Add Rule**:
   - Actions: **Set Groups in Twingate**
   - For each: `role`
   - With value matching: `.*` (all roles) or specific regex pattern
   - Save
3. **Users** tab → **Apply to all** → **Reapply Mappings**

## Configuration Values

| Field | Source | Destination |
|-------|--------|-------------|
| SCIM Base URL | Twingate Admin Console (SCIM Endpoint) | OneLogin Configuration tab |
| SCIM Bearer Token | Twingate Admin Console (SCIM Token) | OneLogin Configuration tab |

## Gotchas
- If "Require admin approval" is enabled, all sync changes remain **Pending** until manually approved in the Users tab
- SCIM Username mapping must match the field actually used in OneLogin (Username vs Email); incorrect mapping breaks user identification
- Group sync requires both enabling the Groups parameter AND creating a role-mapping rule — neither alone is sufficient
- Must run **Reapply Mappings** after both user and group configuration changes to trigger initial sync

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate Admin Console (SCIM Endpoint/Token location)
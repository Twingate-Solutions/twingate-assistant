# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, attribute updates, deactivation, and group membership sync.

## Key Information
- Supported operations: create users, update attributes, deactivate users, provision groups/memberships
- Requires **Business or Enterprise** Twingate plan
- SCIM token and endpoint come from Twingate Admin Console

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
   - Set "When users are deleted in OneLogin…" to **Delete**
   - Uncheck "Require admin approval" for create/delete/update (optional but recommended)
   - Click **Save**
5. In **Users** tab → **Apply to all** → **Reapply Mappings**

### Group Sync
1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → **Save**
2. **Rules** tab → **Add Rule**:
   - Set action: **Set Groups in Twingate**
   - For each: `role`
   - With value matching: `.*` (all roles) or specific pattern
   - Save
3. **Users** tab → **Apply to all** → **Reapply Mappings**

## Configuration Values
| Field | Source | Maps To |
|-------|--------|---------|
| SCIM Base URL | Twingate Admin Console (SCIM Endpoint) | OneLogin Configuration tab |
| SCIM Bearer Token | Twingate Admin Console (SCIM Token) | OneLogin Configuration tab |
| SCIM Username | OneLogin `Username` or `Email` | Twingate user identifier |

## Gotchas
- **Admin approval enabled**: user/group changes stay in "Pending" state until manually approved in Users tab
- **Deletion behavior**: must explicitly set deleted users action to `Delete`; default may not remove users from Twingate
- **Group sync**: roles (not custom attributes) are the recommended mapping source for groups
- Must run **Reapply Mappings** after both initial setup and any rule changes to trigger sync

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate Admin Console (SCIM endpoint/token location)
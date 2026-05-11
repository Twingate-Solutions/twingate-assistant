# Configure SCIM User & Group Sync (OneLogin)

## Summary
Configures SCIM provisioning between OneLogin and Twingate to sync users and groups. Requires the OneLogin Twingate application to be set up first. Supports user creation, attribute updates, deactivation, and group membership sync.

## Key Information
- Supported plans: Business and Enterprise only
- Prerequisite: OneLogin Twingate application must already be configured
- SCIM uniquely identifies users via **SCIM Username** field
- Group sync uses OneLogin **Roles** mapped to SCIM Groups (recommended)

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Twingate application configured in catalog
- SCIM Endpoint and SCIM Token from Twingate Admin Console

## Supported SCIM Features
- Create users
- Update user attributes
- Deactivate users (on OneLogin deactivation or removal from app)
- Provision groups and group membership

---

## Step-by-Step: User Sync

1. Copy **SCIM Endpoint** and **SCIM Token** from Twingate Admin Console
2. In OneLogin Twingate app → **Configuration** tab: paste into **SCIM Base URL** and **SCIM Bearer Token** → click **Enable**
3. In **Parameters** tab: verify **SCIM Username** mapping
   - Default: `Username` → `SCIM Username`
   - If not using Username field: change mapping to `Email`
4. In **Provisioning** tab:
   - Check **Enable provisioning**
   - Set "When users are deleted in OneLogin…" → **Delete**
   - Save
5. In **Users** tab: **Apply to all** → **Reapply Mappings**

---

## Step-by-Step: Group Sync

1. **Parameters** tab → **Optional Parameters** → click **Groups** → check **Include in User Provisioning** → Save
2. **Rules** tab → **Add Rule**:
   - Actions: `Set Groups in Twingate`
   - For each: `role`
   - Value matches: `.*` (all roles) or specific pattern
   - Save
3. **Users** tab → **Apply to all** → **Reapply Mappings**

---

## Configuration Values

| OneLogin Field | Source |
|---|---|
| SCIM Base URL | Twingate Admin Console → SCIM Endpoint |
| SCIM Bearer Token | Twingate Admin Console → SCIM Token |
| SCIM Username mapping | `Username` or `Email` |
| Deleted user behavior | `Delete` |

---

## Gotchas
- **Admin approval**: If "Require admin approval" is enabled, all changes stay in **Pending** state until manually approved — uncheck for all 3 actions (create, delete, update) to auto-sync
- **Deletion behavior** must be explicitly set to `Delete`; default may not deactivate users in Twingate
- **Reapply Mappings** must be triggered manually after any configuration change to push updates to existing users
- Group sync requires a Rule mapping roles → SCIM Groups; it is not automatic

## Related Docs
- OneLogin Twingate Application Setup (prerequisite)
- Twingate SCIM general documentation
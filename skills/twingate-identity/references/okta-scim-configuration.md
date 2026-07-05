# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM-based provisioning between Okta and Twingate to sync users and groups. Requires the Twingate Okta app to be installed first and a Business or Enterprise plan. Supports user create, update, deactivation, and group push operations.

## Key Information
- Supported operations: create users, update attributes, deactivate users, push groups
- Plan requirement: Business or Enterprise only
- SCIM endpoint is pre-configured during initial app installation — no need to re-enter it
- Do **not** modify SCIM Attribute Mappings in Okta
- Previously assigned users sync immediately upon enabling provisioning

## Prerequisites
- Twingate app installed from Okta Integration Catalog (see Okta app configuration article)
- Business or Enterprise Twingate plan
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, open Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy **SCIM Token** from Twingate Admin Console
3. Enable **API Integration**, paste SCIM Token, click **Test API Credentials** to verify
4. Under Provisioning tab, enable all 3 provisioning options → **Save**

### Push Groups
1. Go to **Push Groups** tab → click **Push Groups** → select **Find groups by name**
2. Search for group, select it → **Save**

## Configuration Values
| Parameter | Value |
|-----------|-------|
| SCIM Token | Copied from Twingate Admin Console |
| SCIM Endpoint | Pre-configured (do not modify) |
| Attribute Mappings | Do not change |

## Gotchas
- **Users must be assigned to the Twingate app** — pushing a group to Twingate does NOT sync group members unless those users are also assigned to the app
- **Removing a user from a group does not remove them from Twingate** if they are individually assigned to the app. Must remove from the app itself, OR use group-only assignment so removing from group cascades removal
- To ensure full group sync, assign the group (not individual users) to the Twingate app in Okta
- Group members added before SCIM setup were synced immediately upon enabling provisioning

## Related Docs
- Okta app configuration article (initial setup / Integration Catalog)
- Twingate SCIM overview article
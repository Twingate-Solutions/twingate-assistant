# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM-based provisioning to sync users and groups from Okta to Twingate. Requires the Twingate Okta app to be installed first before enabling SCIM. Supports user creation, attribute updates, deactivation, and group push.

## Key Information
- Supported features: create users, update user attributes, deactivate users, push groups
- Deactivation triggers: user deactivated in Okta OR removed from Twingate Okta app
- SCIM endpoint is pre-configured during initial app installation — do not re-enter it
- Do not modify SCIM Attribute Mappings in Okta

## Prerequisites
- Twingate Business or Enterprise plan
- Twingate app installed from Okta Integration Catalog
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, open the Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy the SCIM Token from the Twingate Admin Console
3. Check **Enable API Integration**, paste the SCIM Token → click **Test API Credentials** to verify
4. Under **Provisioning** tab, enable all 3 provisioning options → click **Save**
   - Previously assigned users sync to Twingate immediately upon save

### Push Groups
1. Go to **Push Groups** tab → click **Push Groups** → select **Find groups by name**
2. Search for and select the group → click **Save**

## Configuration Values
| Field | Value |
|-------|-------|
| API Token | SCIM Token from Twingate Admin Console |
| SCIM Endpoint | Pre-configured (do not change) |
| Attribute Mappings | Do not modify |

## Gotchas
- **Users must be assigned to the app** to sync group membership correctly. Pushing a group alone does not sync members unless they are also app-assigned.
- **Removing a user from a group does not remove them from Twingate** if they are individually assigned to the app — you must remove them from the app itself.
- Exception: if only groups (not individual users) are assigned to the app, removing a user from all push groups will remove them from Twingate.
- Assign groups to the app (not just push them) to guarantee all group members sync correctly.

## Related Docs
- [Okta configuration overview](https://www.twingate.com/docs/okta) — initial app setup
- Okta app configuration article — assigning groups to the app
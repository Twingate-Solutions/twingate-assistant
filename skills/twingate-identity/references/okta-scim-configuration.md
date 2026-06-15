# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM provisioning between Okta and Twingate to sync users and groups. Requires the Twingate Okta app from the Integration Catalog to be installed first. Supports user creation, attribute updates, deactivation, and group push.

## Key Information
- Supported features: create users, update attributes, deactivate users, push groups
- SCIM endpoint is pre-configured during initial app installation — do not re-enter it
- Do not modify SCIM Attribute Mappings in Okta
- Previously assigned users sync to Twingate immediately upon enabling provisioning

## Prerequisites
- Twingate **Business or Enterprise** plan
- Twingate app installed from Okta Integration Catalog (see Okta app configuration article)
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, open the Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy the **SCIM Token** from the Twingate Admin Console
3. Enable **API Integration**, paste the SCIM Token → click **Test API Credentials** to verify
4. Under Provisioning tab, enable all 3 provisioning options → click **Save**

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
- **Users must be assigned to the app** to sync — pushing a group to Twingate does not sync members unless they are also assigned to the Twingate app in Okta
- **Removing a user from a group does not remove them from Twingate** if they are individually assigned to the app; must remove them from the app itself
- Exception: if only groups (not individual users) are assigned to the app, removing a user from all push groups will remove them from Twingate
- Best practice: assign groups to the app (not individual users) so group membership changes propagate correctly

## Related Docs
- Okta app configuration overview (Integration Catalog setup)
- Twingate Admin Console (SCIM Token location)
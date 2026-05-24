# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM-based provisioning between Okta and Twingate to sync users and groups. Requires the Twingate Okta app to be installed first. Available on Business and Enterprise plans only.

## Key Information
- Supported operations: create users, update user attributes, deactivate users, push groups
- SCIM endpoint is pre-configured during initial app installation — no manual entry needed
- Do **not** modify SCIM Attribute Mappings in Okta
- Previously assigned users sync to Twingate immediately upon enabling provisioning

## Prerequisites
- Twingate Business or Enterprise plan
- Twingate app installed from Okta Integration Catalog
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, open the Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy the SCIM Token from the Twingate Admin Console
3. Enable **API Integration**, paste the SCIM Token, click **Test API Credentials**
4. Enable all 3 provisioning options under the Provisioning tab → **Save**

### Push Groups
1. Go to **Push Groups** tab → click **Push Groups** → select **Find groups by name**
2. Search for and select the group → **Save**

## Configuration Values
| Field | Value |
|-------|-------|
| SCIM Token | Copied from Twingate Admin Console |
| SCIM Endpoint | Pre-configured (do not change) |
| Attribute Mappings | Do not modify |

## Gotchas
- **Group members won't sync** unless those users are also assigned to the Twingate app in Okta — group push alone is insufficient
- **Removing a user from a group does not remove them from Twingate** if they are individually assigned to the app; must remove them from the app itself
- Best practice: assign groups (not individual users) to the app so group membership changes automatically propagate
- Only users already assigned to the app at provisioning time will have correct group membership on initial sync

## Related Docs
- Okta app initial setup / Integration Catalog configuration
- Okta SCIM overview article
- Twingate Admin Console (SCIM Token location)
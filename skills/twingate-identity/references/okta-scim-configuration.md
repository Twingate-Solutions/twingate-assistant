# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM-based provisioning between Okta and Twingate to sync users and groups. Requires the Twingate Okta app to be installed first. Supported on Business and Enterprise plans only.

## Key Information
- Supported features: create users, update user attributes, deactivate users, push groups
- SCIM endpoint is pre-configured during initial app installation — do not re-enter it
- Do not modify SCIM Attribute Mappings
- Previously assigned users sync to Twingate immediately upon enabling provisioning

## Prerequisites
- Twingate Business or Enterprise plan
- Twingate app installed from Okta Integration Catalog
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, open the Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy the **SCIM Token** from Twingate Admin Console
3. Enable **API Integration**, paste the SCIM Token, verify with **Test API Credentials**
4. Under Provisioning tab, enable all 3 provisioning options → **Save**

### Push Groups
1. Under **Push Groups** tab → **Push Groups** button → **Find groups by name**
2. Search for group, select it → **Save**

## Configuration Values
| Field | Value |
|-------|-------|
| SCIM Token | Copied from Twingate Admin Console |
| SCIM Endpoint | Pre-configured (do not change) |
| Attribute Mappings | Do not modify |

## Gotchas
- **Users must be assigned to the Twingate app** — pushing a group does not sync members unless they are also assigned to the app directly or via group assignment
- **Removing a user from a group does not remove them from Twingate** if they are individually assigned to the app; must remove from the app itself
- Best practice: assign groups (not individual users) to the app so group membership changes propagate correctly to Twingate
- Only users already assigned to the app at provisioning time will have correct group membership on initial sync

## Related Docs
- Okta app configuration overview (initial installation)
- Twingate Admin Console (SCIM Token location)
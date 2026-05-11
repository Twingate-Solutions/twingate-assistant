# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM-based provisioning between Okta and Twingate to sync users and groups. Requires the Twingate Okta app to be installed first. Available on Business and Enterprise plans only.

## Key Information
- Supported operations: create users, update user attributes, deactivate users, push groups
- SCIM endpoint is pre-configured during initial app installation — no need to re-enter it
- Do not modify SCIM Attribute Mappings in Okta
- Previously assigned users sync to Twingate immediately upon enabling provisioning

## Prerequisites
- Twingate Business or Enterprise plan
- Twingate app installed from Okta Integration Catalog
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, go to Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy SCIM Token from Twingate Admin Console
3. Enable **API Integration**, paste SCIM Token, verify with **Test API Credentials**
4. Under Provisioning tab, enable all 3 provisioning options → **Save**

### Push Groups
1. Go to **Push Groups** tab → **Push Groups** button → **Find groups by name**
2. Search for group, select it → **Save**

## Gotchas
- **Users must be assigned to the Twingate app** to sync correctly — pushing a group alone does not sync members unless those members are also assigned to the app
- **Removing a user from a group does not remove them from Twingate** if they are individually assigned to the app; you must remove them from the app directly
- Clean alternative: assign only groups (not individual users) to the app — then removing a user from all push groups removes them from Twingate
- To ensure complete group membership sync, assign the group to the app (not just configure group push)

## Configuration Values
| Field | Value |
|-------|-------|
| SCIM Token | Retrieved from Twingate Admin Console |
| SCIM Endpoint | Pre-configured (do not change) |
| Attribute Mappings | Do not modify |

## Related Docs
- Okta configuration overview article
- Twingate app setup from Okta Integration Catalog (initial installation)
- Okta app configuration article (group assignment)
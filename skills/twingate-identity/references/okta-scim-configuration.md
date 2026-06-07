# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM provisioning between Okta and Twingate to sync users and groups. Requires the Twingate Okta app to be installed first, then connected via a SCIM token from Twingate's Admin Console.

## Key Information
- Supported operations: create users, update user attributes, deactivate users, push groups
- Deactivation triggers: user deactivated in Okta OR removed from Twingate Okta app
- Do **not** modify SCIM Attribute Mappings in Okta
- Previously assigned users sync immediately upon enabling provisioning

## Prerequisites
- Twingate **Business or Enterprise** plan
- Twingate app installed from Okta Integration Catalog (SCIM endpoint pre-configured during install)
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy SCIM Token from Twingate Admin Console
3. Enable **API Integration**, paste SCIM Token → click **Test API Credentials** to validate
4. Under Provisioning tab, enable all 3 provisioning options → **Save**

### Push Groups
1. **Push Groups** tab → **Push Groups** button → **Find groups by name**
2. Search for group → select → **Save**

## Configuration Values
| Parameter | Value |
|-----------|-------|
| SCIM Endpoint | Pre-configured (set during app install, not re-entered) |
| SCIM Token | Copied from Twingate Admin Console |

## Gotchas
- **Group members won't sync** unless users are also assigned to the Twingate app in Okta — group push alone is insufficient
- **Removing user from a group does not remove from Twingate** if the user is directly assigned to the app; must remove from app itself
- Cleanest approach: assign **groups** (not individual users) to the app — then removing user from group removes them from Twingate (assuming no other push group membership)
- Do not alter SCIM Attribute Mappings

## Related Docs
- Okta app setup (Integration Catalog installation)
- Okta configuration overview article
- Twingate Admin Console (SCIM token location)
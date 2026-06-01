# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM-based provisioning between Okta and Twingate to sync users and groups. Requires the Twingate app to already be installed from Okta's Integration Catalog. Available on Business and Enterprise plans only.

## Key Information
- Supported operations: create users, update user attributes, deactivate users, push groups
- SCIM endpoint is pre-configured during initial app installation — do not re-enter it
- Do not modify SCIM Attribute Mappings in Okta
- Previously assigned users sync to Twingate immediately upon enabling provisioning

## Prerequisites
- Twingate Business or Enterprise plan
- Twingate app installed from Okta Integration Catalog (prior step)
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, open the Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy the **SCIM Token** from Twingate Admin Console
3. Enable **API Integration** and paste the SCIM Token → click **Test API Credentials** to verify
4. Under Provisioning tab, enable all 3 provisioning options → click **Save**

### Push Groups
1. Go to **Push Groups** tab → click **Push Groups** → select **Find groups by name**
2. Search for group, select it → click **Save**

## Configuration Values
| Parameter | Source | Notes |
|-----------|--------|-------|
| SCIM Token | Twingate Admin Console | Paste into Okta API Integration field |
| SCIM Endpoint | Pre-configured | Do not modify |

## Gotchas
- **Users must be assigned to the Twingate app** to sync group memberships correctly — pushing a group alone is insufficient if members aren't app-assigned
- Removing a user from a group does **not** remove them from Twingate if they are individually assigned to the app; must remove them from the app directly
- Best practice: assign groups (not individual users) to the app so group removal propagates correctly to Twingate
- "Test API Credentials" must succeed before provisioning will work

## Troubleshooting
| Issue | Resolution |
|-------|------------|
| Groups pushing but users not syncing | Verify users or the group itself is assigned to the Twingate app in Okta |
| Removed user still appears in Twingate | Remove user from the Twingate app in Okta, not just the group |

## Related Docs
- Okta app configuration (Integration Catalog setup)
- Twingate Admin Console (SCIM Token location)
- Okta overview configuration article
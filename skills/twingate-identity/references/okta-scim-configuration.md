# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM-based provisioning between Okta and Twingate to sync users and groups. Requires the Twingate Okta app to already be installed from the Integration Catalog. Available on Business and Enterprise plans only.

## Key Information
- Supported SCIM features: create users, update user attributes, deactivate users, group push
- SCIM endpoint is pre-configured during initial app installation — no manual entry needed
- Previously assigned users sync to Twingate immediately upon enabling provisioning

## Prerequisites
- Twingate Business or Enterprise plan
- Twingate app installed from Okta Integration Catalog (SCIM endpoint already set)
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, open Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy SCIM Token from Twingate Admin Console
3. Enable **API Integration**, paste SCIM Token, click **Test API Credentials** to verify
4. Under Provisioning tab, enable all 3 provisioning options → **Save**

### Push Groups
1. Go to **Push Groups** tab → click **Push Groups** → select **Find groups by name**
2. Search for group, select it → **Save**

## Configuration Values
| Field | Value |
|-------|-------|
| SCIM Token | Copied from Twingate Admin Console |
| SCIM Endpoint | Pre-configured (do not modify) |
| Attribute Mappings | Do not change |

## Gotchas
- **Do not modify SCIM Attribute Mappings** — will break sync
- Group members only sync if they are **also assigned to the Twingate app** in Okta; pushing a group alone is insufficient
- Removing a user from a group does **not** remove them from Twingate if they are individually assigned to the app — must remove from the app directly
- Safest pattern: assign **groups** (not individual users) to the app; then removing from group removes from Twingate (unless in another push group)

## Troubleshooting
| Issue | Fix |
|-------|-----|
| Groups push but users not syncing | Assign users or the group itself to the Twingate app in Okta |
| Removed user from group still appears in Twingate | Remove user from the Twingate app in Okta, or use group-only assignment model |

## Related Docs
- Okta app configuration (Integration Catalog setup)
- Twingate Okta overview article
- Initial Twingate Okta app installation guide
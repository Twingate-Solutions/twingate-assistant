---
source: https://www.twingate.com/docs/okta-scim-configuration
type: docs
fetched: 2026-08-14
source_version: ee115b55c725f16230f5c2639d1f34492ba6cd8365dc6206bae2ae2457b4def6
---

# Okta SCIM User & Group Sync Configuration

## Summary
Configures SCIM provisioning between Okta and Twingate to sync users and groups. Requires the Twingate Okta app to be installed first, then an API token-based integration is enabled. Supports user creation, attribute updates, deactivation, and group push.

## Key Information
- Supported features: create users, update attributes, deactivate users, push groups
- Plan requirement: Business or Enterprise only
- SCIM endpoint URL is pre-configured during initial app installation — do not re-enter it
- Do not modify SCIM Attribute Mappings in Okta
- Previously assigned users sync to Twingate immediately upon enabling provisioning

## Prerequisites
- Twingate Business or Enterprise plan
- Twingate app installed from Okta Integration Catalog (see Okta app configuration article)
- SCIM Token from Twingate Admin Console

## Step-by-Step

### Enable SCIM Provisioning
1. In Okta, open the Twingate app → **Provisioning** tab → click **Configure API Integration**
2. Copy the **SCIM Token** from the Twingate Admin Console
3. Check **Enable API Integration**, paste the SCIM Token, click **Test API Credentials** to verify
4. Under Provisioning tab, enable all 3 provisioning options → click **Save**

### Push Groups
1. Go to **Push Groups** tab → click **Push Groups** → select **Find groups by name**
2. Search for the group, select it → click **Save**

## Configuration Values
| Parameter | Source | Notes |
|-----------|--------|-------|
| SCIM Token | Twingate Admin Console | Paste into Okta API Integration field |
| SCIM Endpoint | Pre-configured | Do not modify |

## Gotchas
- **Group members won't sync unless assigned to the app**: Setting up group push does not automatically provision users — users or the group itself must be explicitly assigned to the Twingate Okta app
- **Removing user from group ≠ removing from Twingate** if the user is directly assigned to the app; must remove from the app itself, or use group-only assignment strategy
- **Cleanest group sync approach**: Assign groups (not individual users) to the app — then removing a user from a group removes them from Twingate, provided they aren't in other push groups
- Do not alter SCIM Attribute Mappings or provisioning will break

## Related Docs
- Okta app configuration (initial install from Integration Catalog)
- Twingate Admin Console (SCIM Token location)
- Twingate Okta overview article
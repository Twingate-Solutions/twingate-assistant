# Twingate Okta Application Configuration

## Summary
Step-by-step guide to activate the Twingate app in Okta's catalog and link it to the Twingate Admin console. Covers app assignment, visibility settings, and credential retrieval for completing the integration.

## Key Information
- Twingate is available in the Okta App Catalog (pre-built integration)
- Hide the app from users' Okta dashboard — authentication only works from the Twingate Client app, not via Okta dashboard tile
- Admin must assign themselves to the app before completing integration
- Integration requires three values from Okta: Domain, Client ID, Client Secret

## Prerequisites
- Okta admin access
- Twingate Admin console access
- Twingate subdomain available
- Twingate Client app installed (for final authentication verification step)

## Step-by-Step

### In Okta
1. **Applications → Browse App Catalog** → search "Twingate" → select → click **Add**
2. Enter your **Twingate subdomain** in the Subdomain field
3. Check both **Application Visibility** boxes (hides app from user dashboard)
4. Assign app to users/groups — must include yourself

### In Twingate Admin Console
1. Navigate to the Okta integration setup screen
2. Enter **Okta Domain** (found in upper-right global header of Okta dashboard)
3. Enter **Client ID** and **Client Secret** (found in **Sign On** tab of the Twingate Okta app)
4. Follow the wizard and sign in with Okta to verify credentials

## Configuration Values

| Field | Source in Okta |
|-------|---------------|
| Okta Domain | Global header, upper-right corner of Okta dashboard |
| Client ID | Twingate app → Sign On tab |
| Client Secret | Twingate app → Sign On tab |
| Subdomain | Your Twingate subdomain |

## Gotchas
- **Do not skip assigning yourself** — you cannot complete the integration without being assigned to the app
- **Admin group isolation**: Create a dedicated Okta group (e.g., "Admins") for Twingate admin users. If you use a shared group and later remove it from the Twingate app, your own account will lose access
- **Application Visibility**: Must hide the tile — users cannot initiate sessions from Okta dashboard, only from the Twingate Client
- A live Okta sign-in is required during setup to validate credentials before integration activates

## Related Docs
- Okta configuration overview (referenced as "this article")
- [Okta guide for finding your Okta Domain](https://help.okta.com/en/prod/Content/Topics/Settings/settings-customization-general.htm)
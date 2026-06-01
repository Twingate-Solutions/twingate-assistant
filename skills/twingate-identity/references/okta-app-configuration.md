# Twingate Okta Application Configuration

## Summary
Configures the Twingate application in Okta and connects it to the Twingate Admin console via OIDC. Users authenticate through the Twingate Client app, not the Okta dashboard. Requires copying credentials from Okta into Twingate to complete the integration.

## Key Information
- Twingate app is available in the Okta App Catalog (search "Twingate")
- Hide the app from users' Okta dashboard — authentication only works from the Twingate Client, not Okta SSO tiles
- Must assign at least yourself to the app before completing integration
- Admin group recommendation: create a dedicated Okta group (e.g., "Admins") assigned to the Twingate app to prevent accidental self-lockout

## Prerequisites
- Okta admin access
- Twingate Admin console access
- Twingate subdomain available
- Overview setup completed (see Okta configuration overview article)

## Step-by-Step

**In Okta:**
1. Go to **Applications → Browse App Catalog**
2. Search for and select **Twingate**
3. Click **Add**
4. Enter your **Twingate subdomain**
5. Check both **Application Visibility** boxes (hides app from user dashboard)
6. Assign the app to users or groups (include yourself)

**In Twingate Admin Console:**
1. Navigate to the Okta integration activation screen
2. Enter **Okta Domain** (found in upper-right global header of Okta dashboard)
3. Enter **Client ID** (from **Sign On** tab of Twingate Okta app)
4. Enter **Client Secret** (from **Sign On** tab of Twingate Okta app)
5. Follow the wizard and sign in with Okta to verify credentials

## Configuration Values

| Field | Source |
|-------|--------|
| `Subdomain` | Your Twingate subdomain |
| `Okta Domain` | Okta dashboard global header (upper-right) |
| `Client ID` | Twingate Okta app → Sign On tab |
| `Client Secret` | Twingate Okta app → Sign On tab |

## Gotchas
- **Do not skip assigning yourself** — you'll be locked out before completing integration
- **Don't use a shared group** that includes yourself if it might be removed later — use a dedicated admin group
- **Application Visibility boxes must be checked** — users cannot initiate auth from Okta; must use Twingate Client
- Integration requires an active Okta sign-in test as part of the wizard (credentials are verified live)

## Related Docs
- Okta configuration overview (referenced as "this article")
- Okta guide for finding Okta Domain (referenced as "this Okta guide")
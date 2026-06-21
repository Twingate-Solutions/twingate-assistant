# Twingate Okta Application Configuration

## Summary
Configures the Twingate application in Okta and completes the integration in the Twingate Admin console. Requires adding Twingate from the Okta App Catalog and connecting it using domain, client ID, and client secret values.

## Key Information
- Twingate app is available in the Okta App Catalog (not a custom SAML/OIDC setup)
- Users can only authenticate via the Twingate Client app, not from the Okta dashboard
- Integration requires a verification sign-in step to confirm credentials are correct

## Prerequisites
- Okta admin access
- Twingate Admin console access
- Your Twingate subdomain

## Step-by-Step

### In Okta
1. Go to **Applications → Browse App Catalog**
2. Search for and select **Twingate**
3. Click **Add**
4. Enter your Twingate subdomain
5. Check both **Application Visibility** boxes (hides app from user Okta dashboard)
6. Assign the app to users or groups (assign at least yourself)

### In Twingate Admin Console
1. Navigate to Okta integration activation screen
2. Enter **Okta Domain** (found in upper-right global header of Okta dashboard)
3. Enter **Client ID** (from **Sign On** tab of Twingate Okta app)
4. Enter **Client Secret** (from **Sign On** tab of Twingate Okta app)
5. Complete wizard by signing in with Okta to verify credentials

## Configuration Values

| Field | Source |
|-------|--------|
| Okta Domain | Okta dashboard upper-right global header |
| Client ID | Twingate app → Sign On tab |
| Client Secret | Twingate app → Sign On tab |
| Subdomain | Your Twingate subdomain |

## Gotchas
- **Hide app from Okta dashboard**: Must check Application Visibility boxes — users cannot initiate auth from Okta, only from the Twingate Client
- **Admin group management**: If you assign yourself via a group you later remove from the Twingate app, your own account loses access and you cannot log in to Twingate
- **Assign yourself**: You must be assigned to the app before completing integration to authenticate during the verification step

## Best Practices
- Create a dedicated Okta group (e.g., "Admins") for Twingate admin users
- Avoid assigning yourself only through a shared group that may be removed later

## Related Docs
- [Okta configuration overview](https://www.twingate.com/docs/) (referenced as "this article")
- [Okta guide for finding Okta Domain](https://help.okta.com/) (referenced in page)
# Twingate Okta Application Configuration

## Summary
Steps to activate the Twingate application in Okta's app catalog and connect it to the Twingate Admin console. Requires entering subdomain, assigning users/groups, then providing Okta credentials back in Twingate.

## Key Information
- Twingate is available in the Okta App Catalog (no manual SAML setup needed)
- Users cannot authenticate via Okta dashboard tile — only from Twingate Client app on device
- Integration requires three values from Okta: Domain, Client ID, Client Secret
- Twingate will prompt you to sign in with Okta to validate credentials during setup

## Prerequisites
- Access to Okta Admin dashboard
- Access to Twingate Admin console
- At least one user (yourself) assigned to the Twingate Okta app before completing integration

## Step-by-Step

### In Okta
1. Go to **Applications → Browse App Catalog**
2. Search for and select **Twingate**
3. Click **Add**
4. Enter your Twingate subdomain
5. Check both **Application Visibility** boxes (hides app from Okta dashboard)
6. Assign the app to users or groups (must include yourself)

### In Twingate Admin Console
1. Navigate to the Okta integration setup screen
2. Enter **Okta Domain** (found in upper-right global header of Okta dashboard)
3. Enter **Client ID** and **Client Secret** (found in **Sign On** tab of the Twingate Okta app)
4. Complete the wizard by signing in with Okta to validate credentials

## Configuration Values

| Field | Source Location |
|-------|----------------|
| Okta Domain | Upper-right global header in Okta dashboard |
| Client ID | Twingate app → Sign On tab in Okta |
| Client Secret | Twingate app → Sign On tab in Okta |
| Subdomain | Your Twingate subdomain |

## Gotchas
- **Hide app from Okta dashboard**: Users attempting to authenticate via Okta tile will fail — auth must start from Twingate Client
- **Admin group management**: Don't assign yourself only through a group that may be removed later — losing group membership removes your Twingate access
- **Recommended**: Create a dedicated Okta group (e.g., "Admins") specifically for Twingate admin access to avoid accidental lockout
- Must assign yourself before completing integration or you cannot authenticate to finish setup

## Related Docs
- [Okta Configuration Overview](https://www.twingate.com/docs/) (referenced as "this article")
- [Okta Domain location guide](https://help.okta.com/) (Okta's official guide)
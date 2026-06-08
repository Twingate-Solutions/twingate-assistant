# Twingate Okta Application Configuration

## Summary
Covers the steps to activate the Twingate app in Okta's App Catalog and complete the integration in the Twingate Admin Console. Requires assigning users/groups and entering Okta credentials into Twingate's settings.

## Key Information
- Twingate app is available in the Okta App Catalog (searchable by name)
- Hide the app from the Okta user dashboard — users must authenticate via the Twingate Client app, not the Okta dashboard tile
- At least one admin must be assigned to the Okta app to complete setup
- A verification sign-in with Okta is required to confirm credentials are correct before activation finalizes

## Prerequisites
- Okta admin access
- Twingate Admin Console access
- Twingate subdomain available

## Step-by-Step

### In Okta
1. Go to **Applications → Browse App Catalog**
2. Search for and select **Twingate**
3. Click **Add**
4. Enter your **Twingate subdomain**
5. Check both **Application Visibility** boxes to hide from user dashboard
6. Assign the app to users or groups (must include yourself)

### In Twingate Admin Console
1. Navigate to the Okta integration activation screen
2. Enter **Okta Domain** (found in upper-right global header of Okta dashboard)
3. Enter **Client ID** and **Client Secret** (from the **Sign On** tab of the Twingate Okta app)
4. Follow the wizard and sign in with Okta to verify credentials

## Configuration Values

| Field | Source |
|-------|--------|
| `Subdomain` | Your Twingate subdomain |
| `Okta Domain` | Upper-right global header in Okta dashboard |
| `Client ID` | Sign On tab of Twingate app in Okta |
| `Client Secret` | Sign On tab of Twingate app in Okta |

## Gotchas
- **Do not** use a shared group that includes yourself if it may be removed later — losing group membership removes your Twingate login access
- Recommended pattern: create a dedicated Okta group (e.g., "Admins") assigned to the Twingate app for admin users
- Users cannot authenticate from the Okta dashboard tile; authentication only works from the Twingate Client application

## Related Docs
- [Okta Configuration Overview](https://www.twingate.com/docs/) (referenced as "this article")
- [Okta: Finding your Okta Domain](https://help.okta.com/) (referenced as "this Okta guide")
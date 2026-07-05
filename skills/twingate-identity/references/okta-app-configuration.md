# Twingate Okta Application Configuration

## Summary
Covers the steps to activate the Twingate app in the Okta App Catalog and connect it to the Twingate Admin Console. Requires assigning users/groups in Okta and entering Okta credentials into Twingate to complete the integration.

## Key Information
- Twingate is available directly in the Okta App Catalog (no manual SAML setup)
- Users authenticate via the Twingate Client app, not through the Okta dashboard tile
- After setup, Twingate prompts you to sign in with Okta to validate credentials

## Prerequisites
- Access to Okta Admin dashboard
- Access to Twingate Admin Console
- Your Twingate subdomain available
- At least one user (yourself) assigned to the Okta app before completing integration

## Step-by-Step

### In Okta
1. Go to **Applications → Browse App Catalog**
2. Search for and select **Twingate**
3. Click **Add**
4. Enter your **Twingate subdomain**
5. Check both **Application Visibility** boxes to hide the tile from the Okta user dashboard
6. Assign the app to users or groups (must include yourself)

### In Twingate Admin Console
1. Navigate to the Okta integration setup screen
2. Enter **Okta Domain** (found in the upper-right global header of Okta dashboard)
3. Enter **Client ID** and **Client Secret** (found in the **Sign On** tab of the Twingate Okta app)
4. Follow the wizard and sign in with Okta to validate credentials

## Configuration Values

| Field | Source |
|-------|--------|
| `Subdomain` | Your Twingate subdomain |
| `Okta Domain` | Upper-right corner of Okta dashboard |
| `Client ID` | Sign On tab of Twingate app in Okta |
| `Client Secret` | Sign On tab of Twingate app in Okta |

## Gotchas
- **Hide app tile**: Users cannot authenticate from the Okta dashboard tile — only from the Twingate Client app. Enable both Application Visibility checkboxes to prevent confusion.
- **Admin group management**: Create a dedicated Okta group (e.g., "Admins") for Twingate admins. If you use a general group and later remove it from the Twingate app, your own account will lose access.
- **Must assign yourself**: Okta integration wizard requires signing in with Okta to verify credentials — you must be assigned to the app before completing setup.

## Related Docs
- [Okta configuration overview](https://www.twingate.com/docs/okta) (referenced as "this article")
- [Okta guide for finding your Okta Domain](https://help.okta.com/en-us/content/topics/common/find-your-domain.htm) (referenced as "this Okta guide")
# Twingate Okta Application Configuration

## Summary
Step-by-step guide for activating the Twingate app in Okta's catalog and completing the integration in the Twingate Admin console. Covers app assignment, credential retrieval, and integration activation.

## Key Information
- Twingate is available directly in the Okta App Catalog (no manual SAML setup required)
- Users can only authenticate via Twingate Client app — not from the Okta dashboard
- Integration requires Okta Domain, Client ID, and Client Secret from Okta
- A test sign-in via Okta is required to validate credentials before activation completes

## Prerequisites
- Access to Okta Admin dashboard
- Access to Twingate Admin console
- Your Twingate subdomain

## Step-by-Step

### In Okta
1. Go to **Applications** → **Browse App Catalog**
2. Search for and select **Twingate**
3. Click **Add**
4. Enter your **Twingate subdomain**
5. Check both **Application Visibility** boxes (hides app from user Okta dashboard)
6. Assign the app to users or groups — include yourself at minimum

### In Twingate Admin Console
1. Navigate to the Okta integration activation screen
2. Enter **Okta Domain** (found in upper-right global header of Okta dashboard)
3. Enter **Client ID** and **Client Secret** (found in **Sign On** tab of the Twingate Okta app)
4. Complete the wizard by signing in with Okta to validate credentials

## Configuration Values
| Field | Source |
|-------|--------|
| Okta Domain | Upper-right global header in Okta dashboard |
| Client ID | Sign On tab of Twingate app in Okta |
| Client Secret | Sign On tab of Twingate app in Okta |
| Subdomain | Your Twingate subdomain |

## Gotchas
- **Hide the app** from the Okta dashboard — authentication only works when initiated from the Twingate Client, not from the Okta tile
- **Assign yourself directly or via a dedicated admin group** — if you assign yourself through a general group that later gets removed from the Twingate app, you will lose admin access
- Recommended: Create a dedicated Okta group (e.g., "Admins") for Twingate admin users to avoid accidental lockout

## Related Docs
- [Okta configuration overview](https://www.twingate.com/docs/) (referenced as "this article")
- [Okta guide for finding your Okta Domain](https://help.okta.com) (referenced as "this Okta guide")
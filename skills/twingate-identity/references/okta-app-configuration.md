---
source: https://www.twingate.com/docs/okta-app-configuration
type: docs
fetched: 2026-08-14
source_version: 3f8f3b0ef9ae96a2bbc62a735ecccdac9383bdc2163c06cb8bddaf6809fc7c6f
---

# Twingate Okta Application Configuration

## Summary
Step-by-step guide for activating the Twingate application in Okta and completing the integration in the Twingate Admin console. Covers app catalog setup, user/group assignment, and credential configuration.

## Key Information
- Twingate is available in the Okta App Catalog (pre-built integration)
- Users authenticate via Twingate Client app, not Okta dashboard — hide the app from Okta dashboard
- Integration requires Okta Domain, Client ID, and Client Secret from Okta
- Must assign at least yourself to the app before completing integration
- Twingate verifies credentials by requiring an Okta sign-in during setup wizard

## Prerequisites
- Okta admin access
- Twingate Admin console access
- Twingate subdomain available

## Step-by-Step

### In Okta
1. Navigate to **Applications** → **Browse App Catalog**
2. Search for and select **Twingate**
3. Click **Add**
4. Enter your **Twingate subdomain**
5. Check both **Application Visibility** boxes (hides app from user Okta dashboard)
6. Assign app to users or groups (must include yourself)

### In Twingate Admin Console
1. Navigate to Okta integration setup
2. Enter **Okta Domain** (found in upper-right global header of Okta dashboard)
3. Enter **Client ID** and **Client Secret** (from **Sign On** tab of Twingate app in Okta)
4. Complete the sign-in wizard to verify credentials

## Configuration Values

| Field | Source |
|-------|--------|
| `Subdomain` | Your Twingate subdomain |
| `Okta Domain` | Okta dashboard upper-right global header |
| `Client ID` | Twingate app → Sign On tab in Okta |
| `Client Secret` | Twingate app → Sign On tab in Okta |

## Gotchas
- **Do not** use a shared group that includes yourself for admin assignment — if that group is removed from the Twingate app, your account loses access and you cannot log in
- **Recommended:** Create a dedicated Okta group (e.g., "Admins") assigned to the Twingate app for admin users
- App must be hidden from Okta dashboard; users can only authenticate from the Twingate Client application
- Must assign yourself to the app before completing integration, otherwise Okta sign-in verification step will fail

## Related Docs
- [Okta configuration overview](https://www.twingate.com/docs/) (referenced as "this article")
- [Okta guide for finding Okta Domain](https://help.okta.com/) (referenced as "this Okta guide")
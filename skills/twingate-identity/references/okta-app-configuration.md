# Twingate Okta Application Configuration

## Summary
Configures the Twingate application within Okta and connects it to the Twingate Admin console. Requires adding Twingate from the Okta App Catalog and then entering Okta credentials into Twingate's admin interface.

## Key Information
- Twingate app is available in the Okta App Catalog (searchable)
- Users can only authenticate via the Twingate Client app, not from the Okta dashboard
- Integration requires three values from Okta: Domain, Client ID, Client Secret
- A verification sign-in step confirms credentials are correct before activation completes

## Prerequisites
- Admin access to both Okta and Twingate Admin console
- Twingate subdomain available
- See overview article for full Okta configuration context

## Step-by-Step

### In Okta
1. Go to **Applications → Browse App Catalog**
2. Search for and select **Twingate**
3. Click **Add**
4. Enter your Twingate subdomain
5. Check both **Application Visibility** boxes (hides app from user Okta dashboard)
6. Assign the app to users or groups (assign yourself at minimum)

### In Twingate Admin Console
1. Navigate to Okta integration setup
2. Enter **Okta Domain** (found in upper-right global header of Okta dashboard)
3. Enter **Client ID** and **Client Secret** (found in **Sign On** tab of the Twingate Okta app)
4. Complete the wizard by signing in with Okta to verify credentials

## Configuration Values
| Field | Source |
|-------|--------|
| Subdomain | Your Twingate subdomain |
| Okta Domain | Okta dashboard global header (upper-right) |
| Client ID | Twingate app → Sign On tab in Okta |
| Client Secret | Twingate app → Sign On tab in Okta |

## Gotchas
- **Hide app from Okta dashboard**: Must check Application Visibility boxes — users cannot initiate auth from Okta dashboard, only from the Twingate Client
- **Admin group isolation**: Create a dedicated Okta group (e.g., "Admins") for Twingate app assignment; if you use a shared group and later remove it from the Twingate app, your own account will lose access
- At least one user (yourself) must be assigned before completing integration

## Related Docs
- Okta configuration overview (referenced as "this article")
- Okta guide for locating Okta Domain (referenced as "this Okta guide")
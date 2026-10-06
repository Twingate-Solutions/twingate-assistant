---
source: https://www.twingate.com/docs/okta-app-configuration
type: docs
fetched: 2026-10-04
source_version: 9d686447b54784293d9b1141f9ab15be86f5b4f41bc54ddab11a469d5e389d0b
trust: official
---

# Twingate Okta Application Configuration

## Summary
Configures the Twingate application in Okta as an identity provider for user authentication. Covers adding the Twingate app from the Okta catalog, assigning users/groups, and completing the integration in the Twingate Admin Console.

## Key Information
- Twingate authenticates users via the Twingate Client app, not through the Okta dashboard directly
- Hide the Twingate app from users' Okta dashboard (Application Visibility checkboxes) to avoid confusion
- Subdomain input must include the service shard (e.g., `autoco.us2`, not just `autoco`)
- After saving credentials in Twingate, a sign-in verification step confirms credentials are correct

## Prerequisites
- Admin access to both Okta and Twingate Admin Console
- Twingate subdomain and service shard (visible in Admin Console URL)
- At least one user/group assigned to the Twingate Okta app (including yourself)

## Step-by-Step

### In Okta
1. Go to **Applications → Browse App Catalog**
2. Search for **Twingate** and select it
3. Click **Add**
4. Enter subdomain including shard (e.g., `autoco.us2`) in the **Subdomain** field
5. Check both **Application Visibility** boxes to hide from user dashboards
6. Assign the app to users or groups (must include yourself)

### In Twingate Admin Console
1. Navigate to the Okta integration setup screen
2. Enter **Okta Domain** — copy from the global header (upper-right) of the Okta dashboard
3. Enter **Client ID** and **Client Secret** — copy from the **Sign On** tab of the Twingate Okta app
4. Follow the wizard and sign in with Okta to verify credentials

## Configuration Values

| Field | Source | Example |
|---|---|---|
| Subdomain | Twingate Admin Console URL | `autoco.us2` |
| Okta Domain | Okta dashboard global header | `company.okta.com` |
| Client ID | Twingate app → Sign On tab | — |
| Client Secret | Twingate app → Sign On tab | — |

## Gotchas
- **Subdomain must include service shard** — omitting the shard (e.g., `.us2`) is a common misconfiguration
- **Admin group isolation**: Create a dedicated Okta group for Twingate admins; if you share a group with other users and later remove that group from the app, your own account loses access
- Users cannot initiate authentication from Okta — sessions must start from the Twingate Client application

## Related Docs
- [Okta Configuration Overview](https://www.twingate.com/docs/) (referenced as "this article" in source)
- [Okta guide for finding Okta Domain](https://help.okta.com/en-us/content/topics/common/find-org-url.htm)
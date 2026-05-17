# OneLogin Configuration

## Page Title
OneLogin Configuration (Twingate IdP Integration)

## Summary
Twingate integrates with OneLogin to delegate authentication via OIDC and synchronize users/groups via SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Requires Business or Enterprise plan; SCIM additionally requires OneLogin's Unlimited Plan.

## Key Information
- Authentication: SP-Initiated SSO via OpenID Connect (OIDC)
- User/group sync: SCIM protocol
- Users must be assigned to the OneLogin Twingate app to gain access
- Hide the app in OneLogin portal — users must authenticate from the Twingate client, not the portal

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Unlimited Plan (for SCIM/user sync)
- Admin access to both OneLogin and Twingate Admin consoles

## Step-by-Step

### OneLogin Side
1. Go to **Applications > Add App**, search for "Twingate", select it
2. Disable **"Visible in portal"** toggle → click **Save**
3. Assign the app to OneLogin roles (recommend creating a dedicated role, not just Default)
4. If save fails with "SCIM Base URL cannot be blank": go to **Configuration** tab, enter `https://twingate.com`, save to bypass validation

### Twingate Side
5. In Twingate Admin console, open OneLogin integration setup
6. Enter **OneLogin Subdomain** (from your dashboard URL or **Settings > Branding**)
7. Copy **Client ID** and **Client Secret** from the **SSO** tab of the OneLogin Twingate app
8. Complete the wizard by signing in with OneLogin to validate credentials
9. Configure SCIM separately (see Related Docs)

## Configuration Values

| Field | Source |
|-------|--------|
| `OneLogin Subdomain` | Dashboard URL or Settings > Branding |
| `Client ID` | OneLogin app → SSO tab |
| `Client Secret` | OneLogin app → SSO tab |
| SCIM Base URL (placeholder) | `https://twingate.com` (temporary fix only) |

## Gotchas
- **"SCIM Base URL cannot be blank" error**: Known OneLogin UI bug; enter `https://twingate.com` as a placeholder to save — real SCIM config is done separately
- **Role assignment risk**: Avoid assigning only the Default role; if Default role is later removed, you could lose admin access to Twingate. Create a dedicated admin role first
- **Portal visibility**: Do NOT leave app visible in OneLogin portal — authentication only works when initiated from the Twingate client app
- SCIM requires OneLogin Unlimited Plan (separate from Twingate plan tier)

## Related Docs
- [SCIM user & group sync configuration](https://www.twingate.com/docs/scim-onelogin) (separate setup required)
- [Twingate pricing page](https://www.twingate.com/pricing)
- OneLogin SCIM documentation (OneLogin's own docs)
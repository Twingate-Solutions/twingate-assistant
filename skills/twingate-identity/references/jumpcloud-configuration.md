# JumpCloud Configuration

## Page Title
JumpCloud Configuration (SAML + SCIM Integration)

## Summary
Twingate integrates with JumpCloud for user authentication via SAML and user/group synchronization via SCIM. Only users and groups associated with the Twingate app in JumpCloud can access Twingate resources. Available on Business and Enterprise plans only.

## Key Information
- Authentication: SAML (delegated to JumpCloud)
- Provisioning: SCIM (user/group sync)
- Only JumpCloud users assigned to the Twingate app can access resources
- Groups sync automatically once bound; includes all member users

## Prerequisites
- Twingate Business or Enterprise plan
- JumpCloud admin console access
- Twingate Admin Console access

## Step-by-Step

### Initial Setup
1. Create the Twingate application in JumpCloud admin console
2. In Twingate Admin Console, exchange metadata:
   - Upload Twingate-provided `.xml` file to JumpCloud
   - Enter JumpCloud-provided metadata URL into Twingate
3. Set the login URL within JumpCloud
4. Select initial group of JumpCloud users to sync
5. Configure SCIM provisioning:
   - Copy Twingate-provided SCIM endpoint and token
   - Paste into **Identity Management** section of JumpCloud's Twingate application

### Selective Group Sync (Post-Setup)
1. JumpCloud admin portal → **User Authentication** → **SSO Applications**
2. Click Twingate application
3. Click **User Groups** tab
4. Check groups to sync
5. Click **Save**
- Use **"show bound User Groups"** checkbox to view currently selected groups

### Certificate Renewal
1. Twingate Admin Console → select **"Renew Certificate"**
2. Renew certificate in JumpCloud's Twingate application
3. Twingate Admin Console modal → select **"Confirm Certificate Renewal"**

## Configuration Values
| Item | Source | Destination |
|------|--------|-------------|
| Twingate metadata `.xml` | Twingate Admin Console | JumpCloud |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |

## Gotchas
- Certificate renewal requires initiating from Twingate **before** renewing in JumpCloud — order matters
- Groups must be explicitly bound in JumpCloud; unbound groups will not sync
- Users not assigned to the Twingate app in JumpCloud cannot authenticate or access resources

## Related Docs
- Twingate pricing page (for plan eligibility)
- General SAML/SCIM configuration docs
- Twingate Admin Console identity provider setup
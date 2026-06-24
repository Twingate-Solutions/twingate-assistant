# JumpCloud Configuration

## Page Title
JumpCloud Configuration (Twingate Integration)

## Summary
Twingate integrates with JumpCloud to synchronize user accounts (SCIM) and delegate authentication (SAML). Only users and groups associated with the Twingate app in JumpCloud can access Twingate Resources. Requires Business or Enterprise plan.

## Key Information
- **Authentication**: SAML via JumpCloud
- **Provisioning**: SCIM (user and group sync)
- **Scope**: Only JumpCloud users/groups assigned to the Twingate app gain access
- **Plan requirement**: Business & Enterprise only

## Prerequisites
- Twingate Business or Enterprise plan
- Admin access to both JumpCloud Admin Console and Twingate Admin Console

## Step-by-Step Configuration

### Initial Setup
1. Create the Twingate application in JumpCloud admin console
2. In Twingate Admin Console:
   - Exchange metadata (upload Twingate-provided `.xml` file; input JumpCloud-provided metadata URL)
   - Set the login URL in JumpCloud
   - Select initial group of JumpCloud users to sync
3. Configure SCIM in JumpCloud:
   - Copy Twingate-provided SCIM endpoint and token
   - Paste into **Identity Management** section of the Twingate app in JumpCloud

### Selective Group Sync (Post-Setup)
1. JumpCloud admin portal → **User Authentication** → **SSO Applications**
2. Click the Twingate application
3. Click **User Groups** tab
4. Check boxes next to groups to sync
5. Click **Save**
- Groups and their member users sync automatically after saving
- Use **"show bound User Groups"** checkbox to review already-selected groups

### Certificate Renewal
1. Twingate Admin Console → select **"Renew Certificate"**
2. Renew certificate in the Twingate app within JumpCloud
3. Return to Twingate Admin Console modal → select **"Confirm Certificate Renewal"**

## Configuration Values
| Item | Source | Destination |
|------|--------|-------------|
| SAML metadata `.xml` | Twingate Admin Console | JumpCloud app setup |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |

## Gotchas
- Users not assigned to the Twingate app in JumpCloud cannot use Twingate, regardless of Twingate configuration
- Certificate renewal requires a specific sequence—confirm in Twingate **after** renewing in JumpCloud, not before
- Group sync includes all user members of selected groups automatically

## Related Docs
- Twingate pricing page (for plan eligibility)
- General SAML/SCIM identity provider configuration docs
- Twingate Admin Console documentation
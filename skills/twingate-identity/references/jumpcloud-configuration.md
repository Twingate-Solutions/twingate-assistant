# JumpCloud Configuration

## Page Title
JumpCloud Configuration (SAML + SCIM Integration)

## Summary
Twingate integrates with JumpCloud to synchronize user accounts (SCIM) and delegate authentication (SAML). Only users/groups assigned to the Twingate app in JumpCloud can access Twingate resources. Requires Business or Enterprise plan.

## Key Information
- **Authentication**: SAML via JumpCloud
- **Provisioning**: SCIM protocol for user/group sync
- **Scope**: Only JumpCloud users/groups associated with the Twingate app gain access
- **Plan requirement**: Business & Enterprise only

## Prerequisites
- Twingate Business or Enterprise plan
- JumpCloud admin console access
- Twingate Admin Console access

## Step-by-Step

### Initial Setup
1. Create the Twingate application in JumpCloud admin console
2. In Twingate Admin Console:
   - Exchange metadata (upload Twingate-provided `.xml` file; input JumpCloud metadata URL)
   - Set login URL in JumpCloud
   - Select initial JumpCloud user group to sync
3. Configure SCIM provisioning:
   - Copy Twingate-provided SCIM endpoint and token
   - Paste into **Identity Management** section of JumpCloud's Twingate app

### Selective Group Sync (Post-Setup)
1. JumpCloud admin portal → **User Authentication** → **SSO Applications**
2. Click Twingate application
3. Click **User Groups** tab
4. Check groups to sync → **Save**
- Groups and their members sync automatically after saving
- Use **"show bound User Groups"** checkbox to view currently selected groups

### Certificate Renewal
1. Twingate Admin Console → **Renew Certificate**
2. Renew certificate in JumpCloud's Twingate application
3. Twingate Admin Console modal → **Confirm Certificate Renewal**

## Configuration Values
| Item | Source | Destination |
|------|--------|-------------|
| Twingate metadata `.xml` | Twingate Admin Console | JumpCloud app setup |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint | Twingate Admin Console | JumpCloud → Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud → Identity Management |
| Login URL | Twingate Admin Console | JumpCloud app config |

## Gotchas
- Users/groups **not** assigned to the Twingate app in JumpCloud cannot authenticate or access resources
- Certificate renewal requires completing steps in **both** consoles in sequence; skipping "Confirm Certificate Renewal" in Twingate will break auth
- Group sync is bidirectional in configuration but one-directional in data flow (JumpCloud → Twingate)

## Related Docs
- Twingate pricing page (plan eligibility)
- General SAML/SCIM integration documentation
- Other IdP configuration guides (Okta, Azure AD, etc.)
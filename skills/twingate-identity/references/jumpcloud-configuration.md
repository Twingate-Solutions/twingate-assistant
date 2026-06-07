# JumpCloud Configuration

## Page Title
JumpCloud Configuration (SAML + SCIM Integration)

## Summary
Twingate integrates with JumpCloud to synchronize user accounts via SCIM and delegate authentication via SAML. Only users/groups associated with the Twingate app in JumpCloud can access Twingate Resources. Requires Business or Enterprise plan.

## Key Information
- **Authentication**: SAML (delegated to JumpCloud)
- **Provisioning**: SCIM (user/group sync)
- **Scope**: Only users/groups bound to the Twingate JumpCloud app can use Twingate

## Prerequisites
- Twingate Business or Enterprise plan
- JumpCloud admin console access
- Twingate Admin Console access

## Step-by-Step Configuration

### Initial Setup
1. Create Twingate application in JumpCloud admin console
2. In Twingate Admin Console:
   - Exchange metadata: upload Twingate-provided `.xml` file
   - Input JumpCloud-provided metadata URL
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
- Groups and their members sync automatically after save
- Use **show bound User Groups** checkbox to audit currently synced groups

### Certificate Renewal
1. Twingate Admin Console → **Renew Certificate**
2. Renew certificate in JumpCloud Twingate application
3. Twingate Admin Console modal → **Confirm Certificate Renewal**

## Configuration Values
| Item | Source | Destination |
|------|--------|-------------|
| Twingate metadata `.xml` | Twingate Admin Console | JumpCloud app setup |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |

## Gotchas
- Only users/groups **explicitly bound** to the JumpCloud Twingate app can authenticate — unbound users are blocked
- Certificate renewal requires a **specific 3-step sequence** across both consoles; order matters
- Initial setup requires selecting at least one group during configuration before SCIM provisioning

## Related Docs
- Twingate pricing page (for plan eligibility)
- General SAML/SCIM integration documentation
- Twingate Admin Console setup guides
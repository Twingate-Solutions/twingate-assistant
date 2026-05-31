# JumpCloud Configuration

## Page Title
JumpCloud Configuration (SAML + SCIM Integration)

## Summary
Twingate integrates with JumpCloud to synchronize user accounts (via SCIM) and delegate authentication (via SAML). Only users/groups assigned to the Twingate app in JumpCloud can access Twingate resources. Available on Business and Enterprise plans only.

## Key Information
- **Authentication**: SAML (delegated to JumpCloud)
- **Provisioning**: SCIM (user and group sync)
- **Scope**: Only JumpCloud users/groups bound to the Twingate app are provisioned

## Prerequisites
- Twingate Business or Enterprise plan
- Admin access to JumpCloud admin console
- Admin access to Twingate Admin Console

## Step-by-Step Setup

1. **Create Twingate app in JumpCloud** — Add Twingate as an SSO application in the JumpCloud admin console
2. **Exchange metadata** — In Twingate Admin Console:
   - Upload Twingate-provided `.xml` file to JumpCloud
   - Input JumpCloud-provided metadata URL into Twingate
   - Set login URL in JumpCloud
   - Select initial group(s) to sync
3. **Configure SCIM provisioning** — Copy Twingate-provided SCIM endpoint and token into the **Identity Management** section of the JumpCloud Twingate application

## Configuration Values
| Value | Source | Destination |
|-------|--------|-------------|
| Twingate metadata `.xml` | Twingate Admin Console | JumpCloud |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint URL | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |

## Selective Group Sync
- **Path**: JumpCloud admin portal → User Authentication → SSO Applications → Twingate → User Groups tab
- Check boxes next to desired groups → Save
- Groups and their members sync automatically to Twingate
- Use "show bound User Groups" checkbox to view currently selected groups

## Certificate Renewal
1. Select **Renew Certificate** in Twingate Admin Console
2. Renew certificate in JumpCloud Twingate application
3. Select **Confirm Certificate Renewal** in Twingate Admin Console modal

## Gotchas
- Users not assigned to the JumpCloud Twingate app will not be provisioned or able to authenticate
- Must complete SAML metadata exchange **before** configuring SCIM
- Certificate renewal requires coordinated steps across both consoles — order matters

## Related Docs
- Twingate pricing page (for plan eligibility)
- General SAML/SCIM integration documentation
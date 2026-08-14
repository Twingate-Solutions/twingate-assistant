---
source: https://www.twingate.com/docs/okta-configuration
type: docs
fetched: 2026-08-14
source_version: b3e59d28f23ce0442259add2d471f95ec58ed90ab07c9a81b89f1e93b5552b34
---

# Okta Configuration

## Page Title
Okta Configuration (Twingate + Okta Integration)

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via OpenID Connect (OIDC) and SCIM. Only users assigned to the Okta Twingate application can access Twingate resources. Setup requires configuration in both the Okta Admin console and the Twingate Admin console.

## Key Information
- **Plan requirement**: Business and Enterprise plans only
- **Authentication method**: SP-Initiated SSO via OpenID Connect (OIDC)
- **User/group sync method**: SCIM protocol
- **Two-phase setup**: Configure in Okta first, then validate in Twingate Admin console
- **Okta Lifecycle Management module** is required for direct SCIM sync; without it, users only appear in Twingate after first manual login

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- Okta Lifecycle Management module (required for automatic SCIM user/group sync)

## Step-by-Step
1. Create and configure the Twingate application in the **Okta Admin console**
2. Configure SCIM synchronization separately in Okta
3. Complete and validate the integration in the **Twingate Admin console** using credentials from the Okta Twingate application

## Without Lifecycle Management Module
- Follow standard Okta connection steps
- Define user access within Okta manually
- Users appear in Twingate Admin panel **only after first login** via Twingate Client + Okta authentication
- Groups must be assigned manually after user first login

## Configuration Values
| Component | Protocol/Standard |
|-----------|------------------|
| Authentication | OpenID Connect (OIDC) |
| User/Group Sync | SCIM |
| SSO Type | SP-Initiated |

## Gotchas
- Users not assigned to the Okta Twingate application **cannot** use Twingate at all
- Without Lifecycle Management, users are invisible in Twingate Admin until they authenticate at least once
- SCIM synchronization must be configured **separately** from OIDC — completing one does not configure the other
- Authentication policies for Twingate client access are controlled via the Okta Twingate application settings

## Related Docs
- [Twingate Okta Application setup](#) (linked in source as "Configure the Twingate Okta Application")
- [SCIM synchronization configuration](#) (linked in source as "Configure SCIM synchronization")
- Twingate pricing page (for plan eligibility)
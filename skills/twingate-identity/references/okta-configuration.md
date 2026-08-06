---
source: https://www.twingate.com/docs/okta-configuration
type: docs
fetched: 2026-08-05
source_version: b9601e736322b145a0717b7721a1eb8facbfb15a7b6256c00810a5cd5e8d2f2f
---

# Okta Configuration

## Page Title
Okta Configuration (Twingate + Okta Integration)

## Summary
Twingate integrates with Okta to synchronize user accounts and delegate authentication via the Okta Twingate application. The integration uses OpenID Connect (OIDC) for authentication and SCIM for user/group synchronization. Only users assigned to the Okta Twingate application can access Twingate resources.

## Key Information
- **Plans required**: Business and Enterprise only
- **Authentication method**: SP-Initiated SSO via OpenID Connect (OIDC)
- **Sync protocol**: SCIM for user and group synchronization
- **Two-phase setup**: Configure in Okta Admin console first, then complete in Twingate Admin console

## Prerequisites
- Twingate Business or Enterprise plan
- Okta admin access
- **Okta Lifecycle Management module** required for direct SCIM user/group sync
  - Without it: users only appear in Twingate Admin panel after first client login; groups must be managed manually

## Step-by-Step
1. Create and configure the Twingate application in the **Okta Admin console**
2. Configure SCIM synchronization separately in Okta (requires Lifecycle Management module)
3. Complete and validate integration in the **Twingate Admin console** (set up Authentication Policy using credentials from Okta Twingate app)

## Configuration Values
- Authentication: OpenID Connect (OIDC)
- Sync: SCIM protocol
- SSO type: Service Provider (SP) Initiated

## Gotchas
- **Lifecycle Management module is NOT included by default** — without it, SCIM sync is unavailable; users must log in manually before appearing in Twingate Admin
- Without Lifecycle Management: group assignments must be done manually in Twingate
- SCIM configuration is a **separate step** from OIDC setup — both must be completed independently
- Okta sign-in policies for Twingate client users are controlled via the Okta Twingate application

## Related Docs
- [Twingate Okta Application setup](#) (linked inline)
- [SCIM synchronization configuration](#) (linked inline)
- Twingate pricing page (for plan verification)
# Security Policies: Migration Guide

## Page Title
Security Policies Migration Guide

## Summary
Twingate migrated all existing networks to Security Policies on April 21st, 2021, preserving all existing security configurations. Security Policies expand access control capabilities beyond IdP-level settings, enabling per-Resource security rules managed directly in the Twingate Admin Console.

## Key Information
- Security Policies are configured in a new **Policies** section of the Admin Console
- Policies are assigned to Resources via Groups; policy applies when a Group member accesses a Group Resource
- New capabilities include: 2FA without IdP, per-Resource 2FA, per-Resource session lifetimes, future device posture/geolocation support

## Terminology Changes

| Old Term | New Term |
|---|---|
| Default Access Policy | Network Sign In Policy + Default Policy |
| Admin Access Policy | Admin Console Sign In Policy |
| Custom Access Policies | Custom Resource Policies |

## Migration Behavior by IdP

### Google, Entra ID, or No IdP
- **Network Sign In Policy**: inherits session lifetime + 2FA setting from Default Access Policy
- **Default Policy**: same session lifetime as Default Access Policy; no additional controls
- **Default Policy**: assigned to all existing Groups
- **Admin Console Sign In**: 2FA enabled if previously enabled in Admin Access Policy

### Okta and OneLogin (additional changes)
- All Google/Entra ID changes apply, plus:
- Additional custom Access Policies → new Security Policies with matching names, session lifetimes, and Group assignments

## Gotchas
- The Default Access Policy previously served dual purpose (Client auth + Group default); these are now split into two distinct policies
- Okta/OneLogin networks may have additional policies created; Google Workspace and Entra ID had identical Default and Admin Access Policies, so no extra policies are created
- Migration was a one-time event (April 21, 2021); existing networks were already migrated

## Prerequisites
- No action required for existing networks — migration was automatic
- Post-migration behavior is identical to pre-migration behavior

## Related Docs
- [Security Policies documentation](https://www.twingate.com/docs/security-policies) — full configuration reference
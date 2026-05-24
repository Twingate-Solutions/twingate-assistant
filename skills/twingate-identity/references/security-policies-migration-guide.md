# Security Policies: Migration Guide

## Page Title
Security Policies Migration Guide

## Summary
Twingate introduced Security Policies to replace the older Access Policy system, providing more granular access control configured directly in the Admin Console. Existing networks were migrated on April 21st, 2021, with all existing security rules preserved. Post-migration behavior is identical to pre-migration for end users.

## Key Information
- Security Policies are assigned to **Groups**; policy applies when a Group member accesses a Group Resource
- New **Policies** section added to Admin Console
- 2FA now available without requiring an IdP
- 2FA can be scoped to specific Resources (not just login)
- Custom session lifetimes configurable per Resource
- Foundation for future features: device posture, geolocation restrictions

## Terminology Mapping

| Old Term | New Term |
|---|---|
| Default Access Policy | Network Sign In Policy + Default Policy |
| Admin Access Policy (Okta/OneLogin) | Admin Console Sign In Policy |
| Custom Access Policies | Custom Resource Policies |

## Migration Behavior by IdP

### Google, Entra ID, or No IdP
- **Network Sign In Policy**: inherits session lifetime + 2FA setting from Default Access Policy
- **Default Policy**: same session lifetime as Default Access Policy; no extra controls added
- **Default Policy** assigned to all existing Groups
- **Admin Console Sign In Policy**: 2FA enabled if previously enabled

### Okta and OneLogin (additional changes)
- Custom Access Policies → new Security Policies with matching names
- Session lifetimes preserved from existing Access Policies
- Group assignments preserved from existing Access Policies

## Prerequisites
- None for migration (automatic); existing config preserved
- For new 2FA without IdP: no IdP configuration required

## Gotchas
- Admin Access Policy on Okta/OneLogin was distinct from the Default Access Policy; on Google/Entra ID they were identical—migration handles each case differently
- Default Policy is assignable to Groups and can be changed after migration
- Custom policy migration (Okta/OneLogin) only applies if you configured policies beyond the Admin and Default Access Policies—uncommon scenario

## Related Docs
- [Security Policies documentation](https://www.twingate.com/docs/security-policies) (referenced in page)
# Security Policies: Migration Guide

## Page Title
Security Policies Migration Guide

## Summary
Twingate introduced Security Policies to replace the older Access Policy system, enabling more granular access control configured directly in the Admin Console without requiring IdP support. Existing networks were automatically migrated on April 21st, 2021, preserving all prior security configurations. Post-migration behavior is identical to pre-migration behavior.

## Key Information
- Security Policies are assigned to Groups; when a User in a Group accesses a Resource in that Group, the assigned Policy applies
- New **Policies** section added to Admin Console for configuration
- New capabilities unavailable previously:
  - 2FA without an IdP configured
  - 2FA scoped to specific Resources (not just login)
  - Custom session lifetimes per Resource

## Terminology Mapping

| Old Term | New Term | Notes |
|---|---|---|
| Default Access Policy | Network Sign In Policy + Default Policy | Split into two distinct policies |
| Admin Access Policy (Okta/OneLogin) | Admin Console Sign In Policy | Behavior unchanged |
| Custom Access Policies | Custom Resource Policies | Expanded capabilities |

## Migration Behavior by IdP

### Google, Entra ID, or No IdP
- **Network Sign In Policy**: inherits session lifetime + 2FA setting from Default Access Policy
- **Default Policy**: same session lifetime as Default Access Policy; no extra controls added
- **Default Policy**: assigned to all existing Groups
- **Admin Console Sign In Policy**: 2FA enabled if previously enabled in Admin Access Policy

### Okta and OneLogin (additional steps)
- All Google/Entra ID migration steps apply, plus:
  - Each additional custom Access Policy → new Security Policy (same session lifetime, same name)
  - New Security Policies assigned to same Groups as original Access Policies

## Prerequisites
- None for migration (automatic); existing configuration preserved
- For new Security Policy setup: access to Twingate Admin Console

## Gotchas
- The Default Access Policy previously served dual purpose (user auth + Group default); it is now **split** into two separate policies — ensure both are configured as expected post-migration
- Admin Access Policy only existed separately for Okta and OneLogin; for Google Workspace and Entra ID it was identical to Default Access Policy
- Custom Resource Policies require a Sign In policy component plus any additional access requirements — different structure from old custom Access Policies

## Related Docs
- [Security Policies documentation](https://www.twingate.com/docs/security-policies) — full configuration reference
- Twingate Groups — used for assigning Security Policies to Resources
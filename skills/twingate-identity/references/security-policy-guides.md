# Policy Guides

## Page Title
Security Policy Guides

## Summary
Twingate Security Policies support multiple rule types that control access to resources. This page serves as an index to individual policy configuration guides covering authentication, 2FA, device trust, and device-only policies.

## Key Information
- Security Policies are composed of distinct rule types, each configured separately
- Four primary policy rule categories: Authentication, Two-Factor Authentication, Device-Only Resource Policies, and Trusted Devices
- Each rule type has dedicated documentation with full configuration details

## Policy Rule Types

| Rule Type | Purpose |
|-----------|---------|
| Authentication | Controls re-authentication frequency |
| Two-Factor Authentication | Sets 2FA requirements applied to auth rules |
| Device-Only Resource Policies | Evaluates device requirements without user auth checks |
| Trusted Devices | Requires devices to be trusted (manual or automatic) before meeting policy |

## Related Docs
- Authentication settings guide
- Two-factor Authentication settings guide
- Device-only Resource Policies guide
- Trusted Devices guide (including automatic trust configuration)

## Gotchas
- 2FA settings are applied *to* authentication requirements — they are not standalone; configure Authentication rules first
- Device-Only policies bypass user authentication evaluation entirely — use carefully for sensitive resources
- Trusted Devices can be enforced via manual approval or automatic trust; automatic trust has different security implications

---
*This page is an index only. Refer to linked individual guides for actionable configuration steps.*
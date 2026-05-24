# Security Policy Guides

## Page Title
Security Policy Guides

## Summary
Twingate supports multiple Security Policy rule types for controlling access to resources. This page serves as an index linking to individual guides for each policy type.

## Key Information
- Four main Security Policy rule categories are documented:
  - **Authentication** – controls re-authentication frequency and 2FA requirements
  - **Two-factor Authentication (2FA)** – settings applied to authentication requirements
  - **Device-only Resource Policies** – evaluates device requirements exclusively
  - **Trusted Devices** – determines whether devices must be trusted (manually or automatically)

## Prerequisites
- Access to Twingate Admin Console
- Security Policies feature available on your plan tier

## Policy Types Reference

| Policy Type | Controls |
|---|---|
| Authentication | Re-auth frequency, 2FA enforcement |
| Two-factor Authentication | 2FA-specific settings |
| Device-only Resource Policies | Device requirement evaluation only |
| Trusted Devices | Manual or automatic device trust |

## Gotchas
- Device-only Resource Policies bypass user/auth checks — ensure this is intentional when configured
- Trusted Devices can be set to automatic trust, which reduces friction but lowers security posture
- 2FA settings are distinct from Authentication settings — both must be configured appropriately

## Related Docs
- Authentication settings guide
- Two-factor Authentication guide
- Device-only Resource Policies guide
- Trusted Devices guide (includes automatic trust configuration)
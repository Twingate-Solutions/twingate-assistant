# Security Policy Guides

## Page Title
Security Policy Guides

## Summary
Twingate supports multiple Security Policy rule types that control access to resources. These policies govern authentication frequency, 2FA requirements, device trust, and device-only evaluations.

## Key Information
- Four distinct policy categories available:
  - **Authentication** – controls re-authentication frequency and 2FA requirements
  - **Two-factor Authentication** – specific settings applied to authentication requirements
  - **Device-only Resource Policies** – evaluates only device requirements (not user auth)
  - **Trusted Devices** – requires devices to be trusted (manually or automatically) before meeting policy requirements

## Prerequisites
- Active Twingate deployment
- Admin access to configure Security Policies

## Configuration Areas

| Policy Type | Controls |
|---|---|
| Authentication | Re-auth frequency, 2FA enforcement |
| Two-factor Authentication | 2FA-specific settings within auth requirements |
| Device-only Resource Policies | Device posture checks without user auth evaluation |
| Trusted Devices | Manual or automatic device trust enforcement |

## Gotchas
- Device-only policies bypass user authentication checks — use carefully for resources where device posture alone is the access criterion
- Trusted Devices can be set to manual or automatic trust; automatic trust may reduce security posture if not paired with other controls
- 2FA settings are a sub-component of Authentication settings — both must be configured appropriately together

## Related Docs
- Authentication settings guide
- Two-factor Authentication guide
- Device-only Resource Policies guide
- Trusted Devices guide
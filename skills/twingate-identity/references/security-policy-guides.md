# Security Policy Guides

## Page Title
Security Policy Guides

## Summary
This page serves as an index for Twingate's Security Policy rule documentation. It links to individual guides covering authentication, two-factor authentication, device-only policies, and trusted device requirements.

## Key Information
- Security Policies support four main rule categories:
  - **Authentication** – controls re-authentication frequency and 2FA requirements
  - **Two-factor Authentication (2FA)** – defines how 2FA requirements are applied
  - **Device-only Resource Policies** – evaluates device requirements independently of user auth
  - **Trusted Devices** – controls whether devices must be trusted (manually or automatically) to satisfy policy

## Prerequisites
- Access to Twingate Admin Console
- Security Policies feature available on your plan tier

## Configuration Areas

| Rule Type | Controls |
|-----------|----------|
| Authentication | Re-auth frequency, 2FA enforcement |
| Two-factor Authentication | 2FA method/requirement application |
| Device-only Policies | Device posture checks without user auth evaluation |
| Trusted Devices | Manual vs. automatic device trust |

## Gotchas
- Device-only Resource Policies evaluate **only** device requirements — user authentication state is not considered in these policies
- Trusted device status (manual vs. automatic) directly impacts whether a device can satisfy Security Policy requirements
- 2FA settings are distinct from Authentication settings — both must be configured appropriately for full enforcement

## Related Docs
- Authentication settings guide
- Two-factor Authentication settings guide
- Device-only Resource Policies guide
- Trusted Devices guide
# Twingate Security Policy Guides

## Page Title
Security Policy Guides (Index)

## Summary
This is an index page listing the available Security Policy rule types in Twingate. Each policy type controls a specific aspect of access control, covering authentication frequency, 2FA, device-only rules, and device trust requirements.

## Key Information
- Four distinct Security Policy rule categories are documented separately
- Policies combine authentication, 2FA, device, and trust controls
- Each rule type links to its own dedicated guide

## Policy Types

| Policy Type | Purpose |
|---|---|
| **Authentication** | Controls re-authentication frequency and 2FA requirements |
| **Two-factor Authentication** | Configures 2FA enforcement settings |
| **Device-only Resource Policies** | Evaluates device requirements independent of user auth |
| **Trusted Devices** | Requires devices to be manually or automatically trusted |

## Related Docs
- Authentication settings guide
- Two-factor Authentication settings guide
- Device-only Resource Policies guide
- Trusted Devices guide

## Gotchas
- Device-only Resource Policies bypass user authentication checks — evaluate device posture exclusively
- Trusted devices can be set to manual or automatic trust — these behave differently in enforcement

---
*This page is a navigation index only; implementation details are in the linked sub-guides.*
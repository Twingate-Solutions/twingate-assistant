# Policy Guides

## Page Title
Security Policy Guides

## Summary
Twingate Security Policies support multiple rule types that control access to resources. This page serves as an index linking to detailed guides for each policy rule category.

## Key Information
- Four distinct Security Policy rule types are available
- Each rule type has its own dedicated documentation guide
- Policies can be combined to enforce layered access controls

## Policy Rule Types

| Policy Type | Purpose |
|---|---|
| **Authentication** | Controls re-authentication frequency and 2FA requirements |
| **Two-factor Authentication** | Configures specific 2FA enforcement settings |
| **Device-only Resource Policies** | Restricts policy evaluation to device requirements only (bypasses user auth checks) |
| **Trusted Devices** | Requires devices to be trusted (manually or automatically) before meeting policy requirements |

## Related Docs
- Authentication settings guide
- Two-factor Authentication settings guide
- Device-only Resource Policies guide
- Trusted Devices guide

## Gotchas
- Device-only Resource Policies explicitly skip user authentication evaluation — use only when device posture alone is sufficient for access control
- Trusted Devices can be approved manually or automatically; automatic trust may reduce security posture if misconfigured
- 2FA settings are configured separately from general Authentication settings — both must be reviewed when setting up auth policies

---
*This page is an index only; implementation details are in the linked sub-guides.*
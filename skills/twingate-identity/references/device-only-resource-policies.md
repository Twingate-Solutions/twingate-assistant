# Device-only Resource Policies

## Summary
Device-only Resource Policies skip user authentication requirement checks, validating only device requirements for resource access. Minimum Authentication Requirements (session validity) are always enforced regardless of this setting. This enables frictionless access to low-risk resources and supports pre-login system resource access.

## Key Information
- Applies only to **Resource Policies** (not other policy types)
- Disabling auth requirements removes per-resource user authentication checks, but **Minimum Authentication Requirements are always enforced**
- User must be signed into Twingate client with a valid session
- Authentication session **persists across restarts** unless user explicitly logs out
- Standard Resource Policy sessions do **not** persist across restarts — users must re-authenticate each time

## Prerequisites
- Existing Resource Policy to modify
- Understanding of Minimum Authentication Requirements configuration (session length, device security rules)

## Step-by-Step: Enable Device-only Policy
1. Navigate to the Resource Policy configuration screen
2. Locate the **Authentication Requirements** setting
3. Select **Disable** next to "Authentication Requirements"
4. Save the policy
5. To re-enable, return to the same screen and re-enable the option

## Configuration Values
| Setting | Behavior |
|---|---|
| Authentication Requirements | `Disabled` = device-only mode; `Enabled` = standard mode |
| Minimum Authentication Requirements | Always enforced; typically configured as session length (e.g., 30 days) |

## Evaluation Logic (Device-only Policy)
Access is granted when ALL conditions are true:
1. Minimum Authentication Requirements session is **valid and active** (e.g., user authenticated within last N days)
2. Device Security requirements are **met**
3. User is **signed in** to Twingate client

## Gotchas
- Minimum Auth Requirements are **never bypassed** — even with device-only policies, expired sessions block access
- Device-only policies persist sessions across machine restarts; standard policies do not — important distinction for UX and system automation
- Use case for pre-login access (e.g., Windows Start Before Logon) requires device-only policy with appropriate Minimum Auth Requirements
- Explicitly logging out of the Twingate client **invalidates** the persisted session for device-only resources

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Trusted Devices](https://www.twingate.com/docs/trusted-devices) (marking devices as trusted)
- [Windows Start Before Logon](https://www.twingate.com/docs/windows-start-before-logon)
- Minimum Authentication Requirements configuration
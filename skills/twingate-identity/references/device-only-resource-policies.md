# Device-only Resource Policies

## Summary
Device-only Resource Policies skip user authentication checks and only evaluate device requirement rules. Minimum Authentication Requirements (session validity) are always enforced regardless of this setting. Useful for allowing trusted devices frictionless access or enabling pre-login system resource access.

## Key Information
- Applies only to **Resource Policies** (not other policy types)
- Default policies check both user authentication AND device requirements
- Device-only mode: checks **device requirements only**, skips user auth requirements
- Minimum Authentication Requirements (session length + device security) are **always evaluated** even in device-only mode
- Authentication session **persists across restarts** unless user explicitly logs out
- Standard Resource Policy sessions do **not** persist across restarts (users must re-authenticate)

## Prerequisites
- Existing Resource Policy to modify
- Understanding of Minimum Authentication Requirements configuration
- Trusted device marking configured (if using trusted-device access pattern)

## Step-by-Step: Enable Device-Only Policy

1. Navigate to the Resource Policy configuration screen
2. Locate the **Authentication Requirements** setting
3. Select **Disable** next to "Authentication Requirements"
4. Save configuration
5. To re-enable: return to same screen and re-enable the option

## Configuration Values

| Setting | Behavior |
|---|---|
| Authentication Requirements = Disabled | Only device rules evaluated |
| Authentication Requirements = Enabled | Both user auth + device rules evaluated |
| Minimum Authentication Requirements | Always enforced regardless of above setting |

## Gotchas

- **Session length still applies**: Even with device-only enabled, user must have authenticated within the Minimum Authentication Requirements window (e.g., last 30 days)
- **Device Security requirements still apply**: Both session length AND device security must be met under Minimum Auth Requirements
- **Restart behavior difference**: Device-only policy sessions survive restarts; standard Resource Policy sessions do not — this is intentional, not a bug
- **Explicit logout breaks access**: If user logs out of Twingate Client, device-only Resources require re-authentication before access resumes
- **Use case boundary**: Device-only is appropriate for low-risk resources and pre-login system access (e.g., Windows Start Before Logon), not for sensitive resources requiring active user verification

## Common Use Cases
- Trusted devices accessing low-risk resources without MFA prompts
- System resources needing access before interactive user session (Windows Start Before Logon)
- Reducing friction for known/managed device fleets

## Related Docs
- [Resource Policies](#)
- [Trusted Devices (marked as trusted)](#)
- [Windows Start Before Logon](#)
- [Minimum Authentication Requirements](#)
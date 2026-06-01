# Device-only Resource Policies

## Summary
Device-only Resource Policies skip user authentication requirement checks, relying solely on device requirement rules. Minimum Authentication Requirements (session validity) are always enforced regardless of this setting. Useful for frictionless access to low-risk resources or system resources before interactive login.

## Key Information
- Applies only to **Resource Policies** (not other policy types)
- Default Resource Policies check both user authentication AND device requirements
- Device-only mode: checks **device requirements only**, skips user auth requirements
- **Minimum Authentication Requirements are always enforced** even in device-only mode
- Authentication session persists across machine restarts/client relaunches (unless user explicitly logs out)
- Standard Resource Policy sessions are **never** maintained across restarts

## Prerequisites
- User must be signed in to the Twingate client with a valid session
- Minimum Authentication Requirements must be valid and active
- Device must meet configured Device Security requirements

## Configuration Steps
1. Navigate to the Resource Policy configuration screen
2. Locate **Authentication Requirements** setting
3. Select **Disable** to enable device-only mode
4. Re-enable by selecting the enable option in the same screen

## Behavior Details

### Minimum Authentication Requirements Evaluation
| Condition | Required |
|-----------|----------|
| Valid active session within session length window | ✅ Always |
| Device Security requirements met | ✅ Always |
| User authentication challenge | ❌ Skipped |

### Session Persistence Comparison
| Policy Type | Persists across restart? |
|-------------|--------------------------|
| Device-only Resource Policy | ✅ Yes (if within session window) |
| Standard Resource Policy | ❌ Never |

## Use Cases
- Trusted devices accessing resources without repeated auth prompts
- System/service resources needing access **before** interactive user login (e.g., [Windows Start Before Logon](https://www.twingate.com/docs/windows-start-before-logon))
- Low-risk resources where device trust is sufficient

## Gotchas
- "Device-only" does not mean zero authentication — Minimum Authentication Requirements (e.g., 30-day session) still apply
- User must have authenticated at least once within the configured session length window
- Explicit logout breaks session persistence; restart alone does not
- Device Security requirements must still be satisfied at access time

## Related Docs
- Resource Policies
- Trusted Device marking
- Windows Start Before Logon
- Minimum Authentication Requirements
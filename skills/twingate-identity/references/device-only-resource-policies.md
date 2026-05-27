# Device-only Resource Policies

## Summary
Device-only Resource Policies bypass user authentication checks, relying solely on device requirement rules for access control. Minimum Authentication Requirements (session validity) are always enforced regardless of this setting. This enables frictionless access to low-risk resources and pre-login system resource access.

## Key Information
- Default Resource Policies check both user authentication AND device requirements
- Device-only mode skips user authentication requirement rules but **always** enforces Minimum Authentication Requirements
- Session is maintained across restarts/client relaunches unless user explicitly logs out
- Standard Resource Policy sessions are **never** maintained across restarts (users must re-authenticate)
- Supports use cases like Windows Start Before Logon (pre-interactive session access)

## Prerequisites
- Must be applied to Resource Policies only (not other policy types)
- User must be signed in to Twingate client with a valid session
- Minimum Authentication Requirements must be configured and valid

## Configuration Steps
1. Navigate to the Resource Policy configuration screen
2. Locate the **Authentication Requirements** setting
3. Select **Disable** option next to "Authentication Requirements"
4. Save configuration
5. To re-enable: return to same screen and re-enable Authentication Requirements

## How Minimum Authentication Requirements Are Evaluated (Device-Only Mode)
| Requirement | Behavior |
|-------------|----------|
| Session length | User must have authenticated within configured window (e.g., 30 days) |
| Device Security requirements | Must be met at time of access |
| Session persistence | Maintained across restarts unless explicit logout |

## Gotchas
- **Session persistence asymmetry**: Device-only policy sessions survive restarts; standard Resource Policy sessions do not — users behind standard policies must always re-authenticate after restart
- Disabling Authentication Requirements does **not** disable Minimum Authentication Requirements — these are separate controls
- "Device-only" does not mean no authentication ever occurred; the user must have authenticated within the Minimum Authentication Requirements window
- Trusted device marking alone is insufficient — session validity is still checked

## Related Docs
- Resource Policies
- Trusted Devices
- Windows Start Before Logon
- Minimum Authentication Requirements
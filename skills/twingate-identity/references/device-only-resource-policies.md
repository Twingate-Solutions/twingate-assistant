# Device-only Resource Policies

## Summary
Device-only Resource Policies enforce device security requirements without requiring user re-authentication. They are useful for system services, monitoring endpoints, or resources needing access before interactive user sessions. The Sign In Policy session must still be valid for access to be granted.

## Key Information
- Disabling authentication requirements on a Resource Policy leaves only device security checks active
- Sign In Policy is **always** enforced regardless of device-only configuration
- Device posture is re-evaluated approximately every **5 minutes**; non-compliant devices lose access at next check
- Sessions persist across Client restarts and device reboots (unlike standard Resource Policy sessions)
- Compatible with Windows **Start Before Logon** for pre-login network access

## Prerequisites
- Existing Resource Policy in Admin Console
- Valid Sign In Policy configured
- User must have active sign-in session (authenticated within Sign In Policy timeframe)

## Step-by-Step: Create a Device-only Policy
1. Open a Resource Policy in the Admin Console
2. Locate **Authentication Requirements** setting
3. Select **Disable** next to Authentication Requirements
4. Save the policy — device checks remain active; auth checks are removed

## Configuration Values
| Setting | Value/Notes |
|---|---|
| Authentication Requirements | Set to `Disabled` |
| Device posture check interval | ~5 minutes (fixed, not configurable) |
| Session persistence | Survives restarts/reboots |
| Sign In Policy timer | Does **not** extend on device-only resource access |

## Session Behavior Details
| Behavior | Device-only Policy | Standard Resource Policy |
|---|---|---|
| Sign In Policy timer extends | ❌ No | ✅ Yes |
| Persists across restarts | ✅ Yes | ❌ No |
| Requires re-auth | ❌ No | ✅ Yes |
| Device posture enforced | ✅ Yes | ✅ Yes |

## Gotchas
- Accessing device-only resources does **not** reset or extend the Sign In Policy timer — users can be locked out when the timer expires even if actively using device-only resources
- Device posture revocation has up to ~5 minute lag; non-compliant devices retain access until next check cycle
- Sign In Policy session expiry still blocks access — "device-only" means no *additional* auth prompt, not no auth ever
- Sessions persist across reboots only for device-only policies; standard policies require re-authentication after restart

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Start Before Logon](https://www.twingate.com/docs/start-before-logon) (Windows)
- [Sign In Policy](https://www.twingate.com/docs/sign-in-policy)
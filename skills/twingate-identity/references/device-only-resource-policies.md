# Device-only Resource Policies

## Summary
Device-only Resource Policies enforce device security requirements without requiring user re-authentication. Access remains available as long as the Sign In Policy session is valid and the device meets the configured security profile. Useful for system services, monitoring endpoints, or pre-login network access.

## Key Information
- Disables authentication requirement on a Resource Policy, leaving only device posture checks
- Sign In Policy is **always enforced** regardless — user must have a valid sign-in session
- Device posture re-evaluated approximately every **5 minutes**; non-compliant devices lose access at next check
- Sessions **persist across Client restarts and device reboots** (unlike standard Resource Policy sessions)
- Sign In Policy timer does **not** extend when accessing device-only resources
- Compatible with Windows **Start Before Logon** for pre-login system access

## Prerequisites
- Existing Resource Policy to modify
- Valid Sign In Policy configured
- User must have authenticated within Sign In Policy's configured timeframe

## Step-by-Step Configuration
1. Open Admin Console
2. Navigate to the target Resource Policy
3. Locate **Authentication Requirements** section
4. Select **Disable** next to Authentication Requirements
5. Save the policy — device-only mode is now active

## Configuration Values
| Setting | Value |
|---|---|
| Authentication Requirements | Disabled |
| Device posture check interval | ~5 minutes |
| Session persistence across restart | Yes (device-only) |
| Session persistence across restart | No (standard policies) |

## Session Behavior Comparison

| Behavior | Device-only Policy | Standard Resource Policy |
|---|---|---|
| Extends Sign In Policy timer | No | Yes |
| Persists across restarts | Yes | No |
| Requires active auth | No | Yes |
| Device posture enforced | Yes | Yes |

## Gotchas
- **Sign In Policy still required**: Disabling auth on the Resource Policy does not bypass the Sign In Policy — users without a valid session cannot access device-only resources
- **Timer does not reset**: Accessing device-only resources will not prevent Sign In Policy session expiration; users may be forced to re-authenticate even if actively using device-only resources
- **5-minute posture lag**: Device falling out of compliance is not immediately revoked — up to 5-minute window before access is cut
- **Not a bypass mechanism**: Device-only ≠ unauthenticated access; it reduces friction for already-authenticated sessions only

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Start Before Logon (Windows)](https://www.twingate.com/docs/start-before-logon)
- [Sign In Policy](https://www.twingate.com/docs/sign-in-policy)
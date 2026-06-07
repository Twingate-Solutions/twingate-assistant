# Device-only Resource Policies

## Summary
Device-only Resource Policies enforce device security requirements without requiring user re-authentication. Access is granted as long as the user has a valid Sign In Policy session and their device meets the required security profile. Useful for system services, monitoring endpoints, or pre-login network access.

## Key Information
- Disabling authentication requirements on a Resource Policy leaves only device posture checks active
- Sign In Policy is **always enforced** regardless of device-only setting — user must have a valid sign-in session
- Device posture is re-evaluated approximately every **5 minutes**; non-compliant devices lose access at next check
- Sessions persist across Client restarts and device reboots (unlike standard Resource Policy sessions)
- Accessing device-only resources does **not** extend the Sign In Policy timer
- Compatible with Windows **Start Before Logon** for pre-login system-level access

## Prerequisites
- Existing Resource Policy in Admin Console
- Valid Sign In Policy configured
- Device profile/security requirements defined

## Step-by-Step: Create a Device-only Policy
1. Open the Admin Console
2. Navigate to the target Resource Policy
3. Locate **Authentication Requirements**
4. Select **Disable** next to Authentication Requirements
5. Save the policy — device checks remain active; auth requirement is removed

## Configuration Values
| Setting | Value | Notes |
|---|---|---|
| Authentication Requirements | Disabled | Removes auth check, keeps device check |
| Device posture check interval | ~5 minutes | Automatic, not configurable here |
| Session persistence across restart | Yes | Unlike standard Resource Policies |
| Sign In Policy timer extension | No | Device-only access does not reset timer |

## Gotchas
- **Sign In Policy still required**: Disabling auth on a Resource Policy does not bypass the Sign In Policy — users must still have authenticated within the Sign In Policy's configured window
- **Timer does not reset**: Accessing device-only resources won't extend the Sign In Policy countdown, which can cause unexpected session expiry
- **Posture lag**: Up to 5-minute delay before access is revoked after device falls out of compliance
- **Standard policies don't persist**: Only device-only policy sessions survive restarts; standard Resource Policy sessions are cleared on restart

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Start Before Logon](https://www.twingate.com/docs/start-before-logon) (Windows)
- [Sign In Policy](https://www.twingate.com/docs/sign-in-policy)
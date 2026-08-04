# Device-Only Resource Policies

## Page Title
Device-only Policies

## Summary
Device-only Resource Policies enforce device security requirements without requiring user re-authentication. Access is granted as long as the user has a valid Sign In Policy session and the device meets the required security profile. Useful for system services, monitoring endpoints, or pre-login network access.

## Key Information
- Disables the **authentication requirement** on a Resource Policy while keeping device security checks active
- Sign In Policy is **always enforced** regardless — user must have a valid sign-in session
- Sessions **persist across Client restarts and reboots** (unlike standard Resource Policy sessions)
- Device posture is **re-evaluated every ~5 minutes**; non-compliant devices lose access at next check
- Accessing device-only resources does **not** extend the Sign In Policy timer
- Compatible with **Windows Start Before Logon** for pre-login system-level access

## Prerequisites
- Existing Resource Policy configured in Admin Console
- Valid Sign In Policy configured with appropriate session timeframe
- Device profile/posture requirements defined

## Step-by-Step Configuration
1. Open the **Admin Console**
2. Navigate to the target **Resource Policy**
3. Locate **Authentication Requirements**
4. Select **Disable** next to Authentication Requirements
5. Save the policy — device-only mode is now active

## Configuration Values
| Setting | Value/Behavior |
|---|---|
| Authentication Requirements | Disabled |
| Device posture check interval | ~5 minutes |
| Session persistence across restart | Yes |
| Sign In Policy timer extension on access | No |

## Gotchas
- **Sign In Policy still applies** — disabling auth on the Resource Policy does not bypass Sign In Policy; users must still have authenticated within the Sign In Policy window
- **Timer does not reset** — device-only resource access does not count as authentication for Sign In Policy timer purposes; sessions can expire even while actively using device-only resources
- **Posture check delay** — up to 5 minutes may pass before a non-compliant device loses access
- **Standard Resource Policy sessions are NOT persistent** across restarts; only device-only policy sessions persist

## Related Docs
- [Resource Policies](#) — standard policy configuration
- [How Sessions Work](#) — detailed interaction between device-only policies, Sign In Policy, and IdP sessions
- Start Before Logon (Windows) — combining with device-only policies for pre-login access
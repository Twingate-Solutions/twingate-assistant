# Device-only Resource Policies

## Summary
Device-only Resource Policies enforce device security requirements without requiring user re-authentication. They are useful for system services, monitoring endpoints, or resources needing access before an interactive user session exists. The Sign In Policy session must still be valid for access to be granted.

## Key Information
- Disabling authentication requirements on a Resource Policy leaves only device security checks active
- Sign In Policy is **always enforced** regardless of device-only setting — user must have a valid sign-in session
- Device posture is re-evaluated approximately every **5 minutes**; non-compliant devices lose access at next check
- Compatible with Windows **Start Before Logon** for pre-login system-level network access

## Prerequisites
- Existing Resource Policy in Admin Console
- Valid Sign In Policy configured
- Device profile/security requirements defined

## Step-by-Step: Enable Device-only Mode
1. Open Admin Console
2. Navigate to the target Resource Policy
3. Select **Disable** next to **Authentication Requirements**
4. Save the policy

## Configuration Values
| Setting | Value |
|---|---|
| Authentication Requirements | Disabled |
| Device posture check interval | ~5 minutes |

## Session Behavior

| Behavior | Device-only Policy | Standard Resource Policy |
|---|---|---|
| Sign In Policy timer extends on access | ❌ No | ✅ Yes |
| Session persists across client restarts/reboots | ✅ Yes | ❌ No |
| Requires valid Sign In Policy session | ✅ Yes | ✅ Yes |

## Gotchas
- Disabling authentication on Resource Policy does **not** bypass the Sign In Policy — users still need a valid sign-in session
- Accessing device-only resources does **not** reset or extend the Sign In Policy timer
- If the Sign In Policy session expires, resources become inaccessible even in device-only mode
- Device posture revocation is not immediate — up to 5-minute delay before non-compliant devices lose access

## Related Docs
- [Resource Policies](#) — base policy configuration
- [How Sessions Work](#) — detailed interaction between device-only policies, Sign In Policy, and IdP sessions
- Start Before Logon (Windows) — system-level pre-login access
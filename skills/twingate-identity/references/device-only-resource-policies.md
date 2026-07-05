# Device-only Resource Policies

## Page Title
Device-only Policies

## Summary
Device-only Resource Policies enforce device security requirements without requiring user re-authentication. Access is granted as long as the device meets the required security profile and the user's Sign In Policy session remains valid. Useful for system services, monitoring endpoints, or pre-login network access.

## Key Information
- Disables authentication requirement on a Resource Policy, leaving only device security checks active
- Sign In Policy is **always** enforced regardless — user must have a valid sign-in session
- Session persists across Client restarts and device reboots (unlike standard Resource Policies)
- Device posture re-evaluated approximately every **5 minutes**; access revoked at next check if device falls out of compliance
- Sign In Policy timer does **not** extend when accessing device-only resources
- Compatible with Windows **Start Before Logon** for pre-interactive-login network access

## Prerequisites
- Existing Resource Policy configured in Admin Console
- User must have valid Sign In Policy session before accessing device-only resources
- Device must meet the configured security profile

## Step-by-Step: Create a Device-only Policy
1. Open Admin Console
2. Navigate to the target Resource Policy
3. Locate **Authentication Requirements**
4. Select **Disable** next to Authentication Requirements

## Configuration Values
| Setting | Value/Notes |
|---|---|
| Authentication Requirements | Set to `Disabled` |
| Device posture check interval | ~5 minutes |
| Session persistence | Survives restarts/reboots |
| Sign In Policy timer behavior | Continues countdown; not reset by device-only access |

## Gotchas
- **Sign In Policy still enforced**: Disabling auth on Resource Policy does not bypass Sign In Policy — users still need a valid session
- **Timer not extended**: Accessing device-only resources does not refresh the Sign In Policy timer; users may be prompted to re-authenticate when timer expires
- **Posture drift**: If device falls out of compliance, access is revoked at the next ~5-minute posture check, not immediately
- **Standard Resource Policy sessions don't persist across restarts** — device-only policies behave differently in this regard

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Start Before Logon](https://www.twingate.com/docs/start-before-logon) (Windows only)
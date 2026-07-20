# Sign In Policy

## Summary
The Sign In Policy defines baseline requirements users must meet before accessing the Twingate Client. It acts as a first gate—users cannot view or access any Resources until satisfied. Configured under **Policies > Sign In Policy** in the Admin Console.

## Key Information
- Three configurable requirements: Device Security, Authentication Frequency, MFA
- Sign-in sessions **persist across restarts/reboots**; Resource Policy sessions do not
- Sign In Policy evaluated at sign-in and when session timer expires; Resource Policies evaluated per-Resource access
- Sign-in session uses a **rolling window**—resets on successful Resource Policy re-authentication

## Prerequisites
- Access to Admin Console
- Device Profiles configured (if using Trusted Profile device security)
- IdP configured for authentication

## Configuration Values

| Setting | Options/Range | Notes |
|---|---|---|
| Device Security | Approved OS requirements or Trusted Profile | Links to Device Profiles; changes auto-reflected |
| Authentication Frequency | 7–31 days | Rolling window; resets on Resource Policy re-auth |
| MFA | Enabled/Disabled | Native Twingate MFA only |

## Step-by-Step
1. Navigate to **Admin Console > Policies > Sign In Policy** tab
2. Configure **Device Security**: select Approved OS or Trusted Device Profile
3. Set **Authentication Frequency**: choose interval (7–31 days)
4. Toggle **MFA** if requiring native Twingate MFA at sign-in

## Gotchas
- **Double MFA**: Enabling MFA in Sign In Policy AND at IdP level forces users to complete MFA twice. Configure in only one place.
- **Device non-compliance**: Devices failing Device Security are **blocked entirely** from signing in—not just restricted from specific Resources.
- **Device Profile changes** automatically affect Sign In Policy without additional configuration.
- **Admin Console** has a separate sign-in policy under **Settings > Admin Console Security**—independent from Client Sign In Policy.
- Lenient Sign In Policy (e.g., 30 days) is intentional design—use Resource Policies for stricter per-Resource enforcement.

## Sign In Policy vs Resource Policy

| | Sign In Policy | Resource Policy |
|---|---|---|
| Controls | Client access | Per-Resource access |
| Evaluated | At sign-in + session expiry | Each Resource access (after timer expiry) |
| Session persists across restart | ✅ Yes | ❌ No |

## Related Docs
- [Device Profiles](https://www.twingate.com/docs/device-profiles)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Multi-Factor Authentication](https://www.twingate.com/docs/multi-factor-authentication)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- Resource Policies documentation
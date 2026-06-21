# Sign In Policy

## Summary
The Sign In Policy defines baseline requirements users must meet before accessing the Twingate Client. It acts as the first authentication gate—users cannot see or access any Resources until it's satisfied. Configured per-network under **Policies > Sign In Policy** in the Admin Console.

## Key Information
- Three configurable requirements: Device Security, Authentication Frequency, MFA
- Evaluated once at sign-in, then again when the session timer expires
- Sign-in sessions **persist across Client restarts/reboots**
- Resource Policy re-authentication resets the sign-in session timer (rolling window)
- Admin Console has a **separate** sign-in policy under **Settings > Admin Console Security**

## Configuration Values

| Setting | Options/Range | Notes |
|---|---|---|
| Device Security | Approved OS or Trusted Profile | Links to Device Profiles config automatically |
| Authentication Frequency | 7–31 days | Rolling window; resets on Resource Policy re-auth |
| MFA | Enabled/Disabled | Native Twingate MFA only |

## Prerequisites
- Device Profiles configured (if using Trusted Profiles for Device Security)
- IdP integrated (for re-authentication prompts)

## Step-by-Step
1. Navigate to **Policies > Sign In Policy** tab in Admin Console
2. Configure **Device Security**: select Approved OS requirements or a Trusted Device Profile
3. Set **Authentication Frequency**: choose interval between 7–31 days
4. Enable/disable **MFA** as needed
5. Save changes (Device Profile changes apply automatically)

## Gotchas
- **Double MFA**: If MFA is enforced at both the IdP and Sign In Policy, users authenticate twice per sign-in. Choose one location only.
- **Device blocked entirely**: Devices failing Device Security requirements cannot sign in at all—not just blocked from specific Resources.
- **Resource Policy sessions ≠ Sign-in sessions**: Resource Policy sessions do NOT persist across restarts; sign-in sessions do.
- **Lenient Sign In Policy is valid**: Per-Resource security is handled by Resource Policies, so a 30-day sign-in frequency is a reasonable default.
- **Session expiry = full sign-out**: When the sign-in timer expires, the user is fully signed out and must re-authenticate via IdP.

## Related Docs
- [Device Profiles](https://www.twingate.com/docs/device-profiles)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Multi-Factor Authentication](https://www.twingate.com/docs/multi-factor-authentication)
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
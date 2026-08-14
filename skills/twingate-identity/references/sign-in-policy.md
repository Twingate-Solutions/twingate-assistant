---
source: https://www.twingate.com/docs/sign-in-policy
type: docs
fetched: 2026-08-14
source_version: 5ac115b77da5ecf569d78ef3ef3943ef0a590702d54b1d4a0b638b2d2bf1364f
---

# Sign In Policy

## Summary
The Sign In Policy defines baseline requirements users must meet before accessing the Twingate Client. It acts as the first authentication gate—no Resources are accessible until this policy is satisfied, regardless of Resource Policy settings. Configured under **Policies > Sign In Policy** in the Admin Console.

## Key Information
- Evaluated **once at sign-in** and again when the session timer expires (not per-resource)
- Three configurable requirements: Device Security, Authentication Frequency, MFA
- Sign-in sessions **persist across client restarts and reboots**; Resource Policy sessions do not
- Session timer uses a **rolling window**—resets on successful Resource Policy re-authentication

## Prerequisites
- Access to Admin Console
- Device Profiles configured (if using Trusted Profiles for Device Security)
- IdP configured for authentication

## Configuration Values

| Setting | Options/Range | Notes |
|---|---|---|
| Authentication Frequency | 7–31 days | Rolling window, resets on Resource Policy re-auth |
| Device Security | Approved OS or Trusted Profile | Linked directly to Device Profiles config |
| MFA | Enable/Disable | Twingate-native MFA only |

## Step-by-Step
1. Navigate to **Admin Console > Policies > Sign In Policy**
2. Configure **Device Security**: select Approved OS requirements or link a Trusted Profile
3. Set **Authentication Frequency**: choose interval (7–31 days)
4. Toggle **MFA** if requiring Twingate-native MFA at sign-in

## Gotchas
- **Double MFA**: If IdP already enforces MFA, enabling it in Sign In Policy causes users to complete MFA twice. Configure MFA in only one place.
- **Device Security blocks entirely**: Devices failing Device Security requirements cannot sign in at all—they won't see any Resources.
- **Device Profile changes propagate automatically** to Sign In Policy without additional configuration steps.
- **Admin Console has a separate policy**: Configured under **Settings > Admin Console Security**—independent from the Client Sign In Policy.
- A **lenient Sign In Policy** (e.g., 30 days) is acceptable when Resource Policies enforce stricter per-resource controls.

## Sign In Policy vs. Resource Policies

| Aspect | Sign In Policy | Resource Policies |
|---|---|---|
| Scope | Client access (all resources) | Per-resource access |
| Evaluated | At sign-in + session expiry | Each resource access (when timer expired) |
| Session persists on restart | Yes | No |

## Related Docs
- [Device Profiles](https://www.twingate.com/docs/device-profiles)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Multi-Factor Authentication](https://www.twingate.com/docs/multi-factor-authentication)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- Resource Policies documentation
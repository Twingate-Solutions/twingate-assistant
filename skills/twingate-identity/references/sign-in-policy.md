# Sign In Policy

## Summary
The Sign In Policy defines baseline requirements users must meet before accessing the Twingate Client. It acts as a first gate evaluated at sign-in and session expiry, separate from per-Resource Policy controls. Admin Console access has its own independent policy.

## Key Information
- Located at: **Admin Console → Policies → Sign In Policy tab**
- Three configurable requirements: Device Security, Authentication Frequency, MFA
- Evaluated once at sign-in; Resource Policies evaluated per-resource access
- Sign-in sessions persist across client restarts and reboots
- Resource Policy sessions do **not** persist across restarts

## Configuration Values

### Authentication Frequency
- Range: **7 days to 31 days** (rolling window)
- Timer resets on successful Resource Policy re-authentication

### Device Security
- Requires devices to meet either:
  - Approved Operating System requirements, OR
  - A Trusted Profile defined in Device Profiles
- Non-compliant devices are fully blocked from signing in

### MFA
- Native Twingate MFA at sign-in
- Frequency tied to Authentication Frequency setting

## Gotchas
- **Double MFA**: Enabling MFA in both Sign In Policy and IdP forces users to complete MFA twice per sign-in — configure in one place only
- **Device Profiles are linked**: Changes to Device Profiles automatically affect Sign In Policy; no separate sync needed
- **Admin Console policy is separate**: Configured under Settings → Admin Console Security; does not affect Client sign-in
- **Session persistence asymmetry**: Sign-in sessions survive restarts; Resource Policy sessions do not
- **Lenient Sign In Policy is acceptable**: Resource Policies handle per-resource strictness, so a 30-day sign-in interval is reasonable

## Step-by-Step: Configure Sign In Policy
1. Navigate to **Admin Console → Policies → Sign In Policy**
2. Configure **Device Security** (links to Device Profiles)
3. Set **Authentication Frequency** (7–31 days)
4. Enable/disable **MFA** (check if IdP already enforces MFA)
5. Save changes

## How Sign In vs. Resource Policies Relate

| Aspect | Sign In Policy | Resource Policy |
|---|---|---|
| Controls | Client access | Per-resource access |
| Evaluated | At sign-in + session expiry | Per resource access attempt |
| Persists across restarts | Yes | No |

## Prerequisites
- Access to Admin Console with admin permissions
- Device Profiles configured (if using Trusted Profiles for Device Security)
- IdP configured for authentication frequency enforcement

## Related Docs
- [Device Profiles](https://www.twingate.com/docs/device-profiles)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Multi-Factor Authentication](https://www.twingate.com/docs/multi-factor-authentication)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
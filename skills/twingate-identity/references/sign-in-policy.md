# Sign In Policy

## Summary
The Sign In Policy defines baseline requirements users must meet before accessing the Twingate Client. It acts as a first gate evaluated at sign-in and session expiry, separate from per-Resource policies. Users cannot access any Resources until this policy is satisfied.

## Key Information
- Located at: Admin Console → **Policies** → **Sign In Policy** tab
- Three configurable requirements: Device Security, Authentication Frequency, MFA
- Session persists across Client restarts/reboots; Resource Policy sessions do not
- Admin Console has its own separate policy under **Settings → Admin Console Security**

## Configuration Values

| Setting | Options/Range | Notes |
|---|---|---|
| Authentication Frequency | 7–31 days | Rolling window; resets on successful Resource Policy re-auth |
| Device Security | Approved OS or Trusted Profile | Linked directly to Device Profiles config |
| MFA | Enabled/Disabled | Tied to authentication frequency interval |

## Sign-In Requirements Detail

**Device Security**
- Must meet Approved Operating System requirements OR a Trusted Profile from Device Profiles
- Non-compliant devices are blocked from signing in entirely
- Changes to Device Profiles automatically apply here

**Authentication Frequency**
- Rolling window timer—resets when a Resource Policy re-authentication succeeds
- Session expiry signs out the user; re-auth via IdP required to sign back in

**MFA**
- Twingate-native MFA, prompted each sign-in
- Frequency tied to the authentication frequency setting

## Sign In Policy vs. Resource Policies

| | Sign In Policy | Resource Policies |
|---|---|---|
| Controls | Client access | Per-Resource access |
| Evaluated | Once at sign-in + session expiry | Each Resource access (when timer expired) |
| Session persists across restart | Yes | No |

## Gotchas
- **Double MFA**: Enabling MFA in both the IdP and Sign In Policy causes users to complete MFA twice. Configure in one place only.
- **Lenient Sign In Policy is intentional**: Use Resource Policies for stricter per-resource controls; Sign In Policy doesn't need to be restrictive.
- **Device Profiles are shared**: Modifying Device Profiles affects the Sign In Policy automatically—no separate update needed.
- **Session timer is rolling**: Active users accessing authenticated Resources auto-extend their sign-in session.
- **Admin Console policy is separate**: Changing the Sign In Policy does not affect Admin Console access requirements.

## Related Docs
- [Device Profiles](https://www.twingate.com/docs/device-profiles)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Multi-Factor Authentication](https://www.twingate.com/docs/multi-factor-authentication)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- Resource Policies documentation
# Sign In Policy

## Summary
The Sign In Policy defines baseline requirements users must meet before accessing the Twingate Client. It acts as a prerequisite gate—all users must satisfy it before any Resources are accessible, regardless of Resource Policy permissiveness. Configured in Admin Console under **Policies > Sign In Policy**.

## Key Information
- Three configurable requirements: Device Security, Authentication Frequency, MFA
- Evaluated once at sign-in and again when session timer expires
- Sign-in sessions **persist across Client restarts/reboots**; Resource Policy sessions do not
- Session timer uses a **rolling window**—resets on successful Resource Policy re-authentication
- Session expiry causes full Client sign-out; user must re-authenticate via IdP

## Prerequisites
- Device Profiles configured (required for Device Security requirement)
- IdP integration configured (for authentication frequency/session management)

## Configuration Values

| Setting | Options/Range |
|---|---|
| Authentication Frequency | 7 days to 31 days (rolling window) |
| MFA | Enabled / Disabled |
| Device Security | Approved OS requirements OR Trusted Device Profile |

## Step-by-Step
1. Navigate to Admin Console → **Policies** → **Sign In Policy** tab
2. Configure **Device Security**: link to existing Device Profiles or Approved OS requirements
3. Set **Authentication Frequency**: choose interval (7–31 days)
4. Configure **MFA**: enable only if not already enforced via IdP

## Gotchas
- **Double MFA**: Enabling MFA in both Sign In Policy and IdP forces users to complete MFA twice per sign-in—configure in one place only
- **Device Security is blocking**: Devices failing Device Security requirements are fully blocked from signing in (no fallback)
- **Device Profile changes auto-propagate**: Modifying Device Profiles immediately affects Sign In Policy behavior
- **Admin Console has a separate policy**: Configured under Settings → Admin Console Security; completely independent of Client Sign In Policy
- **Lenient Sign In Policy is intentional**: Resource Policies handle per-resource strictness; Sign In Policy doesn't need to be restrictive

## Sign In Policy vs Resource Policies

| | Sign In Policy | Resource Policies |
|---|---|---|
| Controls | Client access | Per-resource access |
| Evaluated | At sign-in + session expiry | Each resource access (when timer expired) |
| Session persists on restart | ✅ Yes | ❌ No |

## Related Docs
- Device Profiles
- How Sessions Work
- Multi-Factor Authentication
- Admin Console Security
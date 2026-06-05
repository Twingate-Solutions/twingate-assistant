# Sign In Policy

## Summary
The Sign In Policy defines baseline requirements users must meet before accessing the Twingate Client. It acts as a first gate—no Resources are visible or accessible until policy is satisfied. Configured under **Policies > Sign In Policy** in the Admin Console.

## Key Information
- Policy evaluated **once at sign-in** and again when session timer expires (unlike Resource Policies which evaluate per-access)
- Three configurable requirements: Device Security, Authentication Frequency, MFA
- Sign-in sessions **persist across Client restarts and reboots**; Resource Policy sessions do not
- Rolling window session timer—resets when a Resource Policy re-authentication succeeds

## Configuration Values

| Setting | Options/Range |
|---|---|
| Authentication Frequency | 7 days to 31 days (rolling window) |
| Device Security | Approved OS requirements OR Trusted Profile (from Device Profiles) |
| MFA | Enabled/Disabled (Twingate native MFA) |

## Sign-in Requirements Detail

### Device Security
- Links directly to Device Profiles configuration—changes there auto-reflect here
- Non-compliant devices are **blocked entirely** from signing in

### Authentication Frequency
- Rolling window resets on successful Resource Policy re-authentication
- Session expiry signs user out; next sign-in triggers IdP authentication prompt

### MFA
- Twingate native MFA, tied to authentication frequency interval
- **Do not enable in both IdP and Sign In Policy**—users will be prompted twice

## Gotchas
- Sign In Policy and Admin Console Security are **separate configurations**; Admin Console policy lives under **Settings > Admin Console Security**
- Enabling MFA at both IdP level and Sign In Policy level causes double MFA prompts at sign-in
- Device Profile changes automatically affect Sign In Policy—no separate update needed
- A lenient Sign In Policy (e.g., 31 days) is acceptable when Resource Policies enforce stricter per-resource controls
- Resource Policy session timers are **not** maintained across restarts; Sign In Policy sessions are

## Relationship: Sign In Policy vs. Resource Policies

| Aspect | Sign In Policy | Resource Policies |
|---|---|---|
| Controls | Client access | Per-Resource access |
| Evaluated | At sign-in + session expiry | Each Resource access attempt |
| Session persists on restart | Yes | No |

## Prerequisites
- Access to Admin Console
- Device Profiles configured (if using Trusted Profiles for Device Security)
- IdP integration configured (for authentication frequency/MFA redirect)

## Related Docs
- Device Profiles
- How Sessions Work
- Multi-Factor Authentication
- Admin Console Security
- Resource Policies

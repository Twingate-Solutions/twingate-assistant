# Security Policies

## Summary
Twingate uses layered policies to control network access, configured under the Admin Console **Policies** tab. Three policy types work together: Resource Policies (per-resource requirements), Sign In Policy (baseline login requirements), and Device Profiles (device trust definitions).

## Key Information

- **Three policy types**: Resource Policies, Sign In Policy, Device Profiles
- **Evaluation order**: Device Profiles → Sign In Policy → Resource Policy
- Device posture checked at sign-in and ~every 5 minutes thereafter
- Admin Console session is fixed at 1 hour (static, non-configurable)
- Resource Policy re-auth success resets the Sign In Policy session timer (rolling window)
- IdP session expiry is captured at sign-in and compared on each policy check

## Resource Policies

- Applied per-Resource; controls authentication frequency, MFA, device security, and geoblocking (Enterprise only)
- Default Policy auto-assigned to new Resources
- Group-level overrides apply the **more permissive** of the two policies
- Group overrides persist even if Resource-level policy changes
- **Best practice**: Set strictest policy at Resource level; use Group overrides to relax for specific teams
- Authentication requirement can be disabled to create device-only policies (Sign In Policy session must still be valid)

## Sign In Policy

- Baseline for all users before accessing any Resource
- Three requirements: Device Security, Authentication Frequency, MFA
- Authentication frequency uses a **rolling window** (resets on qualifying Resource Policy re-auth)
- **Best practice**: Set lenient (e.g., 30-day frequency); enforce stricter controls via Resource Policies

## Device Profiles

### Trusted Profiles
- One profile per platform; requires a verification method
- **Supported integrations**: Manual, CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password
- Can include additional device posture checks
- Referenced in both Sign In Policy and Resource Policies

### Approved Operating Systems
- Enable/disable per platform; blocking a platform prevents sign-in entirely
- Per-platform posture checks: disk encryption, screen lock, firewall, minimum OS version

## Configuration Values

| Setting | Notes |
|---|---|
| Admin Console session | 1 hour (fixed) |
| Device posture check interval | ~5 minutes |
| Sign In Policy frequency | Configurable (recommended: 30 days) |
| Resource Policy auth frequency | Configurable per policy |
| Geoblocking | Enterprise plan only |

## Gotchas

- Group-level policy overrides apply the **more permissive** policy — set the strictest policy at Resource level
- Group overrides are **not** automatically reset when the Resource-level policy changes
- IdP session expiry (not Twingate session) governs re-auth redirects; short IdP sessions cause frequent re-auth prompts
- Disabling authentication on a Resource Policy only skips Resource-level re-auth; Sign In Policy session must still be valid
- Admin Console session is separate from user sessions and cannot be extended

## Related Docs

- Resource Policies
- Device-only Resource Policies
- How Sessions Work
- Approved Operating Systems
- Device Profiles & Device Posture Checks
- Admin Console Security
- Policy Overrides
# Security Policies

## Summary
Twingate uses layered policies to control network access, configured under the **Policies** tab in the Admin Console. Three components work together: Resource Policies (per-resource requirements), Sign In Policy (baseline sign-in requirements), and Device Profiles (device trust definitions).

## Key Information

- **Three policy types**: Resource Policies, Sign In Policy, Device Profiles
- **Evaluation order**: Device Profiles → Sign In Policy → Resource Policy (all must pass)
- Device posture checked at sign-in and ~every 5 minutes thereafter
- Admin Console session: fixed 1-hour static timeout (cannot be changed)
- When Resource Policy re-auth succeeds and is a superset of Sign In Policy, the Sign In Policy session timer resets (rolling window)

## Resource Policies

- Define per-resource requirements: Authentication frequency, MFA, Device Security, Location (geoblocking = Enterprise only)
- Assigned at Resource level; applies to all Groups accessing that Resource
- **Group-level overrides**: Twingate applies the **more permissive** of Resource policy vs. Group override
- Recommended: Set strictest policy at Resource level, use Group overrides to relax
- Group overrides persist if Resource-level policy changes
- Authentication requirement can be disabled → device-only policy (Sign In Policy session still required)

## Sign In Policy

- Baseline for all users before accessing any Resource
- Three settings: Device Security, Authentication frequency, MFA
- Authentication frequency uses a **rolling window** (resets on successful Resource Policy re-auth)
- **Recommended**: Set lenient (e.g., 30-day frequency); use Resource Policies for sensitive resources

## Device Profiles

### Trusted Profiles
- Single platform per profile
- Verification methods: Manual, CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password
- Can include additional posture checks on top of verification method
- Referenced in Sign In Policy and/or Resource Policies

### Approved Operating Systems
- Enable/disable platforms globally (blocking a platform prevents all sign-ins from it)
- Per-platform posture checks: disk encryption, screen lock, firewall, minimum OS version

## How Sessions Work

- Twingate stores IdP session expiry at sign-in
- On policy re-auth check: compares current time to stored expiry; if valid, no redirect
- After expiry: redirects to IdP, captures new expiry
- **IdP session lifetime directly affects re-authentication behavior**

## Gotchas

- Group-level policy overrides apply the **more permissive** policy — set strict defaults at Resource level
- Group overrides are **not reset** when Resource-level policy changes; must be manually cleared
- Disabling authentication on a Resource Policy still requires a valid Sign In Policy session
- Admin Console has a **separate, fixed 1-hour session** that cannot be modified
- Geoblocking (Location Requirements) is **Enterprise plan only**
- Device posture is re-evaluated ~every 5 minutes, not just at access time

## Prerequisites

- Admin Console access
- Identity provider (IdP) configured for authentication
- MDM/EDR integration configured if using Trusted Profiles (optional)

## Related Docs

- Resource Policies
- Device-only Resource Policies
- Device Profiles
- Device Posture Checks
- Approved Operating Systems
- How Sessions Work
- Admin Console Security
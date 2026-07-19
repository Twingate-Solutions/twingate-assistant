# Security Policies

## Summary
Twingate uses layered policies to control network access, configured under the **Policies** tab in the Admin Console. Three components work together: Resource Policies (per-resource access requirements), Sign In Policy (baseline client sign-in requirements), and Device Profiles (device trust/posture definitions).

## Key Information

- **Three policy layers** evaluated in order: Device Profiles → Sign In Policy → Resource Policy
- Device posture checked at sign-in and approximately every **5 minutes** thereafter
- **Default Policy** automatically assigned to new Resources
- Resource Policies support up to 3 requirement types: Authentication, Device Security, Location (geoblocking is Enterprise-only)
- Admin Console session = **1 hour static** (non-configurable, non-rolling)

## Policy Components

### Resource Policies
- Assigned at Resource level; applies to all Groups with access
- **Group-level overrides** available; Twingate applies the **more permissive** of the two policies
- Can disable authentication requirement to create **device-only policies** (Sign In Policy session still required)
- Group overrides persist even if Resource-level policy changes

### Sign In Policy
- Three requirements: Device Security, Authentication frequency, MFA
- Authentication frequency uses a **rolling window** — resets when a Resource Policy re-auth succeeds (if Resource Policy is a superset of Sign In Policy requirements)
- Recommended: set lenient (e.g., 30-day frequency); use Resource Policies for sensitive resources

### Device Profiles
Two sections:
- **Trusted Profiles**: Verification via manual, CrowdStrike, Intune, Jamf, Kandji, SentinelOne, or 1Password; per-platform; supports additional posture checks
- **Approved Operating Systems**: Enable/disable platforms; per-platform posture checks (disk encryption, screen lock, firewall, min OS version); blocking a platform prevents sign-in entirely

## Configuration Values

| Setting | Notes |
|---|---|
| Authentication frequency (Sign In Policy) | Recommended: 30 days |
| Admin Console session | 1 hour, static, non-configurable |
| Device posture check interval | ~5 minutes |
| Geoblocking (Location Requirements) | Enterprise plan only |

## Gotchas

- Group-level policy overrides apply the **more permissive** policy — set the strictest policy at Resource level, use overrides to relax
- Group overrides are **not reset** when Resource-level policy changes; must be explicitly cleared
- IdP session expiry is captured and stored at sign-in; Twingate checks stored expiry on re-auth, not a fresh IdP call
- Disabling authentication on a Resource Policy skips re-auth checks but still requires a valid Sign In Policy session
- Blocking an OS in Approved Operating Systems prevents users on that platform from signing in at all

## Related Docs
- Resource Policies (detailed)
- Device-only Resource Policies
- How Sessions Work
- Device Profiles
- Device Posture Checks
- Approved Operating Systems
- Admin Console Security
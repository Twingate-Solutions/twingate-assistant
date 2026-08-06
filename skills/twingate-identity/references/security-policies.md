---
source: https://www.twingate.com/docs/security-policies
type: docs
fetched: 2026-08-05
source_version: b01b72f9ecb3d0b3d3a1943450a92fe7685a4c3d47ed7f5b76fe80d5852f0172
---

# Security Policies

## Summary
Twingate uses layered policies to control network access, configured under the **Policies** tab in the Admin Console. Three components work together: Resource Policies (per-resource access rules), Sign In Policy (baseline client access requirements), and Device Profiles (device trust definitions).

## Key Information

- **Three policy types**: Resource Policies, Sign In Policy, Device Profiles
- **Evaluation order**: Device Profiles → Sign In Policy → Resource Policy
- Device posture checked at sign-in and ~every 5 minutes thereafter
- Admin Console has a fixed 1-hour session (non-configurable, non-rolling)
- Sign In Policy session timer **resets** when a Resource Policy re-auth succeeds (if Resource Policy requirements are a superset of Sign In Policy)

## Prerequisites

- Admin Console access
- Enterprise plan required for geoblocking (location requirements)
- MDM/EDR integration configured if using Trusted Profiles with those providers

## Resource Policies

**Requirements per policy (up to 3 types):**
- Authentication frequency + MFA requirement
- Device Security (Trusted Profiles or approved OS)
- Location/geoblocking (Enterprise only)

**Policy assignment:**
- Assigned at Resource level; applies to all Groups on that Resource
- Groups can have per-Resource policy overrides
- When override exists, Twingate applies the **more permissive** of the two policies
- Group overrides persist if the Resource-level policy changes

**Best practice**: Set strictest policy at Resource level; use Group overrides to relax for specific teams.

**Disable auth requirement** on a Resource Policy to create a device-only policy (user still needs valid Sign In Policy session).

## Sign In Policy

Three requirements:
1. Device Security (Approved OS or Trusted Profile)
2. Authentication frequency (rolling window, resets on Resource Policy re-auth)
3. MFA (Twingate native 2FA)

**Recommended config**: Set lenient Sign In Policy (e.g., 30-day auth frequency); enforce strict requirements via Resource Policies.

## Device Profiles

### Trusted Profiles
- One platform per profile
- Verification methods: Manual, CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password
- Can add device posture checks on top of verification method
- Referenced in Sign In Policy and/or Resource Policies

### Approved Operating Systems
- Enable/disable per platform
- Blocking a platform prevents sign-in entirely
- Per-platform posture checks: disk encryption, screen lock, firewall, minimum OS version

## Session/Auth Gotchas

- **IdP session expiry is captured at sign-in**; Twingate stores the expiry timestamp and compares on each policy check — no redirect occurs until expiry passes
- Resource Policy re-auth extends Sign In Policy session only if Resource Policy requirements are a **superset** of Sign In Policy
- Admin Console session: **1 hour, static, cannot be changed**
- Default Policy is auto-assigned to new Resources — configure it intentionally

## Configuration Values

| Setting | Notes |
|---|---|
| Admin Console session | 1 hour (fixed) |
| Device posture check interval | ~5 minutes |
| Recommended Sign In Policy frequency | 30 days |
| Geoblocking | Enterprise plan only |

## Related Docs

- Resource Policies
- Device-only Resource Policies
- Device Profiles
- Device Posture Checks
- Approved Operating Systems
- How Sessions Work
- Admin Console Security
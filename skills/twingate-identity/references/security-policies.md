---
source: https://www.twingate.com/docs/security-policies
type: docs
fetched: 2026-09-20
source_version: 1aed2e27cb8f56f0d904921bd96458a189e0f64080392c56b4a78060af6d5465
---

# Security Policies

## Page Title
Security Policies

## Summary
Twingate uses a layered policy system to control network access, configured under the **Policies** tab in the Admin Console. Three components work together: Resource Policies (per-resource access requirements), Sign In Policy (baseline client authentication), and Device Profiles (device trust definitions).

## Key Information
- **Three policy types**: Resource Policies, Sign In Policy, Device Profiles
- Every network includes a **Default Policy** auto-assigned to new Resources
- Policy evaluation order: Device Profiles → Sign In Policy → Resource Policy
- Device posture re-checked approximately **every 5 minutes**
- Admin Console session is fixed at **1 hour** (non-configurable, non-rolling)

## Resource Policies
- Define per-Resource requirements: Authentication frequency/MFA, Device Security, Location (geoblocking, Enterprise only)
- Assigned at Resource level; Groups can have **override policies**
- Group-level override always takes precedence over Resource-level policy
- If user belongs to both an override Group and a plain Group, Twingate disambiguates among Group-tied policies only
- **Best practice**: Apply strictest policy at Resource level; use Group overrides to relax for specific teams
- Authentication requirement can be **disabled** to create device-only policies (relies on Sign In Policy session validity)

## Sign In Policy
- Baseline requirements before any Resource access
- Three settings: Device Security, Authentication frequency, MFA
- Session timer uses a **rolling window** — resets when Resource Policy re-auth succeeds (if Resource Policy is a superset of Sign In Policy requirements)
- **Best practice**: Keep lenient (e.g., 30-day frequency); use Resource Policies for sensitive resources

## Device Profiles
**Trusted Profiles** — per-platform device verification:
- Methods: Manual, CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password
- Can include additional posture checks
- Referenced in both Sign In Policy and Resource Policies

**Approved Operating Systems** — platform baselines:
- Enable/disable per platform (blocking prevents sign-in entirely)
- Posture checks: disk encryption, screen lock, firewall, minimum OS version (varies by platform)

## Configuration Values
| Setting | Location | Notes |
|---|---|---|
| Authentication frequency | Resource Policy / Sign In Policy | Rolling window for Sign In; per-policy for Resources |
| MFA requirement | Resource Policy / Sign In Policy | Twingate native 2FA |
| Geoblocking | Resource Policy | Enterprise tier only |
| Admin Console session | Fixed | 1 hour, static, cannot change |

## Gotchas
- **IdP session expiry is captured at sign-in** — Twingate stores the IdP-returned expiry time; re-auth check compares current time to stored expiry, not a fresh IdP check
- A user in both an override Group and a non-override Group for the same Resource is **not** automatically locked into the override — the non-override Group still contributes the Resource-level policy to comparison
- Group-level overrides persist even if the Resource-level policy changes — must be **explicitly reset**
- Disabling authentication on a Resource Policy skips re-auth prompts but does **not** bypass Sign In Policy session validity

## Prerequisites
- Admin Console access
- Enterprise plan for geoblocking/location requirements

## Related Docs
- Resource Policies
- How Twingate resolves multiple policies
- Device-only Resource Policies
- How Sessions Work
- Device Profiles
- Device Posture Checks
- Approved Operating Systems
- Admin Console Security
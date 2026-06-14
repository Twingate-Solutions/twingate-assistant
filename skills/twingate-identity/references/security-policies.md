# Security Policies

## Summary
Twingate uses three layered policy types to control network access: Resource Policies (per-resource requirements), Sign In Policy (baseline client access), and Device Profiles (device trust definitions). All configuration is in the Admin Console under the **Policies** tab.

## Key Information
- **Three policy types**: Resource Policies → Sign In Policy → Device Profiles (evaluated in this order)
- Resource Policies support: Authentication frequency, Device Security, Location/geoblocking (Enterprise only)
- Default Policy auto-assigned to new Resources; additional policies can be created
- Group-level policy overrides apply whichever policy is **more permissive** (Resource-level vs Group-level)
- Device posture checked at sign-in and approximately every 5 minutes thereafter
- Admin Console session = 1 hour, static (non-configurable)

## Policy Layer Evaluation Order
1. **Device Profiles** — device must meet Approved OS requirements or a Trusted Profile
2. **Sign In Policy** — user must have valid sign-in session (IdP-based)
3. **Resource Policy** — evaluated per Resource at access time

## Configuration Values

| Setting | Recommendation |
|---|---|
| Sign In Policy auth frequency | 30 days (lenient baseline) |
| Resource Policy | Strict (1D-MFA-AllTrusted pattern) |
| Group overrides | Use to relax for specific teams |
| Admin Console session | 1 hour (fixed) |

## Trusted Profile Verification Methods
- Manual verification
- CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password

## Device Posture Checks (per platform)
- Hard drive encryption, screen lock, firewall, minimum OS version

## Gotchas
- Group-level overrides persist even if the Resource-level policy changes — must be explicitly reset
- When override is set, Twingate applies the **more permissive** policy (not stricter)
- IdP session expiry is captured and stored at sign-in; Twingate compares current time against stored expiry — IdP session lifetime directly affects re-auth behavior
- Disabling authentication on a Resource Policy creates device-only policy; user won't re-authenticate as long as Sign In Policy session is valid
- Resource Policy re-auth resets the Sign In Policy session timer only if its requirements are a **superset** of Sign In Policy requirements
- Blocking a platform under Approved Operating Systems prevents all users on that platform from signing in entirely

## Best Practice
Set the strictest policy at the Resource level; use Group overrides to relax for specific teams. Keep Sign In Policy lenient to reduce unnecessary re-auth prompts.

## Related Docs
- Resource Policies
- Device-only Resource Policies
- How Sessions Work
- Device Profiles
- Approved Operating Systems
- Device Posture Checks
- Admin Console Security
- Policy Overrides
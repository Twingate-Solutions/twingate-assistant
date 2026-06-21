# Security Policies

## Summary
Twingate uses a layered policy system to control network access through three components: Resource Policies, Sign In Policy, and Device Profiles. All configuration lives under the **Policies** tab in the Admin Console. Policies are evaluated in order: device compliance → sign-in session → resource-specific requirements.

## Key Information
- **Resource Policies**: Per-resource rules covering authentication frequency, MFA, device requirements, and geoblocking (Enterprise only)
- **Sign In Policy**: Baseline gate all users must pass before accessing any resource; applies globally
- **Device Profiles**: Define trusted devices via MDM/EDR integrations or manual verification; set per-platform OS requirements
- Default Policy auto-assigns to new Resources
- Admin Console session: fixed 1-hour static timeout, not configurable

## Policy Evaluation Order
1. **Device Profiles** — device must meet Approved OS or Trusted Profile (checked at sign-in + ~every 5 min)
2. **Sign In Policy** — valid IdP session required
3. **Resource Policy** — evaluated per-resource access attempt

## Resource Policy Overrides
- Assigned at resource level; Groups can have per-Group overrides
- Twingate applies the **more permissive** of resource-level or group-level policy
- Best practice: set **strictest policy at resource level**, use group overrides to relax for specific teams
- Group overrides persist if resource-level policy changes later

## Configuration Options

### Resource Policy Requirements
| Type | Details |
|------|---------|
| Authentication | Re-auth frequency, MFA required |
| Device Security | Trusted Profiles or approved OS |
| Location | Country-level geoblocking (Enterprise) |

### Trusted Profile Verification Methods
- Manual verification
- CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password
- One platform per profile

### Approved OS Posture Checks (per platform)
- Hard drive encryption, screen lock, firewall, minimum OS version

## Session Behavior
- IdP session expiry is captured and stored at sign-in
- Resource Policy re-auth checks stored expiry (no redirect if still valid)
- When Resource Policy re-auth succeeds and its requirements are a **superset** of Sign In Policy, the Sign-In session timer **resets** (rolling window)
- Sign In Policy timer resets on successful resource-level re-auth

## Recommended Configuration
- Sign In Policy: lenient (e.g., 30-day frequency)
- Resource Policies: enforce strict controls on sensitive resources
- Disable authentication on Resource Policy to create **device-only policies** (user still needs valid Sign In session)

## Gotchas
- Group-level overrides apply the **more permissive** policy — don't use overrides to tighten security
- Disabling authentication requirement on a Resource Policy skips re-auth checks but still enforces device requirements
- IdP session expiry drives re-auth behavior; short IdP sessions cause frequent redirects
- Admin Console 1-hour session is static and cannot be modified
- Geoblocking is Enterprise-only

## Related Docs
- Resource Policies
- Device-only Resource Policies
- How Sessions Work
- Device Profiles
- Device Posture Checks
- Approved Operating Systems
- Admin Console Security
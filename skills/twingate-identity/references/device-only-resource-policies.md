---
source: https://www.twingate.com/docs/device-only-resource-policies
type: docs
fetched: 2026-11-13
source_version: 2a2d9a9c8c7800d4c7bbdf01fbb6ff0769f8364771dd4cf76911bcda5ac1b0b4
trust: official
---

# Device-only Policies

## Summary
A device-only Resource Policy enforces device security requirements without requiring the user to re-authenticate. It suits system services, monitoring endpoints, and Resources that must be reachable before an interactive user session exists. The Sign In Policy is still always enforced.

## Key Information
- By default, Resource Policies include both authentication and device requirements. Device-only mode disables the authentication requirement and keeps only the device check.
- The Sign In Policy still applies. Users need a valid sign-in session (authenticated within the Sign In Policy's configured timeframe) to access any Resource, including those behind device-only policies.
- **Sign In Policy timer does not extend.** Device-only access does not count as authentication, so the timer keeps counting down from its last reset.
- **Sessions persist across restarts.** After a Client restart or device reboot, device-only Resources are immediately accessible if the Sign In session hasn't expired and the device still meets the required profile. Standard Resource Policy sessions do not persist across restarts.
- **Device posture is re-checked about every 5 minutes.** Access is revoked at the next check if the device falls out of compliance.
- **Windows:** device-only policies can be combined with Start Before Logon to give system-level services network access before interactive sign-in.

## Prerequisites
- Admin Console access to edit Resource Policies.
- A device profile/security requirement configured on the policy (the device check is the only remaining control).
- A Sign In Policy that gives a suitable session duration.
- For Start Before Logon: Windows devices with that feature set up.

## Step-by-Step
1. Open the Admin Console and go to the Resource Policy you want to change.
2. Next to **Authentication Requirements**, select **Disable**.
3. Confirm the policy shows device-only mode, then save.

## Configuration Values
- No env vars, CLI flags, or API parameters are given on this page.
- UI setting: Authentication Requirements → Disable.
- Posture re-evaluation interval: ~5 minutes (not documented as configurable).

## Gotchas
- Disabling authentication does not bypass the Sign In Policy. Once that session expires, device-only access stops until the user signs in again.
- Device-only access won't keep the Sign In session alive, so always-on scenarios still depend on the Sign In Policy timeframe.
- Non-compliant devices lose access within about 5 minutes, not instantly.
- Restart behavior differs from standard policies, so don't assume the same session semantics.

## Related Docs
- How Sessions Work (sessions guide covering Sign In Policy and IdP session interaction)
- Resource Policies
- Sign In Policies
- Start Before Logon (Windows)
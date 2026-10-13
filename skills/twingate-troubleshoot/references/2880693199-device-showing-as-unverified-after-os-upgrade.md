---
source: https://help.twingate.com/articles/2880693199-device-showing-as-unverified-after-os-upgrade
type: help
fetched: 2026-10-11
source_version: f2c316138436e9139c9db02d8f394c203924169ddbe9fd0267f8534be8e980a6
trust: official
---

# Device Showing as Unverified After OS Major Version Upgrade

## Summary
When a device shows as unverified after a major OS upgrade, the new OS version hasn't been added to the Device Trust allowed versions list. Twingate uses an explicit allowlist for major OS versions, not a minimum-version-floor model. Adding the new major version to the Device Trust profile resolves the issue.

## Key Information
- **Allowed versions model**: Major OS versions must be explicitly allowlisted — upgrading beyond the highest allowed major version breaks verification
- **Minor version minimums**: For each allowed major version, you can optionally set a minimum minor version (e.g., allow macOS 27.x but require ≥ 27.1.0)
- **Scope**: Affects any user who upgrades to a new major OS version not yet in the profile
- **Impact**: Device shows as "unverified" and cannot access Twingate-protected resources until resolved

## Prerequisites
- Admin access to the Twingate Admin Console
- Knowledge of which major OS version the affected device upgraded to

## Step-by-Step: Add New Major OS Version

1. Log in to the **Twingate Admin Console**
2. Navigate to **Device Trust** → select the relevant profile
3. Locate the **OS version settings**
4. Add the new major OS version (e.g., macOS 27) to the allowed versions list
5. Optionally set a minimum minor version requirement
6. **Save** changes
7. Affected users should now pass device verification

## Gotchas
- This is **not** a minimum-floor model — allowing macOS 26 does not automatically allow macOS 27
- Every new major OS release (e.g., annual macOS updates) requires a manual admin action before devices on that version can be verified
- Consider proactively adding anticipated new major versions ahead of user upgrades to avoid disruption
- Minor version gating can block users on `.0` releases if a minimum minor version is set (e.g., 27.1.0 required means 27.0.x fails)

## Related Docs
- Twingate Admin Console: Device Trust profile configuration
- Twingate Help: Device Trust overview
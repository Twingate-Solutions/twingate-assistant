---
source: https://help.twingate.com/articles/2880693199-device-showing-as-unverified-after-os-upgrade
type: help
fetched: 2026-09-20
source_version: fabd8b00615dbe415005297bbf68571f553dcf744f396d8bcca9ddaf56697049
---

# Device Showing as Unverified After OS Major Version Upgrade

## Summary
When a device shows as unverified after a major OS upgrade, it's because Device Trust uses an explicit allowlist of major OS versions rather than a minimum version floor. Each new major OS version must be manually added to the Device Trust profile before devices running it can be verified.

## Key Information
- Device Trust OS version settings work as an **allowlist**, not a minimum version check
- Each major OS version must be explicitly added to the allowed versions list
- Per major version, you can optionally set a **minimum minor version** requirement
- Example: Allowing major version `27` with minimum minor `27.1.0` means `27.0.x` fails but `27.1.0+` passes
- This applies every time a new major OS version is released

## Prerequisites
- Access to Twingate Admin Console
- Permission to modify Device Trust profiles

## Step-by-Step Resolution

1. Log in to the **Twingate Admin Console**
2. Navigate to the **Device Trust profile**
3. Locate the OS version settings
4. Add the new major OS version (e.g., macOS 27) to the allowed versions list
5. Optionally set a minimum minor version requirement
6. Save changes

Affected users' devices will be verifiable immediately after the change is saved.

## Gotchas
- **Not a minimum floor**: Adding macOS 26 does not automatically allow macOS 27 — each major version is independent
- **Proactive updates needed**: Plan to update Device Trust profiles when new major OS versions release to avoid user disruption
- Minor version gating is additive — if the major version isn't in the allowlist, minor version settings are irrelevant

## Related Docs
- Twingate Device Trust configuration
- Twingate Admin Console
---
source: https://help.twingate.com/articles/2880693199-device-showing-as-unverified-after-os-upgrade
type: help
fetched: 2026-09-27
source_version: 517c38863981d7b368fff46bdd6c3ed2aa41005a590a82ffc25939ca4c0501bb
---

# Device Showing as Unverified After OS Major Version Upgrade

## Summary
After a major OS version upgrade, devices may show as unverified because Twingate's Device Trust uses an explicit allowlist of major OS versions rather than a minimum version floor. Each new major OS version must be manually added to the Device Trust profile before devices running it can be verified.

## Key Information
- Device Trust OS version configuration is an **allowlist**, not a minimum version check
- Each major OS version must be explicitly permitted in the Device Trust profile
- Per major version, you can optionally set a **minimum minor version** (e.g., allow macOS 27 but require ≥ 27.1.0)
- Devices on minor versions below the minimum minor version will fail verification even if the major version is allowed
- This applies whenever any new major OS version is released

## Prerequisites
- Admin access to the Twingate Admin Console
- An existing Device Trust profile configured

## Step-by-Step: Add a New Major OS Version

1. Log in to the **Twingate Admin Console**
2. Navigate to your **Device Trust profile**
3. Locate the OS version settings section
4. Add the new major OS version (e.g., macOS 27) to the allowed versions list
5. Optionally set a minimum minor version requirement
6. Save changes

Affected users' devices should pass verification immediately after saving.

## Configuration Values

| Setting | Description | Example |
|---|---|---|
| Allowed Major Version | Major OS version explicitly permitted | `27` (macOS 27) |
| Minimum Minor Version | Optional floor within an allowed major version | `27.1.0` |

## Gotchas
- Adding a major version with **no minimum minor version** allows all minor versions under it
- Setting a minimum minor version of `27.1.0` blocks devices on `27.0.x` even though major version `27` is allowed
- This behavior affects **every** new major OS release — plan to update Device Trust profiles proactively when OS upgrades roll out to users

## Related Docs
- Twingate Device Trust configuration (Admin Console → Device Trust)
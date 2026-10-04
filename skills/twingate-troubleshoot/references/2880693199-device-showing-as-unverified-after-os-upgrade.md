---
source: https://help.twingate.com/articles/2880693199-device-showing-as-unverified-after-os-upgrade
type: help
fetched: 2026-10-04
source_version: f1fd284d1bdd6c41614efcfd49ea8c926227c6d41cdf45dcbc7b04f120c82bfb
trust: official
---

# Device Showing as Unverified After OS Major Version Upgrade

## Summary
When a device shows as unverified after a major OS upgrade, it's because Twingate's Device Trust uses an explicit allowlist for major OS versions rather than a minimum-version floor. The new major OS version must be manually added to the Device Trust profile before affected devices can be verified.

## Key Information
- Device Trust OS version settings work as an **allowed versions list**, not a minimum version check
- Each allowed major version can have an optional **minimum minor version** requirement
- New major OS releases (e.g., macOS 27) are **not automatically trusted** — they require explicit addition
- Minor version floor example: allowing major `27` with minimum `27.1.0` blocks devices on `27.0.x`

## Prerequisites
- Admin access to the Twingate Admin Console
- An existing Device Trust profile configured with OS version requirements

## Step-by-Step: Add a New Major OS Version

1. Log in to the **Twingate Admin Console**
2. Navigate to your **Device Trust profile**
3. Locate the OS version settings section
4. Add the new major OS version (e.g., macOS 27) to the allowed versions list
5. Optionally configure a minimum minor version requirement
6. Save changes

Affected users' devices should pass verification immediately after the profile is updated.

## Gotchas
- **Proactive management required**: Each new major OS version must be added before or as users upgrade — failure to do so blocks verification for all devices on that version
- **Minor version gating is additive**: Setting a minimum minor version (e.g., `27.1.0`) will block devices even on an allowed major version if they haven't updated to the minimum minor
- This is a common support issue after annual OS release cycles (macOS, Windows, etc.)

## Related Docs
- Twingate Admin Console: Device Trust profile configuration
- [Twingate Help Center](https://help.twingate.com)
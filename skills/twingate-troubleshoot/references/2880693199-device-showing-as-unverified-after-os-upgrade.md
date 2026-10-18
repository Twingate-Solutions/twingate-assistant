---
source: https://help.twingate.com/articles/2880693199-device-showing-as-unverified-after-os-upgrade
type: help
fetched: 2026-10-18
source_version: 69e55a85d6c1d5e0b0f8dfceb9d738180d17045abb3b78f4375d36e46bc3fd2e
trust: official
---

# Device Showing as Unverified After OS Major Version Upgrade

## Summary
When a device shows as unverified after a major OS upgrade, it's because Twingate's Device Trust uses an explicit allowlist for major OS versions rather than a minimum-version floor. Each new major OS version must be manually added to the Device Trust profile before devices running it can be verified.

## Key Information
- Device Trust OS version settings work as an **allowed versions list**, not a minimum version threshold
- Each major OS version must be explicitly added to the allowlist
- Per major version, an optional **minimum minor version** can be set (e.g., allow macOS 27 but require ≥ 27.1.0)
- Devices on a major OS version not in the allowlist will show as **unverified** regardless of patch level

## How Minor Version Requirements Work
| Configuration | Result |
|---|---|
| Allow major `27`, no minor minimum | All `27.x.x` devices trusted |
| Allow major `27`, minimum `27.1.0` | `27.0.x` fails; `27.1.0`+ passes |

## Resolution Steps
1. Log in to the **Twingate Admin Console**
2. Navigate to the relevant **Device Trust profile**
3. Locate the OS version settings
4. Add the new major OS version to the allowed versions list
5. (Optional) Set a minimum minor version requirement
6. Save changes

Users' devices should verify successfully once the new major version is added.

## Gotchas
- This affects **every** new major OS release — plan to update Device Trust profiles proactively when new OS versions are released (e.g., annually for macOS)
- Failing to add the new major version blocks all users on that OS version, even if they are on a fully updated/patched build
- Minor version minimums only apply within an already-allowed major version; a missing major version entry overrides everything

## Related Docs
- Twingate Admin Console → Device Trust profile settings
- Twingate Device Trust documentation (help.twingate.com)
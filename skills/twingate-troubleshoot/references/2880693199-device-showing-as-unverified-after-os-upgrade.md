---
source: https://help.twingate.com/articles/2880693199-device-showing-as-unverified-after-os-upgrade
type: help
fetched: 2026-11-19
source_version: faee1bdc36744d3ccfa896f4053040935e08e2980062fa023036b716cfe79f25
trust: official
---

# Device showing as unverified after OS major version upgrade

## Summary
A device can show as unverified after a major OS upgrade because the new major version isn't in the Device Trust profile's allowed versions list. Twingate treats major OS versions as an explicit allowlist, not a minimum version floor. Adding the new major version to the profile fixes verification.

## Key Information
- Device Trust OS version settings work as an **allowed versions list**, not a minimum version.
- Each allowed major version can also have a **minimum minor version** requirement.
- Example: allowing major version `27` trusts macOS 27.x. Setting a minimum minor version of `27.1.0` rejects `27.0.x` and accepts `27.1.0` or later.
- Every new major OS release (e.g., macOS 27) must be added explicitly before devices running it can be verified.
- Upgraded devices are not automatically trusted, even if the previous major version was allowed.

## Prerequisites
- Access to the Twingate Admin Console with permission to edit Device Trust profiles.
- Knowledge of which major OS version the affected device upgraded to.

## Step-by-Step
1. Log in to the Twingate Admin Console.
2. Go to the relevant Device Trust profile.
3. Find the OS version settings.
4. Add the new major OS version (e.g., macOS 27) as an allowed version.
5. Optionally set a minimum minor version for it.
6. Save changes.
7. Have affected users retry; their devices should then verify.

## Configuration Values
- **Allowed major versions** (per OS): list of major versions that are trusted.
- **Minimum minor version** (per allowed major): e.g., `27.1.0`.
- No env vars, CLI flags, or API parameters are given in this article.

## Gotchas
- Don't assume the setting is a floor. A higher major version is not automatically accepted.
- Plan to update the profile whenever a new major OS version is released, ideally before users upgrade.
- A minimum minor version applies per major version. `27.0.x` fails if the minimum is `27.1.0`, even though major 27 is allowed.
- If a device still fails after adding the version, check that the profile you edited is the one applied to that device or user.

## Related Docs
- Twingate Device Trust profile configuration
- Twingate Admin Console documentation
- Troubleshooting device verification
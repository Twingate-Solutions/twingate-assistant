# Device Profiles (Twingate)

## Summary
Device Profiles define trust criteria controlling which devices can sign in to Twingate and access specific Resources. Configuration has two components: Trusted Device Profiles (MDM/EDR/manual verification per platform) and Approved Operating Systems (baseline posture checks per platform). Devices must satisfy all requirements within a profile; multiple profiles can apply to a single device.

## Key Information
- **Wristband model**: Devices earn profiles; sign-in requires at least one valid profile; Resource access requires the specific profile(s) configured on that Resource's policy
- **All requirements within a profile are additive** — device must pass every check in a profile
- Trusted Device Profiles target a **single platform** each
- Disabling a platform in Approved OS blocks all devices on that platform *unless* they satisfy a Trusted Device Profile for that platform
- Blocked devices see an explanatory message in the Twingate Client

## Prerequisites
- Admin access to Twingate Admin Console
- MDM/EDR integration credentials if using automated verification (CrowdStrike, Intune, Jamf, Iru, SentinelOne, 1Password)
- macOS standalone Client required for firewall and HD encryption posture checks on macOS

## Step-by-Step: Create a Trusted Device Profile
1. Navigate to **Policies → Device Profiles** tab
2. Click **Create**
3. Select target platform
4. Choose verification method (manual, or MDM/EDR integration)
5. Configure optional posture checks
6. Save — profile becomes available automatically in Sign In Policy and Resource Policies

## Configuration Values

### Verification Methods
| Method | Notes |
|---|---|
| Manual | By serial number (bulk upload supported) or device instance; API-programmable |
| CrowdStrike | Via Falcon API + ZTA score |
| Intune | Via compliance status API |
| Jamf | macOS only |
| Iru (Kandji) | macOS only |
| SentinelOne | Via API |
| 1Password | Via Extended Access Management |

### Posture Checks by Platform
| Platform | Available Checks |
|---|---|
| Windows | HD encryption, screen lock, firewall, antivirus, min OS version |
| macOS | Screen lock, biometric config, firewall*, HD encryption*, min OS version |
| Linux | HD encryption, firewall |
| iOS | Screen lock, biometric config, min OS version |
| Android | HD encryption, screen lock, biometric config |

*macOS standalone Client only

### Resource Policy Device Security Options
- `Any Device` — no device restriction
- `Only Trusted Devices` — any Trusted Device Profile
- `Custom` — select specific profiles

## Gotchas
- macOS firewall and HD encryption checks **only work with the standalone Client**, not browser-based access
- Disabling a platform in Approved OS does **not** block devices that satisfy a Trusted Device Profile for that platform
- Serial number bulk upload works before or after device sign-in
- Trusted Device Profiles must be explicitly assigned in Resource Policies — they don't auto-restrict Resources

## Related Docs
- Device Posture Checks reference
- Manually Verified Devices
- CrowdStrike, Intune, Jamf, Iru, SentinelOne, 1Password integration configuration pages
- Sign In Policy
- Resource Policies
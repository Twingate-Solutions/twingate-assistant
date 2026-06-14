# Device Profiles (Twingate Device Security Guide)

## Summary
Device Profiles define trust criteria controlling which devices can sign in to Twingate and access specific Resources. Configuration combines **Trusted Device Profiles** (MDM/EDR/manual verification) and **Approved Operating Systems** (platform-level posture checks). Devices must satisfy all requirements within a profile (additive logic).

## Key Information
- Device Profiles live under **Policies → Device Profiles tab**
- Two components: **Trusted Device Profiles** + **Approved Operating Systems**
- A device needs ≥1 profile satisfied to sign in; Resource access requires the specific profile(s) that policy demands
- All checks within a single Trusted Device Profile are AND logic (all must pass)
- Trusted Device Profiles are automatically available in Sign In Policy and Resource Policies once created

## Verification Methods (Trusted Device Profiles)
- **Manual**: Serial number (bulk upload supported) or individual instance; also via Twingate API
- **MDM/EDR integrations**: CrowdStrike (ZTA score), Intune (compliance status), Jamf (macOS), Iru/Kandji (macOS), SentinelOne, 1Password Extended Access Management

## Posture Checks by Platform (Approved Operating Systems)
| Platform | Checks Available |
|----------|-----------------|
| Windows | HD encryption, screen lock, firewall, antivirus, min OS version |
| macOS | Screen lock, biometric, firewall*, HD encryption*, min OS version |
| Linux | HD encryption, firewall |
| iOS | Screen lock, biometric, min OS version |
| Android | HD encryption, screen lock, biometric |

*macOS firewall and HD encryption require **macOS standalone Client** only.

## Configuration Steps
1. Go to **Policies → Device Profiles**
2. Click **Create** → select platform → choose verification method
3. Add optional posture checks
4. In Resource Policies, set **Device Security** to `Only Trusted Devices` or `Custom` to select specific profiles

## Blocking Platforms
- Disable a platform in Approved Operating Systems → all devices on that platform blocked at sign-in
- Exception: devices satisfying a Trusted Device Profile for that platform still pass
- Use case: block unmanaged devices while permitting MDM-enrolled ones

## Common Patterns
- **Contractors (baseline) + Employees (trusted)**: Approved OS for contractors; Trusted Profiles for employees; assign Trusted Profiles to sensitive Resources
- **Block Android except test devices**: Disable Android in Approved OS; create manual-verification Trusted Profile for test devices
- **Require MDM for macOS**: Disable macOS in Approved OS; create Trusted Profile with MDM integration

## Gotchas
- Disabling a platform blocks sign-in entirely unless a Trusted Device Profile for that platform exists and is satisfied
- macOS firewall/HD encryption posture checks only work with standalone Client (not browser-based)
- Trusted Device Profiles are per-platform; one profile cannot span multiple OSes
- Blocked devices see an explicit block message in the Twingate Client

## Related Docs
- Device Posture Checks (detailed per-platform evaluation logic)
- Manually Verified Devices
- CrowdStrike / Intune / Jamf / Iru / SentinelOne / 1Password configuration guides
- Sign In Policy
- Resource Policies
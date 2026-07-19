# Device Profiles (Twingate Device Security)

## Summary
Device Profiles define trust criteria for device access to Twingate. Configuration includes Trusted Device Profiles (MDM/EDR/manual verification) and Approved Operating Systems (baseline posture checks). Profiles act additively—devices must satisfy all requirements in a profile, and resources can require specific profiles.

## Key Information
- **Two components**: Trusted Device Profiles + Approved Operating Systems
- **Sign-in**: Device needs at least one valid profile/OS approval
- **Resource access**: Specific profiles can be required per resource
- **All requirements are additive**: Device must pass every check in a profile
- Blocked devices see an error message in the Twingate Client

## Verification Methods (Trusted Device Profiles)
| Method | Notes |
|--------|-------|
| Manual | By serial number, bulk upload, or Twingate API |
| CrowdStrike | Via Falcon API + ZTA score |
| Intune | Compliance status via Microsoft Intune API |
| Jamf | macOS only |
| Iru (Kandji) | macOS only |
| SentinelOne | Via SentinelOne API |
| 1Password | Via 1Password Extended Access Management |

## Posture Checks by Platform
| Platform | Available Checks |
|----------|-----------------|
| Windows | HD encryption, screen lock, firewall, antivirus, min OS version |
| macOS | Screen lock, biometric, firewall*, HD encryption*, min OS version |
| Linux | HD encryption, firewall |
| iOS | Screen lock, biometric, min OS version |
| Android | HD encryption, screen lock, biometric |

## Configuration Steps
1. Navigate to **Policies → Device Profiles**
2. Click **Create** under Trusted Device Profiles
3. Select platform → choose verification method → configure posture checks
4. Configure **Approved Operating Systems** per platform (enable/disable + posture checks)
5. Apply profiles in **Resource Policies** → Device Security → `Only Trusted Devices` or `Custom`

## Resource Policy Values
- `Any Device` — no device restriction
- `Only Trusted Devices` — any valid Trusted Device Profile
- `Custom` — select specific profiles

## Gotchas
- **macOS firewall + HD encryption** posture checks require the **macOS standalone Client** only
- Disabling a platform in Approved OS blocks all devices on that platform **unless** they satisfy a Trusted Device Profile for that platform
- Trusted Device Profiles are **per-platform**—one profile cannot span multiple OSes
- Profiles are automatically available in both Sign-In and Resource policies once created

## Common Config Patterns
- **Block platform except managed devices**: Disable in Approved OS + create Trusted Profile with MDM verification
- **Tiered access (employees vs contractors)**: Approved OS for contractors, Trusted Profiles for employees; assign Trusted Profiles only to sensitive resources
- **Require MDM for macOS**: Disable macOS in Approved OS + create Trusted Profile with MDM method

## Related Docs
- Device Posture Checks reference
- Manually Verified Devices
- CrowdStrike / Intune / Jamf / Iru / SentinelOne / 1Password configuration guides
- Twingate API (for programmatic device trust)
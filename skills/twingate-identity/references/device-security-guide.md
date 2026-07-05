# Device Profiles (Twingate Device Security)

## Summary
Device Profiles define trust criteria controlling which devices can sign in to Twingate and access specific Resources. Configuration consists of two components: Trusted Device Profiles (MDM/EDR/manual verification) and Approved Operating Systems (baseline posture checks per platform).

## Key Information
- Device Profiles act as "wristbands" — devices earn profiles by meeting criteria; Resources require specific profiles
- **Sign In Policy**: device needs at least one qualifying profile/OS approval to authenticate
- **Resource Policy**: specific Trusted Device Profiles can be required per Resource
- All requirements within a single Trusted Device Profile are **additive** (AND logic — device must satisfy all)
- Blocked devices see an in-client error message explaining the policy failure

## Trusted Device Profile Verification Methods
| Method | Notes |
|---|---|
| Manual | Serial number or per-instance; bulk upload supported; API-programmable |
| CrowdStrike | Falcon API + ZTA score |
| Intune | Microsoft Intune compliance status |
| Jamf | macOS only |
| Iru (Kandji) | macOS only |
| SentinelOne | Via SentinelOne API |
| 1Password | Via 1Password Extended Access Management |

## Approved OS Posture Checks by Platform
| Platform | Available Checks |
|---|---|
| Windows | HD encryption, screen lock, firewall, antivirus, min OS version |
| macOS | Screen lock, biometric, firewall*, HD encryption*, min OS version |
| Linux | HD encryption, firewall |
| iOS | Screen lock, biometric, min OS version |
| Android | HD encryption, screen lock, biometric |

*macOS firewall and HD encryption require the **macOS standalone Client**

## Configuration Steps
1. Navigate to **Policies → Device Profiles tab**
2. Create Trusted Device Profile: select platform → choose verification method → add posture checks
3. Configure Approved Operating Systems: enable/disable platforms, set per-platform posture checks
4. Apply to Resource Policies: set Device Security to **Only Trusted Devices** or **Custom** to select specific profiles

## Common Configuration Patterns
- **Block platform except managed devices**: Disable platform in Approved OS + create Trusted Profile for that platform
- **Employees vs. contractors**: Approved OS for contractors (baseline), Trusted Profiles for employees; assign Trusted Profiles only to employee Resources
- **Require MDM for macOS**: Disable macOS in Approved OS → create Trusted Profile with MDM integration → add to Resource Policies

## Gotchas
- Disabling a platform in Approved OS does **not** block devices that satisfy a Trusted Device Profile for that platform
- macOS firewall/HD encryption posture checks only work with standalone Client (not browser extension)
- Each Trusted Device Profile targets **one platform only**
- Profile requirements are AND logic — one failed check fails the entire profile

## Related Docs
- Manually Verified Devices
- CrowdStrike / Intune / Jamf / Iru / SentinelOne / 1Password Configuration guides
- Device Posture Checks reference
- Sign In Policy
- Resource Policies
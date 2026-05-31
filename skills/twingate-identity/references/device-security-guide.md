# Device Profiles (Twingate Device Security Guide)

## Summary
Device Profiles define trust criteria that devices must meet to access Twingate networks and resources. Configuration includes Trusted Device Profiles (MDM/EDR/manual verification) and Approved Operating Systems (platform-level posture checks). Profiles act additively—all requirements in a profile must be satisfied simultaneously.

## Key Information
- **Two components**: Trusted Device Profiles + Approved Operating Systems
- **Wristband model**: Devices can satisfy multiple profiles; sign-in requires ≥1 profile match; resource access requires the specific profile(s) assigned to that resource
- **Trusted Device Profile requirements are AND logic**—every check must pass
- Profiles are automatically available in Sign In Policy and Resource Policies once created
- Blocked devices receive an in-client error message explaining the failure

## Prerequisites
- Twingate admin access to Policies page
- For MDM/EDR verification: configured integration (CrowdStrike, Intune, Jamf, Iru, SentinelOne, 1Password)
- macOS firewall/HD encryption checks require macOS standalone Client

## Verification Methods
| Method | Notes |
|--------|-------|
| Manual | Serial number or device instance; bulk upload supported; API-configurable |
| CrowdStrike | Falcon API + ZTA score |
| Intune | Compliance status via Microsoft Intune API |
| Jamf | macOS only |
| Iru (Kandji) | macOS only |
| SentinelOne | Falcon API |
| 1Password | Extended Access Management |

## Posture Checks by Platform
| Platform | Available Checks |
|----------|-----------------|
| Windows | HD encryption, screen lock, firewall, antivirus, min OS version |
| macOS | Screen lock, biometric, firewall*, HD encryption*, min OS version |
| Linux | HD encryption, firewall |
| iOS | Screen lock, biometric, min OS version |
| Android | HD encryption, screen lock, biometric |

*Requires macOS standalone Client

## Configuration Steps
1. Navigate to **Policies → Device Profiles**
2. Click **Create** under Trusted Device Profiles
3. Select target platform
4. Choose verification method
5. Configure optional posture checks
6. Apply profile to Resource Policies via **Device Security → Only Trusted Devices** or **Custom**

## Common Patterns
- **Block unmanaged platform, allow managed**: Disable platform in Approved OS → create Trusted Profile with MDM verification
- **Tiered access (employees vs. contractors)**: Approved OS for contractors; Trusted Profiles for employees; assign employee profiles to sensitive resources
- **Test device exceptions**: Disable platform in Approved OS → create manual Trusted Profile → mark specific devices trusted

## Gotchas
- Disabling a platform in Approved OS only blocks sign-in if **no Trusted Device Profile** for that platform exists and is satisfied
- All posture checks within a single Trusted Device Profile are evaluated as AND—no partial credit
- macOS firewall and HD encryption posture checks **will not work** without the standalone Client (not the browser extension)

## Related Docs
- Device Posture Checks reference
- Manually Verified Devices
- CrowdStrike / Intune / Jamf / Iru / SentinelOne / 1Password configuration guides
- Sign In Policy
- Resource Policies
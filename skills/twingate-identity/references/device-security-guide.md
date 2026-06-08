# Device Profiles (Twingate)

## Summary
Device Profiles define trust criteria for devices accessing Twingate resources, split into Trusted Device Profiles (MDM/EDR/manual verification) and Approved Operating Systems (baseline posture). Profiles act additively—a device must satisfy all requirements in a profile to earn it. Resources can require specific profiles for access.

## Key Information
- **Two components**: Trusted Device Profiles (verification-based) + Approved Operating Systems (platform baseline)
- **Sign-in policy**: Device needs at least one profile match to sign in
- **Resource policy**: Can require specific profiles via `Only Trusted Devices` or `Custom`
- All requirements within a single profile are **AND logic** (all must pass)
- Blocked devices see an in-client error message explaining the failure

## Verification Methods (Trusted Device Profiles)
| Method | Notes |
|---|---|
| Manual | By serial number (bulk upload supported) or device instance; API-programmable |
| CrowdStrike | Falcon API + ZTA score |
| Intune | Microsoft Intune compliance status |
| Jamf | macOS only |
| Iru (Kandji) | macOS only |
| SentinelOne | Cross-platform |
| 1Password | Extended Access Management |

## Posture Checks by Platform (Approved OS)
| Platform | Checks |
|---|---|
| Windows | HD encryption, screen lock, firewall, antivirus, min OS version |
| macOS | Screen lock, biometric, firewall*, HD encryption*, min OS version |
| Linux | HD encryption, firewall |
| iOS | Screen lock, biometric, min OS version |
| Android | HD encryption, screen lock, biometric |

*macOS firewall and HD encryption require **macOS standalone Client** only.

## Configuration Steps
1. Navigate to **Policies → Device Profiles tab**
2. Click **Create** under Trusted Device Profiles
3. Select platform, choose verification method, add posture checks
4. Configure **Approved Operating Systems**: enable/disable platforms, set posture checks
5. Apply profiles in **Resource Policies**: set Device Security to `Only Trusted Devices` or `Custom`

## Gotchas
- Disabling a platform in Approved OS blocks **all** devices on that platform **unless** they match a Trusted Device Profile for that platform
- macOS firewall/HD encryption posture checks only work with standalone Client, not browser extension
- Manual verification can be done pre-enrollment via serial number bulk upload
- Profiles are automatically available in both Sign In and Resource policies once created

## Common Patterns
- **Block platform except managed devices**: Disable in Approved OS + create Trusted Profile with MDM verification
- **Tiered access (employee vs contractor)**: Approved OS for contractors, Trusted Profiles for employees; assign Trusted Profiles only to sensitive resources
- **MDM-required platform**: Disable platform in Approved OS, create Trusted Profile with MDM integration

## Related Docs
- Device Posture Checks reference
- Manually Verified Devices
- CrowdStrike / Intune / Jamf / Iru / SentinelOne / 1Password configuration guides
- Twingate API (for programmatic device trust)
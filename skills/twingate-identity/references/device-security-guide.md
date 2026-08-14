---
source: https://www.twingate.com/docs/device-security-guide
type: docs
fetched: 2026-08-14
source_version: b6b3c4371422a612de40f54aedcf4ad409870cc22ef207c18f54367bc600133e
---

# Device Profiles (Twingate Device Security)

## Summary
Device Profiles define trust criteria for devices accessing Twingate resources. Configuration includes Trusted Device Profiles (MDM/EDR/manual verification) and Approved Operating Systems (platform-level posture checks). Profiles act additively—devices must satisfy all requirements in a profile, and policies control which profiles are required per resource.

## Key Information
- **Two components**: Trusted Device Profiles + Approved Operating Systems
- **Sign-in policy**: Device needs ≥1 qualifying profile/OS approval to sign in
- **Resource policy**: Specific profiles can be required per resource (`Only Trusted Devices` or `Custom`)
- All requirements within a single Trusted Device Profile are **AND logic** (all must pass)
- Blocked devices see an in-client error message explaining the denial

## Verification Methods for Trusted Device Profiles
| Method | Notes |
|---|---|
| Manual | By serial number (bulk upload supported) or device instance; API-programmable |
| CrowdStrike | Falcon API + ZTA score |
| Intune | Microsoft Intune compliance status |
| Jamf | macOS only |
| Iru (Kandji) | macOS only |
| SentinelOne | API-based |
| 1Password | Extended Access Management |

## Posture Checks by Platform (Approved Operating Systems)
| Platform | Available Checks |
|---|---|
| Windows | HD encryption, screen lock, firewall, antivirus, min OS version |
| macOS | Screen lock, biometric, firewall*, HD encryption*, min OS version |
| Linux | HD encryption, firewall |
| iOS | Screen lock, biometric, min OS version |
| Android | HD encryption, screen lock, biometric |

*macOS firewall and HD encryption require the **macOS standalone Client**.

## Prerequisites
- Admin or Helpdesk Admin role for manual device verification
- Relevant MDM/EDR integration configured before creating integration-based profiles
- macOS standalone Client for firewall/HD encryption posture checks on macOS

## Step-by-Step: Create a Trusted Device Profile
1. Go to **Policies → Device Profiles tab**
2. Click **Create**
3. Select target platform
4. Choose a verification method
5. Configure optional posture checks
6. Save — profile is immediately available in Sign-In and Resource Policies

## Common Configuration Patterns
| Scenario | Profile Config | Policy Config |
|---|---|---|
| Block platform except managed devices | Disable platform in Approved OS; create Trusted Profile with MDM | Add Trusted Profile to Resource Policies |
| Employees trusted, contractors baseline | Approved OS for contractors; Trusted Profiles for employees | Assign Trusted Profiles to employee-only resources |
| Require MDM for macOS | Disable macOS in Approved OS; create MDM-backed Trusted Profile | Add macOS profile to relevant Resource Policies |

## Gotchas
- Disabling a platform in Approved OS blocks **all** devices on that platform **unless** they satisfy a Trusted Device Profile for that platform
- Firewall and HD encryption posture checks on macOS only work with the standalone Client, not the browser extension
- Serial number bulk upload can be done before or after devices sign in
- Each Trusted Device Profile targets **one platform only**

## Related Docs
- Manually Verified Devices
- CrowdStrike / Intune / Jamf / Iru / SentinelOne / 1Password Configuration guides
- Device Posture Checks reference
- Resource Policies configuration
- Sign In Policy configuration
# Device Security Guide

## Summary
Twingate device security lets admins define trusted device standards via Minimum OS Requirements and Trusted Profiles, then enforce those standards at sign-in or per-Resource through Security Policies. Devices meeting requirements receive access "wristbands" checked at authentication and resource access points.

## Key Information
- **Two security categories**: Minimum OS Requirements (basic posture checks) and Trusted Profiles (advanced verification + Trust Methods)
- **Enforcement levels**: Sign-in level and per-Resource Policy level
- **Default state**: All platforms allowed, no posture checks enabled
- **Policy options per Resource**: Any Device, Only Trusted Devices, or Custom

## Device Posture Checks by Platform

| Platform | Available Checks |
|----------|-----------------|
| Windows | HD Encryption, Screen Lock, Firewall, Antivirus, Min OS Version |
| macOS | Screen Lock, Biometric Config, Firewall*, HD Encryption*, Min OS Version |
| Linux | HD Encryption, Firewall |
| iOS | Screen Lock, Biometric Config, Min OS Version |
| Android | HD Encryption, Screen Lock, Biometric Config |

*macOS standalone app only

## Supported Trust Methods (Trusted Profiles)
- Manual Trust
- CrowdStrike
- Intune
- Jamf
- Iru
- SentinelOne
- 1Password

## Common Configuration Scenarios

| Goal | Device Security Config | Policy Config |
|------|----------------------|---------------|
| Allow only macOS/iOS | Block Android/Windows/Linux in Min OS Requirements | Policy allowing macOS/iOS profiles |
| Employees trusted, contractors not | Min OS Requirements for contractors; Manual Trust Trusted Profiles for employees | Separate Resource policies per group |
| Block Android except test devices | Block Android in Min OS Requirements; Manual Trust Trusted Profile for test devices | Add Android Trusted Profile as allowed |
| MDM/EDR-only macOS | Block macOS in Min OS Requirements; configure MDM/EDR integration; create Trusted Profile | Add macOS Trusted Profile to Resource policies |

## Step-by-Step: Restricting Platform Access
1. Navigate to Device Security settings
2. Set Minimum OS Requirements — block unwanted platforms, configure posture checks for allowed platforms
3. Create Trusted Profiles for platforms requiring advanced verification (select Trust Method)
4. Assign Trusted Profiles to specific devices if using Manual Trust
5. Configure Resource Security Policies: choose Any Device / Only Trusted Devices / Custom

## Gotchas
- Blocking a platform in Min OS Requirements does NOT block devices in a Trusted Profile for that platform — Trusted Profile overrides
- Firewall and HD Encryption on macOS **only available in standalone app**, not the browser extension
- Sign-in requires meeting **both** device security requirements AND minimum authentication requirements
- Devices failing requirements are blocked entirely (sign-in or resource access)

## Related Docs
- Security Policies
- Device Posture Data Collection
- MDM/EDR Integration Setup (CrowdStrike, Intune, Jamf, SentinelOne, 1Password)
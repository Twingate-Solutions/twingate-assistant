# Device Security Guide

## Summary
Twingate device security lets admins define trusted device criteria using Minimum OS Requirements (native posture checks) and Trusted Profiles (MDM/EDR integrations + posture checks). These requirements attach to Security Policies controlling both sign-in access and per-Resource access.

## Key Information
- Two categories: **Minimum OS Requirements** (basic posture checks per platform) and **Trusted Profiles** (advanced verification via MDM/EDR integrations)
- Default state: all platforms allowed, no posture checks enforced
- Device requirements apply at **sign-in level** and/or **per-Resource Policy**
- A device can satisfy multiple profiles simultaneously ("wristband" model)
- Sign-in allows any device meeting *any* requirement; Resource access enforces specific policy rules

## Device Posture Checks by Platform

| Platform | Available Checks |
|----------|-----------------|
| Windows | HD Encryption, Screen Lock, Firewall, Antivirus, Min OS Version |
| macOS | Screen Lock, Biometric, Firewall*, HD Encryption*, Min OS Version (*standalone app only) |
| Linux | HD Encryption, Firewall |
| iOS | Screen Lock, Biometric, Min OS Version |
| Android | HD Encryption, Screen Lock, Biometric |

## Supported Trust Methods (Trusted Profiles)
- Manual Trust
- CrowdStrike
- Intune
- Jamf
- Kandji
- SentinelOne
- 1Password

## Resource Policy Device Options
- **Any Device** – passes if device meets any Minimum OS Requirement or Trusted Profile
- **Only Trusted Devices** – requires Trusted Profile match only
- **Custom** – specify exact set of requirement profiles required

## Common Configuration Patterns

| Goal | Approach |
|------|----------|
| Block specific OS | Set Minimum OS Requirement for that platform to "blocked" |
| Employees trusted, contractors not | Trusted Profile (Manual Trust) for employees; Minimum OS Requirements for contractors |
| Allow only MDM-managed macOS | Block macOS in Min OS Requirements; create Trusted Profile requiring MDM integration |
| Exempt specific Android test devices | Block Android in Min OS Requirements; create Android Trusted Profile with Manual Trust for test devices |

## Prerequisites
- Twingate desktop or mobile client installed on target devices
- MDM/EDR integration configured before creating Trusted Profiles requiring it
- Security Policies configured and assigned to Resources

## Gotchas
- macOS Firewall and HD Encryption posture checks **only available in the standalone app**, not the browser extension
- Blocking a platform in Minimum OS Requirements does not block it from a Trusted Profile—you must handle both independently (e.g., Android block scenario requires both a block rule and a separate Trusted Profile for exceptions)
- Sign-in still requires minimum authentication requirements to be met in addition to device security
- Posture checks are collected natively by the Twingate client—see separate posture collection documentation for details

## Related Docs
- Security Policies
- MDM/EDR Integration setup (CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password)
- Device posture data collection details
- macOS standalone app documentation
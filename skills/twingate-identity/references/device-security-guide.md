# Device Security Guide

## Summary
Twingate device security lets admins define trusted device criteria using Minimum OS Requirements (native posture checks) and Trusted Profiles (advanced verification via MDM/EDR integrations). These definitions are applied at sign-in and/or per-Resource via Security Policies.

## Key Information
- Two device security categories: **Minimum OS Requirements** (basic posture) and **Trusted Profiles** (advanced verification)
- Default state: all platforms allowed, no posture checks enforced
- Device requirements apply at two levels: sign-in authentication and individual Resource access
- A device can satisfy multiple profiles simultaneously; policies gate which profiles are required per Resource

## Prerequisites
- Admin access to Twingate console
- For Trusted Profiles with integrations: MDM/EDR (CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password) must be configured

## Device Posture Checks by Platform

| Platform | Available Checks |
|----------|-----------------|
| Windows | HD Encryption, Screen Lock, Firewall, Antivirus, Min OS Version |
| macOS | Screen Lock, Biometric, Firewall*, HD Encryption*, Min OS Version |
| Linux | HD Encryption, Firewall |
| iOS | Screen Lock, Biometric, Min OS Version |
| Android | HD Encryption, Screen Lock, Biometric |

*macOS standalone app only

## Trusted Profile Verification Methods
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
- **Custom** – specify exact set of allowed profiles/requirements

## Common Configuration Patterns

| Goal | Approach |
|------|----------|
| Block specific OS platforms | Set Minimum OS Requirement for that platform to blocked |
| Employees trusted, contractors not | Trusted Profile (Manual Trust) for employees; Minimum OS Requirements for contractors |
| MDM/EDR required for access | Block platform in Min OS Requirements; create Trusted Profile requiring MDM integration |
| Allowlist specific devices on blocked OS | Block OS in Min OS Requirements; create Trusted Profile with Manual Trust for exceptions |

## Gotchas
- Blocking a platform in Minimum OS Requirements does not block devices with a matching Trusted Profile — Trusted Profiles can override OS-level blocks
- Firewall and HD Encryption checks on macOS are **only available in the standalone app**, not the browser extension
- Sign-in requires meeting minimum authentication requirements in addition to device security requirements
- Devices failing any required check are blocked from both sign-in and Resource access

## Related Docs
- Security Policies
- Device Posture Data Collection
- MDM/EDR Integration setup (CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password)
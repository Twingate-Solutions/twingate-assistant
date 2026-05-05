## Device Security Guide

Reference for Twingate's two-tier device requirement model: **Minimum OS Requirements** (broad baseline) and **Trusted Profiles** (specific verification + posture). Both can gate sign-in and Resource access.

### Two Categories of Device Requirements

**Minimum OS Requirements**
- Configure baseline posture per platform: screen lock, HD encryption, AV, firewall, minimum OS version
- Used to set the "floor" for any device accessing Twingate
- Configurable per platform (Windows, macOS, Linux, iOS, Android)
- Can also be used to **block** entire platforms (e.g., disallow Android entirely)

**Trusted Profiles**
- Layered on top of Minimum OS — for Resources requiring stricter trust
- Requires a **Trust Method** + optional additional posture checks
- Trust Methods: Manual Trust, CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password

### The Wristband Analogy

Each device can have multiple "wristbands" -- one per Profile/Requirement it satisfies:
- Meets macOS Minimum OS Requirements -> 1 wristband
- Meets macOS Minimum OS + macOS CrowdStrike Trusted Profile -> 2 wristbands

**Sign-in to Twingate**: any wristband suffices.
**Resource access**: only wristbands explicitly allowed by the Resource Policy work.

This means a device can sign in to Twingate but still be blocked from a specific Resource if that Resource requires a Profile the device doesn't satisfy.

### Common Configuration Scenarios

| Scenario | Minimum OS | Trusted Profiles |
|---|---|---|
| Allow only macOS + iOS with basic posture | Block Windows/Android/Linux; configure posture for macOS+iOS | Resource Policy uses "All Devices" |
| Employees trusted, contractors not | Posture checks for contractor-grade requirements | Trusted Profiles for employee platforms with Manual Trust; Resource Policies separate employee vs. contractor Resources |
| Allow Android only for specific test devices | Block Android | Trusted Profile for Android with Manual Trust + test devices marked verified |
| MDM/EDR-only macOS access | Block macOS in Minimum OS | Trusted Profile for macOS requiring CrowdStrike (or Jamf/Kandji/Intune); apply this Profile to Resources macOS users need |

### Resource Policy Device Setting

Three options when creating a Resource Policy:
- **Any Device** -- meets either Minimum OS or any Trusted Profile
- **Only Trusted Devices** -- meets at least one Trusted Profile (the most common production setting)
- **Custom** -- meets a specific subset of Profiles/Requirements

If the device fails all required wristbands, it's blocked from the Resource.

### Default Configuration

Out of the box: all platforms allowed, no posture checks. **Tighten this per /docs/security-policies-best-practices** before going to production.

### Decision Notes

- **Most production deployments**: Minimum OS = baseline posture + block unused platforms; Trusted Profiles = per (OS, EDR) combination; Resource Policies = "Only Trusted Devices" for sensitive Resources, "Any Device" for low-risk
- For BYOD contractors without EDR: create a Trusted Profile with Manual Trust + native posture checks; mark contractor devices verified in the Admin Console
- Always combine posture checks with Trusted Profiles -- relying on posture alone via Minimum OS doesn't capture EDR/MDM signal

### Gotchas

- Minimum authentication requirements still apply on top of device requirements -- a device can be wristband-eligible but blocked by MAR
- Manual Trust devices stay verified until explicitly un-verified -- they don't auto-expire; build a process to revoke when devices are decommissioned
- macOS standalone Client supports more posture checks than the App Store version -- choose deliberately

### Related Docs

- /docs/device-posture-checks -- Per-platform posture check details
- /docs/trusted-devices -- Trusted Devices policy rule
- /docs/manually-verified-devices -- Manual Trust workflow
- /docs/managed-devices -- MDM/EDR Trust Method integrations
- /docs/security-policies, /docs/security-policies-best-practices -- Policy model + risk-tier design
- /docs/crowdstrike-configuration, /docs/intune-configuration, /docs/jamf-configuration, /docs/kandji-configuration, /docs/sentinelone-configuration, /docs/1password-configuration -- Per-Trust-Method setup

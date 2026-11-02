---
source: https://help.twingate.com/articles/2024206011-crowdstrike-is-not-detected
type: help
fetched: 2026-11-01
source_version: 97d2f5a021b1bda3c6956d31bf1fa8c2a9889abc9877233872b1c4d1e5eec1f1
trust: official
---

# CrowdStrike Not Detected by Twingate

## Page Title
CrowdStrike Is Not Detected

## Summary
CrowdStrike may be installed and reporting to its own dashboard but still show as "not detected" in Twingate. The root cause is that CrowdStrike's Zero Trust Assessment (ZTA) feature for third parties is not enabled or configured, preventing the required `data.zta` file from being deployed on devices.

## Key Information
- Twingate uses CrowdStrike's **Falcon Zero Trust Assessment (ZTA)** feature to detect device security status
- The ZTA third-party integration must be explicitly enabled with CrowdStrike — it is not on by default
- Twingate's Customer ID (CID) must be shared with CrowdStrike to authorize the integration
- Without this, the `data.zta` file will be missing or 0 bytes on endpoints

## Prerequisites
- CrowdStrike Falcon installed and reporting to CrowdStrike dashboard
- CrowdStrike Falcon Zero Trust Assessment feature licensed/enabled
- Twingate Device Security with CrowdStrike integration configured

## Platforms
- macOS
- Windows

## Troubleshooting Steps

1. Check for the presence and size of the `data.zta` file:
   - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`
   - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\data.zta`
     *(Note: "Asssessment" has a triple-s in the Windows path — likely a typo in CrowdStrike's directory name)*

2. If the file is **missing or empty (0 bytes)**, the ZTA third-party feature is not enabled.

## Resolution
- Contact **CrowdStrike customer support** to enable the Zero Trust Assessment feature for third parties
- Provide CrowdStrike with **Twingate's CID** to authorize the integration
- Once enabled, CrowdStrike will deploy the `data.zta` file to managed devices, and Twingate will detect it

## Gotchas
- CrowdStrike being active and reporting to its own console does **not** mean ZTA third-party access is enabled — these are separate features
- The Windows path contains a typo (`ZeroTrustAsssessment` with three `s`) — verify the actual directory name on the target system
- Resolution requires action through **CrowdStrike support**, not Twingate support

## Related Docs
- [CrowdStrike Configuration (Twingate)](https://help.twingate.com) — referenced internally for setup details
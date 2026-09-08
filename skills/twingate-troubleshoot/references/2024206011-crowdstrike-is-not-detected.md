---
source: https://help.twingate.com/articles/2024206011-crowdstrike-is-not-detected
type: help
fetched: 2026-09-06
source_version: 834d91c2555c6ede843a34f61a4492478c0e8b43eed468cad8000deeeeabbff6
---

# CrowdStrike Not Detected by Twingate

## Page Title
CrowdStrike Is Not Detected

## Summary
CrowdStrike may be installed and reporting to its own dashboard but still show as "not detected" in Twingate. The root cause is that CrowdStrike's Zero Trust Assessment (ZTA) feature for third parties is not enabled, preventing Twingate from reading the required ZTA data file.

## Key Information
- **Affected components:** Twingate Client, Device Security, CrowdStrike integration
- **Affected platforms:** macOS, Windows
- **The ZTA file (`data.zta`) must exist and be non-empty** for Twingate to detect CrowdStrike
- CrowdStrike ZTA Third Party integration requires your organization's CID to be shared with CrowdStrike

## Prerequisites
- CrowdStrike Falcon installed and reporting to CrowdStrike dashboard
- CrowdStrike Falcon Zero Trust Assessment feature must be licensed/enabled
- Twingate CID must be registered with CrowdStrike for third-party ZTA access

## Troubleshooting Steps

1. **Check for the `data.zta` file** in the platform-specific directory:
   - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/`
   - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\`

2. **Verify the file is not empty (0 KB)** — a missing or empty file confirms ZTA third-party access is not configured.

3. **If file is missing or empty:** Contact CrowdStrike customer support to enable Zero Trust Assessment for third parties and provide them with the Twingate CID.

## Configuration Values

| Item | Value |
|------|-------|
| ZTA file (macOS) | `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta` |
| ZTA file (Windows) | `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\data.zta` |

## Gotchas
- **Typo in Windows path in docs:** `ZeroTrustAsssessment` has three `s`s — verify actual filesystem path on the device
- CrowdStrike being functional and reporting to its own console does **not** mean ZTA third-party access is enabled — these are separate configurations
- The `data.zta` file being present at 0 KB is a known symptom of the ZTA feature not being enabled

## Resolution
Contact CrowdStrike customer support to:
1. Enable the Falcon Zero Trust Assessment feature
2. Register Twingate's CID as an authorized third party

## Related Docs
- [CrowdStrike Configuration](https://help.twingate.com/articles/crowdstrike-configuration) (Twingate docs — referenced but URL not provided)
- CrowdStrike Falcon Zero Trust Assessment documentation (vendor)
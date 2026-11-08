---
source: https://help.twingate.com/articles/2024206011-crowdstrike-is-not-detected
type: help
fetched: 2026-11-08
source_version: 9b73f8ea0cbebb062b7d21c921fc1b53ae56d2952f49920636971b23044e40f4
trust: official
---

# CrowdStrike Not Detected by Twingate

## Page Title
CrowdStrike is Not Detected

## Summary
CrowdStrike may be installed and reporting correctly to its own dashboard while still showing "CrowdStrike not detected" in Twingate. The root cause is typically that CrowdStrike's Zero Trust Assessment (ZTA) feature for third parties is not enabled or configured, preventing the required `data.zta` file from being deployed on devices.

## Key Information
- Applies to: Twingate Client, Device Security, CrowdStrike integration
- Platforms: macOS, Windows
- CrowdStrike Falcon Zero Trust Assessment must be enabled **and** configured to allow third-party access
- Without ZTA enabled, the `data.zta` file will be missing or 0 KB on endpoints
- Twingate reads the `data.zta` file to validate CrowdStrike status

## Prerequisites
- CrowdStrike Falcon installed and reporting to CrowdStrike dashboard
- CrowdStrike Zero Trust Assessment feature license/entitlement
- CrowdStrike CID (Customer ID) shared with Twingate for the third-party integration

## Troubleshooting Steps

1. **Check for the `data.zta` file** in the appropriate directory:
   - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/`
   - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\`

2. **Verify file is not missing or empty (0 KB).** A missing or empty file confirms ZTA is not configured.

3. **If file is missing/empty:** Contact CrowdStrike customer support to enable ZTA for third parties and provide them your Twingate CID.

## Configuration Values

| Item | Value |
|------|-------|
| macOS ZTA file path | `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta` |
| Windows ZTA file path | `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\data.zta` |
| Required CrowdStrike feature | Falcon Zero Trust Assessment (Third Party) |

## Gotchas
- Note the double `s` typo in the Windows path (`ZeroTrustAsssessment`) — this appears in the official documentation and may reflect the actual directory name on disk
- CrowdStrike, not Twingate, controls ZTA enablement; resolution requires contacting CrowdStrike support directly
- CrowdStrike can appear fully functional from its own perspective while ZTA remains disabled

## Related Docs
- [CrowdStrike Configuration](https://help.twingate.com/articles/crowdstrike-configuration) (referenced in source)
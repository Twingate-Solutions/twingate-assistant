---
source: https://help.twingate.com/articles/2024206011-crowdstrike-is-not-detected
type: help
fetched: 2026-10-04
source_version: d6a025600f55afe54e7bdae01037f71507ba10305dd9ba94cf790694a6bd391e
trust: official
---

# CrowdStrike Not Detected by Twingate

## Page Title
CrowdStrike is Not Detected

## Summary
CrowdStrike may be installed and reporting to its dashboard but still show as "not detected" in Twingate Device Security. The root cause is that CrowdStrike's Zero Trust Assessment (ZTA) feature for third parties is not enabled, which prevents the required `data.zta` file from being deployed on devices.

## Key Information
- Affects macOS and Windows platforms
- Twingate reads CrowdStrike ZTA data via a local file (`data.zta`) written by CrowdStrike
- The ZTA file will be missing or 0 bytes if the feature is not enabled
- CrowdStrike must be explicitly configured to share ZTA data with third parties (Twingate)

## Prerequisites
- CrowdStrike Falcon installed and reporting to CrowdStrike dashboard
- CrowdStrike Falcon Zero Trust Assessment feature enabled on your CrowdStrike account
- Twingate CID provided to CrowdStrike to authorize the third-party integration

## Troubleshooting Steps

1. **Locate the `data.zta` file** on the device:
   - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/`
   - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\` *(note: double `s` in `Asssessment` is in the original path)*

2. **Check file status:**
   - File missing → ZTA feature not enabled or not deployed
   - File present but 0 KB → Third-party CID not configured with CrowdStrike

3. **Enable the feature:** Contact CrowdStrike customer support to enable Zero Trust Assessment for third parties and provide Twingate's CID.

## Configuration Values

| Item | Value |
|------|-------|
| ZTA file (macOS) | `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta` |
| ZTA file (Windows) | `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\data.zta` |

## Gotchas
- CrowdStrike being installed and functional does **not** automatically enable ZTA for third parties — it requires explicit opt-in
- The Windows path contains a typo (`ZeroTrustAsssessment` with three `s` characters) — verify against actual filesystem
- The ZTA file can exist but be 0 KB, which is also an indicator of misconfiguration, not just absence

## Related Docs
- [CrowdStrike Configuration (Twingate)](https://help.twingate.com/articles/crowdstrike-configuration) — referenced in article for enabling ZTA and CID setup
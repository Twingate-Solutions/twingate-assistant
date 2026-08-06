---
source: https://help.twingate.com/articles/2024206011-crowdstrike-is-not-detected
type: help
fetched: 2026-08-06
source_version: 9786755835b272d5376d85bc588fdde050ada0f9b149f5a8d2a5a29d9f78c2d2
---

# CrowdStrike Not Detected by Twingate

## Page Title
CrowdStrike is Not Detected

## Summary
CrowdStrike may be installed and reporting to its own dashboard but still show as "not detected" in Twingate. This occurs because the CrowdStrike Zero Trust Assessment (ZTA) feature for third parties must be explicitly enabled. Without it, the required `data.zta` file is not deployed on devices.

## Key Information
- Issue is **not** a Twingate Client problem — it's a CrowdStrike configuration gap
- Requires CrowdStrike Falcon **Zero Trust Assessment** feature enabled for third parties
- Twingate's CID must be shared with CrowdStrike to enable the integration
- Missing or 0kb `data.zta` file confirms the root cause

## Prerequisites
- CrowdStrike Falcon installed and reporting to CrowdStrike dashboard
- CrowdStrike Zero Trust Assessment (ZTA) feature licensed/available
- CrowdStrike customer support contact to enable third-party ZTA

## Troubleshooting Steps

1. **Verify `data.zta` file exists and is non-empty:**
   - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`
   - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\data.zta`

2. **If file is missing or 0kb:** ZTA for third parties is not enabled — proceed to resolution.

3. **If file exists with content:** Check Twingate CrowdStrike Configuration docs for further setup.

## Resolution
1. Contact **CrowdStrike customer support** to enable the Zero Trust Assessment feature for third parties
2. Provide Twingate's **CID** to CrowdStrike to authorize the integration
3. Confirm `data.zta` is populated on endpoints after enablement

## Configuration Values
| Item | Value |
|------|-------|
| macOS ZTA path | `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta` |
| Windows ZTA path | `%ProgramData%\CrowdStrike\ZeroTrustAsssessment\data.zta` |

## Gotchas
- **Typo in Windows path:** Official doc shows `ZeroTrustAsssessment` (triple 's') — verify actual filesystem path on your system
- CrowdStrike dashboard showing device as healthy does **not** mean ZTA third-party access is enabled
- This feature requires action on the **CrowdStrike side**, not within Twingate

## Related Docs
- Twingate CrowdStrike Configuration guide (referenced but not linked in source)
- Twingate Device Security documentation
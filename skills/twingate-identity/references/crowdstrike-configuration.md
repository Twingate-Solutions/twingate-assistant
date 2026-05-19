# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture as a requirement for accessing private resources. The integration uses the CrowdStrike API to validate managed devices and can be incorporated into Security Policies via Device Security Trusted Profiles. Requires Business or Enterprise plan.

## Key Information
- CrowdStrike Zero Trust Assessment (ZTA) must be enabled on your Falcon CID (contact CrowdStrike Support)
- Twingate pulls device lists via CrowdStrike API and reads the local ZTA file or Agent ID on endpoints
- Linux support requires Twingate client version 2024.018+
- Initial sync after setup takes up to 10 minutes

## Prerequisites
- Twingate Business or Enterprise plan
- CrowdStrike Falcon Zero Trust Assessment feature enabled (request via CrowdStrike Support)
- Verify ZTA file exists and is non-empty:
  - Windows: `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - macOS: `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step

1. **Generate CrowdStrike API Client** in Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the API Client ID, API Client Secret, and Base URL

2. **In Twingate**: Navigate to **Settings → Device Settings**

3. **Connect CrowdStrike**: Click "Connect" next to CrowdStrike, enter:
   - API Client ID
   - API Client Secret
   - Base URL (your CrowdStrike tenant URL)

4. **Verify status** on the Device Settings page

5. **Create Trusted Profile**: Add CrowdStrike as a Trust Method for macOS, Windows, or Linux

6. **Attach Trusted Profile** to Security Policies

## Configuration Values
| Parameter | Description |
|---|---|
| API Client ID | From CrowdStrike Falcon API client |
| API Client Secret | From CrowdStrike Falcon API client |
| Base URL | CrowdStrike tenant base URL |

Required API scopes: `Hosts: Read`, `Zero Trust Assessment: Read`

## Gotchas
- ZTA feature is **not enabled by default**—must be explicitly requested from CrowdStrike Support
- Up to **10-minute delay** on initial sync; devices may show incorrect state during this window
- **Recoverable errors** (API unresponsive): Integration auto-retries; last successful sync time is displayed
- **Unrecoverable errors** (deleted API client, changed permissions): Integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials
- Linux requires Twingate client v2024.018+

## Related Docs
- Device Security Trusted Profiles
- Security Policies
- Twingate pricing page (plan eligibility)
# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Device Security Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture using the CrowdStrike API and Zero Trust Assessment (ZTA) scores. Verified devices can be required as a condition for accessing private resources via Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Uses CrowdStrike API to pull managed device list and validate device identity via Agent ID or ZTA file
- ZTA score file must exist and be non-empty on endpoints before integration will work
- Supports macOS, Windows, and Linux (Linux requires Twingate client v2024.018+)
- Initial sync takes up to 10 minutes after setup

## Prerequisites
- Twingate Business or Enterprise plan
- CrowdStrike Falcon Zero Trust Assessment feature enabled on your Falcon CID (must be requested via CrowdStrike Support)
- Verify ZTA file exists and is non-empty:
  - **Windows:** `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - **macOS:** `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step

1. **Generate CrowdStrike API client** in Falcon platform with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the **API Client ID**, **API Client Secret**, and **Base URL**

2. In Twingate, go to **Settings → Device Settings**

3. Click **Connect** next to CrowdStrike; enter:
   - API Client ID
   - API Client Secret
   - Base URL (CrowdStrike tenant URL)

4. Confirm integration status on Device Settings page

5. Create a **Trusted Profile** requiring CrowdStrike as a Trust Method under Device Security

6. Add Trusted Profile to a **Security Policy**

## Configuration Values

| Field | Source |
|---|---|
| API Client ID | CrowdStrike Falcon API client |
| API Client Secret | CrowdStrike Falcon API client |
| Base URL | CrowdStrike tenant base URL |

**Required API Scopes:** `Hosts: Read`, `Zero Trust Assessment: Read`

## Gotchas
- ZTA feature must be explicitly enabled by CrowdStrike Support — it is not on by default
- Empty (0KB) ZTA file means the feature is not active; integration will not work
- Initial sync delay of up to 10 minutes — devices may show incorrect verification state during this window
- **Recoverable errors** (API unresponsive): auto-resolves when API is reachable again; last successful sync time is shown
- **Unrecoverable errors** (deleted API client, changed permissions): integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials

## Related Docs
- Device Security Trusted Profiles
- Security Policies
- Twingate pricing page (plan eligibility)
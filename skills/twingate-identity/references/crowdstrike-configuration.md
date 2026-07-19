# CrowdStrike Configuration

## Page Title
CrowdStrike Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with CrowdStrike Falcon to verify device security posture as a requirement for accessing private resources. The integration uses the CrowdStrike API to validate managed devices and incorporates CrowdStrike verification into Security Policy Trusted Profiles. Requires Business or Enterprise plan.

## Key Information
- CrowdStrike acts as a **Trust Method** within Device Security Trusted Profiles
- Twingate pulls managed device list via CrowdStrike API; client reads local Agent ID or ZTA file for device verification
- Supports macOS, Windows, and Linux (Linux requires client v2024.018+)
- Initial sync after setup takes **up to 10 minutes**

## Prerequisites
- Twingate Business or Enterprise plan
- CrowdStrike Falcon **Zero Trust Assessment (ZTA) feature must be enabled** by CrowdStrike Support for your CID
- Verify ZTA is active by confirming non-empty file exists:
  - Windows: `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta`
  - macOS: `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`

## Step-by-Step Configuration

1. **In CrowdStrike Falcon**, create a new API client with these scopes:
   - `Hosts: Read`
   - `Zero Trust Assessment: Read`
   - Save the **API Client ID**, **API Client Secret**, and **Base URL**

2. **In Twingate**, go to **Settings → Device Settings**

3. Click **Connect** next to CrowdStrike; enter:
   - API Client ID
   - API Client Secret
   - Base URL (CrowdStrike tenant URL)

4. Confirm integration status on the Device Settings page

5. Create a **Trusted Profile** requiring CrowdStrike as a Trust Method, then add to a Security Policy

## Configuration Values
| Field | Source |
|-------|--------|
| API Client ID | CrowdStrike Falcon API client |
| API Client Secret | CrowdStrike Falcon API client |
| Base URL | CrowdStrike tenant base URL |

## Gotchas
- ZTA feature is **not enabled by default**—must contact CrowdStrike Support explicitly
- Without ZTA enabled, `data.zta` file will be absent/empty and integration will not function
- Devices show incorrect verification state during the initial 10-minute sync window ("Waiting to sync")
- **Recoverable errors** (API unresponsive): last successful sync time shown; auto-resolves when API is reachable
- **Unrecoverable errors** (API client deleted or permissions changed): integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials

## Related Docs
- Device Security Trusted Profiles
- Security Policies
- Twingate Pricing (plan eligibility)